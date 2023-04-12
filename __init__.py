def prog_tiles():
    import importlib
    prog1 = importlib.import_module('temp.programshop.test channel')
    from temp.programshop.Tetris import title as prog2title
    prog_titles = [prog1.title(), prog2title()]
    return prog_titles
