from dev.frontdesk.commands.basic import TimeCommand, SearchCommand

# instantiate the commands
time_command = TimeCommand()
search_command = SearchCommand()

# create a list of commands
commands = [time_command, search_command]

# --------------------------------------------------
# below should be automatically generated from
# the commands list above

# create a dictionary of commands
command_dict = {i.name: i for i in commands}

# number of commands
num_commands = len(commands)

# create a list of command names
command_names = [i.name for i in commands]
