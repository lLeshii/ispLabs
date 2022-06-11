from serializer import own_serializer
import argparse

def main():
    parser = argparse.ArgumentParser(description="Argument Parser")
    parser.add_argument('src', type=str, help='Source file')
    parser.add_argument('dest', type=str, help='Destination file')
    parser.add_argument('file_ext', type=str, help='New file extension')

    arg_list = parser.parse_args()
    serializer = own_serializer.Serializer(arg_list.src, arg_list.file_ext)

    obj = serializer.load()
    serializer.path = arg_list.dest
    serializer.ser_nam = arg_list.file_ext.lower()
    serializer.dump(obj)

    print(f"You are master of the gym")
print(f".")
print(f"⠄⠄⠄⠄⠄⢀⣀⣀⣤⡶⢖⡻⢟⣻⠿⠢⠄⣀")
print(f"⠄⠄⣀⢔⡾⣫⢿⢋⠈⠄⡜⡩⠄⠄⠤⠤⠤⠤⠽⣆")
print(f"⢀⣰⢉⢸⡀⢇⡜⢎⣤⣷⣧⣧⣮⣤⡄⠒⠒⠚⠿⠿⣧")
print(f"⢸⣰⢕⣵⣷⣼⠄⣾⣿⠟⠛⠉⠛⠛⠛⠿⢶⣄⣀⡀⠘⡄")
print(f"⢏⠡⢸⣿⢿⣿⠟⠑⠁⠄⡤⡇⠄⠄⠄⠄⠄⠘⢷⠻⣷⡇")
print(f"⢸⢡⡿⠁⡩⠋⠄⠄⠄⠄⡿⠄⠄⠄⠄⠄⠄⠄⠘⣇⢨⢳")
print(f"⠸⡾⡅⠄⠄⠄⠄⠄⠄⡀⠃⣠⣴⡶⠶⠶⠦⠄⠄⢻⣴⣷")
print(f"⠄⢱⣷⡀⠄⢀⣤⣶⡾⡀⠄⣉⣰⣶⠖⠛⠗⠒⠄⠈⢿⣿⣿⡆")
print(f"⠄⠄⢻⣇⠠⢟⣭⠦⢴⠚⡄⠨⡇⠬⠟⠖⠄⠄⠄⠄⠄⢿⢾⣸")
print(f"⠄⠄⠈⠿⡄⠈⠁⠐⠈⠰⠄⠄⠿⠄⢆⠄⠄⠄⠄⠄⠄⢤⢓⡏")
print(f"⠄⠄⠈⡿⣧⡀⠄⠄⠄⠳⢣⣀⡼⠂⠄⠄⢈⣱⠄⠄⠄⢸⠉")
print(f"⠄⠄⠄⢂⠻⣇⠄⠄⠄⠁⠄⢀⡳⢔⡳⢞⡏⢸⠄⠄⠄⢸")
print(f"⠄⠄⠄⠄⠑⠚⡆⠰⠄⠐⠾⠍⠠⢑⣀⠕⠄⠘⠄⠄⢀⣾")
print(f"⠄⠄⠄⠄⠄⠄⢸⡀⠈⠄⠄⠈⠉⠉⠔⠁⠄⠘⢀⣼⡿⡿⡄")
print(f"⠄⠄⠄⠄⠄⠄⠄⢻⠪⢌⡀⠄⠄⠄⠄⠄⠄⢰⠞⠋⠙⠄⢣⡀")
print(f"⠄⠄⠄⠄⠄⠄⠄⠘⡄⠄⠙⠢⢅⡠⡤⢤⠒⠁⠄⠄⠄⠁⠈⠻")
print(f"⠄⠄⠄⠄⠄⠄⠄⣠⣧⠄⠄⠄⢀⠄⠄⣡⠄⠄⠄⠄⠄⠄⠄⠄")
print(f"⠄⠄⠄⠄⣠⡴⠎⠻⣟⡀⠄⠄⠸⢄⣬⣿⠄⠄⠄⠄⠠⠒⡢⠢")
print(f"⠄⢀⡠⠊⠈⠄⠄⠄⠈⢻⣀⠄⢂⠈⠫⢟⠄⠄⠄⠄⠄⠉⠊⠄")
print(f"⠉⠉⡠⠖⠚⠛⠒⠤⠄⣈⠎⠄⠄⠣⣀⡈⠄⣀⣀⣀⣠⣀⣀⣀")
print(f"⠄⠄⠄⠄⠠⠐⠚⠑⠄⠄⠄⡀⠄⠄⣠⣶⡿⠉⠄⠄⠄⠄⠄⠄")


if __name__ == "__main__":
    main()
