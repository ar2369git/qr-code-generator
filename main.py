#!/usr/bin/env python3
import argparse
import os
import sys
import qrcode

def generate_qr(url: str, output_dir: str):
    # ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    img = qrcode.make(url)
    output_path = os.path.join(output_dir, "qr.png")
    img.save(output_path)
    print(f"Saved QR code for {url} → {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Generate a QR code for a URL.")
    parser.add_argument(
        "--url", "-u",
        required=True,
        help="The URL to encode in the QR code."
    )
    parser.add_argument(
        "--out", "-o",
        default="qr_codes",
        help="Output directory for generated QR codes."
    )
    args = parser.parse_args()

    generate_qr(args.url, args.out)

if __name__ == "__main__":
    main()
