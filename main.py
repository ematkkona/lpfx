import argparse
import cmd
from controller import LaunchpadController
from scripting.script_runner import ScriptRunner

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

def main():
    parser = argparse.ArgumentParser(description="Launchpad FX Controller")
    parser.add_argument("--script", type=str, help="Path to FX script file (.fx)")
    parser.add_argument("--live", action="store_true", help="Start interactive live scripting shell")
    args = parser.parse_args()

    controller = LaunchpadController()

    if args.script:
        runner = ScriptRunner(controller)
        runner.load_and_run(args.script)
    elif args.live:
        shell = LiveShell(controller)
        shell.cmdloop()
    else:
        controller.run_loop()

if __name__ == "__main__":
    main()
