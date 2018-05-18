---
Description: 'Specifies the sharing mode of an IMFSensorDevice.'
ms.assetid: 'D405AB48-13EC-4859-91B6-0DB797F85DBE'
title: MFSensorDeviceMode enumeration
---

# MFSensorDeviceMode enumeration

Specifies the sharing mode of an [**IMFSensorDevice**](imfsensordevice.md).

## Syntax


```C++
typedef enum _MFSensorDeviceMode { 
  MFSensorDeviceMode_Controller  = 0,
  MFSensorDeviceMode_Shared      = 1
} MFSensorDeviceMode;
```



## Constants

<dl> <dt>

<span id="MFSensorDeviceMode_Controller"></span><span id="mfsensordevicemode_controller"></span><span id="MFSENSORDEVICEMODE_CONTROLLER"></span>**MFSensorDeviceMode\_Controller**
</dt> <dd>

The device is in controller mode, which means its settings can be modified.

</dd> <dt>

<span id="MFSensorDeviceMode_Shared"></span><span id="mfsensordevicemode_shared"></span><span id="MFSENSORDEVICEMODE_SHARED"></span>**MFSensorDeviceMode\_Shared**
</dt> <dd>

The device is in shared mode, which means it's settings can't be modified.

</dd> </dl>

 

 



