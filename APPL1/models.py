from django.db import models


class Device_String(models.Model):
    NAME_FIELD = (
    ('Boom_1', 'Boom-1'),
    ('Boom_2', 'Boom-2'),
    ('Boom_3', 'Boom-3'),
    ('Boom_4', 'Boom-4'),
    ('Boom_5', 'Boom-5'),
    ('Boom_6', 'Boom-6'),
    ('Boom_7', 'Boom-7'),
    ('Boom_8', 'Boom-8'),
    ('Boom_9', 'Boom-9'),
    ('Boom_10', 'Boom-10'),
    ('Boom_11', 'Boom-11'),
    ('Boom_12', 'Boom-12'),
    ('Boom_13', 'Boom-13'),
    ('Boom_14', 'Boom-14'),
    ('Boom_15', 'Boom-15'),
    ('Boom_16', 'Boom-16'),
    ('Boom_17', 'Boom-17'),
    ('Boom_18', 'Boom-18'),
    ('Boom_19', 'Boom-19'),
    ('Boom_20', 'Boom-20'),
    ('Boom_21', 'Boom-21'),
    ('Boom_22', 'Boom-22'),
    ('Boom_23', 'Boom-23'),
    ('Boom_24', 'Boom-24'),
    ('Boom_25', 'Boom-25'),
    ('Boom_26', 'Boom-26'),
    ('Boom_27', 'Boom-27'),
    ('Boom_28', 'Boom-28'),
    ('Boom_29', 'Boom-29'),
    ('Boom_30', 'Boom-30'),
    ('Boom_31', 'Boom-31'),
    ('Boom_32', 'Boom-32'),
    ('Boom_33', 'Boom-33'),
    ('Boom_34', 'Boom-34'),
    ('Boom_35', 'Boom-35'),
    ('Boom_36', 'Boom-36'),
    ('Boom_37', 'Boom-37'),
    ('Boom_38', 'Boom-38'),
    ('Boom_39', 'Boom-39'),
    ('Boom_40', 'Boom-40'),
    ('Boom_41', 'Boom-41'),
    ('Boom_42', 'Boom-42'),
    ('Boom_43', 'Boom-43'),
    ('Boom_44', 'Boom-44'),
    ('Boom_45', 'Boom-45'),
    )
    Name = models.CharField(max_length=7, primary_key=True, default='Please_choose', choices=NAME_FIELD)
    Status = models.CharField(max_length=50)
    Program = models.IntegerField(default='0')
    Program_Alias = models.CharField(max_length=50, default='- - -')
    History = models.CharField(max_length=50)
    Time = models.CharField(max_length=5, null=True)
    Data = models.DateField(null=True)
    Plan_Program = models.IntegerField(default='0')
    Plan_Program_Alias = models.CharField(max_length=50, default='- - -')
    Repeat = models.CharField(max_length=50)
    Plan_Time = models.CharField(max_length=5, null=True)
    Plan_Data = models.DateField(null=True)


    def __str__(self):
        return self.Name
