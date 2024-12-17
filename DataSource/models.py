from django.db import models
from django.contrib.auth import get_user_model
import json, random, time

## Custom Import 
#from VR3DCognitive.models import TimestampedModel


User = get_user_model()
# Create your models here.

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']

class VRModel(TimestampedModel):

    def __init__(self):
        super().__init__()
        return self

    def __init__(self, sessionId,frameNumber,topic,message):
        super().__init__()
        self.sessionID    = sessionId
        self.frameNumber = frameNumber
        self.timestamp    = time.time()
        self.topic  = topic
        self.sensorData  = message
        self.headUserPresence = False
        self.headIsTracked = False
        self.headTrackingState = 0
        self.headDevicePosition =  ""
        self.headDeviceRotation = ""
        self.headDeviceVelocity = ""
        self.headDeviceAngularVelocity =  ""
        self.headCenterEyePosition = ""
        self.headCenterEyeRotation  =  ""
        self.headCenterEyeVelocity  = ""
        self.headCenterEyeAngularVelocity  = ""
        self.headLeftEyePosition  = ""
        self.headLeftEyeRotation  = ""
        self.headLeftEyeVelocity  = ""
        self.headLeftEyeAngularVelocity = ""
        self.headRightEyePosition  = ""
        self.headRightEyeRotation  = ""
        self.headRightEyeVelocity  = ""
        self.headRightEyeAngularVelocity  = ""
        self.ctrlrLeftPrimary2DAxis  = ""
        self.ctrlrLeftGrip =  0
        self.ctrlrLeftGripButton = False
        self.ctrlrLeftMenuButton  = False
        self.ctrlrLeftPrimaryButton  = False
        self.ctrlrLeftPrimaryTouch  = False
        self.ctrlrLeftSecondaryButton  = False
        self.ctrlrLeftSecondaryTouch  = False
        self.ctrlrLeftTrigger  = False
        self.ctrlrLeftTriggerButton  = False
        self.ctrlrLeftTriggerTouch  = False
        self.ctrlrLeftPrimary2DAxisClick  = False
        self.ctrlrLeftPrimary2DAxisTouch  = False
        self.ctrlrLeftThumbrestTouch  = False
        self.ctrlrLeftDeviceIsTracked  = False
        self.ctrlrLeftDeviceTrackingState = 0
        self.ctrlrLeftDevicePosition   = ""
        self.ctrlrLeftDeviceRotation  = ""
        self.ctrlrLeftDeviceVelocity  = ""
        self.ctrlrLeftDeviceAngularVelocity  = ""
        self.ctrlrLeftPointerIsTracked  = False
        self.ctrlrLeftPointerTrackingState = 0
        self.ctrlrLeftPointerPosition  = ""
        self.ctrlrLeftPointerRotation   = ""
        self.ctrlrLeftPointerVelocity  = ""
        self.ctrlrLeftPointerAngularVelocity  = ""
        self.ctrlrLeftIsTracked   = False
        self.ctrlrLeftTrackingState = 0
        self.ctrlrRightPrimary2DAxis =""
        self.ctrlrRightGrip = 0
        self.ctrlrRightGripButton   = False
        self.ctrlrRightMenuButton  = False
        self.ctrlrRightPrimaryButton  = False
        self.ctrlrRightPrimaryTouch  = False
        self.ctrlrRightSecondaryButton  = False
        self.ctrlrRightSecondaryTouch  = False
        self.ctrlrRightTrigger = 0
        self.ctrlrRightTriggerButton  = False
        self.ctrlrRightTriggerTouch  = False
        self.ctrlrRightPrimary2DAxisClick  = False
        self.ctrlrRightPrimary2DAxisTouch  = False
        self.ctrlrRightThumbrestTouch  = False
        self.ctrlrRightDeviceIsTracked  = False
        self.ctrlrRightDeviceTrackingState = 0
        self.ctrlrRightDevicePosition  = ""
        self.ctrlrRightDeviceRotation  = ""
        self.ctrlrRightDeviceVelocity  = ""
        self.ctrlrRightDeviceAngularVelocity  = ""
        self.ctrlrRightPointerIsTracked  = False
        self.ctrlrRightPointerTrackingState = 0
        self.ctrlrRightPointerPosition  = ""
        self.ctrlrRightPointerRotation  = ""
        self.ctrlrRightPointerVelocity  = ""
        self.ctrlrRightPointerAngularVelocity  = ""
        self.ctrlrRightIsTracked  = False
        self.ctrlrRightTrackingState = 0
        self.eyeLeftRot  = ""
        self.eyeRightRot  = ""

   
    sessionID    = models.CharField(max_length=150)    
    frameNumber = models.CharField(max_length=20)    
    timestamp    = models.CharField(max_length=150)  
    topic  = models.TextField(max_length=500,default="")   
    sensorData  = models.TextField(max_length=500)
    headUserPresence = models.BooleanField(default=False)
    headIsTracked = models.BooleanField(default=False)
    headTrackingState = models.SmallIntegerField(default=0)
    headDevicePosition = models.CharField(max_length=30,default="")
    headDeviceRotation = models.CharField(max_length=30,default="")
    headDeviceVelocity = models.CharField(max_length=30,default="")
    headDeviceAngularVelocity = models.CharField(max_length=30,default="")
    headCenterEyePosition = models.CharField(max_length=30,default="")
    headCenterEyeRotation  = models.CharField(max_length=30,default="")
    headCenterEyeVelocity  = models.CharField(max_length=30,default="")
    headCenterEyeAngularVelocity  = models.CharField(max_length=30,default="")
    headLeftEyePosition  = models.CharField(max_length=30,default="")
    headLeftEyeRotation  = models.CharField(max_length=50,default="")
    headLeftEyeVelocity  = models.CharField(max_length=30,default="")
    headLeftEyeAngularVelocity =  models.CharField(max_length=30,default="")
    headRightEyePosition  = models.CharField(max_length=30,default="")
    headRightEyeRotation  = models.CharField(max_length=30,default="")
    headRightEyeVelocity  = models.CharField(max_length=30,default="")
    headRightEyeAngularVelocity  = models.CharField(max_length=30,default="")
    ctrlrLeftPrimary2DAxis  = models.CharField(max_length=30,default="")
    ctrlrLeftGrip =  models.SmallIntegerField(default=0)
    ctrlrLeftGripButton = models.BooleanField(default=False)
    ctrlrLeftMenuButton  = models.BooleanField(default=False)
    ctrlrLeftPrimaryButton  = models.BooleanField(default=False)
    ctrlrLeftPrimaryTouch  = models.BooleanField(default=False)
    ctrlrLeftSecondaryButton  = models.BooleanField(default=False)
    ctrlrLeftSecondaryTouch  = models.BooleanField(default=False)
    ctrlrLeftTrigger  = models.BooleanField(default=False)
    ctrlrLeftTriggerButton  = models.BooleanField(default=False)
    ctrlrLeftTriggerTouch  = models.BooleanField(default=False)
    ctrlrLeftPrimary2DAxisClick  = models.BooleanField(default=False)
    ctrlrLeftPrimary2DAxisTouch  = models.BooleanField(default=False)
    ctrlrLeftThumbrestTouch  = models.BooleanField(default=False)
    ctrlrLeftDeviceIsTracked  = models.BooleanField(default=False)
    ctrlrLeftDeviceTrackingState = models.SmallIntegerField(default=0)
    ctrlrLeftDevicePosition   = models.CharField(max_length=30,default="")
    ctrlrLeftDeviceRotation  = models.CharField(max_length=50,default="")
    ctrlrLeftDeviceVelocity  = models.CharField(max_length=30,default="")
    ctrlrLeftDeviceAngularVelocity  = models.CharField(max_length=30,default="")
    ctrlrLeftPointerIsTracked  = models.BooleanField(default=False)
    ctrlrLeftPointerTrackingState = models.SmallIntegerField(default=0)
    ctrlrLeftPointerPosition  = models.CharField(max_length=30,default="")
    ctrlrLeftPointerRotation   = models.CharField(max_length=30,default="")
    ctrlrLeftPointerVelocity  = models.CharField(max_length=30,default="")
    ctrlrLeftPointerAngularVelocity  = models.CharField(max_length=30,default="")
    ctrlrLeftIsTracked   = models.BooleanField(default=False)
    ctrlrLeftTrackingState = models.SmallIntegerField(default=0)
    ctrlrRightPrimary2DAxis  = models.CharField(max_length=30,default="")
    ctrlrRightGrip = models.SmallIntegerField(default=0)
    ctrlrRightGripButton   = models.BooleanField(default=False)
    ctrlrRightMenuButton  = models.BooleanField(default=False)
    ctrlrRightPrimaryButton  = models.BooleanField(default=False)
    ctrlrRightPrimaryTouch  = models.BooleanField(default=False)
    ctrlrRightSecondaryButton  = models.BooleanField(default=False)
    ctrlrRightSecondaryTouch  = models.BooleanField(default=False)
    ctrlrRightTrigger = models.SmallIntegerField(default=0)
    ctrlrRightTriggerButton  = models.BooleanField(default=False)
    ctrlrRightTriggerTouch  = models.BooleanField(default=False)
    ctrlrRightPrimary2DAxisClick  = models.BooleanField(default=False)
    ctrlrRightPrimary2DAxisTouch  = models.BooleanField(default=False)
    ctrlrRightThumbrestTouch  = models.BooleanField(default=False)
    ctrlrRightDeviceIsTracked  = models.BooleanField(default=False)
    ctrlrRightDeviceTrackingState = models.SmallIntegerField(default=0)
    ctrlrRightDevicePosition  = models.CharField(max_length=30,default="")
    ctrlrRightDeviceRotation  = models.CharField(max_length=50,default="")
    ctrlrRightDeviceVelocity  = models.CharField(max_length=30,default="")
    ctrlrRightDeviceAngularVelocity  = models.CharField(max_length=30,default="")
    ctrlrRightPointerIsTracked  = models.BooleanField(default=False)
    ctrlrRightPointerTrackingState = models.SmallIntegerField(default=0)
    ctrlrRightPointerPosition  = models.CharField(max_length=30,default="")
    ctrlrRightPointerRotation  = models.CharField(max_length=30,default="")
    ctrlrRightPointerVelocity  = models.CharField(max_length=30,default="")
    ctrlrRightPointerAngularVelocity  = models.CharField(max_length=30,default="")
    ctrlrRightIsTracked  = models.BooleanField(default=False)
    ctrlrRightTrackingState = models.SmallIntegerField(default=0)
    eyeLeftRot  = models.CharField(max_length=50,default="")
    eyeRightRot  = models.CharField(max_length=50,default="")

    class Meta:
        db_table ='vr_models'
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
        db_table = 'vrusers_dp'
        ordering = ['-created_at']

 #   "sessionID": "2024-10-01T12-34-32",
