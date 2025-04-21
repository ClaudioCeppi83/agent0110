# Proyecto "Agente 0110" 
 
## Descripcion general del proyecto: 

Agente de inteligencia artificial ejecutable desde una ventana gráfica en Linux. Este agente estará construido sobre Ollama en modo local y podrá cargar cualquier modelo compatible con Ollama, incluyendo modelos de propósito general y especializados. 

El agente debe permitir al usuario trabajar con programación en todos los lenguajes conocidos, asistido por MCPs (Model Context Protocols) personalizados. Estos MCPs están instalados localmente y deben ser escaneados dinámicamente desde una ruta específica en el sistema (por ejemplo, ~/ollama/mcps/). 

## Requisitos funcionales del agente: 

1. **Selección de Modelo Ollama:**
    ◦ Interfaz para elegir cualquier modelo de los instalados en Ollama (ollama list). 
    ◦ Posibilidad de cambiar el modelo en tiempo real sin reiniciar la interfaz. 
2. **Gestión de MCPs:**
    ◦ Escaneo automático de directorios MCP locales. 
    ◦ Interfaz con checkboxes o menús desplegables para activar MCPs específicos. 
    ◦ Posibilidad de previsualizar el contenido de cada MCP (context.md, meta.json, etc.). 
3. **Área de entrada de texto:**
    ◦ Zona de texto multilínea donde el usuario puede escribir prompts personalizados, instrucciones o código. 
    ◦ Botón "Enviar" que inicia la interacción con el modelo, aplicando los MCPs seleccionados como contexto previo. 
4. **Terminal embebida (solo lectura):**
    ◦ Muestra todas las acciones internas del agente, incluyendo: 
        ▪ Carga de modelo. 
        ▪ MCPs cargados. 
        ▪ Peticiones generadas. 
        ▪ Código generado o errores detectados. 
    ◦ Estilo consola, tipo log en tiempo real. 
5. **Contexto operativo:**
    ◦ Toda la interacción ocurre en entorno local (Ubuntu o cualquier otra distribución Linux). 
    ◦ El agente no realiza llamadas externas: usa exclusivamente el modelo alojado y los MCPs locales. 
    ◦ Si se requiere leer archivos, debe permitirse la selección desde la interfaz y el agente interpretará su contenido. 
6. **Control de permisos de MCPs (lectura/escritura de archivos):**
    ◦ El agente debe pedir permiso explícito al usuario para realizar cualquier acción externa sobre el sistema de archivos, como lectura o escritura. 
    ◦ Debe existir un menú de configuración con opciones de checkbox para definir permisos automáticos: 
        ▪ Permitir lectura automática de archivos. 
        ▪ Permitir escritura automática de archivos. 
        ▪ Desactivar ambos (modo manual). 
    ◦ Si alguna opción no está habilitada, el agente debe pausar la acción correspondiente y solicitar autorización antes de proceder. 
7. **Capacidades del agente IA:**
    ◦ Generación, análisis, explicación, documentación y depuración de código. 
    ◦ Multilenguaje: Python, C++, Rust, JavaScript, SQL, Haskell, Bash, etc. 
    ◦ Uso avanzado de MCPs para enriquecer la generación con estándares, patrones y estilo del usuario. 
    ◦ Posibilidad de hacer refactorización o revisión completa de proyectos completos. 

**Instrucciones técnicas internas:**
    • Cargar MCPs como inyección de contexto previa a cada prompt enviado al modelo. 
    • Mantener una estructura modular, donde los MCPs puedan ser sustituidos, añadidos o eliminados sin romper el sistema. 
    • El agente debe explicar en la terminal qué está haciendo en cada paso. 

Responde siempre como un asistente técnico altamente capacitado, con claridad y precisión. Al finalizar cada tarea, ofrece sugerencias de mejora o preguntas que profundicen el proyecto. 


## Planificación del proyecto: 

**Planificación Técnica: Agente de IA Local con Ollama, MCPs e Integración IDE**

**Objetivo:** Desarrollar un agente de IA local para Linux con GUI, protocolos personalizados (MCPs) e integración profunda con VSCode/Neovim. 

