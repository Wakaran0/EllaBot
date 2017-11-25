import core

instructions = core.get_instructions()

for element in instructions:
    print('Instruction:', element['instruction'])
    print('Parameters:', element['actions'])

print(core.get_corresponding_instructions('a', instructions))
