import os
import sys
from pretty_help import PrettyHelp
import yaml
from discord.ext import commands


def handle_exception(exctype, value, traceback):
    """
    Handle exceptions (for config.yml) at a global level.
    """
    if exctype == KeyError:
        print(f'The key {value} was not found in your config.yml. Please make sure your config.yml matches the '
              f'structure of config.example.yml')
        sys.exit(1)
    else:
        sys.__excepthook__(exctype, value, traceback)


sys.excepthook = handle_exception

try:
    config = yaml.load(open('config.yml'), Loader=yaml.CLoader)
except:
    print('The config.yaml file could not be loaded.')
    sys.exit(1)

bot = commands.Bot(command_prefix=commands.when_mentioned_or(config['prefix']),
                   case_insensitive=True,
                   owner_id=287888563020890138,
                   help_command=PrettyHelp(sort_commands=True, color=0xeb4034)
                   )

if __name__ == '__main__':
    print('[Categories]'.center(30, '-') + '\n')
    """
    Load all the commands present in the commands folder.
    """
    for directory in os.listdir('commands'):
        for file in os.listdir(f'commands\\{directory}'):
            if file.endswith('.py') and not file.startswith('_'):
                bot.load_extension(f'commands.{directory}.{file[:-3]}')
                print(f'Loaded the category: {file}')

    print('\n' + '[Events]'.center(30, '-') + '\n')
    """
    Load all the events present in the events folder.
    """
    for file in os.listdir('events'):
        if file.endswith('.py') and not file.startswith('_'):
            bot.load_extension(f'events.{file[:-3]}')
            print(f'Loaded the event: {file}')

    print('\n' + ''.center(30, '-') + '\n')

    bot.run(config['token'])
