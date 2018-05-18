---
title: DSM\_COUNTERS structure
description: The DSM\_COUNTERS structure holds the various timer counters that are applicable to all LUNs that are controlled by the DSM.
ms.assetid: '3202aec4-d95e-4162-86a1-17595ed2a5b5'
keywords: ["DSM_COUNTERS structure Storage Devices", "PDSM_COUNTERS structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- DSM_COUNTERS
api_location:
- mpiowmi.h
api_type:
- HeaderDef
---

# DSM\_COUNTERS structure

The DSM\_COUNTERS structure holds the various timer counters that are applicable to all LUNs that are controlled by the DSM.

## Syntax


```C++
typedef struct _DSM_COUNTERS {
  ULONG     PathVerifyEnabled;
  ULONG     PathVerificationPeriod;
  ULONG     PDORemovePeriod;
  ULONG     RetryCount;
  ULONG     RetryInterval;
  ULONG     Reserved32;
  ULONGLONG Reserved64;
} DSM_COUNTERS, *PDSM_COUNTERS;
```



## Members

<dl> <dt>

**PathVerifyEnabled**
</dt> <dd>

An unsigned 32-bitfield that is used as a flag. This field indicates if path verification must be performed by MPIO periodically on all paths that expose devices that are controlled by this particular DSM.

</dd> <dt>

**PathVerificationPeriod**
</dt> <dd>

An unsigned 32-bitfield that is used to indicate the periodicity (in seconds) with which MPIO has been requested to perform path verification. This field is only honored if *PathVerifyEnabled* is **TRUE**.

</dd> <dt>

**PDORemovePeriod**
</dt> <dd>

An unsigned 32-bitfield that controls the amount of time (in seconds) that the pseudo-LUN will continue to remain in system memory, even after losing all its path information.

</dd> <dt>

**RetryCount**
</dt> <dd>

An unsigned 32-bitfield that specifies the number of times a failed I/O will be retried.

</dd> <dt>

**RetryInterval**
</dt> <dd>

An unsigned 32-bitfield that specifies the interval of time (in seconds) after which a failed request is retried.

</dd> <dt>

**Reserved32**
</dt> <dd>

Should be zero.

</dd> <dt>

**Reserved64**
</dt> <dd>

Should be zero.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiowmi.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DSM_COUNTERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