1. **Definición del Problema**

**Problema central:**
Los desarrolladores necesitan una herramienta local que: 
    • Interactúe con modelos LLM (Ollama) sin dependencia de la nube. 
    • Personalice la generación de código mediante MCPs (estándares de equipo/proyecto). 
    • Se integre directamente en sus IDEs (VSCode, Neovim) para flujos ágiles. 

**Dolores actuales:**
    • Soluciones cloud (GitHub Copilot) exponen código sensible. 
    • Falta de control sobre el contexto inyectado en prompts. 
    • Interfaz fragmentada entre terminal, IDE y herramientas de IA. 

2. **Público Objetivo**

|-----------------------|-----------------------------------------------------------------------------|
| **Perfil**            | **Necesidades Específicas**                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| *Devs Linux*          | Privacidad, soporte para modelos locales (Llama 3, CodeLlama).              |
|-----------------------|-----------------------------------------------------------------------------|
| *Equipos de Software* | MCPs para estandarizar código (ej: clean architecture, patrones de equipo). |
|-----------------------|-----------------------------------------------------------------------------|
| *Data Scientists*     | Soporte para modelos especializados (ej: SQL, Pandas, PyTorch).             |
|-----------------------|-----------------------------------------------------------------------------|

3. **Requisitos Funcionales** 

**Núcleo del Agente**

|---------|-------------------------|---------------------------------------------------------------------|
| **ID**  | **Requisito**           | **Detalle**                                                         |
|---------|-------------------------|---------------------------------------------------------------------|
| RF-01   | GUI Linux (PyQt/Slint)  | Listado de modelos Ollama, selector de MCPs, terminal de logs.      |
|---------|-------------------------|---------------------------------------------------------------------|
| RF-02   | Gestión de MCPs         | Escaneo dinámico de ~/ollama/mcps/, previsualización de context.md. |
|---------|-------------------------|---------------------------------------------------------------------|
| RF-03   | Persistencia (SQLite)   | Historial de conversaciones guardado en ~/.ollama/history.db.       |
|---------|-------------------------|---------------------------------------------------------------------|
 
**Integración con IDEs**

|---------|-----------------------|--------------------------------------------------------------------------------|
| **ID**  | **Requisito**         | **Detalle**                                                                    |
|---------|-----------------------|--------------------------------------------------------------------------------|
| RF-04   | Extensión VSCode      | Comandos para refactorizar, documentar, y explicar código.                     |
|---------|-----------------------|--------------------------------------------------------------------------------|
| RF-05   | Plugin Neovim         | Soporte para :OllamaGenerate, :OllamaDebug con MCPs activos.                   |
|---------|-----------------------|--------------------------------------------------------------------------------|
| RF-06   | Permisos de escritura | Confirmación manual antes de modificar archivos (a menos que se auto-permita). |
|---------|-----------------------|--------------------------------------------------------------------------------|

** Gestión de Modelos**

|---------|---------------------------------|----------------------------------------------------------------------|
| **ID**  | **Requisito**                   | **Detalle**                                                          |
|---------|---------------------------------|----------------------------------------------------------------------|
| RF-07   | Descarga/eliminación de modelos | Interfaz para ollama pull y ollama rm con verificación de recursos.  |
|---------|---------------------------------|----------------------------------------------------------------------|
| RF-08   | Benchmarking                    | Test de velocidad/calidad (ej: tokens/segundo, precisión en código). |
|---------|---------------------------------|----------------------------------------------------------------------|

4. **MVP vs. Roadmap**

**Fase 1 (MVP)**
    • GUI básica en Python (PyQt) + Ollama. 
    • Selección de modelos y MCPs. 
    • Terminal de logs interactiva. 

**Fase 2 (Integración IDE)**
    • API REST con FastAPI (endpoints para VSCode/Neovim). 
    • Extensión VSCode con: 
        ◦ Análisis de código abierto. 
        ◦ Refactorización asistida (Ctrl+Shift+P → Ollama: Refactor). 
    • Plugin Neovim con comandos Lua. 

