def compose(notes, moves, start_position):
    song = []
    position = start_position

    for move in moves:
        position = (position + move) % len(notes)
        song.append(notes[position])

    return song

def main():
    result = compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
    print(result)

if __name__ == "__main__":
    main()
