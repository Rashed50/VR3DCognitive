from django.db import models
from django.contrib.auth import get_user_model


## Custom Import 
from VR3DCognitive.models import TimestampedModel


User = get_user_model()
# Create your models here.

class VRModel(TimestampedModel):

    sessionID    = models.CharField(max_length=150)    
    frame_number = models.CharField(max_length=20)    
    timestamp    = models.CharField(max_length=150)    
    sensor_data  = models.TextField(max_length=500) 

    class Meta:
        db_table ='vr3d_info'
        ordering = ['-created_at']




class Country(TimestampedModel):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'countries'
        db_table = 'country'
        ordering = ['name']


class VRUser(TimestampedModel):
    vr_user_id = models.AutoField(primary_key=True)
    user_id    = models.OneToOneField(User, on_delete=models.CASCADE)

    contact_no = models.CharField(max_length=13, null=True, blank=True)    
    country_id = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    state_id   = models.SmallIntegerField(default=1)
    city       = models.CharField(max_length=100, null=True, blank=True)
    address    = models.TextField(max_length=300, null=True, blank=True)
    address2   = models.TextField(max_length=300, null=True, blank=True)
    zip        = models.CharField(max_length=10,  null=True, blank=True)

    def __str__(self):
        return self.contact_no if self.contact_no else "No contact number"

    class Meta:
        db_table = 'vrusers'
        ordering = ['-created_at']

 #   "sessionID": "2024-10-01T12-34-32",
#   "frameNumber": 25,
#   "timestamp": "2024-10-01T12-34-34.0749",
#   "sensorData": {
#     "HeadUserPresence": "False",
#     "HeadIsTracked": "False",
#     "HeadTrackingState": "0",
#     "HeadDevicePosition": "(0.00, 0.00, 0.00)",
#     "HeadDeviceRotation": "(0.00000, 0.00000, 0.00000, 1.00000)",
#     "HeadDeviceVelocity": "(0.00, 0.00, 0.00)",
#     "HeadDeviceAngularVelocity": "(0.00, 0.00, 0.00)",
#     "HeadCenterEyePosition": "(0.00, 0.00, 0.00)",
#     "HeadCenterEyeRotation": "(0.00000, 0.00000, 0.00000, 1.00000)",
#     "HeadCenterEyeVelocity": "(0.00, 0.00, 0.00)",
#     "HeadCenterEyeAngularVelocity": "(0.00, 0.00, 0.00)",
#     "HeadLeftEyePosition": "(0.00, 0.00, 0.00)",
#     "HeadLeftEyeRotation": "(0.00000, 0.00000, 0.00000, 1.00000)",
#     "HeadLeftEyeVelocity": "(0.00, 0.00, 0.00)",
#     "HeadLeftEyeAngularVelocity": "(0.00, 0.00, 0.00)",
#     "HeadRightEyePosition": "(0.00, 0.00, 0.00)",
#     "HeadRightEyeRotation": "(0.00000, 0.00000, 0.00000, 1.00000)",
#     "HeadRightEyeVelocity": "(0.00, 0.00, 0.00)",
#     "HeadRightEyeAngularVelocity": "(0.00, 0.00, 0.00)",
#     "CtrlrLeftPrimary2DAxis": "(0.00, 0.00)",
#     "CtrlrLeftGrip": "0",
#     "CtrlrLeftGripButton": "False",
#     "CtrlrLeftMenuButton": "False",
#     "CtrlrLeftPrimaryButton": "False",
#     "CtrlrLeftPrimaryTouch": "False",
#     "CtrlrLeftSecondaryButton": "False",
#     "CtrlrLeftSecondaryTouch": "False",
#     "CtrlrLeftTrigger": "0",
#     "CtrlrLeftTriggerButton": "False",
#     "CtrlrLeftTriggerTouch": "False",
#     "CtrlrLeftPrimary2DAxisClick": "False",
#     "CtrlrLeftPrimary2DAxisTouch": "False",
#     "CtrlrLeftThumbrestTouch": "False",
#     "CtrlrLeftDeviceIsTracked": "False",
#     "CtrlrLeftDeviceTrackingState": "0",
#     "CtrlrLeftDevicePosition": "(0.00, 0.00, 0.00)",
#     "CtrlrLeftDeviceRotation": "(0.00000, 0.00000, 0.00000, 1.00000)",
#     "CtrlrLeftDeviceVelocity": "(0.00, 0.00, 0.00)",
#     "CtrlrLeftDeviceAngularVelocity": "(0.00, 0.00, 0.00)",
#     "CtrlrLeftPointerIsTracked": "False",
#     "CtrlrLeftPointerTrackingState": "0",
#     "CtrlrLeftPointerPosition": "(0.00, 0.00, 0.00)",
#     "CtrlrLeftPointerRotation": "(0.00000, 0.00000, 0.00000, 1.00000)",
#     "CtrlrLeftPointerVelocity": "(0.00, 0.00, 0.00)",
#     "CtrlrLeftPointerAngularVelocity": "(0.00, 0.00, 0.00)",
#     "CtrlrLeftIsTracked": "False",
#     "CtrlrLeftTrackingState": "0",
#     "CtrlrRightPrimary2DAxis": "(0.00, 0.00)",
#     "CtrlrRightGrip": "0",
#     "CtrlrRightGripButton": "False",
#     "CtrlrRightMenuButton": "False",
#     "CtrlrRightPrimaryButton": "False",
#     "CtrlrRightPrimaryTouch": "False",
#     "CtrlrRightSecondaryButton": "False",
#     "CtrlrRightSecondaryTouch": "False",
#     "CtrlrRightTrigger": "0",
#     "CtrlrRightTriggerButton": "False",
#     "CtrlrRightTriggerTouch": "False",
#     "CtrlrRightPrimary2DAxisClick": "False",
#     "CtrlrRightPrimary2DAxisTouch": "False",
#     "CtrlrRightThumbrestTouch": "False",
#     "CtrlrRightDeviceIsTracked": "False",
#     "CtrlrRightDeviceTrackingState": "0",
#     "CtrlrRightDevicePosition": "(0.00, 0.00, 0.00)",
#     "CtrlrRightDeviceRotation": "(0.00000, 0.00000, 0.00000, 1.00000)",
#     "CtrlrRightDeviceVelocity": "(0.00, 0.00, 0.00)",
#     "CtrlrRightDeviceAngularVelocity": "(0.00, 0.00, 0.00)",
#     "CtrlrRightPointerIsTracked": "False",
#     "CtrlrRightPointerTrackingState": "0",
#     "CtrlrRightPointerPosition": "(0.00, 0.00, 0.00)",
#     "CtrlrRightPointerRotation": "(0.00000, 0.00000, 0.00000, 1.00000)",
#     "CtrlrRightPointerVelocity": "(0.00, 0.00, 0.00)",
#     "CtrlrRightPointerAngularVelocity": "(0.00, 0.00, 0.00)",
#     "CtrlrRightIsTracked": "False",
#     "CtrlrRightTrackingState": "0",
#     "EyeLeftRot": "(0.00000, 0.00000, 0.00000, 1.00000)",
#     "EyeRightRot": "(0.00000, 0.00000, 0.00000, 1.00000)"
#   }