import re
from django.db import models

def cellphone_validation(cell_phone):
    if not re.match(r'^01[016789][1-9]\d{6,7}$',cell_phone):
        raise forms.VladationError("올바른 전화번호를 입력해주시기 바랍니다.")
# Create your models here.
class SignUp(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    cell_phone = models.CharField(max_length=13 ,validators=[cellphone_validation])
    timestamp = models.DateTimeField(auto_now_add = True, auto_now =False)
    updated  = models.DateTimeField(auto_now_add = False, auto_now =True)
    def __str__(self):
        return self.name
