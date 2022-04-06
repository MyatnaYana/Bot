from operator import itemgetter

class File:
    def __init__(self, id, filename, memory, log_id):
        self.id = id
        self.filename = filename
        self.memory = memory
        self.log_id = log_id


class Catalog:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Fillog:
    def __init__(self, log_id, fillog_id):
        self.log_id = log_id
        self.fillog_id = fillog_id
def first_f(one_to_many,catalogs):
    res_1 = []
    res_1 = [(c.name, list(filename for filename, _, name in one_to_many if name == c.name)) for c in catalogs if
             c.name[0] == 'А']
    return res_1
def sec_f(one_to_many,catalogs):
    res_2 = []
    for c in catalogs:
        log_files = list(filter(lambda x: x[2] == c.name, one_to_many))
        if len(log_files) > 0:
            mem = [size for _, size, _ in log_files]
            max_mem = max(mem)
            res_2.append((c.name, max_mem))
    res_2sort = sorted(res_2, key=itemgetter(1))
    return(res_2sort)

def third_f(many_to_many, files,catalogs,file_catalogs):
    many_to_many_temp = [(f.filename, c.log_id,)
                         for f in files
                         for c in file_catalogs
                         if f.id == c.fillog_id]
    many_to_many = [(x[0], logs.name)
                    for x in many_to_many_temp
                    for logs in catalogs
                    if logs.id == x[1]]
    res_3 = sorted(many_to_many, key=itemgetter(1), reverse=True)
    return res_3

def main():
    catalogs = [
        Catalog(1, 'Путешествия'),
        Catalog(2, 'Сериалы'),
        Catalog(3, 'АСОИУ'),
        Catalog(4, 'Алиса')]

    files = [
        File(1, 'Аннотация 1-10', 36, 3),
        File(2, 'Новая Зеландия', 1560, 1),
        File(3, 'Акация', 5432, 2),
        File(4, 'Концерт в Самаре 11.09', 2054, 4),
        File(5, 'Контрольный вопрос 310', 53, 3),
        File(6, 'Абхазия', 5783, 1) ]

    file_catalogs = [
        Fillog(1, 2),
        Fillog(1, 6),
        Fillog(2, 3),
        Fillog(3, 1),
        Fillog(3, 5),
        Fillog(4, 4)]

    one_to_many = [(f.filename, f.memory, c.name)
                   for c in catalogs
                   for f in files
                   if f.log_id == c.id]

    many_to_many_temp = [(c.name, fc.log_id, fc.fillog_id)
                         for c in catalogs
                         for fc in file_catalogs
                         if c.id == fc.fillog_id]

    many_to_many = [(f.filename, f.memory, name)
                    for name, log_id, fillog_id in many_to_many_temp
                    for f in files
                    if f.id == fillog_id]

    print('Задание Г1')

    print(first_f(one_to_many,catalogs))

    print('\nЗадание Г2:')
    print((sec_f(one_to_many,catalogs)))

    print('\nЗадание Г3:')

    print(third_f(many_to_many,files,catalogs,file_catalogs))

if __name__ == '__main__':
    main()