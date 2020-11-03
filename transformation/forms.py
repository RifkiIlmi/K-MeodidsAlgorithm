from django import forms

TAHUN = (
  ('Choose',
      (
        ('-','-'),
        ('2012','2012'),
        ('2013','2013'),
        ('2014','2014'),
        ('2015','2015'), 
        ('2016','2016'), 
        ('2017','2017'), 
        ('2018','2018'), 
        ('2019','2019'), 
      )
   ),
)

TRANSFORM = (
  ('Choose',
      (
        ('-','-'),
        ('minmax_norm','Min-Max Normalization'),
      )
   ),
)

class TransformationForm(forms.Form):
    tahun = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=TAHUN)
    normalization = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), choices=TRANSFORM)


        