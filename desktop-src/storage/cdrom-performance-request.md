---
title: CDROM\_PERFORMANCE\_REQUEST structure
description: The CDROM\_PERFORMANCE\_REQUEST structure is used as an input parameter to the IOCTL\_CDROM\_GET\_PERFORMANCE I/O control request and describes the performance data requested.
ms.assetid: E43D2F2C-B5A1-4724-AEBC-F4B6A85EA846
keywords:
- CDROM_PERFORMANCE_REQUEST structure Storage Devices
- PCDROM_PERFORMANCE_REQUEST structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CDROM_PERFORMANCE_REQUEST
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

# CDROM\_PERFORMANCE\_REQUEST structure

The **CDROM\_PERFORMANCE\_REQUEST** structure is used as an input parameter to the [**IOCTL\_CDROM\_GET\_PERFORMANCE**](ioctl-cdrom-get-performance.md) I/O control request and describes the performance data requested.

## Syntax


```C++
typedef struct _CDROM_PERFORMANCE_REQUEST {
  CDROM_PERFORMANCE_REQUEST_TYPE       RequestType;
  CDROM_PERFORMANCE_TYPE               PerformanceType;
  CDROM_PERFORMANCE_EXCEPTION_TYPE     Exceptions;
  CDROM_PERFORMANCE_TOLERANCE_TYPE     Tolerance;
  ULONG                                StartingLba;
} CDROM_PERFORMANCE_REQUEST, *PCDROM_PERFORMANCE_REQUEST;
```



## Members

<dl> <dt>

**RequestType**
</dt> <dd>

The [**CDROM\_PERFORMANCE\_REQUEST\_TYPE**](cdrom-performance-request-type.md) enumeration specifies the request type, **CdromPerformanceRequest**, or **CdromWriteSpeedRequest**.

</dd> <dt>

**PerformanceType**
</dt> <dd>

The [**CDROM\_PERFORMANCE\_TYPE**](cdrom-performance-type.md) enumeration specifies the type of performance data.

</dd> <dt>

**Exceptions**
</dt> <dd>

The [**CDROM\_PERFORMANCE\_EXCEPTION\_TYPE**](cdrom-performance-exception-type.md) enumeration specifies the type of exception.

</dd> <dt>

**Tolerance**
</dt> <dd>

The [**CDROM\_PERFORMANCE\_TOLERANCE\_TYPE**](cdrom-performance-tolerance-type.md) enumeration specifies the performance tolerance for the nominal performance and the time tolerance (seek delay) for the exception list.

</dd> <dt>

**StartingLba**
</dt> <dd>

The starting logical block address field.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CDROM\_GET\_PERFORMANCE**](ioctl-cdrom-get-performance.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_PERFORMANCE_REQUEST%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