**Fase 3 (Avanzado)**
    • Gestión visual de modelos (descarga/benchmarking). 
    • Plantillas MCPs preinstaladas (Python, Rust, SQL). 
    • Soporte para JetBrains. 

5. **Arquitectura Técnica**

*flowchart TB:*

subgraph GUI[Agente Principal] 
    A[Interfaz PyQt] --> B[API FastAPI] 
    B --> C[Ollama] 
    C --> D[(Modelos Locales)] 
    B --> E[(MCPs)] 
    B --> F[(SQLite)] 
end 
 
subgraph IDEs 
    G[VSCode] -->|HTTP| B 
    H[Neovim] -->|CLI| B 
end 

**Stack Tecnológico **

• Lenguajes: Python (FastAPI, PyQt), TypeScript (VSCode), Lua (Neovim). 

• Protocolos: REST API, WebSockets (opcional para logs en tiempo real). 

• Seguridad: Bcrypt para autenticación, checksum en MCPs. 

6. **Limitaciones y Soluciones**

|-----------------------------|--------------------------------------------------------|
| **Limitación**              | **Solución Propuesta**                                 |
|-----------------------------|--------------------------------------------------------|
| Solo Linux inicialmente     | PyQt/Slint para futuro soporte multiplataforma.        |
|-----------------------------|--------------------------------------------------------|
| Rendimiento con modelos 70B | Barra de temperatura + sugerencias de modelos ligeros. |
|-----------------------------|--------------------------------------------------------|
| Autenticación multiusuario  | SQLite + bcrypt (modo invitado sin historial).         |
|-----------------------------|--------------------------------------------------------|

7. **Preguntas Clave Pendientes**

    1. ¿Priorizar la extensión VSCode o el plugin Neovim primero? 
        ◦ **Recomendación:** VSCode (mayor alcance inicial). 
    1. ¿Usar WebSockets para logs en vivo o REST es suficiente? 
        ◦ **Recomendación:** REST para el MVP, WebSockets en Fase 3.

8. **Próximos Pasos**

    1. **Desarrollo del núcleo:**
        ◦ Crear GUI básica + conexión a Ollama. 
    1. **API REST:**
        ◦ Implementar endpoints para /generate, /models, /mcps. 
    1. **Extensión VSCode:**
        ◦ Prototipo con comandos básicos.

## Arquitectura y Diseño Detallado

1. **Introducción y Alcance**

    **1.1 Objetivo del Documento**
    Este documento sirve como referencia técnica exhaustiva para el equipo de desarrollo, describiendo cada aspecto arquitectónico, de diseño y de implementación del Agente 0110. Incluye: 
        • Decisiones de arquitectura justificadas. 
        • Especificaciones técnicas detalladas. 
        • Guías de implementación para cada módulo. 

    **1.2 Alcance del Proyecto**
        • MVP: Interfaz gráfica en PyQt para Linux con integración a Ollama y gestión básica de MCPs. 
        • Futuro: Soporte para IDE (VSCode/Neovim), API REST, y extensibilidad multiplataforma.

2. **Requisitos Técnicos Detallados**

    **2.1 Requisitos Funcionales (Expandidos)**

    |--------|---------------------------|----------------------------------------------------------------------------------------|
    | **ID** | **Requisito**             | **Especificación Técnica**                                                             |
    |--------|---------------------------|----------------------------------------------------------------------------------------|
    | RF-01  | GUI Linux                 | PyQt6 con QDarkStyle, soporte para temas claros/oscuros.                               |
    |--------|---------------------------|----------------------------------------------------------------------------------------|
    | RF-02  | Gestión de Modelos Ollama | Consumo de ollama list via subproceso, actualización en tiempo real.                   |
    |--------|---------------------------|----------------------------------------------------------------------------------------|
    | RF-03  | Escaneo de MCPs           | Monitorización de ~/ollama/mcps/ con inotify (Linux).                                  |
    |--------|---------------------------|----------------------------------------------------------------------------------------|
    | RF-04  | Terminal Embebida         | Widget basado en libvte (QTermWidget) con soporte para pestañas y scrollback infinito. |
    |--------|---------------------------|----------------------------------------------------------------------------------------|
    | RF-05  | Seguridad                 | Capa de permisos con confirmación manual (default) y auto-gestión vía config.json.     |
    |--------|---------------------------|----------------------------------------------------------------------------------------|

    **2.2 Requisitos No Funcionales**

    |------------------|-----------------------------------------------------------------------------|
    | **Categoría**    | **Detalle**                                                                 |
    |------------------|-----------------------------------------------------------------------------|
    | *Rendimiento*    | Máximo 2 segundos de latencia en generación de respuestas (modelos <= 13B). |
    |------------------|-----------------------------------------------------------------------------|
    | *Seguridad*      | Hashing de MCPs con SHA-256 para verificación de integridad.                |
    |------------------|-----------------------------------------------------------------------------|
    | *Extensibilidad* | Diseño modular con interfaces claras para añadir nuevos tipos de MCPs.      |
    |------------------|-----------------------------------------------------------------------------|

