try:
	import asyncio
	from os import system
	from typing import List
	import secrets, sys
	import os
	import aiohttp
except ImportError:
	os.system('pip install os')
	os.system('pip install typing')
	os.system('pip install random')
	os.system('pip install requests')
	os.system('pip install sys')
	os.system('clear')
	import asyncio
	from os import system
	from typing import List
	import secrets, sys
	import os
	import aiohttp
else:
	import asyncio
	from os import system
	from typing import List
	import secrets, sys
	import os
	import aiohttp

# = = = = = = = = = = = = 
BRed="\033[1;31m" # Red
BGreen="\033[1;32m" # Green
BYellow="\033[1;33m" # Yellow
BBlue="\033[1;34m" # Blue
BPurple="\033[1;35m" # Purple
BCyan="\033[1;36m" # Cyan
BWhite="\033[1;37m" # White
Z = '\033[1;31m' #احمر
A = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
X = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
S = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
# = = = = = = = = = = = =

os.system('clear')
print(F+'  ____      _                 ____             _ ')
print(F+' / ___|   _| |__   ___ _ __  |  _ \  __ _ _ __| | __')
print(F+'''| |  | | | | '_ \ / _ \ '__| | | | |/ _` | '__| |/ / ''')
print(F+'| |__| |_| | |_) |  __/ |    | |_| | (_| | |  |   < ')
print(F+' \____\__, |_.__/ \___|_|    |____/ \__,_|_|  |_|\_\ ')
print(F+'      |___/ ')

print('')

print(A+'~ Code By Cyber Dark')
print(A+'~ Facebook : /CyberDarkCrew)
print(A+'~ TikTok   : @CyberDarkCrew')
print(A+'~ Instagram: @CyberDarkCrew')
print(A+'~ Twitter  : @CyberDarkCrew')


print(F+'''
~ Cyber Dark Team ~
Telegram : 
	Mahmoud : @L_N_X_0
	Ahmed   : @M3x4il
	Hosin   : @Hosinballo
	Salem   : @k_J_I_A
	Omer    : @nice_nice
 ''')
print('')
def write_file(arg: str) -> None:
    with open('hits.txt', 'a', encoding='UTF-8') as f:
        f.write(f'{arg}\n')


class Checker:
    def __init__(self, usernames: List[str]):
        self.to_check = usernames

    async def _check(self, session: aiohttp.ClientSession, username: str) -> None:
        async with session.head(f'https://www.tiktok.com/@{username}') as response:
            if response.status == 200 and len(username) > 2:
                print(
                    '%s[UNAVAILABLE] @%s%s'
                    % ('\u001b[31;1m', username, '\u001b[0m')
                )
            else:
                print(
                    '%s[AVAILABLE] %s%s'
                    % ('\u001b[32;1m', username, '\u001b[0m')
                )
                write_file(username)

    async def start(self):
        print(X+'Loading...')
        async with aiohttp.ClientSession() as sess:
            return await asyncio.gather(*[self._check(sess, u) for u in self.to_check])

userx = input(C+"Name File Users :")

if __name__ == '__main__':
    system('Checker by Cyber Dark and TikTok.com/@cyb3r_dark')
    with open(userx, encoding='UTF-8') as f:
        username_list = [line.strip() for line in f]

    checker = Checker(username_list)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(checker.start())
