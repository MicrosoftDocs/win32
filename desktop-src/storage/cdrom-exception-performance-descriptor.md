---
title: CDROM\_EXCEPTION\_PERFORMANCE\_DESCRIPTOR structure
description: The CDROM\_EXCEPTION\_PERFORMANCE\_DESCRIPTOR structure indicates that the result data from the IOCTL\_CDROM\_GET\_PERFORMANCE I/O control request is for exception conditions.
ms.assetid: 054C8E89-D0A6-46D1-A5AA-2BE73931BB7A
keywords:
- CDROM_EXCEPTION_PERFORMANCE_DESCRIPTOR structure Storage Devices
- PCDROM_EXCEPTION_PERFORMANCE_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CDROM_EXCEPTION_PERFORMANCE_DESCRIPTOR
api_location:
- Ntddcdrm.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# CDROM\_EXCEPTION\_PERFORMANCE\_DESCRIPTOR structure

The **CDROM\_EXCEPTION\_PERFORMANCE\_DESCRIPTOR** structure indicates that the result data from the [**IOCTL\_CDROM\_GET\_PERFORMANCE**](ioctl-cdrom-get-performance.md) I/O control request is for exception conditions. Exception conditions are exception locations that could cause seek delays to occur. The **CDROM\_EXCEPTION\_PERFORMANCE\_DESCRIPTOR** is returned by the **IOCTL\_CDROM\_GET\_PERFORMANCE** I/O control request when the request type is **CdromPerformanceRequest** and the **Except** field of the [**CDROM\_PERFORMANCE\_HEADER**](cdrom-performance-header.md) is true (1). Separate descriptors are returned for read and write performance requests. The fields in **CDROM\_EXCEPTION\_PERFORMANCE\_DESCRIPTOR** correspond to the similarly named fields in the Performance Descriptor - Exceptions table described in the MultiMedia Command Set - 6 (MMC-6) specification.

## Syntax


```C++
typedef struct _CDROM_EXCEPTION_PERFORMANCE_DESCRIPTOR {
  UCHAR LBA[4];
  UCHAR Time[2];
} CDROM_EXCEPTION_PERFORMANCE_DESCRIPTOR, *PCDROM_EXCEPTION_PERFORMANCE_DESCRIPTOR;
```



## Members

<dl> <dt>

**LBA**
</dt> <dd>

The LBA field indicates that there is a seek delay between the logical block address (LBA) and the preceding LBA (LBA -1).

</dd> <dt>

**Time**
</dt> <dd>

The Time field indicates the expected additional seek delay between LBA and the preceding LBA (LBA - 1) from nominal, in units of tenths of milliseconds (100 microseconds). The cause of the seek delay might be linear replacement, zone boundaries, or other media dependent features.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CDROM\_GET\_PERFORMANCE**](ioctl-cdrom-get-performance.md)
</dt> <dt>

[**CDROM\_PERFORMANCE\_HEADER**](cdrom-performance-header.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_EXCEPTION_PERFORMANCE_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






