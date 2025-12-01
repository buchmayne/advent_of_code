"""
Following the same rotations as in the above example, the dial points at zero a few extra times during its rotations:

    The dial starts by pointing at 50.
    The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
    The dial is rotated L30 to point at 52.
    The dial is rotated R48 to point at 0.
    The dial is rotated L5 to point at 95.
    The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
    The dial is rotated L55 to point at 0.
    The dial is rotated L1 to point at 99.
    The dial is rotated L99 to point at 0.
    The dial is rotated R14 to point at 14.
    The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.

In this example, the dial points at 0 three times at the end of a rotation, plus three more times during a rotation. So, in this example, the new password would be 6.
"""
f = open("input_data.txt", "r")
data = f.read().split("\n")

f = open("test_data.txt", "r")
test_data = f.read().split("\n")

def part_1(data: list) -> int:
    position: int = 50
    count_dial_pointed_to_zero: int = 0
    for rotation in data:
        direction: str = rotation[0]
        distance_str: str = rotation[1:]
        if len(distance_str) > 2:
            distance: int = int(distance_str[-2:])
        else:
            distance: int = int(distance_str)
        
        if direction == 'L':
            raw_position: int = position - distance
            if raw_position < 0:
                position: int = 100 + raw_position
            else:
                position: int = raw_position
        
        elif direction == 'R':
            raw_position: int = position + distance
            if raw_position > 99:
                position: int = raw_position - 100
            else:
                position:int = raw_position
        
        if position == 0:
            count_dial_pointed_to_zero += 1

    return count_dial_pointed_to_zero

def part_2(data: list) -> int:
    position: int = 50
    count_dial_pointed_to_zero: int = 0
    count_dial_clicked_zero: int = 0
    count_full_spins: int = 0
    
    for rotation in data:
        direction: str = rotation[0]
        distance_str: str = rotation[1:]
        
        if len(distance_str) > 2:
            distance: int = int(distance_str[-2:])
            count_full_spins += int(distance_str[:len(distance_str) - 2])
        else:
            distance: int = int(distance_str)
        
        if direction == 'L':
            raw_position: int = position - distance
            if raw_position < 0:
                if position != 0:
                    count_dial_clicked_zero += 1
                position: int = 100 + raw_position
                
            else:
                position: int = raw_position
        
        elif direction == 'R':
            raw_position: int = position + distance
            if raw_position >= 100:
                position: int = raw_position - 100
                if position != 0:
                    count_dial_clicked_zero += 1
            else:
                position: int = raw_position
        
        if position == 0:
            count_dial_pointed_to_zero += 1
        
        print(f"{rotation}, {position}, points {count_dial_clicked_zero}, position {count_dial_pointed_to_zero}")

    part_2_solution: int = count_dial_clicked_zero + count_full_spins + count_dial_pointed_to_zero
    
    return part_2_solution

def test_part_1():
    assert part_1(test_data) == 3, "Incorrect Solution to Part 1"

def test_part_2():
    assert part_2(test_data) == 6, "Incorrect Solution to Part 2"

if __name__ == "__main__":
    part_1_solution: int = part_1(data)
    part_2_solution: int = part_2(data)
    
    test_part_1()
    test_part_2()
    
    print(f"Part 1: {part_1_solution}\nPart 2: {part_2_solution}")