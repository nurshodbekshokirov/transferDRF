from django.db import models

class Club(models.Model):
    nom = models.CharField(max_length=100)
    davlat = models.CharField(max_length=100)
    logo = models.FileField(null=True)
    president = models.CharField(max_length=100)
    coach = models.CharField(max_length=80)
    yili = models.CharField(max_length=30)
    eng_qim_tr = models.CharField(max_length=50)
    eng_qim_sotuv = models.CharField(max_length=50)

    def __str__(self):
        return self.nom
class Player(models.Model):
    pozit = [
        ('Midfielder', 'Midfielder'),
        ('Defender', 'Defender'),
        ('Forward', 'Forward'),
        ('Keeper', 'Keeper')

    ]
    ism = models.CharField(max_length=50)
    t_yil = models.DateField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='futbolchilari')
    tr_narxi = models.PositiveIntegerField()
    millat = models.CharField(max_length=50)
    pozitsiya = models.CharField(max_length=50, choices=pozit)

    def __str__(self):
        return self.ism
class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    eski = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='sotuvlari')
    yangi = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='sotib_olganlari')
    narxi = models.PositiveIntegerField()
    tax_narxi = models.PositiveIntegerField()
    mavsum = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.player}'
class Hozirgi_mavsum(models.Model):
    hozirgi_mavsum = models.CharField(max_length=100)

    def __str__(self):
        return self.hozirgi_mavsum



# Create your models here.
