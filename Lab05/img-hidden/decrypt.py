import sys
from PIL import Image

def decode_image(encoded_image_path):
    img = Image.open(encoded_image_path)
    width, height = img.size
    binary_message = ""
    
    # Duyệt qua từng pixel để trích xuất các bit cuối cùng (LSB)
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            
            # Duyệt qua 3 kênh màu (R, G, B)
            for color_channel in range(3):
                # Lấy bit cuối cùng của kênh màu hiện tại và nối vào chuỗi nhị phân
                binary_message += format(pixel[color_channel], '08b')[-1]

    message = ""
    # Chuyển đổi chuỗi bit nhị phân thành các ký tự (mỗi ký tự chiếm 8 bit)
    for i in range(0, len(binary_message), 8):
        char = chr(int(binary_message[i:i+8], 2))
        
        # Kết thúc thông điệp khi gặp dấu hiệu dừng '\0' (hoặc lính canh kết thúc)
        if char == '\0':  # Kết thúc thông điệp khi gặp dấu '\0'
            break
        message += char
        
    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return
        
    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()