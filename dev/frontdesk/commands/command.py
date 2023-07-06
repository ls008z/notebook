class Command:
    def __init__(self):
        self.name = "<command>"

    def __str__(self):
        return f"Command: {self.name}"

    def execute(self):
        print(f"Execution for {self.name} is not implemented.")

    def help(self):
        print(f"Help for {self.name} is not implemented.")


if __name__ == "__main__":
    basic_command = Command()
    basic_command.execute()
    basic_command.help()

    print(basic_command)
