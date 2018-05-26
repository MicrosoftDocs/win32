---
title: CDROM\_NOMINAL\_PERFORMANCE\_DESCRIPTOR structure
description: The CDROM\_NOMINAL\_PERFORMANCE\_DESCRIPTOR structure gives the host an approximation of logical unit performance.
ms.assetid: F931CE79-7070-43B9-BFED-9F3D5B18623E
keywords:
- CDROM_NOMINAL_PERFORMANCE_DESCRIPTOR structure Storage Devices
- PCDROM_NOMINAL_PERFORMANCE_DESCRIPTOR structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CDROM_NOMINAL_PERFORMANCE_DESCRIPTOR
api_location:
- Ntddcdrm.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CDROM\_NOMINAL\_PERFORMANCE\_DESCRIPTOR structure

The **CDROM\_NOMINAL\_PERFORMANCE\_DESCRIPTOR** structure gives the host an approximation of logical unit performance. It is returned by the [**IOCTL\_CDROM\_GET\_PERFORMANCE**](ioctl-cdrom-get-performance.md) I/O control request when the request type is **CdromPerformanceRequest** and the **Except** field of the [**CDROM\_PERFORMANCE\_HEADER**](cdrom-performance-header.md) is false (0). Separate descriptors are returned for read and write performance requests. The fields in **CDROM\_NOMINAL\_PERFORMANCE\_DESCRIPTOR** correspond to the similarly named fields in the "Performance Descriptor - Nominal Performance" table described in the MultiMedia Command Set - 6 (MMC-6) specification.

## Syntax


```C++
typedef struct _CDROM_NOMINAL_PERFORMANCE_DESCRIPTOR {
  UCHAR  StartLba[4];
  UCHAR StartPerformance[4];
  UCHAR  EndLba[4];
  UCHAR  EndPerformance[4];
} CDROM_NOMINAL_PERFORMANCE_DESCRIPTOR, *PCDROM_NOMINAL_PERFORMANCE_DESCRIPTOR;
```



## Members

<dl> <dt>

 **StartLba**
</dt> <dd>

The StartLba field (Start LBA) contains the first logical block address of the extent described by this descriptor.

</dd> <dt>

**StartPerformance**
</dt> <dd>

The StartPerformance field (Start Performance) contains the nominal logical unit performance at the Start LBA in kilobytes per second.

</dd> <dt>

 **EndLba**
</dt> <dd>

The EndLba field (End LBA) contains the last logical block address of the extent described by this descriptor.

</dd> <dt>

 **EndPerformance**
</dt> <dd>

The EndPerformance field (End Performance) contains the nominal logical unit performance at the End LBA in kilobytes per second.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_NOMINAL_PERFORMANCE_DESCRIPTOR%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