#   "frameNumber": 25,
#   "timestamp": "2024-10-01T12-34-34.0749",
#   "sensorData": {
    # "HeadUserPresence": "False",
    # "HeadIsTracked": "False",
    # "HeadTrackingState": "0",
    # "HeadDevicePosition": "(0.00, 0.00, 0.00)",
    # "HeadDeviceRotation": "(0.00000, 0.00000, 0.00000, 1.00000)",
    # "HeadDeviceVelocity": "(0.00, 0.00, 0.00)",
    # "HeadDeviceAngularVelocity": "(0.00, 0.00, 0.00)",
    # "HeadCenterEyePosition": "(0.00, 0.00, 0.00)",
    # "HeadCenterEyeRotation": "(0.00000, 0.00000, 0.00000, 1.00000)",
    # "HeadCenterEyeVelocity": "(0.00, 0.00, 0.00)",
    # "HeadCenterEyeAngularVelocity": "(0.00, 0.00, 0.00)",
    # "HeadLeftEyePosition": "(0.00, 0.00, 0.00)",
    # "HeadLeftEyeRotation": "(0.00000, 0.00000, 0.00000, 1.00000)",
    # "HeadLeftEyeVelocity": "(0.00, 0.00, 0.00)",
    # "HeadLeftEyeAngularVelocity": "(0.00, 0.00, 0.00)",
    # "HeadRightEyePosition": "(0.00, 0.00, 0.00)",
    # "HeadRightEyeRotation": "(0.00000, 0.00000, 0.00000, 1.00000)",
    # "HeadRightEyeVelocity": "(0.00, 0.00, 0.00)",
    # "HeadRightEyeAngularVelocity": "(0.00, 0.00, 0.00)",
    # "CtrlrLeftPrimary2DAxis": "(0.00, 0.00)",
    # "CtrlrLeftGrip": "0",
    # "CtrlrLeftGripButton": "False",
    # "CtrlrLeftMenuButton": "False",
    # "CtrlrLeftPrimaryButton": "False",
    # "CtrlrLeftPrimaryTouch": "False",
    # "CtrlrLeftSecondaryButton": "False",
    # "CtrlrLeftSecondaryTouch": "False",
    # "CtrlrLeftTrigger": "0",
    # "CtrlrLeftTriggerButton": "False",
    # "CtrlrLeftTriggerTouch": "False",
    # "CtrlrLeftPrimary2DAxisClick": "False",
    # "CtrlrLeftPrimary2DAxisTouch": "False",
    # "CtrlrLeftThumbrestTouch": "False",
    # "CtrlrLeftDeviceIsTracked": "False",
    # "CtrlrLeftDeviceTrackingState": "0",

    # "CtrlrLeftDevicePosition": "(0.00, 0.00, 0.00)",
    # "CtrlrLeftDeviceRotation": "(0.00000, 0.00000, 0.00000, 1.00000)",
    # "CtrlrLeftDeviceVelocity": "(0.00, 0.00, 0.00)",
    # "CtrlrLeftDeviceAngularVelocity": "(0.00, 0.00, 0.00)",
    # "CtrlrLeftPointerIsTracked": "False",
    # "CtrlrLeftPointerTrackingState": "0",
    # "CtrlrLeftPointerPosition": "(0.00, 0.00, 0.00)",
    # "CtrlrLeftPointerRotation": "(0.00000, 0.00000, 0.00000, 1.00000)",
    # "CtrlrLeftPointerVelocity": "(0.00, 0.00, 0.00)",
    # "CtrlrLeftPointerAngularVelocity": "(0.00, 0.00, 0.00)",
    # "CtrlrLeftIsTracked": "False",
    # "CtrlrLeftTrackingState": "0",
    # "CtrlrRightPrimary2DAxis": "(0.00, 0.00)",
    # "CtrlrRightGrip": "0",
    # "CtrlrRightGripButton": "False",
    # "CtrlrRightMenuButton": "False",
    # "CtrlrRightPrimaryButton": "False",
    # "CtrlrRightPrimaryTouch": "False",
    # "CtrlrRightSecondaryButton": "False",
    # "CtrlrRightSecondaryTouch": "False",
    # "CtrlrRightTrigger": "0",
    # "CtrlrRightTriggerButton": "False",
    # "CtrlrRightTriggerTouch": "False",
    # "CtrlrRightPrimary2DAxisClick": "False",
    # "CtrlrRightPrimary2DAxisTouch": "False",
    # "CtrlrRightThumbrestTouch": "False",
    # "CtrlrRightDeviceIsTracked": "False",
    # "CtrlrRightDeviceTrackingState": "0",
    # "CtrlrRightDevicePosition": "(0.00, 0.00, 0.00)",
    # "CtrlrRightDeviceRotation": "(0.00000, 0.00000, 0.00000, 1.00000)",
    # "CtrlrRightDeviceVelocity": "(0.00, 0.00, 0.00)",
    # "CtrlrRightDeviceAngularVelocity": "(0.00, 0.00, 0.00)",
    # "CtrlrRightPointerIsTracked": "False",
    # "CtrlrRightPointerTrackingState": "0",
    # "CtrlrRightPointerPosition": "(0.00, 0.00, 0.00)",
    # "CtrlrRightPointerRotation": "(0.00000, 0.00000, 0.00000, 1.00000)",
    # "CtrlrRightPointerVelocity": "(0.00, 0.00, 0.00)",
    # "CtrlrRightPointerAngularVelocity": "(0.00, 0.00, 0.00)",
    # "CtrlrRightIsTracked": "False",
    # "CtrlrRightTrackingState": "0",
    # "EyeLeftRot": "(0.00000, 0.00000, 0.00000, 1.00000)",
    # "EyeRightRot": "(0.00000, 0.00000, 0.00000, 1.00000)"
#   }