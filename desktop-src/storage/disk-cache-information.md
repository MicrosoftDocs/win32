---
title: DISK\_CACHE\_INFORMATION structure
description: The DISK\_CACHE\_INFORMATION structure is used with the IOCTL\_DISK\_GET\_CACHE\_INFORMATION request to retrieve cache information.
ms.assetid: 17ea8b6b-d41f-4224-880a-49443756d0de
keywords:
- DISK_CACHE_INFORMATION structure Storage Devices
- PDISK_CACHE_INFORMATION structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DISK_CACHE_INFORMATION
api_location:
- ntdddisk.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DISK\_CACHE\_INFORMATION structure

The DISK\_CACHE\_INFORMATION structure is used with the [**IOCTL\_DISK\_GET\_CACHE\_INFORMATION**](ioctl-disk-get-cache-information.md) request to retrieve cache information.

## Syntax


```C++
typedef struct _DISK_CACHE_INFORMATION {
  BOOLEAN                       ParametersSavable;
  BOOLEAN                       ReadCacheEnabled;
  BOOLEAN                       WriteCacheEnabled;
  DISK_CACHE_RETENTION_PRIORITY ReadRetentionPriority;
  DISK_CACHE_RETENTION_PRIORITY WriteRetentionPriority;
  USHORT                        DisablePrefetchTransferLength;
  BOOLEAN                       PrefetchScalar;
  union {
    struct {
      USHORT Minimum;
      USHORT Maximum;
      USHORT MaximumBlocks;
    } ScalarPrefetch;
    struct {
      USHORT Minimum;
      USHORT Maximum;
    } BlockPrefetch;
  };
} DISK_CACHE_INFORMATION, *PDISK_CACHE_INFORMATION;
```



## Members

<dl> <dt>

**ParametersSavable**
</dt> <dd>

Indicates, when set to 1, that the device is capable of saving any parameters in nonvolatile storage.

</dd> <dt>

**ReadCacheEnabled**
</dt> <dd>

Indicates, when set to 1, that the read cache is enabled.

</dd> <dt>

**WriteCacheEnabled**
</dt> <dd>

Indicates, when set to 1, that the write cache is enabled.

</dd> <dt>

**ReadRetentionPriority**
</dt> <dd>

Determines the likelihood of various types of data remaining in the cache. By means of this value, for instance, data cached from a READ or WRITE operation might be given a different priority than data cached under other circumstances, such as prefetch operations. Thus a value of **EqualPriority** indicates that no data is held in the cache on a preferential basis. When **ReadRetentionPriority** is set to **EqualPriority**, all types of data have equal access to cache memory. On the other hand, a value of **KeepPrefetchedData** indicates that a preference is to be given to prefetched data while a value of **KeepReadData** indicates that a preference is to be given to data cached from a READ operation. For more information about the values that can be assigned to this member see the [**DISK\_CACHE\_RETENTION\_PRIORITY**](disk-cache-retention-priority.md) enumeration.

</dd> <dt>

**WriteRetentionPriority**
</dt> <dd>

See discussion under **ReadRetentionPriority**.

</dd> <dt>

**DisablePrefetchTransferLength**
</dt> <dd>

Disables prefetching. Prefetching might be disabled whenever the number of blocks requested exceeds the value in **DisablePrefetchTransferLength**. When zero, prefetching is disabled no matter what the size of the block request.

</dd> <dt>

**PrefetchScalar**
</dt> <dd>

When **TRUE**, Indicates that **ScalarPrefetch.Maximum** should be used together with the transfer length to calculate the amount of data that can be prefetched. When **FALSE**, **BlockPrefetch.Maximum** will be the maximum number of disk blocks that can be prefetched.

</dd> <dt>

**ScalarPrefetch**
</dt> <dd> <dl> <dt>

**Minimum**
</dt> <dd>

Contains the scalar multiplier of the transfer length of the request when **PrefetchScalar** is **TRUE**. If **PrefetchScalar** is **TRUE**, the value in **ScalarPrefetch.Minimum** is multiplied by the transfer length to obtain the minimum amount of data that can be prefetched into the cache on a disk operation.

</dd> <dt>

**Maximum**
</dt> <dd>

Contains the scalar multiplier of the transfer length of the request when **PrefetchScalar** is **TRUE**. If **PrefetchScalar** is **TRUE**, the value in **ScalarPrefetch.Maximum** is multiplied by the transfer length to obtain the maximum amount of data that can be prefetched into the cache on a disk operation.

</dd> <dt>

**MaximumBlocks**
</dt> <dd>

Contains the maximum size, in blocks, of the transfer length.

</dd> </dl> </dd> <dt>

**BlockPrefetch**
</dt> <dd> <dl> <dt>

**Minimum**
</dt> <dd>

Contains the scalar multiplier of the transfer length of the request when **PrefetchScalar** is **TRUE**. If **PrefetchScalar** is **TRUE**, the value in **ScalarPrefetch.Minimum** is multiplied by the transfer length to obtain the minimum amount of data that can be prefetched into the cache on a disk operation.

</dd> <dt>

**Maximum**
</dt> <dd>

Contains the scalar multiplier of the transfer length of the request when **PrefetchScalar** is **TRUE**. If **PrefetchScalar** is **TRUE**, the value in **ScalarPrefetch.Maximum** is multiplied by the transfer length to obtain the maximum amount of data that can be prefetched into the cache on a disk operation.

</dd> </dl> </dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_DISK\_GET\_CACHE\_INFORMATION**](ioctl-disk-get-cache-information.md)
</dt> <dt>

[**DISK\_CACHE\_INFORMATION**](disk-cache-information.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DISK_CACHE_INFORMATION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






