import datetime
import dev.frontdesk.commands as commands
import dev.frontdesk.helper as hlp


class NoteTaker:
    def __init__(self):
        self.start_time = datetime.datetime.now().strftime("%H:%M")
        self.commands_names = commands.command_names
        self.command_dict = commands.command_dict

    def print_commands(self):
        print("Here is a list of commands:\n")
        for command in self.commands:
            print("    --  " + command.name)
        print("    --  help")
        print("    --  exit")
        print("\nHow can I help you?")

    def greet(self):
        current_hour = datetime.datetime.now().hour
        if current_hour < 12:
            greeting = "Good morning!"
        elif 12 <= current_hour < 18:
            greeting = "Good afternoon!"
        else:
            greeting = "Good evening!"

        hlp.top_padding()
        print(greeting)
        print(f"The current time is {self.start_time}.")
        self.print_commands()
        hlp.bottom_padding()

    def process_command(self, command):
        if command in self.commands_names:
            self.command_dict[command].execute()
        elif command == "help":
            hlp.top_padding()
            self.print_commands()
            hlp.bottom_padding()
        elif command == "bye" or command == "exit":
            hlp.oneline("Goodbye!")
        else:
            hlp.top_padding()
            print(f"Sorry, I don't understand {command}.\n")
            self.print_commands()
            hlp.bottom_padding()

    def run(self):
        self.greet()
        while True:
            command = input("Enter your command: ")
            self.process_command(command.lower())
            if command.lower() == "bye" or command.lower() == "exit":
                break


if __name__ == "__main__":
    note_taker = NoteTaker()
    note_taker.run()
