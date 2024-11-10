import random
import time
from Resources.colors import MyColors


print(MyColors.RED + '\n***CONNECTING***' + MyColors.END)
time.sleep(1)
print(MyColors.RED + '.' + MyColors.END)
time.sleep(1)
print(MyColors.RED + '.' + MyColors.END)
time.sleep(1)
print(MyColors.RED + '.' + MyColors.END)
time.sleep(1)
print(MyColors.RED + '.' + MyColors.END)
time.sleep(1)
print(MyColors.RED + '.' + MyColors.END)
print(MyColors.RED + '\n***PASS***' + MyColors.END)
time.sleep(1)
print(MyColors.RED + '\n***ACCESS***' + MyColors.END)
time.sleep(.6)
print(MyColors.RED + '\n***SCRAPING***' + MyColors.END)
time.sleep(.6)

char = '123 4567 890qw ertyuio pasdfghjk lzxcvbn m@£$%&.:; '

width_choices = [60, 61, 62, 63, 64]
count = 0
while count < 50:
    line_width = random.choice(width_choices)
    line_char = []
    line = ''
    for i in range(0, line_width):
        line_char.append(random.choice(char))
    completed_line = line.join(line_char)
    print(completed_line)
    time.sleep(.1)
    count += 1


print(MyColors.YELLOW + '\n***RETRIEVING***' + MyColors.END)
time.sleep(1)
print(MyColors.RED + '.' + MyColors.END)
time.sleep(1)
print(MyColors.RED + '.' + MyColors.END)
time.sleep(1)
print(MyColors.RED + '.' + MyColors.END)
time.sleep(.6)
print(MyColors.GREEN + '===========================================================' + MyColors.END)
print(MyColors.GREEN + 'Name= Joao Carlos Goncalves\n'
      'Morada= Rua Bento Goncalves lt727 7o esq XXXX-XXX Lisboa' + MyColors.END)
print(MyColors.GREEN + '===========================================================' + MyColors.END)
time.sleep(.6)
print(MyColors.RED + '\n***DISCONNECTING***' + MyColors.END)
time.sleep(3)
print(MyColors.RED + '\n***OUT***' + MyColors.END)