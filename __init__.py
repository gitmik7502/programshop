def prog_tiles():
    import importlib
    prog2 = importlib.import_module('temp.programshop.test channel')
    from temp.programshop.Tetris import title as prog2title
    prog_titles = [prog1title(), prog2.title()]
    return prog_titles
