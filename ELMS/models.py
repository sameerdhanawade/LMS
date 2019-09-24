from django.db import models

# Create your models here.
class Deptmast(models.Model):
    dept_code = models.IntegerField(db_column='DEPT_CODE', blank=True, null=True)  # Field name made lowercase.
    dept_name = models.CharField(db_column='DEPT_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEPTMAST'


class Empmast(models.Model):
    emp_code = models.IntegerField(db_column='EMP_CODE', blank=True, null=True)  # Field name made lowercase.
    emp_name = models.CharField(db_column='EMP_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dept_code = models.IntegerField(db_column='DEPT_CODE', blank=True, null=True)  # Field name made lowercase.
    a_ret_dt = models.DateTimeField(db_column='A_RET_DT', blank=True, null=True)  # Field name made lowercase.
    sex_ind = models.CharField(db_column='SEX_IND', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPMAST'
