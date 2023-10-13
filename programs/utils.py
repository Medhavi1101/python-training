def print_dir(obj):
    items= [ item for item in dir(obj) if not item.startswith('__')]
    for item in items:
        print(item)