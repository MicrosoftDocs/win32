---
title: TAPE\_DRIVE\_PROBLEM\_TYPE enumeration
description: The TAPE\_DRIVE\_PROBLEM\_TYPE enumerator is used to report problems with the tape drive.
ms.assetid: 'c2732686-5f95-41fd-8e47-8acf6900a44b'
keywords: ["TAPE_DRIVE_PROBLEM_TYPE enumeration Storage Devices"]
topic_type:
- apiref
api_name:
- TAPE_DRIVE_PROBLEM_TYPE
api_location:
- ntddtape.h
api_type:
- HeaderDef
---

# TAPE\_DRIVE\_PROBLEM\_TYPE enumeration

The TAPE\_DRIVE\_PROBLEM\_TYPE enumerator is used to report problems with the tape drive.

## Syntax


```C++
typedef enum _TAPE_DRIVE_PROBLEM_TYPE { 
  TapeDriveProblemNone          = 0,
  TapeDriveReadWriteWarning     = 1,
  TapeDriveReadWriteError       = 2,
  TapeDriveReadWarning          = 3,
  TapeDriveWriteWarning         = 4,
  TapeDriveReadError            = 5,
  TapeDriveWriteError           = 6,
  TapeDriveHardwareError        = 7,
  TapeDriveUnsupportedMedia     = 8,
  TapeDriveScsiConnectionError  = 9,
  TapeDriveTimetoClean          = 10,
  TapeDriveCleanDriveNow        = 11,
  TapeDriveMediaLifeExpired     = 12,
  TapeDriveSnappedTape          = 13
} TAPE_DRIVE_PROBLEM_TYPE;
```



## Constants

<dl> <dt>

<span id="TapeDriveProblemNone"></span><span id="tapedriveproblemnone"></span><span id="TAPEDRIVEPROBLEMNONE"></span>**TapeDriveProblemNone**
</dt> <dd>

Indicates that there is no tape drive problem.

</dd> <dt>

<span id="TapeDriveReadWriteWarning"></span><span id="tapedrivereadwritewarning"></span><span id="TAPEDRIVEREADWRITEWARNING"></span>**TapeDriveReadWriteWarning**
</dt> <dd>

Indicates that the tape drive is having problems doing reads or writes. This is a warning.

</dd> <dt>

<span id="TapeDriveReadWriteError"></span><span id="tapedrivereadwriteerror"></span><span id="TAPEDRIVEREADWRITEERROR"></span>**TapeDriveReadWriteError**
</dt> <dd>

Indicates that the tape drive is having problems doing reads or writes. This is a severe error.

</dd> <dt>

<span id="TapeDriveReadWarning"></span><span id="tapedrivereadwarning"></span><span id="TAPEDRIVEREADWARNING"></span>**TapeDriveReadWarning**
</dt> <dd>

Indicates that the tape drive is having problems doing reads. This is a warning.

</dd> <dt>

<span id="TapeDriveWriteWarning"></span><span id="tapedrivewritewarning"></span><span id="TAPEDRIVEWRITEWARNING"></span>**TapeDriveWriteWarning**
</dt> <dd>

Indicates that the tape drive is having problems doing writes. This is a warning.

</dd> <dt>

<span id="TapeDriveReadError"></span><span id="tapedrivereaderror"></span><span id="TAPEDRIVEREADERROR"></span>**TapeDriveReadError**
</dt> <dd>

Indicates that the tape drive is having problems doing reads. This is a severe error.

</dd> <dt>

<span id="TapeDriveWriteError"></span><span id="tapedrivewriteerror"></span><span id="TAPEDRIVEWRITEERROR"></span>**TapeDriveWriteError**
</dt> <dd>

Indicates that the tape drive is having problems doing writes. This is a severe error.

</dd> <dt>

<span id="TapeDriveHardwareError"></span><span id="tapedrivehardwareerror"></span><span id="TAPEDRIVEHARDWAREERROR"></span>**TapeDriveHardwareError**
</dt> <dd>

Indicates that the tape drive had a hardware error.

</dd> <dt>

<span id="TapeDriveUnsupportedMedia"></span><span id="tapedriveunsupportedmedia"></span><span id="TAPEDRIVEUNSUPPORTEDMEDIA"></span>**TapeDriveUnsupportedMedia**
</dt> <dd>

Indicates that the media format is not supported.

</dd> <dt>

<span id="TapeDriveScsiConnectionError"></span><span id="tapedrivescsiconnectionerror"></span><span id="TAPEDRIVESCSICONNECTIONERROR"></span>**TapeDriveScsiConnectionError**
</dt> <dd>

Indicates that there is a SCSI cable or connection error.

</dd> <dt>

<span id="TapeDriveTimetoClean"></span><span id="tapedrivetimetoclean"></span><span id="TAPEDRIVETIMETOCLEAN"></span>**TapeDriveTimetoClean**
</dt> <dd>

Indicates that the tape drive requires cleaning.

</dd> <dt>

<span id="TapeDriveCleanDriveNow"></span><span id="tapedrivecleandrivenow"></span><span id="TAPEDRIVECLEANDRIVENOW"></span>**TapeDriveCleanDriveNow**
</dt> <dd>

Indicates that the tape drive requires cleaning.

</dd> <dt>

<span id="TapeDriveMediaLifeExpired"></span><span id="tapedrivemedialifeexpired"></span><span id="TAPEDRIVEMEDIALIFEEXPIRED"></span>**TapeDriveMediaLifeExpired**
</dt> <dd>

Indicates that the media life has expired. Media needs to be replaced.

</dd> <dt>

<span id="TapeDriveSnappedTape"></span><span id="tapedrivesnappedtape"></span><span id="TAPEDRIVESNAPPEDTAPE"></span>**TapeDriveSnappedTape**
</dt> <dd>

Indicates that the tape has snapped.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddtape.h (include Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**TAPE\_WMI\_OPERATIONS**](tape-wmi-operations.md)
</dt> <dt>

[*TapeMiniWMIControl*](https://msdn.microsoft.com/library/windows/hardware/ff567957)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TAPE_DRIVE_PROBLEM_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






