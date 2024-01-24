---
description: The WPD\_DEVICE\_TYPES enumeration type describes the different Windows Portable Device (WPD) types commonly used to determine the basic classification and visual appearance of a portable device.
ms.assetid: 51714e0f-e9b7-4474-a8bb-da3875ef5399
title: WPD_DEVICE_TYPES enumeration (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WPD_DEVICE_TYPES
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# WPD\_DEVICE\_TYPES enumeration

The **WPD\_DEVICE\_TYPES** enumeration type describes the different Windows Portable Device (WPD) types commonly used to determine the basic classification and visual appearance of a portable device.

## Syntax


```C++
typedef enum tagWPD_DEVICE_TYPES { 
  WPD_DEVICE_TYPE_GENERIC                       = 0,
  WPD_DEVICE_TYPE_CAMERA                        = 1,
  WPD_DEVICE_TYPE_MEDIA_PLAYER                  = 2,
  WPD_DEVICE_TYPE_PHONE                         = 3,
  WPD_DEVICE_TYPE_VIDEO                         = 4,
  WPD_DEVICE_TYPE_PERSONAL_INFORMATION_MANAGER  = 5,
  WPD_DEVICE_TYPE_AUDIO_RECORDER                = 6
} WPD_DEVICE_TYPES;
```



## Constants

<dl> <dt>

<span id="WPD_DEVICE_TYPE_GENERIC"></span><span id="wpd_device_type_generic"></span>**WPD\_DEVICE\_TYPE\_GENERIC**
</dt> <dd>

A generic WPD that includes multifunction devices that do not fall into one of the other [**WPD\_DEVICE\_TYPES**](wpd-device-types.md) enumeration values.

</dd> <dt>

<span id="WPD_DEVICE_TYPE_CAMERA"></span><span id="wpd_device_type_camera"></span>**WPD\_DEVICE\_TYPE\_CAMERA**
</dt> <dd>

A camera device, such as a digital still camera.

</dd> <dt>

<span id="WPD_DEVICE_TYPE_MEDIA_PLAYER"></span><span id="wpd_device_type_media_player"></span>**WPD\_DEVICE\_TYPE\_MEDIA\_PLAYER**
</dt> <dd>

A media player device that supports playing audio, video, or viewing pictures, such as a portable music player or portable media center. Not all of this functionally is classified as a WPD\_DEVICE\_TYPE\_MEDIA\_PLAYER. For example, portable music player devices are classified as WPD\_DEVICE\_TYPE\_MEDIA\_PLAYER.

</dd> <dt>

<span id="WPD_DEVICE_TYPE_PHONE"></span><span id="wpd_device_type_phone"></span>**WPD\_DEVICE\_TYPE\_PHONE**
</dt> <dd>

A phone device, such as a mobile phone.

</dd> <dt>

<span id="WPD_DEVICE_TYPE_VIDEO"></span><span id="wpd_device_type_video"></span>**WPD\_DEVICE\_TYPE\_VIDEO**
</dt> <dd>

A video device.

</dd> <dt>

<span id="WPD_DEVICE_TYPE_PERSONAL_INFORMATION_MANAGER"></span><span id="wpd_device_type_personal_information_manager"></span>**WPD\_DEVICE\_TYPE\_PERSONAL\_INFORMATION\_MANAGER**
</dt> <dd>

A personal information manager device.

</dd> <dt>

<span id="WPD_DEVICE_TYPE_AUDIO_RECORDER"></span><span id="wpd_device_type_audio_recorder"></span>**WPD\_DEVICE\_TYPE\_AUDIO\_RECORDER**
</dt> <dd>

An audio recorder device.

</dd> </dl>

## Remarks

**WPD\_DEVICE\_TYPES** are read using the [**IPortableDeviceManager**](/windows/desktop/api/PortableDeviceApi/nn-portabledeviceapi-iportabledevicemanager) interface. WPD applications may use these values to determine the generic visual appearance of the device. That is, a camera picture is displayed for camera-like devices, a mobile phone picture is displayed for phone-like devices, and so on.

> [!Note]  
> WPD applications must use the capabilities of the portable device to determine functionally, not the **WPD\_DEVICE\_TYPES** value.

 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Structures and Enumeration Types**](structures-and-enumeration-types.md)
</dt> </dl>

 

 




