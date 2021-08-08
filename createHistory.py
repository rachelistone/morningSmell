import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'morningsmell.settings')
django.setup()

from invitations.models import ProdUser, BuyHistory

day = datetime.now().weekday()
todayProdusers = ProdUser.objects.filter(day=(day+1)%7)# datetime gives 6 for sunday - call it 0, and 0 for monday - call it 1
for produser in todayProdusers:
    if produser.is_active:
        print(produser)
        new_buyHistory = BuyHistory(user=produser.user,product=produser.product, amount=produser.amount,date=datetime.now())
        new_buyHistory.save()