3. **Arquitectura del Sistema**

    **3.1 Diagrama de Alto Nivel**

    graph LR:
        A[Frontend: PyQt] -->|HTTP REST| B[Backend: FastAPI] 
        B --> C[(SQLite)] 
        B --> D[Ollama Client] 
        B --> E[MCPs Manager] 
        D --> F[Modelos Locales] 
        E --> G[Directorio MCPs] 
        A --> H[Terminal Embebida]

    **3.2 Componentes Principales**

    **3.2.1 Frontend (PyQt)**

    • MainWindow: Contenedor principal con: 
        ◦ MenuBar: Modelos, MCPs, Configuración. 
        ◦ QTermWidget: Terminal con pestañas para logs/salida. 
        ◦ QTextEdit: Área de prompts con resaltado de sintaxis (usando QSyntaxHighlighter).         ◦ 
    • Eventos: 
        ◦ Conexión de señales (ej: clicked en "Enviar") a slots del backend. 


    **3.2.2 Backend (FastAPI)**

    • Endpoints Clave: 
        @app.post("/generate") 
        async def generate(prompt: PromptSchema): 
        # 1. Validar MCPs seleccionados 
        # 2. Inyectar contexto 
        # 3. Llamar a Ollama 
        # 4. Loggear en SQLite 
    • Servicios: 
        ◦ OllamaClient: Gestiona comunicación con Ollama via subprocesos. 
        ◦ MCPsManager: Escanea, valida y carga MCPs (patrón Observer para cambios en disco). 

    **3.2.3 Terminal Embebida**

    • Características: 
        ◦ Soporte para ANSI escape codes (colores). 
        ◦ Buffer circular para manejar grandes volúmenes de logs. 

4. **Diseño de Interfaz (GUI) Detallado**

    **4.1 Estructura de Ventanas**

    • Ventana Principal: 

    +-------------------------------------------+
    | [MenuBar: Modelo | MCPs | Configuración]  |
    +-------------------+-----------------------+
    | Terminal                              | 🗙 |
    | (Pestañas: Logs | Salida)             |   |
    |                                       |   |
    |                                       |   |
    +-------------------------------------------+
    | [QTextEdit: Prompt        ]  | [⚡ Enviar] |
    +-------------------------------------------+

    **4.2 Especificaciones de UI **

    • **Colores:** 
        ◦ Fondo terminal: #2D2D2D (similar a VSCode Dark). 
        ◦ Texto: #EEEEEE, errores en #FF5555. 
    • **Fuentes:** 
        ◦ Terminal: Fira Code 11pt. 
        ◦ Interfaz: Inter Medium 10pt. 

5. **Modelo de Datos y Persistencia**

    **5.1 Esquema de SQLite**

    CREATE TABLE sessions ( 
        session_id TEXT PRIMARY KEY, 
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
    ); 
    
    CREATE TABLE history ( 
        id INTEGER PRIMARY KEY, 
        session_id TEXT REFERENCES sessions(session_id), 
        prompt TEXT NOT NULL, 
        response TEXT, 
        model_used TEXT, 
        mcps_activated TEXT,  -- JSON: ["mcp1", "mcp2"] 
        latency_ms INTEGER, 
        FOREIGN KEY (session_id) REFERENCES sessions(session_id) 
    ); 

    **5.2 Gestión de MCPs**

    • **Estructura de Directorios:**

    ~/ollama/mcps/ 
    ├── python/ 
    │   ├── context.md      # Markdown con ejemplos 
    │   ├── meta.json       # {"author": "...", "lang": "python"} 
    │   └── checksum.sha256 # Validación de integridad 

