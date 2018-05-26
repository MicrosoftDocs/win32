---
title: MSFC\_FC4STATISTICS structure
description: The MSFC\_FC4STATISTICS structure is used in conjunction with the GetFC4Statistics WMI method to report traffic statistics on a port of type Nx\_Port for the indicated FC-4 protocol.
ms.assetid: a46a9aff-9bc9-4328-85b2-90f8f80b2e65
keywords:
- MSFC_FC4STATISTICS structure Storage Devices
- PMSFC_FC4STATISTICS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSFC_FC4STATISTICS
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFC\_FC4STATISTICS structure

The MSFC\_FC4STATISTICS structure is used in conjunction with the [**GetFC4Statistics**](https://msdn.microsoft.com/library/windows/hardware/ff553949) WMI method to report traffic statistics on a port of type Nx\_Port for the indicated FC-4 protocol.

## Syntax


```C++
typedef struct _MSFC_FC4STATISTICS {
  ULONGLONG InputRequests;
  ULONGLONG OutputRequests;
  ULONGLONG ControlRequests;
  ULONGLONG InputMegabytes;
  ULONGLONG OutputMegabytes;
} MSFC_FC4STATISTICS, *PMSFC_FC4STATISTICS;
```



## Members

<dl> <dt>

**InputRequests**
</dt> <dd>

Indicates the number of input requests.

</dd> <dt>

**OutputRequests**
</dt> <dd>

Indicates the number of output requests.

</dd> <dt>

**ControlRequests**
</dt> <dd>

Indicates the number of control requests.

</dd> <dt>

**InputMegabytes**
</dt> <dd>

Indicates the number of megabytes of data that has been input.

</dd> <dt>

**OutputMegabytes**
</dt> <dd>

Indicates the number of megabytes of data that has been output.

</dd> </dl>

## Remarks

The statistics counters whose values are reported in the members of this structure are 64-bit signed integers that wrap to zero on exceeding 2\*\*63-1. The statistics counters are not reset during normal operation, so traffic rates may be determined by the difference of counter values derived from two successive calls, with appropriate adjustments to for counter wrap.

If an HBA does not support a specific statistic, it shall return the value of -1 for corresponding counter.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**GetFC4Statistics**](https://msdn.microsoft.com/library/windows/hardware/ff553949)
</dt> <dt>

[**GetFC4Statistics\_IN**](getfc4statistics-in.md)
</dt> <dt>

[**GetFC4Statistics\_OUT**](getfc4statistics-out.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSFC_FC4STATISTICS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






