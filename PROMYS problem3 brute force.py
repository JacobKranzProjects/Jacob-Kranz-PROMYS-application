i=0
fly = 0
jump = 3
rabbit = jump

def flyjump():
    global fly
    fly += 1

def rabbitjump(jump):
    global rabbit
    global fly
    fly = fly*(rabbit+jump)/rabbit
    rabbit = rabbit+jump

while rabbit>fly:
    flyjump()
    rabbitjump(jump)
    # print(fly/rabbit)
    i+=1
    print(fly)
print(i+1, '\n')


i=1
fly = 0
jump = 3
rabbit = jump

while rabbit>fly:
    fly = (fly+1)*(rabbit+jump)/rabbit
    rabbit = jump*(i+1)
    i+=1
    print(fly)

print(i, '\n')
# print(i, fly/rabbit)

i=1
fly = 0
jump = 3
rabbit = jump

while jump*i>fly:
    fly = (fly+1)*(i+1)/(i)
    i+=1
    print(fly)

print(i, '\n')
  


i=1
fly = 0
jump = 3
rabbit = jump

while jump*i>fly:
    # fly = (fly+1)*(i+1)/(i)
    # fly = fly + fly/i + 1 + 1/i
    # fly - fly - fly/i = 1 + 1/i
    # fly/i = -1 - 1/i
    # fly = -i - 1
    i+=1
    print(fly)

print(i, '\n')

"""

fly = 0 = the starting position of the fly
jump = the distance the rabbit jumps
rabbit = 0 = the starting position of the rabbit
n = 1 = the number of jumps of both the rabbit and fly, starting at 1

functions:

fly jumps:
    fly[n] = fly[n-1] + 1
    fly = n



rabbit jumps:
I use a 'scale' variable to express the change in the fly when the rabbit jumps. the logic
behind this is that when the rabbit jumps, we can multiply both the rabbit and the fly by the 
scale factor to get the same value, since the rubber band causes the fly to remain the same
fraction of the way to the rabbit. For example, if the fly is at 1cm, and the rabbit is at
1km, when the rabbit jumps, its distance is multiplied by two, which is the scale factor, so 
we can apply this to the fly, and its distance becomes 2cm, which is still the same fraction
of the distance to the rabbit.

    scale = rabbit[n+1] / rabbit[n]
(for example, rabbit is at 1km, jumps to 2km, distance is doubled, and )
    
    rabbit[n] = rabbit[n-1] + jump
    rabbit = n * jump


    fly[n] = fly[n-1] * [rabbit[n+1] / rabbit[n]]
    fly[n] = fly[n-1] * [(rabbit[n] + jump) / rabbit[n]]

























"""