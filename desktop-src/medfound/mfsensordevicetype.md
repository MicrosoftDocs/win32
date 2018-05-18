---
Description: 'Specifies the type of a sensor device. A value from this enumeration is returned by IMFSensorDevice::GetDeviceType.'
ms.assetid: '13CC03E6-F0E2-4E69-B94F-4CF1BC7D0C23'
title: MFSensorDeviceType enumeration
---

# MFSensorDeviceType enumeration

Specifies the type of a sensor device. A value from this enumeration is returned by [**IMFSensorDevice::GetDeviceType**](imfsensordevice-getdevicetype.md).

## Syntax


```C++
typedef enum _MFSensorDeviceType { 
  MFSensorDeviceType_Unknown        = 0,
  MFSensorDeviceType_Device         = 1,
  MFSensorDeviceType_MediaSource    = 2,
  MFSensorDeviceType_FrameProvider  = 3
} MFSensorDeviceType;
```



## Constants

<dl> <dt>

<span id="MFSensorDeviceType_Unknown"></span><span id="mfsensordevicetype_unknown"></span><span id="MFSENSORDEVICETYPE_UNKNOWN"></span>**MFSensorDeviceType\_Unknown**
</dt> <dd>

The sensor device type is unknown.

</dd> <dt>

<span id="MFSensorDeviceType_Device"></span><span id="mfsensordevicetype_device"></span><span id="MFSENSORDEVICETYPE_DEVICE"></span>**MFSensorDeviceType\_Device**
</dt> <dd>

The sensor device is a physical device. Physical cameras may register as [KSCATEGORY\_SENSOR\_CAMERA](https://msdn.microsoft.com/en-us/library/windows/hardware/ff548567.aspx) or [KSCATEGORY\_VIDEO\_CAMERA](https://msdn.microsoft.com/en-us/library/windows/hardware/ff548567.aspx) or both.

</dd> <dt>

<span id="MFSensorDeviceType_MediaSource"></span><span id="mfsensordevicetype_mediasource"></span><span id="MFSENSORDEVICETYPE_MEDIASOURCE"></span>**MFSensorDeviceType\_MediaSource**
</dt> <dd>

The sensor device is a custom media source.

</dd> <dt>

<span id="MFSensorDeviceType_FrameProvider"></span><span id="mfsensordevicetype_frameprovider"></span><span id="MFSENSORDEVICETYPE_FRAMEPROVIDER"></span>**MFSensorDeviceType\_FrameProvider**
</dt> <dd>

The sensor device is a legacy frame provider.

</dd> </dl>

 

 



