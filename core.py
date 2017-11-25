
def get_instructions():
    """ Returns a list which contains all the possible instructions of the bot

    Returns
    -------
    instructions: List which contains the structured data of each instruction of the bot (List)

    Note
    ----
    Structure of an instruction:
        - instruction : The instruction entered by the user (str)
        - actions : List of the actions which are linked to the instruction (List with str)
    """

    # Open the file which contains all the instructions
    instructions_file = open('data/instructions.txt', 'r')

    # Create a list which contains all the lines of the file
    lines = instructions_file.readlines()

    # Create a list which contains all the structured instructions
    instructions = []

    # Get information from the lines of the file and set the structure of the instructions

    for line in lines:

        # Check if the data is not a comment
        if not (line.startswith('#') or line == "\n"):
            # Split the instruction and the actions
            data = str.split(line, ' ')

            # Create the structured data of the instruction
            instruction = {'instruction': data[0], 'actions': data[1:]}

            # Delete the '\n' of the last action
            if len(instruction['actions']) > 0:
                instruction['actions'][-1] = instruction['actions'][-1][:-1]
            else:
                print('[Warning] The instruction %s has not any action ! Fix that pls dev_sama...' % instruction['instruction'])

            # Add the instruction to the list which is going to be returned
            instructions.append(instruction)

    # Finally close the file and return the instructions

    instructions_file.close()

    return instructions


def get_corresponding_instructions(word, instructions):
    """  Returns a list of corresponding instructions to the given word

    Parameters
    ----------
    word: Word which can correspond with an instruction (str)
    instructions: The list of all the instructions of the bot (List)

    Returns
    -------
    corresponding_instructions: The list of the corresponding instructions (List)
    """

    # Create the list which is going to stock the corresponding instructions
    corresponding_instructions = []

    # Add the corresponding instructions to the list which is going to be returned

    for instruction in instructions:

        if instruction['instruction'].startswith(word):
            corresponding_instructions.append(instruction)

    # Finally return the corresponding instructions
    return corresponding_instructions

