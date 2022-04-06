from unittest import TestCase, main
from main import first_f,sec_f,third_f

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

class Test(TestCase):
       def test_1(self):
           self.assertEqual(first_f(one_to_many,catalogs),[('АСОИУ', ['Аннотация 1-10', 'Контрольный вопрос 310']), ('Алиса', ['Концерт в Самаре 11.09'])])
       def test_2(self):
           self.assertEqual(sec_f(one_to_many,catalogs),[('АСОИУ', 53), ('Алиса', 2054), ('Сериалы', 5432), ('Путешествия', 5783)])
       def test_3(self):
           self.assertEqual(third_f(many_to_many,files,catalogs,file_catalogs),[('Акация', 'Сериалы'), ('Новая Зеландия', 'Путешествия'), ('Абхазия', 'Путешествия'), ('Концерт в Самаре 11.09', 'Алиса'), ('Аннотация 1-10', 'АСОИУ'), ('Контрольный вопрос 310', 'АСОИУ')])
