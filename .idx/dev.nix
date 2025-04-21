# To learn more about how to use Nix to configure your environment
# see: https://firebase.google.com/docs/studio/customize-workspace
{pkgs, ... }: {
	# Which nixpkgs channel to use.
	channel = "stable-24.05"; # or "unstable"
	# Use https://search.nixos.org/packages to find packages
	packages = [
		(pkgs.python312.withPackages (ps: with ps; [
			pyqt6
			pyte
			fastapi
			uvicorn
			python-multipart
			
		]))
		pkgs.qt6.qtbase
	];
	# Sets environment variables in the workspace
	env = {
		PYTHONPATH = "${toString ./.}";
		QT_QPA_PLATFORM = "offscreen";  # Modo sin display
		QT_PLUGIN_PATH = "${pkgs.qt6.qtbase}/${pkgs.qt6.qtbase.qtPluginPrefix}";
	};
	idx = {
		# Search for the extensions you want on https://open-vsx.org/ and use "publisher.id"
		extensions = [
			"ms-python.python"  # Extensión oficial de Python para VS Code
			# "vscodevim.vim"
		];
		# Enable previews
		previews = {
			enable = true;
			previews = {
				# web = {
				#   # Example: run "npm run dev" with PORT set to IDX's defined port for previews,
				#   # and show it in IDX's web preview panel
				#   command = ["npm" "run" "dev"];
				#   manager = "web";
				#   env = {
				#     # Environment variables to set for your server
				#     PORT = "$PORT";
				#   };
				# };
			};
		};
		# Workspace lifecycle hooks
		workspace = {
			# Runs when a workspace is first created
			onCreate = {
				# Example: install JS dependencies from NPM
				# npm-install = "npm install";
				# Open editors for the following files by default, if they exist:
				default.openFiles = [ ".idx/dev.nix" "README.md" ];
			};
			# Runs when the workspace is (re)started
			onStart = {
				# Example: start a background task to watch and re-build backend code
				# watch-backend = "npm run watch-backend";
			};
		};
	};
}
