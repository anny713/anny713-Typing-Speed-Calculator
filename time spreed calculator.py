import time

def calculate_typing_speed(text, start_time, end_time):
    words = text.split()
    num_words = len(words)
    
    elapsed_time = end_time - start_time
    minutes = elapsed_time / 60 
    wpm = num_words / minutes

    return wpm

if __name__ == '__main__':
    text = "The quick brown fox jumps over the lazy dog"
    
    print("Type the following text:")
    print(text)
    
    input("Press Enter when you are ready to start typing...")
    
    start_time = time.time()
    user_input = input("Type the text above and press Enter:\n")
    end_time = time.time()
    
    typing_speed = calculate_typing_speed(user_input, start_time, end_time)
    
    print(f"Your typing speed is: {typing_speed} words per minute")
