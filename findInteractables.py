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
slug_path = os.path.join(current_dir, 'images', 'ingame_slug.png')
cameraPath = os.path.join(current_dir, 'images', 'camera.png')
menuPath = os.path.join(current_dir, 'images', 'menuRed.png')
frogPath = os.path.join(current_dir, 'images', 'frog.png')
jar_fairy_path = os.path.join(current_dir, 'images', 'jar_fairy.png')
gift_path = os.path.join(current_dir, 'images', 'gift.png')
butterfly_path = os.path.join(current_dir, 'images', 'butterfly.png')
upgrade_path = os.path.join(current_dir, 'images', 'upgrade.png')

# Active state
active = True

# Counters for all the interactables
slugs_claimed = 0
jars_claimed = 0
gifts_claimed = 0
frogs_claimed = 0
butterflies_claimed = 0

def main():
    
    # Record the start time
    start_time = time.perf_counter()

    print("Finding interactables. A reminder to please run Command Prompt in administrator, the BlueStacks emulator in full screen and on the primary screen.")

    try:
        while is_admin() and active:
            # Find slug by image that is provided and click it
            find_slug = py.locateCenterOnScreen(slug_path, confidence=0.9)
            if find_slug is not None:
                py.click(find_slug)
                time.sleep(3)
                py.click(x=1280, y=715)
                time.sleep(1)
                py.click(x=1280, y=807)
                global slugs_claimed
                slugs_claimed+=1

            # Find frog by image, click it and get rewards
            find_frog = py.locateCenterOnScreen(frogPath, confidence=0.9)
            if find_frog is not None:
                time.sleep(1)
                py.click(find_frog)
                time.sleep(3)
                py.click(x=1280, y=715)
                time.sleep(1)
                py.click(x=1280, y=807)
                global frogs_claimed
                frogs_claimed+=1

            # Find Jar Fairy by image, click it and get rewards
            find_jar_fairy = py.locateCenterOnScreen(jar_fairy_path, confidence=0.9)
            if find_jar_fairy is not None:
                time.sleep(0.3)
                py.click(find_jar_fairy)
                time.sleep(0.3)
                py.click(x=1323, y=944)
                global jars_claimed
                jars_claimed+=1

            # Find gift by image that is provided and click said gift
            find_gift = py.locateCenterOnScreen(gift_path, confidence=0.9)
            if find_gift is not None:
                time.sleep(0.3)
                py.click(find_gift)
                time.sleep(5)
                # Click 1/3 gift (middle gift)
                py.click(x=957, y=628)
                time.sleep(1)
                # Click reward
                py.click(x=957, y=775)
                # Click again to exit gift menu
                time.sleep(1)
                py.click(x=1280, y=1030)
                global gifts_claimed
                gifts_claimed+=1

            # Find butterfly by image, click it and get rewards
            find_butterfly = py.locateCenterOnScreen(butterfly_path, confidence=0.95)
            if find_butterfly is not None:
                time.sleep(0.5)
                py.click(find_butterfly)
                time.sleep(3)
                py.click(x=1280, y=715)
                time.sleep(1)
                py.click(x=1280, y=807)
                butterflies_claimed+=1

            # Function to hold mouse click until image disappears
            def hold_mouse_until_image_gone(image_path):
                # Find the image on the screen
                image_location = py.locateOnScreen(image_path, confidence=0.9)

                # If the image is found
                if image_location is not None:
                    # Get the center coordinates of the image
                    image_center = py.center(image_location)
                    
                    # Simulate moving the mouse to the center of the image
                    py.moveTo(image_center)
                    
                    # Simulate pressing down the mouse button
                    py.mouseDown()

                    # Loop until the image is no longer found
                    while True:
                        # Find the image on the screen again within a region around the original location
                        image_location = py.locateOnScreen(image_path, confidence=0.9, region=image_location)
                        
                        # If the image is not found, exit the loop
                        if image_location is None:
                            break

                        time.sleep(0.1)  # Adjust sleep duration as needed

                    # Release the mouse button
                    py.mouseUp()
                else:
                    # Handle case when image is not found
                    pass

            # Call the function with the relative path to the image
            hold_mouse_until_image_gone(upgrade_path)

    # End result of how long the script was running for and how many interactables were clicked aka claimed
    except KeyboardInterrupt:
        # Record the end time
        end_time = time.perf_counter()

        # Calculate the total time taken
        total_time = end_time - start_time

        # Use divmod() to convert total time to hours, minutes, and seconds
        hours, remainder = divmod(total_time, 3600)
        minutes, seconds = divmod(remainder, 60)    
    
        print("You have been searching for interactables for: {:.0f} hours, {:.0f} minutes, {:.2f} seconds".format(hours, minutes, seconds))

        counters = {"Slugs": slugs_claimed, "Jars": jars_claimed, "Gifts": gifts_claimed, "Frogs": frogs_claimed, "Butterflies ": butterflies_claimed}

        for message, counter in counters.items():
            print(f"{message}: {counter}")


if __name__ == "__main__":
    main()