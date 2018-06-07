---
title: CDROM\_PERFORMANCE\_HEADER structure
description: The CDROM\_PERFORMANCE\_HEADER structure is used by the IOCTL\_CDROM\_GET\_PERFORMANCE IOCTL to return data. When the request type is CdromPerformanceRequest, the IOCTL returns this header followed by optional descriptors.
ms.assetid: D7B47E18-038E-41B4-85E5-A48931CDCA89
keywords:
- CDROM_PERFORMANCE_HEADER structure Storage Devices
- PCDROM_PERFORMANCE_HEADER structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CDROM_PERFORMANCE_HEADER
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

# CDROM\_PERFORMANCE\_HEADER structure

The CDROM\_PERFORMANCE\_HEADER structure is used by the [**IOCTL\_CDROM\_GET\_PERFORMANCE**](ioctl-cdrom-get-performance.md) IOCTL to return data. When the request type is CdromPerformanceRequest, the IOCTL returns this header followed by optional descriptors.

## Syntax


```C++
typedef struct _CDROM_PERFORMANCE_HEADER {
  UCHAR DataLength[4];
  UCHAR  Except  :1;
  UCHAR Write  :1;
  UCHAR Reserved1  :6;
  UCHAR   Reserved2[3];
  UCHAR  Data[0];
} CDROM_PERFORMANCE_HEADER, *PCDROM_PERFORMANCE_HEADER;
```



## Members

<dl> <dt>

**DataLength**
</dt> <dd>

The size of the available data (not just the size of returned data). The size does not include this **Datalength** field.

</dd> <dt>

 **Except**
</dt> <dd>

The format of the descriptors that follow the header depend on the value in this field. If false (0), the [**CDROM\_NOMINAL\_PERFORMANCE\_DESCRIPTOR**](cdrom-nominal-performance-descriptor.md) follows the **CDROM\_PERFORMANCE\_HEADER** in the returned data. If true (1), the [**CDROM\_EXCEPTION\_PERFORMANCE\_DESCRIPTOR**](cdrom-exception-performance-descriptor.md) follows the **CDROM\_PERFORMANCE\_HEADER** in the returned data.

</dd> <dt>

**Write**
</dt> <dd>

Indicates whether the result data is for read or write performance. If false (0), it indicates that the result data is for read performance. If true (1), it indicates that the result data is for write performance.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

 **Reserved2**
</dt> <dd>

Reserved.

</dd> <dt>

 **Data**
</dt> <dd>

Contains a list of the following records, depending upon the type of request: [**CDROM\_NOMINAL\_PERFORMANCE\_DESCRIPTOR**](cdrom-nominal-performance-descriptor.md), [**CDROM\_EXCEPTION\_PERFORMANCE\_DESCRIPTOR**](cdrom-exception-performance-descriptor.md), [**CDROM\_WRITE\_SPEED\_DESCRIPTOR**](cdrom-write-speed-descriptor.md).

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CDROM\_GET\_PERFORMANCE**](ioctl-cdrom-get-performance.md)
</dt> <dt>

[**CDROM\_NOMINAL\_PERFORMANCE\_DESCRIPTOR**](cdrom-nominal-performance-descriptor.md)
</dt> <dt>

[**CDROM\_EXCEPTION\_PERFORMANCE\_DESCRIPTOR**](cdrom-exception-performance-descriptor.md)
</dt> <dt>

[**CDROM\_WRITE\_SPEED\_DESCRIPTOR**](cdrom-write-speed-descriptor.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_PERFORMANCE_HEADER%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






