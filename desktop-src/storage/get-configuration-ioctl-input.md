---
title: GET\_CONFIGURATION\_IOCTL\_INPUT structure
description: The GET\_CONFIGURATION\_IOCTL\_INPUT structure is used in conjunction with the IOCTL\_CDROM\_GET\_CONFIGURATION request to specify the sort of feature data that the request retrieves.
ms.assetid: 6b8d9cbf-bb05-40a1-9129-52510befebe3
keywords:
- GET_CONFIGURATION_IOCTL_INPUT structure Storage Devices
- PGET_CONFIGURATION_IOCTL_INPUT structure pointer Storage Devices
topic_type:
- apiref
api_name:
- GET_CONFIGURATION_IOCTL_INPUT
api_location:
- ntddmmc.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GET\_CONFIGURATION\_IOCTL\_INPUT structure

The GET\_CONFIGURATION\_IOCTL\_INPUT structure is used in conjunction with the [**IOCTL\_CDROM\_GET\_CONFIGURATION**](ioctl-cdrom-get-configuration.md) request to specify the sort of feature data that the request retrieves.

## Syntax


```C++
typedef struct _GET_CONFIGURATION_IOCTL_INPUT {
  FEATURE_NUMBER Feature;
  ULONG          RequestType;
  PVOID          Reserved[2];
} GET_CONFIGURATION_IOCTL_INPUT, *PGET_CONFIGURATION_IOCTL_INPUT;
```



## Members

<dl> <dt>

**Feature**
</dt> <dd>

Contains an enumerator value of type FEATURE\_NUMBER that indicates the type of feature.

</dd> <dt>

**RequestType**
</dt> <dd>

SCSI\_GET\_CONFIGURATION\_REQUEST\_TYPE\_ALL - Instructs the device to report all of the profiles.

SCSI\_GET\_CONFIGURATION\_REQUEST\_TYPE\_CURRENT - Instructs the device to report the current profile.

SCSI\_GET\_CONFIGURATION\_REQUEST\_TYPE\_ONE - Instructs the device to report one and only one of the profiles.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> </dl>

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddmmc.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**FEATURE\_HEADER**](feature-header.md)
</dt> <dt>

[**FEATURE\_NUMBER**](feature-number.md)
</dt> <dt>

[**IOCTL\_CDROM\_GET\_CONFIGURATION**](ioctl-cdrom-get-configuration.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20GET_CONFIGURATION_IOCTL_INPUT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






