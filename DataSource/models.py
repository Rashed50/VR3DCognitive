from django.db import models

# Create your models here.

class   VRModel(models.Model):

    sessionID = models.CharField(max_length=150)    
    frame_number = models.CharField(max_length=20)    
    timestamp = models.CharField(max_length=150)    
    sensor_data = models.TextField(max_length=500) 

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

      

    class Meta:
        db_table ='vr3d_info'



class VRUser(models.Model):
    class Meta:
        db_table = 'vrusers'
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=13)    
    email = models.CharField(max_length=60,default=None,unique=True)
    password = models.CharField(max_length=60,default=True)
    country_id = models.SmallIntegerField(default=1)
    state_id = models.SmallIntegerField(default=1)
    city = models.CharField(max_length=100,default="")
    address = models.TextField(max_length=300,default=None)
    address2 = models.TextField(max_length=300,default="")
    zip = models.CharField(max_length=10,default="")
    def __str__(self):
        return self.first_name


 