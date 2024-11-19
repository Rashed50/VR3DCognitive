from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from DataSource.models import VRUser

@receiver(post_save, sender=User)
def create_vruser(sender, instance, created, **kwargs):
    """
    Signal to create a VRUser instance when a new User is created.
    """
    if created:  

        VRUser.objects.create(
            user_id    = instance,  
            contact_no = None,   
            country_id = 1,      
            state_id   = 1,        
            city       = None,       
            address    = None,      
            address2   = None,     
            zip        = None           
        )
