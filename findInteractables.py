import pyautogui as py
import ctypes, sys
import time
import os

# Requires Admin permission (CMD) for mouse clicks
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# The current working directory is the directory where the script is running from
current_dir = os.getcwd()

# Create a relative path to the folder with images
slugPath = os.path.join(current_dir, 'images', 'ingame_slug.png')
jarFairyPath = os.path.join(current_dir, 'images', 'jarfairy.png')
giftPath = os.path.join(current_dir, 'images', 'giftBubble.png')
cameraPath = os.path.join(current_dir, 'images', 'camera.png')
menuPath = os.path.join(current_dir, 'images', 'menuRed.png')
frogPath = os.path.join(current_dir, 'images', 'frog.png')
balloonPath = os.path.join(current_dir, 'images', 'balloon.png')

# Counters for all the interactables
slugsClaimed = 0
jarsClaimed = 0
giftsClaimed = 0
camerasClaimed = 0
frogsClaimed = 0
balloonsClaimed = 0

# Record the start time
start_time = time.perf_counter()

print("Finding interactables. A reminder to please run Command Prompt in administrator, the BlueStacks emulator in full screen and on the primary screen.")

try:
    while is_admin():
        # Find slug by image that is provided and click it
        findSlug = py.locateCenterOnScreen(slugPath, confidence=0.9)
        if findSlug is not None:
            py.click(findSlug)
            time.sleep(1)
            py.click(x=960, y=523)
            time.sleep(1)
            py.click(x=960, y=604)
            slugsClaimed+=1

        # Find frog by image, click it and get rewards
        findFrog = py.locateCenterOnScreen(frogPath, confidence=0.9)
        if findFrog is not None:
            time.sleep(1)
            py.click(findFrog)
            time.sleep(1)
            py.click(x=960, y=523)
            time.sleep(1)
            py.click(x=960, y=604)
            frogsClaimed+=1

        # Find Jar Fairy by image, click it and get rewards
        findJarFairy = py.locateCenterOnScreen(jarFairyPath, confidence=0.9)
        if findJarFairy is not None:
            time.sleep(0.3)
            py.click(findJarFairy)
            time.sleep(0.3)
            py.click(x=997, y=711)
            jarsClaimed+=1

        # Find gift by image that is provided and click said gift
        findGift = py.locateCenterOnScreen(giftPath, confidence=0.9)
        if findGift is not None:
            time.sleep(0.3)
            py.click(findGift)
            time.sleep(5)
            # Click 1/3 gift (middle gift)
            py.click(x=957, y=628)
            time.sleep(1)
            # Click reward
            py.click(x=957, y=775)
            # Click again to exit gift menu
            time.sleep(1)
            py.click(x=957, y=775)
            giftsClaimed+=1

        # Find camera by image, click it and get rewards
        findCamera = py.locateCenterOnScreen(cameraPath, confidence=0.95)
        if findCamera is not None:
            time.sleep(0.3)
            py.click(findCamera)
            time.sleep(0.3)
            py.click(x=956, y=865)
            time.sleep(1)
            py.click(x=956, y=865)
            camerasClaimed+=1

        # Refresh Herb Stand and Cook Library buffs
        refreshFoodBuff = py.locateCenterOnScreen(menuPath, confidence=0.9)
        if refreshFoodBuff is not None:
            time.sleep(0.3)
            py.click(refreshFoodBuff)
            time.sleep(0.3)
            # Refresh Herb Stand buff
            py.click(x=857, y=663)

            py.click(refreshFoodBuff)
            time.sleep(0.3)
            # Refresh Cook Library buff
            py.click(x=961, y=653)

        # Record the end time
        end_time = time.perf_counter()

        # Calculate the total time taken
        total_time = end_time - start_time

        # Use divmod() to convert total time to hours, minutes, and seconds
        hours, remainder = divmod(total_time, 3600)
        minutes, seconds = divmod(remainder, 60)

# End result of how long the script was running for and how many interactables were clicked aka claimed
except KeyboardInterrupt:
    print("You have been searching for interactables for: {:.0f} hours, {:.0f} minutes, {:.2f} seconds".format(hours, minutes, seconds))

    counters = {"Slugs": slugsClaimed, "Jars": jarsClaimed, "Gifts": giftsClaimed, "Cameras": camerasClaimed, "Frogs": frogsClaimed}

    for message, counter in counters.items():
        print(f"{message}: {counter}")