6. **API REST (Especificación Técnica)**

    **6.1 Endpoints**

    |------------|-----------|-------------------------------------------|----------------------------------------|
    | **Método** | **Ruta**  | **Body (JSON)**                           | **Respuesta**                          |
    |------------|-----------|-------------------------------------------|----------------------------------------|
    | POST       | /generate | {"model": str, "prompt": str, "mcps": []} | {"response": str, "latency": int}      |
    |------------|-----------|-------------------------------------------|----------------------------------------|
    | GET        | /mcps     |                -                          | {"mcps": [{"name": str, "path": str}]} |
    |------------|-----------|-------------------------------------------|----------------------------------------|

    **6.2 Autenticación**

    • **API Key:** Header X-API-Key para futura integración con IDEs. 

7. **Flujos de Trabajo Críticos**

    **7.1 Inicialización del Agente**

    1. Cargar configuración desde ~/.config/agente0110/config.json. 
    2. Escanear ~/ollama/mcps/ y validar checksums. 
    3. Iniciar servidor FastAPI en localhost:8000. 

    **7.2 Ejecución de un Prompt**

    sequenceDiagram:
        Usuario->>Frontend: Escribe prompt + selecciona MCPs 
        Frontend->>Backend: POST /generate 
        Backend->>Ollama: Ejecuta "ollama run modelo" 
        Ollama->>Backend: Respuesta 
        Backend->>SQLite: Guarda historial 
        Backend->>Frontend: Devuelve respuesta 
        Frontend->>Terminal: Muestra logs + salida 

8. **Estrategia de Pruebas**

    **8.1 Pruebas Unitarias**
        • MCPsManager: Verificar escaneo y carga de MCPs. 
        • OllamaClient: Mock de subprocess.Popen para simular respuestas. 

    **8.2 Pruebas de Integración**
        • GUI + Backend: Scripts Selenium para simular interacciones. 

9. **Guía de Implementación**

    **9.1 Setup del Entorno**

    # Instalar dependencias 
    pip install PyQt6 FastAPI uvicorn python-multipart 
    # Clonar repositorio 
    git clone https://github.com/org/agente-0110.git 

    **9.2 Estructura de Código**
    
    src/ 
    ├── gui/                  # PyQt 
    │   ├── main_window.py    # Ventana principal 
    │   └── widgets/          # Componentes reutilizables 
    ├── api/                  # FastAPI 
    │   ├── models.py         # Pydantic schemas 
    │   └── endpoints.py      # /generate, /models 
    ├── core/                 # Lógica de negocio 
    │   ├── ollama.py         # Client Ollama 
    │   └── mcps.py           # Gestor de MCPs 
    └── tests/                # Pruebas 

10. **Roadmap y Siguientes Pasos**

    1. **Sprint 1:** GUI básica + conexión a Ollama (2 semanas). 
    2. **Sprint 2:** Implementar API REST y terminal interactiva (3 semanas). 
    3. **Sprint 3:** Integración con VSCode (extensión TypeScript). 
 
## Roadmap para el Desarrollo del Agente 

Basado en el documento de arquitectura y los requisitos del proyecto, presento un plan de desarrollo modular con fases claras, puntos de integración y estrategia de testing. 

**Visión General del Roadmap**

Fase 1 (MVP Core) → Fase 2 (API e Integraciones) → Fase 3 (Extensibilidad y Optimización) 

**Fase 1: MVP Core**

**Módulo 1:** Interfaz Gráfica Base 
    • **Objetivo:** Ventana principal funcional con componentes básicos 
    • **Componentes:**
        ◦ MainWindow con QTabWidget 
        ◦ Terminal embebida (QTermWidget) 
        ◦ Área de texto para prompts 
        ◦ Selector de modelos Ollama 
    • **Testing:**
        ◦ Pruebas unitarias para widgets individuales 
        ◦ Pruebas de integración GUI-backend básico 

