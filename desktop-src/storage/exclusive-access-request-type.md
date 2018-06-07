---
title: EXCLUSIVE\_ACCESS\_REQUEST\_TYPE enumeration
description: The EXCLUSIVE\_ACCESS\_REQUEST\_TYPE enumeration is used to report the exclusive access state of a CD-ROM device.
ms.assetid: 314dfdeb-1821-444a-84c6-2ee7fa536122
keywords:
- EXCLUSIVE_ACCESS_REQUEST_TYPE enumeration Storage Devices
- PEXCLUSIVE_ACCESS_REQUEST_TYPE enumeration pointer Storage Devices
topic_type:
- apiref
api_name:
- EXCLUSIVE_ACCESS_REQUEST_TYPE
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# EXCLUSIVE\_ACCESS\_REQUEST\_TYPE enumeration

The EXCLUSIVE\_ACCESS\_REQUEST\_TYPE enumeration is used to report the exclusive access state of a CD-ROM device.

## Syntax


```C++
typedef enum _EXCLUSIVE_ACCESS_REQUEST_TYPE { 
  ExclusiveAccessQueryState    = 0,
  ExclusiveAccessLockDevice    = 1,
  ExclusiveAccessUnlockDevice  = 2
} EXCLUSIVE_ACCESS_REQUEST_TYPE, *PEXCLUSIVE_ACCESS_REQUEST_TYPE;
```



## Constants

<dl> <dt>

<span id="ExclusiveAccessQueryState"></span><span id="exclusiveaccessquerystate"></span><span id="EXCLUSIVEACCESSQUERYSTATE"></span>**ExclusiveAccessQueryState**
</dt> <dd>

A query for the access state of a CD-ROM device.

</dd> <dt>

<span id="ExclusiveAccessLockDevice"></span><span id="exclusiveaccesslockdevice"></span><span id="EXCLUSIVEACCESSLOCKDEVICE"></span>**ExclusiveAccessLockDevice**
</dt> <dd>

A request for the CD-ROM class driver to lock a CD-ROM device for exclusive access by the caller.

</dd> <dt>

<span id="ExclusiveAccessUnlockDevice"></span><span id="exclusiveaccessunlockdevice"></span><span id="EXCLUSIVEACCESSUNLOCKDEVICE"></span>**ExclusiveAccessUnlockDevice**
</dt> <dd>

A request for the CD-ROM class driver to unlock a CD-ROM device that was previously locked for exclusive access.

</dd> </dl>

## Remarks

The EXCLUSIVE\_ACCESS\_REQUEST\_TYPE enumeration is used with the [**IOCTL\_CDROM\_EXCLUSIVE\_ACCESS**](ioctl-cdrom-exclusive-access.md) request to query the access state of a CD-ROM device or to lock or unlock the device for exclusive access.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CDROM\_EXCLUSIVE\_ACCESS**](ioctl-cdrom-exclusive-access.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20EXCLUSIVE_ACCESS_REQUEST_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






