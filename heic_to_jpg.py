#!/home/your-username/dir-to-script/name-of-venv/bin/python3

'''Make the above line point to your python3 executable in your virtual environment.'''

#from PIL import Image

import argparse
import sys

def verify_dependencies():
    """ Verify that required dependencies are installed."""
    missing = []
    
    #try PIL / Pillow
    try:
        from PIL import Image
    except (ImportError, ModuleNotFoundError):
        missing.append("Pillow (PIL)")
    
    # Check pillow_heif
    try:
        import pillow_heif
    except (ImportError, ModuleNotFoundError):
        missing.append("pillow_heif")
    
    if missing:
        # Convert list to lower case matching pip names: 'pillow' and 'pillow-heif'
        pip_names = [name.lower().replace("_", "-") for name in missing]
        print(f"[-] Missing dependencies: {', '.join(missing)}")
        print(f"[->] Please run: pip install {' '.join(pip_names)}")
        sys.exit(1)
    return Image, pillow_heif

if __name__ == '__main__':
    args = argparse.ArgumentParser(description="Convert HEIC images to JPEG format.")
    args.add_argument('heic_file', type=str, help="Path to the HEIC file to convert.")
    args.add_argument('-o', '--output-file', type=str, default='output.jpg', help="Path to save the converted JPEG file.")
    args.add_argument('-q', '--quality', type=int, default=95, help="JPEG quality (1-100). Default is 95.")
    args = args.parse_args()
    
    # verify dependencies and import modules
    Image, pillow_heif = verify_dependencies()
    print(f"[+] Verification Successful!")
    print(f"   • Pillow version: {Image.__version__}")
    print(f"   • pillow_heif version: {pillow_heif.__version__}")
    print("-" * 40)

    # register HEIF opener with Pillow
    pillow_heif.register_heif_opener()

    try:
        # Open HEIC image
        image = Image.open(args.heic_file)
        # Convert to RGB (if needed) and save as JPEG
        image.convert('RGB').save(args.output_file, 'JPEG', quality=args.quality)
        print(f"[+] Successfully converted '{args.heic_file}' -> '{args.output_file}'")
    except Exception as e:
        print(f"[!] Error occurred: {e}")
        sys.exit(1)
