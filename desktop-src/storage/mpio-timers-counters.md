---
title: MPIO\_TIMERS\_COUNTERS structure
description: The MPIO\_TIMERS\_COUNTERS structure controls the timer counters that affect all devices whose controlling DSMs do not implement independent timer counter settings.
ms.assetid: 'edbca8b0-53c1-4538-ac96-52238d75168d'
keywords: ["MPIO_TIMERS_COUNTERS structure Storage Devices", "PMPIO_TIMERS_COUNTERS structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MPIO_TIMERS_COUNTERS
api_location:
- mpiowmi.h
api_type:
- HeaderDef
---

# MPIO\_TIMERS\_COUNTERS structure

The MPIO\_TIMERS\_COUNTERS structure controls the timer counters that affect all devices whose controlling DSMs do not implement independent timer counter settings. To query or set the global counters, the request must be directed to the MPIO control object by using its WMI instance name.

## Syntax


```C++
typedef struct _MPIO_TIMERS_COUNTERS {
  ULONG PathVerifyEnabled;
  ULONG PathVerificationPeriod;
  ULONG PDORemovePeriod;
  ULONG RetryCount;
  ULONG RetryInterval;
} MPIO_TIMERS_COUNTERS, *PMPIO_TIMERS_COUNTERS;
```



## Members

<dl> <dt>

**PathVerifyEnabled**
</dt> <dd>

An unsigned 32-bitfield that is used as a flag. This field indicates whether path verification must be performed by MPIO on all paths periodically.

</dd> <dt>

**PathVerificationPeriod**
</dt> <dd>

An unsigned 32-bitfield that is used to indicate the periodicity (in seconds) with which MPIO has been requested to perform path verification. This field is valid if *PathVerifyEnabled* is **TRUE**.

</dd> <dt>

**PDORemovePeriod**
</dt> <dd>

An unsigned 32-bitfield that controls the amount of time (in seconds) that the pseudo-LUN remains in system memory, even after losing all its path information.

</dd> <dt>

**RetryCount**
</dt> <dd>

An unsigned 32-bitfield that specifies the number of times a failed I/O can be retried.

</dd> <dt>

**RetryInterval**
</dt> <dd>

An unsigned 32-bitfield that specifies the interval of time (in seconds) after which a failed request is retried.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiowmi.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MPIO_TIMERS_COUNTERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





