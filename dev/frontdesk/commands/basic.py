from dev.frontdesk.commands.command import Command
import dev.frontdesk.helper as hlp
import datetime
import webbrowser


class SearchCommand(Command):
    def __init__(self):
        self.name = "google"

    def execute(self):
        hlp.oneline(
            "What would you like to search for? This will take you to Google on your browser."
        )
        query = input("Type your query:")
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
        hlp.oneline(f"Hope the results were helpful!")

    def help(self):
        hlp.oneline("Searches the web for your query.")


class TimeCommand(Command):
    def __init__(self):
        self.name = "time"

    def execute(self):
        current_time = datetime.datetime.now().strftime("%H:%M")
        hlp.oneline(f"The current time is {current_time}.")

    def help(self):
        hlp.oneline("Displays the current time.")


if __name__ == "__main__":
    search_command = SearchCommand()
    search_command.execute()
    search_command.help()

    print(search_command)
