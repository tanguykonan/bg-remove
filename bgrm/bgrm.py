"""========================= 
*** Author : github.com/tanguykonan
****** Name : bgrm
********* Version : 1.0.0
************ Description : A CLI tool to image processing.
=================================================================
"""

try:
    import os
    import logging
    import argparse
    from rembg import remove
    from PIL import Image
    from datetime import datetime
except Exception as error:
    print(f"[IMPORT ERROR]: {error}")

try:
    base_dir = os.path.dirname(__file__)
    logs_dir = os.path.join(base_dir, "logs")
    logs_file = os.path.join(logs_dir, "bgrm.log")

    os.makedirs(logs_dir, exist_ok = True)
    if not os.path.exists(logs_file):
        open(logs_file, "w").close()
except Exception as error:
    print(f"[LOGS-PATH CREATION ERROR]: {error}")

try:
    logger = logging.getLogger('bgrm')
    logger.setLevel(logging.INFO)
    log_handler = logging.FileHandler(
        logs_file,
        encoding='utf-8'
    )
    log_handler.setFormatter(
        logging.Formatter(
            '[%(levelname)s] %(asctime)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    )
    logger.handlers = []
    logger.addHandler(log_handler)
except Exception as error:
    print(f"[LOGGER INITIALISATION ERROR]: {error}")

def main():

    try :
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", "--image", help = "The param \"Image\". Use to remove image background.", type = str)
        parser.add_argument("-g", "--get", help = "The param \"Get\". Use to get user history about bgrm.", type = str)
        parser.add_argument("-v", "--version", action = "store_true", help = "The param \"Version\". Use to know bgrm version.")
        parser.add_argument("-c", "--clean", action = "store_true", help = "The param \"Clean\". Use to clean user history.")
        args = parser.parse_args()

        param_image = args.image
        param_get = args.get
        param_version = args.version
        param_cls = args.clean
    except Exception as error:
        print(f"[BGRM INITIALISATION ERROR]: {error}")

    try :
        if param_image:
            if param_image.endswith((".png",".jpg",".jpeg")):
                input_path = param_image
                output_path = "bgrm-"+input_path
                inp = Image.open(input_path)
                output = remove(inp)
                output.save(output_path, "PNG")
                Image.open(output_path)
                logger.info(f"[Succes]:[Input: {input_path}]-[Output: {output_path}]")
                print(f"Successful: {input_path} background as been remove to {output_path}")
            else:
                print(f"[Failure]-> {param_image} is not valid for opion \"i\".")
                logger.warning(f"[Failure]-> {param_image} is not valid for opion \"i\".")

        if param_get:
            if param_get == "logs":
                with open(logs_file, "r", encoding="utf-8") as log:
                    for ligne in log:
                        print(ligne, end="")
            else:
                print(f"[Failure]-> {param_get} is not valid for opion \"g\".")
                logger.warning(f"[Failure]-> {param_get} is not valid for opion \"g\".")
        
        if param_version:
            msg = "bgrm 1.0.0"
            print(msg)
        
        if param_cls:
            with open(logs_file, "w", encoding = "utf-8") as log:
                print(f"Successful: User history as been clean.")

    except Exception as error:
        print(f"[BGRM EXECUTION ERROR]: {error}")

if __name__ == "__main__":
    main()