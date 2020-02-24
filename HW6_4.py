def ap3(*args):
    mElement = args[0]
    for i in args:
        if i < mElement:
            mElement = i
    return mElement

mElement = min(14, 5, 410, -3, 1, 0, 55)
print(f'Минимальный элемент: {mElement}')