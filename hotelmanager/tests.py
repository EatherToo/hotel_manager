from django.test import TestCase
from django.db import connection

# Create your tests here.
cursor = connection.cursor()
num = 0
cursor.callproc('count_room_num', ("2017-12-1", '2017-12-3', 'std_low', num))

