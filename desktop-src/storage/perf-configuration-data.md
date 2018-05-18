---
title: PERF\_CONFIGURATION\_DATA structure
description: The PERF\_CONFIGURATION\_DATA structure describes the performance optimizations that are supported by the StorPortInitializePerfOpts routine.
ms.assetid: '47db8f0f-9f3b-44d9-8110-dc0b79d0e26a'
keywords: ["PERF_CONFIGURATION_DATA structure Storage Devices", "PPERF_CONFIGURATION_DATA structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- PERF_CONFIGURATION_DATA
api_location:
- storport.h
api_type:
- HeaderDef
---

# PERF\_CONFIGURATION\_DATA structure

The PERF\_CONFIGURATION\_DATA structure describes the performance optimizations that are supported by the [**StorPortInitializePerfOpts**](storportinitializeperfopts.md) routine.

## Syntax


```C++
typedef struct _PERF_CONFIGURATION_DATA {
  ULONG           Version;
  ULONG           Size;
  ULONG           Flags;
  ULONG           ConcurrentChannels;
  ULONG           FirstRedirectionMessageNumber;
  ULONG           LastRedirectionMessageNumber;
  ULONG           DeviceNode;
  ULONG           Reserved;
  PGROUP_AFFINITY MessageTargets;
} PERF_CONFIGURATION_DATA, *PPERF_CONFIGURATION_DATA;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version number of the structure. Set this member when querying and initializing optimizations.

</dd> <dt>

**Size**
</dt> <dd>

The size of the structure, set to **sizeof(PERF\_CONFIGURATION\_DATA)**.

</dd> <dt>

**Flags**
</dt> <dd>

A bitwise-OR of supported flags. Currently, the following flags are supported:



| Flag                                                              | Meaning                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| STOR\_PERF\_DPC\_REDIRECTION<br/>                           | This flag is used to indicate that DPC processing should be spread out over multiple CPUs.<br/> This flag is valid when **Version** is set to 2 or 3.<br/>                                                                                                                                                                                                            |
| STOR\_PERF\_CONCURRENT\_CHANNELS<br/>                       | This flag is used to indicate that concurrent calls to the [**HwStorStartIo**](hwstorstartio.md) routine are supported. Prior to Windows 8, miniports must not set this flag.<br/> This flag is valid when **Version** is set to 2 or 3.<br/>                                                                                                                        |
| STOR\_PERF\_INTERRUPT\_MESSAGE\_RANGES<br/>                 | This flag is used to indicate that interrupt redirection is supported. When you use this flag, you must also set the STOR\_PERF\_DPC\_REDIRECTION flag.<br/> This flag is valid when **Version** is set to 2 or 3.<br/>                                                                                                                                               |
| STOR\_PERF\_ADV\_CONFIG\_LOCALITY<br/>                      | This flag is used to indicate that you should use the group and mask that pertain to the message group with the correct affinity. When you use this flag, you must also set the STOR\_PERF\_INTERRUPT\_MESSAGE\_RANGES and the STOR\_PERF\_DPC\_REDIRECTION flags.<br/> This flag is valid when **Version** is set to 3.<br/>                                         |
| STOR\_PERF\_OPTIMIZE\_FOR\_COMPLETION\_DURING\_STARTIO<br/> | This flag is used to indicate that the miniport driver will complete I/Os concurrently with the submission of new I/Os. When you use this flag, you must also set the STOR\_PERF\_DPC\_REDIRECTION flag.<br/> This flag is valid when **Version** is set to 3. See remarks below.<br/>                                                                                |
| STOR\_PERF\_DPC\_REDIRECTION\_CURRENT\_CPU<br/>             | This flag is used to indicate that you are opting into DPC Redirection (required) but the IO redirection choice is set to the CPU requesting the DPC and not the CPU originating the IO request into Storport.<br/> When you use this flag, you must also set the STOR\_PERF\_DPC\_REDIRECTION flag.<br/> This flag is valid when **Version** is set to 4.<br/> |
| STOR\_PERF\_NO\_SGL<br/>                                    | This flag is used to indicate that miniport doesn't need SGLs to be created by storport driver for an IO request buffer. <br/> This flag is valid when **Version** is set to 5.<br/>                                                                                                                                                                                  |



 

</dd> <dt>

**ConcurrentChannels**
</dt> <dd>

The number of concurrent calls to the [**HwStorStartIo**](hwstorstartio.md) routine that the miniport driver and the device support. This member is only accessed when the STOR\_PERF\_CONCURRENT\_CHANNELS flag has been set. Prior to Windows 8, miniports must not set this value.

</dd> <dt>

**FirstRedirectionMessageNumber**
</dt> <dd>

When the **Flags** member has the STOR\_PERF\_INTERRUPT\_MESSAGE\_RANGES flag set, the miniport driver initializes interrupt redirection to begin with this message number. This member is only accessed when the STOR\_PERF\_INTERRUPT\_MESSAGE\_RANGES flag is set.

</dd> <dt>

**LastRedirectionMessageNumber**
</dt> <dd>

When the **Flags** member has the STOR\_PERF\_INTERRUPT\_MESSAGE\_RANGES flag set, the miniport driver initializes interrupt redirection to end with this message number. This member is only accessed when the STOR\_PERF\_INTERRUPT\_MESSAGE\_RANGES flag is set.

</dd> <dt>

**DeviceNode**
</dt> <dd>

When the **Flags** member has the STOR\_PERF\_ADV\_CONFIG\_LOCALITY flag set, Storport initializes this field to contain the NUMA node number in which the miniport driver's device resides.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for system use.

</dd> <dt>

**MessageTargets**
</dt> <dd>

When the **Flags** member has the STOR\_PERF\_ADV\_CONFIG\_LOCALITY flag set, Storport initializes the fields of in the structures of a [**GROUP\_AFFINITY**](https://msdn.microsoft.com/library/windows/hardware/ff546539) array. These structures correspond to the redirection messages that are currently in use. The array itself is zero-based, but **FirstRedirectionMessageNumber** is not required to be zero. The miniport allocates this array and sets **MessageTargets** to point to it. The miniport driver must allocate a **GROUP\_AFFINITY** array large enough to hold all the returned affinity masks.

</dd> </dl>

## Remarks

The current version of this structure is defined by **STOR\_PERF\_VERSION**. Setting **Version** to this value will allow **Flags** to specify all supported optimizations.

The purpose of the STOR\_PERF\_DPC\_REDIRECTION flag is to ensure that individual CPUs are not overwhelmed with DPC processing. When this flag is set, DPC processing is spread over multiple CPUs. If STOR\_PERF\_DPC\_REDIRECTION\_CURRENT\_CPU is not set, StorPort will attempt to schedule I/O completion DPCs on the same CPU that originated the I/O.

Typically, a miniport completes I/O requests in it's [**HwStorStartIo**](hwstorstartio.md) routine and calls [**StorPortNotification**](https://msdn.microsoft.com/library/windows/hardware/ff567446) with the **RequestComplete** notification type. For processing I/O in this manner, the miniport will leave the STOR\_PERF\_OPTIMIZE\_FOR\_COMPLETION\_DURING\_STARTIO flag set in the **Flags** member allowing Storport to adjust DPC redirection.

For information about enabling message-signaled interrupts for a device, see [Enabling Message-Signaled Interrupts in the Registry](https://msdn.microsoft.com/library/windows/hardware/ff544246).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storport.h (include Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**StorPortInitializePerfOpts**](storportinitializeperfopts.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PERF_CONFIGURATION_DATA%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






