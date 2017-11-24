import core

instructions = core.get_instructions()

for element in instructions:
    print('Instruction:', element['instruction'])
    print('Parameters:', element['actions'])
