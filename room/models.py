from django.db import models


class Room(models.Model):
    room_choice = [('S', 'Single Occupancy'), ('F', 'With fridge'), ('FT', 'with fridge and TV')]
    no = models.CharField(max_length=5)
    name = models.CharField(max_length=10)
    room_type = models.CharField(choices=room_choice, max_length=10000, default=None)
    vacant = models.BooleanField(default=False)
    hostel = models.ForeignKey('Hostel', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Hostel(models.Model):
    name = models.CharField(max_length=5)
    building = models.ManyToManyField('building', default=None, blank=True)
    caretaker = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Building(models.Model):
    code = models.CharField(max_length=100, default=None)
    room_choice = [('S', 'Single Occupancy'), ('F', 'With fridge'), ('FT', 'with fridge and TV')]
    room_type = models.CharField(choices=room_choice, max_length=10000, default='D')

    def __str__(self):
        return self.code
