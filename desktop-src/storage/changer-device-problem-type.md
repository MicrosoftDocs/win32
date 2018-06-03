---
title: CHANGER\_DEVICE\_PROBLEM\_TYPE enumeration
description: The CHANGER\_DEVICE\_PROBLEM\_TYPE data type contains the values returned by the ChangerPerformDiagnostics routine.
ms.assetid: 2ba267ad-cfd7-4a19-9ecb-16be9187406a
keywords:
- CHANGER_DEVICE_PROBLEM_TYPE enumeration Storage Devices
- PCHANGER_DEVICE_PROBLEM_TYPE enumeration pointer Storage Devices
topic_type:
- apiref
api_name:
- CHANGER_DEVICE_PROBLEM_TYPE
api_location:
- ntddchgr.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# CHANGER\_DEVICE\_PROBLEM\_TYPE enumeration

The CHANGER\_DEVICE\_PROBLEM\_TYPE data type contains the values returned by the [**ChangerPerformDiagnostics**](changerperformdiagnostics.md) routine.

## Syntax


```C++
typedef enum _CHANGER_DEVICE_PROBLEM_TYPE { 
  DeviceProblemNone                  = 0,
  DeviceProblemHardware              = 1,
  DeviceProblemCHMError              = 2,
  DeviceProblemDoorOpen              = 3,
  DeviceProblemCalibrationError      = 4,
  DeviceProblemTargetFailure         = 5,
  DeviceProblemCHMMoveError          = 6,
  DeviceProblemCHMZeroError          = 7,
  DeviceProblemCartridgeInsertError  = 8,
  DeviceProblemPositionError         = 9,
  DeviceProblemSensorError           = 10,
  DeviceProblemCartridgeEjectError   = 11,
  DeviceProblemGripperError          = 12,
  DeviceProblemDriveError            = 13
} CHANGER_DEVICE_PROBLEM_TYPE, *PCHANGER_DEVICE_PROBLEM_TYPE;
```



## Constants

<dl> <dt>

<span id="DeviceProblemNone"></span><span id="deviceproblemnone"></span><span id="DEVICEPROBLEMNONE"></span>**DeviceProblemNone**
</dt> <dd>

Indicates the device has no problem.

</dd> <dt>

<span id="DeviceProblemHardware"></span><span id="deviceproblemhardware"></span><span id="DEVICEPROBLEMHARDWARE"></span>**DeviceProblemHardware**
</dt> <dd>

Indicates the device has had a hardware error.

</dd> <dt>

<span id="DeviceProblemCHMError"></span><span id="deviceproblemchmerror"></span><span id="DEVICEPROBLEMCHMERROR"></span>**DeviceProblemCHMError**
</dt> <dd>

Indicates the Cartridge Handling Mechanism (CHM) has some problem.

</dd> <dt>

<span id="DeviceProblemDoorOpen"></span><span id="deviceproblemdooropen"></span><span id="DEVICEPROBLEMDOOROPEN"></span>**DeviceProblemDoorOpen**
</dt> <dd>

Indicates the changer's door is open.

</dd> <dt>

<span id="DeviceProblemCalibrationError"></span><span id="deviceproblemcalibrationerror"></span><span id="DEVICEPROBLEMCALIBRATIONERROR"></span>**DeviceProblemCalibrationError**
</dt> <dd>

Indicates the changer has a calibration problem.

</dd> <dt>

<span id="DeviceProblemTargetFailure"></span><span id="deviceproblemtargetfailure"></span><span id="DEVICEPROBLEMTARGETFAILURE"></span>**DeviceProblemTargetFailure**
</dt> <dd>

Indicates a target failure has occurred.

</dd> <dt>

<span id="DeviceProblemCHMMoveError"></span><span id="deviceproblemchmmoveerror"></span><span id="DEVICEPROBLEMCHMMOVEERROR"></span>**DeviceProblemCHMMoveError**
</dt> <dd>

Indicates the CHM is blocked and cannot move.

</dd> <dt>

<span id="DeviceProblemCHMZeroError"></span><span id="deviceproblemchmzeroerror"></span><span id="DEVICEPROBLEMCHMZEROERROR"></span>**DeviceProblemCHMZeroError**
</dt> <dd>

Indicates the CHM could not define zero on one or more of its axis.

</dd> <dt>

<span id="DeviceProblemCartridgeInsertError"></span><span id="deviceproblemcartridgeinserterror"></span><span id="DEVICEPROBLEMCARTRIDGEINSERTERROR"></span>**DeviceProblemCartridgeInsertError**
</dt> <dd>

Indicates an error occurred while loading a cartridge in the drive.

</dd> <dt>

<span id="DeviceProblemPositionError"></span><span id="deviceproblempositionerror"></span><span id="DEVICEPROBLEMPOSITIONERROR"></span>**DeviceProblemPositionError**
</dt> <dd>

Indicates the CHM has a problem positioning itself to some point.

</dd> <dt>

<span id="DeviceProblemSensorError"></span><span id="deviceproblemsensorerror"></span><span id="DEVICEPROBLEMSENSORERROR"></span>**DeviceProblemSensorError**
</dt> <dd>

Indicates the device's sensors are malfunctioning.

</dd> <dt>

<span id="DeviceProblemCartridgeEjectError"></span><span id="deviceproblemcartridgeejecterror"></span><span id="DEVICEPROBLEMCARTRIDGEEJECTERROR"></span>**DeviceProblemCartridgeEjectError**
</dt> <dd>

Indicates an error occurred while unloading a cartridge.

</dd> <dt>

<span id="DeviceProblemGripperError"></span><span id="deviceproblemgrippererror"></span><span id="DEVICEPROBLEMGRIPPERERROR"></span>**DeviceProblemGripperError**
</dt> <dd>

Indicates the media gripper has a problem.

</dd> <dt>

<span id="DeviceProblemDriveError"></span><span id="deviceproblemdriveerror"></span><span id="DEVICEPROBLEMDRIVEERROR"></span>**DeviceProblemDriveError**
</dt> <dd>

Indicates the changer's drive is malfunctioning.

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddchgr.h</dt> </dl> |



## See also

<dl> <dt>

[**ChangerPerformDiagnostics**](changerperformdiagnostics.md)
</dt> <dt>

[**WMI\_CHANGER\_PROBLEM\_DEVICE\_ERROR**](wmi-changer-problem-device-error.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CHANGER_DEVICE_PROBLEM_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






