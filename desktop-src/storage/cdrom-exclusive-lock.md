---
title: CDROM\_EXCLUSIVE\_LOCK structure
description: The CDROM\_EXCLUSIVE\_LOCK structure is used with the IOCTL\_CDROM\_EXCLUSIVE\_ACCESS request to lock a CD-ROM device for exclusive access.
ms.assetid: 8c94cdb2-965a-448c-aa97-f7aae9550662
keywords:
- CDROM_EXCLUSIVE_LOCK structure Storage Devices
- PCDROM_EXCLUSIVE_LOCK structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CDROM_EXCLUSIVE_LOCK
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CDROM\_EXCLUSIVE\_LOCK structure

The CDROM\_EXCLUSIVE\_LOCK structure is used with the [**IOCTL\_CDROM\_EXCLUSIVE\_ACCESS**](ioctl-cdrom-exclusive-access.md) request to lock a CD-ROM device for exclusive access.

## Syntax


```C++
typedef struct _CDROM_EXCLUSIVE_LOCK {
  CDROM_EXCLUSIVE_ACCESS Access;
  UCHAR                  CallerName[CDROM_EXCLUSIVE_CALLER_LENGTH];
} CDROM_EXCLUSIVE_LOCK, *PCDROM_EXCLUSIVE_LOCK;
```



## Members

<dl> <dt>

**Access**
</dt> <dd>

A [**CDROM\_EXCLUSIVE\_ACCESS**](cdrom-exclusive-access.md) structure that specifies the type of exclusive access request and the flags that are associated with the request.

</dd> <dt>

**CallerName**
</dt> <dd>

A **NULL**-terminated string that identifies the application or system component that has a lock on the CD-ROM device. The length of the string must be less than or equal to CDROM\_EXCLUSIVE\_CALLER\_LENGTH bytes, including the **NULL** character at the end of the string. The string must contain alphanumerics (A - Z, a - z, 0 - 9), spaces, periods, commas, colons (:), semi-colons (;), hyphens (-), and underscores (\_).

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**CDROM\_EXCLUSIVE\_ACCESS**](cdrom-exclusive-access.md)
</dt> <dt>

[**IOCTL\_CDROM\_EXCLUSIVE\_ACCESS**](ioctl-cdrom-exclusive-access.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_EXCLUSIVE_LOCK%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






