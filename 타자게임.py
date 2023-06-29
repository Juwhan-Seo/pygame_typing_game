import pygame
from pygame.locals import QUIT, KEYDOWN, K_RETURN, K_BACKSPACE
from random import sample
import sys


st = '''
import  
print
random
sample
sys
for
while
break
continue
list
tuple
turtle
string
format
class
def
dictionary
del
True
False
if
elif
type
else
update
index
append
sort
reverse
insert
pop
float
int
count
range
return
get
extend
keys
vaules
items
clear
set
add
function
lambda
open
close
write
read
with
as
alert
except
try
finally
raise
in
split
except
raise
semester
tradition
insert
select
from
file
=
+
+=
-
-=
==
*
%
<
>
<=
>=
!=
not
and
or
input
open
lower
key
value
in
pass
\b
\t
\n
\f
\r
\\
\'
\"
'''


words = st.split()
random_word = sample(words, 1)[0]
print(random_word)
pygame.init()


life = 5
score = 0


SUR = pygame.display.set_mode((500, 500))
FPS = pygame.time.Clock()


s = ""
qmess = pygame.font.SysFont("haansaleb", 70)
umess = pygame.font.SysFont("haansaleb", 50)
gmess = pygame.font.SysFont("haansaleb", 50)
game_over = False


while True:
    SUR.fill((0, 0, 0))


    for i in pygame.event.get():
        if i.type == QUIT:
            pygame.quit()
            sys.exit()
        if i.type == KEYDOWN:
            if i.key == K_BACKSPACE:
                s = s[:-1]
            elif i.key == K_RETURN:
                if s == random_word:
                    score += 100
                    random_word = sample(words, 1)[0]
                else:
                    life -= 1
                    if life == 0:
                        game_over = True


                s = ""
            else:
                s += i.unicode
            print(s)


    if not game_over:
        q = qmess.render(random_word, True, (255, 255, 255))
        qx, qy = q.get_width(), q.get_height()
        SUR.blit(q, (250-qx//2, 200-qy//2))


        u = umess.render(s, True, (255, 255, 0))
        ux, uy = u.get_width(), u.get_height()
        SUR.blit(u, (250-ux//2, 450-uy//2))


        pygame.draw.line(SUR, (255, 255, 255), (0, 400), (500, 400), 3)
    else:
        g = gmess.render(f"YOUR SCORE is {score}", True, (255, 0, 0))
        gx, gy = g.get_width(), g.get_height()
        SUR.blit(g, (250-gx//2, 250-gy//2))


    pygame.display.flip()
    FPS.tick(15)
