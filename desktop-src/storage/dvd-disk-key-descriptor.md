---
title: DVD\_DISK\_KEY\_DESCRIPTOR structure
description: The DVD\_DISK\_KEY\_DESCRIPTOR structure is used in conjunction with the IOCTL\_DVD\_READ\_STRUCTURE request to retrieve a DVD disc key descriptor.
ms.assetid: 48b0e44d-51bb-48b1-bcbc-6a51fde3c8db
keywords:
- DVD_DISK_KEY_DESCRIPTOR structure Storage Devices
- PDVD_DISK_KEY_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DVD_DISK_KEY_DESCRIPTOR
api_location:
- ntddcdvd.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DVD\_DISK\_KEY\_DESCRIPTOR structure

The DVD\_DISK\_KEY\_DESCRIPTOR structure is used in conjunction with the [**IOCTL\_DVD\_READ\_STRUCTURE**](ioctl-dvd-read-structure.md) request to retrieve a DVD disc key descriptor.

## Syntax


```C++
typedef struct _DVD_DISK_KEY_DESCRIPTOR {
  UCHAR DiskKeyData[2048];
} DVD_DISK_KEY_DESCRIPTOR, *PDVD_DISK_KEY_DESCRIPTOR;
```



## Members

<dl> <dt>

**DiskKeyData**
</dt> <dd>

Pointer to a buffer containing the disc key data obfuscated by the bus key.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_DVD\_READ\_STRUCTURE**](ioctl-dvd-read-structure.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DVD_DISK_KEY_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






