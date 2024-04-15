import serial
import keyboard

# Arduino'nun bağlı olduğu seri portu ve baud oranını belirtin
ser = serial.Serial('COM3', 9600)  # 'COM3' kısmını Arduino'nun bağlı olduğu port ile değiştirin

while True:
    # Arduino'dan gelen veriyi okuyun
    arduino_data = ser.readline().decode().strip()
    
    # Veriyi işleyin
    button1_state = int(arduino_data[0])
    button2_state = int(arduino_data[1])
    joystick_x_value = int(arduino_data[2:5])
    joystick_y_value = int(arduino_data[5:8])
    joystick_button_state = int(arduino_data[8])
    
    # Burada oyun kontrollerini simüle edebilirsiniz
    # Örneğin, joystick değerlerini kullanarak karakterinizi hareket ettirebilirsiniz
    # Buton durumlarını kullanarak ateş etme gibi eylemleri gerçekleştirebilirsiniz
    
    # Bu örnekte, joystick değerlerini WASD tuşlarına, butonları da boşluk ve sol shift tuşlarına atıyoruz
    keyboard.press('w' if joystick_y_value < 300 else 's' if joystick_y_value > 700 else '')
    keyboard.press('a' if joystick_x_value < 300 else 'd' if joystick_x_value > 700 else '')
    keyboard.press('space' if joystick_button_state == 1 else '')
    keyboard.press('shift' if button1_state == 1 else '')
    
    # Tuşların serbest bırakılmasını sağlamak için tuşları serbest bırakın
    keyboard.release('w' if joystick_y_value < 300 else 's' if joystick_y_value > 700 else '')
    keyboard.release('a' if joystick_x_value < 300 else 'd' if joystick_x_value > 700 else '')
    keyboard.release('space' if joystick_button_state == 1 else '')
    keyboard.release('shift' if button1_state == 1 else '')

# Seri bağlantıyı kapat
ser.close()