**Módulo 2:** Gestión de Modelos Ollama 
    • **Objetivo:** Integración con Ollama local 
    • **Componentes:** 
        ◦ OllamaClient (subprocesos) 
        ◦ Listado dinámico de modelos 
        ◦ Cambio de modelos en tiempo real 
    • **Testing:** 
        ◦ Mock de ollama list para pruebas unitarias 
        ◦ Pruebas de rendimiento con diferentes modelos 

**Módulo 3:** Sistema de MCPs 
    • **Objetivo:** Gestión completa de MCPs 
    • **Componentes:**
        ◦ Escaneo de directorios con inotify 
        ◦ Previsualización de contenido 
        ◦ Sistema de checksums 
    • **Testing:**
        ◦ Pruebas de sistema de archivos con diferentes estructuras MCP 
        ◦ Validación de integridad de archivos 

**Punto de Control Fase 1**
    • Integración completa de los 3 módulos 
    • Demostración de flujo completo: selección modelo → selección MCP → envío prompt → visualización respuesta 

**Fase 2: Extensión Funcional**

**Módulo 4:** API REST 
    • **Objetivo:** Servicio backend independiente 
    • **Componentes:** 
        ◦ Endpoints FastAPI 
        ◦ Sistema de autenticación 
        ◦ Integración con GUI existente 
    • **Testing:** 
        ◦ Pruebas de carga con Locust 
        ◦ Pruebas de seguridad OWASP 

**Módulo 5:** Terminal Avanzada 
    • **Objetivo:** Mejoras en terminal interactiva 
    • **Componentes:** 
        ◦ Soporte ANSI completo 
        ◦ Historial navegable 
        ◦ Filtrado de logs 

**Módulo 6:** Extensión VSCode 
    • **Objetivo:** Integración con IDE 
    • **Componentes:** 
        ◦ Client TypeScript 
        ◦ Comandos básicos 
        ◦ Panel de control 
    • **Testing:**
        ◦ Pruebas E2E en VSCode 
        ◦ Pruebas de compatibilidad 

**Punto de Control Fase 2**
    • GUI puede operar completamente via API 
    • Extensión VSCode funcional con features básicas 

**Fase 3: Optimización y Crecimiento**

**Módulo 7:** Plugin Neovim 
    • **Objetivo:** Integración con Neovim 
    • **Componentes:** 
        ◦ Comandos Lua 
        ◦ Gestión de buffers 

**Módulo 8:** Sistema Multiusuario 
    • **Objetivo:** Soporte para equipos 
    • **Componentes:** 
        ◦ Autenticación bcrypt 
        ◦ Perfiles de usuario 
        ◦ MCPs compartidos 

**Módulo 9:** Benchmarking 
    • **Objetivo:** Optimización de rendimiento 
    • **Componentes:** 
        ◦ Tests comparativos 
        ◦ Sugerencias de modelos 
        ◦ Cache de respuestas 

**Estrategia de Testing Integral**

1. Pruebas Unitarias (por módulo): 
    ◦ Cobertura >80% por módulo 
    ◦ Mocks para componentes externos (Ollama, sistema de archivos) 

2. Pruebas de Integración (entre módulos): 
    ◦ GUI ↔ Backend 
    ◦ API ↔ Ollama 
    ◦ Extensiones ↔ API 

3. Pruebas E2E (por fase): 
    ◦ Flujos completos de usuario 
    ◦ Escenarios realistas 
    
4. Pruebas de Rendimiento: 
    ◦ Latencia en generación de respuestas 
    ◦ Uso de memoria con modelos grandes 

**Recomendaciones Iniciales**

1. Enfoque Iterativo: Comenzar con el núcleo y expandir 
2. Gestión de Dependencias: Control estricto de versiones (especialmente PyQt ↔ FastAPI) 
3. Documentación Paralela: Mantener docs actualizadas con cada módulo 
4. Sistema de Logging: Implementar desde el inicio para diagnóstico 
 