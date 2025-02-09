import copy

def twolayers_hc(st, direction='b', const=1.5):
    """function that copies a HC layer in init Structure() in order to create a two-layer model

    INPUT: 
        - st: siman Structure() with one layer
        - direction ('a', 'b', 'c') (str): in which direction to expand cell and add a layer ('b' by default)
    RETURN: 
        - siman Structure() with two layers"""
    
    st_tw = copy.deepcopy(st)

    # choose the direction where to add a second layer
    if direction == 'a':
        n = 0
    elif direction == 'b':
        n = 1
    elif direction == 'c':
        n = 2
    else:
        print('Wrong symbol is provided for direction; please choose the direction a, b or c')

    # enlarge the cell
    rprimd = st_tw.rprimd[n][n]
    st_tw.rprimd[n][n] = const * rprimd

    # copy the layer
    snd_xcart = copy.deepcopy(st_tw.xcart)
    for xc in snd_xcart:
        xc[xc == xc[n]] += 3.8

    st_tw = st_tw.add_atoms(snd_xcart, 'C')

    return st_tw