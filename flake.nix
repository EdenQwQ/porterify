{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
    treefmt-nix.url = "github:numtide/treefmt-nix";
  };

  outputs =
    { ... }@inputs:
    inputs.flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [ "x86_64-linux" ];
      imports = [
        inputs.treefmt-nix.flakeModule
      ];
      perSystem =
        { pkgs, ... }:
        let
          python = pkgs.python312;
          pythonEnv = python.withPackages (
            ps: with ps; [
              wand
            ]
          );
        in
        {
          devShells.default = pkgs.mkShellNoCC {
            buildInputs = [
              pythonEnv
            ];
            shellHook = ''
              fish
            '';
          };

          packages = rec {
            default = porterify;
            porterify = pkgs.writeShellScriptBin "porterify" ''${pythonEnv}/bin/python ${./porterify.py}'';
          };
          treefmt = {
            projectRootFile = "flake.nix";
            programs.nixfmt.enable = true;
            programs.ruff-format.enable = true;
          };
        };
    };
}
