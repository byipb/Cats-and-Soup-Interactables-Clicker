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
slugPath = os.path.join(current_dir, 'images', 'slug.png')
jarFairyPath = os.path.join(current_dir, 'images', 'jarfairy.png')
giftPath = os.path.join(current_dir, 'images', 'giftBubble.png')
frogPath = os.path.join(current_dir, 'images', 'frog.png')
butterflyPath = os.path.join(current_dir, 'images', 'butterfly.png')
upgradePath = os.path.join(current_dir, 'images', 'upgrade.png')

# Active state
active = True

def main():
    # Counters for all the interactables
    slugsClaimed = 0
    jarsClaimed = 0
    giftsClaimed = 0
    frogsClaimed = 0
    butterfliesClaimed = 0

    # Record the start time
    start_time = time.perf_counter()

    print("Finding interactables.")

    try:
        while is_admin() and active:
            # Find slug by image that is provided and click it
            findSlug = py.locateCenterOnScreen(slugPath, confidence=0.9)
            if findSlug is not None:
                py.click(findSlug)
                time.sleep(1)
                py.click(x=1280, y=715)
                time.sleep(1)
                py.click(x=1280, y=807)
                slugsClaimed+=1

            # Find frog by image, click it and get rewards
            findFrog = py.locateCenterOnScreen(frogPath, confidence=0.9)
            if findFrog is not None:
                time.sleep(1)
                py.click(findFrog)
                time.sleep(1)
                py.click(x=1280, y=715)
                time.sleep(1)
                py.click(x=1280, y=807)
                frogsClaimed+=1

            # Find Jar Fairy by image, click it and get rewards
            findJarFairy = py.locateCenterOnScreen(jarFairyPath, confidence=0.9)
            if findJarFairy is not None:
                time.sleep(0.3)
                py.click(findJarFairy)
                time.sleep(0.3)
                py.click(x=1323, y=944)
                jarsClaimed+=1

            # Find gift by image that is provided and click said gift
            findGift = py.locateCenterOnScreen(giftPath, confidence=0.9)
            if findGift is not None:
                time.sleep(0.3)
                py.click(findGift)
                time.sleep(5)
                # Click 1/3 gift (middle gift)
                py.click(x=1280, y=848)
                time.sleep(1)
                # Click reward
                py.click(x=1280, y=1030)
                # Click again to exit gift menu
                time.sleep(1)
                py.click(x=1280, y=1030)
                giftsClaimed+=1

            # Find butterfly by image, click it and get rewards
            findButterfly = py.locateCenterOnScreen(butterflyPath, confidence=0.95)
            if findButterfly is not None:
                time.sleep(0.3)
                py.click(findButterfly)
                time.sleep(0.3)
                py.click(x=1280, y=715)
                time.sleep(1)
                py.click(x=1280, y=807)
                butterfliesClaimed+=1

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
            hold_mouse_until_image_gone(upgradePath)

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

        counters = {"Slugs": slugsClaimed, "Jars": jarsClaimed, "Gifts": giftsClaimed, "Frogs": frogsClaimed, "Butterflies ": butterfliesClaimed}

        for message, counter in counters.items():
            print(f"{message}: {counter}")

if __name__ == "__main__":
    main()