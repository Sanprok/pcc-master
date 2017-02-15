def show_magicians(magicians):
    for i in magicians:
        print(i)


def make_great(magicians):
    make_gr = []
    while magicians:
        a = 'Great' + magicians.pop()
        make_gr.append(a)
    for i in make_gr:
        magicians.append(i)
    return magicians


magicians = ['san', 'piter', 'martin', ]
# show_magicians(magicians)
#
# make_gr = make_great(magicians[:])
# show_magicians(make_gr)
#
# show_magicians(magicians)
#
# make_great(magicians)
# show_magicians(magicians)

# make_gr = make_great(magicians[:])
show_magicians(magicians)

a = make_great(magicians[:])
show_magicians(a)

make_great(magicians)
show_magicians(magicians)
