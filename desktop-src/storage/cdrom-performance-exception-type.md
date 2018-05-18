---
title: CDROM\_PERFORMANCE\_EXCEPTION\_TYPE enumeration
description: The CDROM\_PERFORMANCE\_EXCEPTION\_TYPE enumeration defines the exceptional conditions for performance data.
ms.assetid: '4AD156F8-911F-4D70-8B0E-8BB0D0747470'
keywords: ["CDROM_PERFORMANCE_EXCEPTION_TYPE enumeration Storage Devices", "PCDROM_PERFORMANCE_EXCEPTION_TYPE enumeration pointer Storage Devices"]
topic_type:
- apiref
api_name:
- CDROM_PERFORMANCE_EXCEPTION_TYPE
api_location:
- Ntddcdrm.h
api_type:
- HeaderDef
---

# CDROM\_PERFORMANCE\_EXCEPTION\_TYPE enumeration

The **CDROM\_PERFORMANCE\_EXCEPTION\_TYPE** enumeration defines the exceptional conditions for performance data. It is a member of the [**CDROM\_PERFORMANCE\_REQUEST**](cdrom-performance-request.md) structure, which is used as an input parameter to the [**IOCTL\_CDROM\_GET\_PERFORMANCE**](ioctl-cdrom-get-performance.md) I/O control request.

## Syntax


```C++
typedef enum _CDROM_PERFORMANCE_EXCEPTION_TYPE { 
  CdromNominalPerformance             = 1,
  CdromEntirePerformanceList          = 2,
     CdromPerformanceExceptionsOnly   = 3
} CDROM_PERFORMANCE_EXCEPTION_TYPE, *PCDROM_PERFORMANCE_EXCEPTION_TYPE;
```



## Constants

<dl> <dt>

<span id="CdromNominalPerformance"></span><span id="cdromnominalperformance"></span><span id="CDROMNOMINALPERFORMANCE"></span>**CdromNominalPerformance**
</dt> <dd>

Requests nominal performance parameters.

</dd> <dt>

<span id="CdromEntirePerformanceList"></span><span id="cdromentireperformancelist"></span><span id="CDROMENTIREPERFORMANCELIST"></span>**CdromEntirePerformanceList**
</dt> <dd>

Requests the entire performance list, as qualified by the **StartingLba** field of the [**CDROM\_PERFORMANCE\_REQUEST**](cdrom-performance-request.md) structure.

</dd> <dt>

<span id="___CdromPerformanceExceptionsOnly_"></span><span id="___cdromperformanceexceptionsonly_"></span><span id="___CDROMPERFORMANCEEXCEPTIONSONLY_"></span> **CdromPerformanceExceptionsOnly** 
</dt> <dd>

Requests only performance exceptions that cause the performance to fall outside the nominal.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**CDROM\_PERFORMANCE\_REQUEST**](cdrom-performance-request.md)
</dt> <dt>

[**IOCTL\_CDROM\_GET\_PERFORMANCE**](ioctl-cdrom-get-performance.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_PERFORMANCE_EXCEPTION_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






