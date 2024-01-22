import platform
import psutil
import socket
import os
import argparse

def get_distro_info():
    return platform.linux_distribution()

def get_memory_info():
    memory = psutil.virtual_memory()
    return {
        'total': memory.total,
        'used': memory.used,
        'free': memory.free
    }

def get_cpu_info():
    cpu_info = {
        'model': platform.processor(),
        'core_count': psutil.cpu_count(logical=False),
        'thread_count': psutil.cpu_count(logical=True),
        'speed': psutil.cpu_freq().current
    }
    return cpu_info

def get_user_info():
    return os.getlogin()

def get_load_average():
    return os.getloadavg()

def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

def main():
    parser = argparse.ArgumentParser(description='Get system information.')
    parser.add_argument('-d', '--distro', action='store_true', help='Get distro info')
    parser.add_argument('-m', '--memory', action='store_true', help='Get memory info')
    parser.add_argument('-c', '--cpu', action='store_true', help='Get CPU info')
    parser.add_argument('-u', '--user', action='store_true', help='Get current user')
    parser.add_argument('-l', '--load', action='store_true', help='Get system load average')
    parser.add_argument('-i', '--ip', action='store_true', help='Get IP address')

    args = parser.parse_args()

    if args.distro:
        print("Distro Info:", get_distro_info())

    if args.memory:
        print("Memory Info:", get_memory_info())

    if args.cpu:
        print("CPU Info:", get_cpu_info())

    if args.user:
        print("Current User:", get_user_info())

    if args.load:
        print("Load Average:", get_load_average())

    if args.ip:
        print("IP Address:", get_ip_address())

if __name__ == "__main__":
    main()