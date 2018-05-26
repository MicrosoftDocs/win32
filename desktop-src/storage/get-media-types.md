---
title: GET\_MEDIA\_TYPES structure
description: The GET\_MEDIA\_TYPES structure is used in conjunction with the IOCTL\_STORAGE\_GET\_MEDIA\_TYPES\_EX request to retrieve information about the types of media supported by a device.
ms.assetid: e803505f-37a0-4b20-bd6f-ce0f79eead03
keywords:
- GET_MEDIA_TYPES structure Storage Devices
- PGET_MEDIA_TYPES structure pointer Storage Devices
topic_type:
- apiref
api_name:
- GET_MEDIA_TYPES
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GET\_MEDIA\_TYPES structure

The GET\_MEDIA\_TYPES structure is used in conjunction with the [**IOCTL\_STORAGE\_GET\_MEDIA\_TYPES\_EX**](ioctl-storage-get-media-types-ex.md) request to retrieve information about the types of media supported by a device.

## Syntax


```C++
typedef struct _GET_MEDIA_TYPES {
  ULONG             DeviceType;
  ULONG             MediaInfoCount;
  DEVICE_MEDIA_INFO MediaInfo[1];
} GET_MEDIA_TYPES, *PGET_MEDIA_TYPES;
```



## Members

<dl> <dt>

**DeviceType**
</dt> <dd>

Specifies one of the system-defined FILE\_DEVICE\_*XXX* constants indicating the type of device (such as FILE\_DEVICE\_DISK, FILE\_DEVICE\_KEYBOARD, and so forth) or a vendor-defined value for a new type of device. For more information, see [Specifying Device Types](https://msdn.microsoft.com/library/windows/hardware/ff563821).

</dd> <dt>

**MediaInfoCount**
</dt> <dd>

Contains the number of [**DEVICE\_MEDIA\_INFO**](device-media-info.md) structures in the array starting at **MediaInfo**.

</dd> <dt>

**MediaInfo**
</dt> <dd>

Contains an array whose first element holds the first DEVICE\_MEDIA\_INFO structure in the array.

</dd> </dl>

## Remarks

A storage class driver must handle the [**IOCTL\_STORAGE\_GET\_MEDIA\_TYPES\_EX**](ioctl-storage-get-media-types-ex.md) request to support any device that the Removable Storage Manager (RSM) accesses, whether the device is a stand-alone device or a data transfer element (drive) in a media library or changer.

## Requirements



|                   |                                                                                                                          |
|-------------------|--------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h or Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_GET\_MEDIA\_TYPES\_EX**](ioctl-storage-get-media-types-ex.md)
</dt> <dt>

[**DEVICE\_MEDIA\_INFO**](device-media-info.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20GET_MEDIA_TYPES%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






