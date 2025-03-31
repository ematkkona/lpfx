import argparse
import cmd
import os
from lpfx.controller import LaunchpadController
from lpfx.scripting.script_runner import ScriptRunner

class LiveShell(cmd.Cmd):
    intro = "🎛️ Launchpad FX Interactive Shell. Type fx commands or 'help'."
    prompt = "🎛️> "

    def __init__(self, controller):
        super().__init__()
        self.runner = ScriptRunner(controller)

    def default(self, line):
        if line.startswith("fx") or line.startswith("wait") or line.startswith("loop"):
            try:
                exec(f"self.runner.{line}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Unknown command. Use fx(), wait(), or loop().")

    def do_list(self, arg):
        fx_dir = os.path.dirname(__file__)
        fx_files = [f for f in os.listdir(fx_dir) if f.endswith(".fx")]
        if not fx_files:
            print("No .fx scripts found.")
        else:
            print("Available FX scripts:")
            for f in fx_files:
                print(f"  - {f}")

    def do_run(self, filename):
        fx_path = os.path.join(os.path.dirname(__file__), filename)
        if not os.path.exists(fx_path):
            print(f"Script '{filename}' not found.")
            return
        try:
            self.runner.load_and_run(fx_path)
        except Exception as e:
            print(f"Failed to run '{filename}': {e}")

    def complete_run(self, text, line, begidx, endidx):
        fx_dir = os.path.dirname(__file__)
        files = [f for f in os.listdir(fx_dir) if f.endswith(".fx")]
        return [f for f in files if f.startswith(text)]


def list_fx_scripts():
    fx_dir = os.path.dirname(__file__)
    fx_files = [f for f in os.listdir(fx_dir) if f.endswith(".fx")]
    if not fx_files:
        print("No .fx scripts found.")
    else:
        print("Available FX scripts:")
        for f in fx_files:
            print(f"  - {f}")


def main():
    parser = argparse.ArgumentParser(description="Launchpad FX Controller")
    parser.add_argument("--script", type=str, help="Path to FX script file (.fx)")
    parser.add_argument("--live", action="store_true", help="Start interactive live scripting shell")
    parser.add_argument("--list", action="store_true", help="List available .fx scripts")

    args = parser.parse_args()

    controller = LaunchpadController()

    if args.script:
        runner = ScriptRunner(controller)
        runner.load_and_run(args.script)
    elif args.live:
        shell = LiveShell(controller)
        shell.cmdloop()
    elif args.list:
        list_fx_scripts()
        return
    else:
        controller.run_loop()

if __name__ == "__main__":
    main()
