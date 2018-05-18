---
title: HYBRID\_INFORMATION structure
description: The HYBRID\_INFORMATION structure contains hybrid disk capability information.
ms.assetid: '5CD8E422-8CEE-43E8-9703-520FDBE6BF5E'
keywords: ["HYBRID_INFORMATION structure Storage Devices", "PHYBRID_INFORMATION structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- HYBRID_INFORMATION
api_location:
- Ntddscsi.h
api_type:
- HeaderDef
---

# HYBRID\_INFORMATION structure

The **HYBRID\_INFORMATION** structure contains hybrid disk capability information. The structure is returned when the HYBRID\_FUNCTION\_GET\_INFO function is selected in a [**IOCTL\_SCSI\_MINIPORT\_HYBRID**](ioctl-scsi-miniport-hybrid.md) request sent to an HBA miniport driver.

## Syntax


```C++
typedef struct _HYBRID_INFORMATION {
  ULONG          Version;
  ULONG          Size;
  BOOLEAN        HybridSupported;
  NVCACHE_STATUS Status;
  NVCACHE_TYPE   CacheTypeEffective;
  NVCACHE_TYPE   CacheTypeDefault;
  ULONG          FractionBase;
  ULONGLONG      CacheSize;
  struct {
    ULONG WriteCacheChangeable  :1;
    ULONG WriteThroughIoSupported  :1;
    ULONG FlushCacheSupported  :1;
    ULONG Removable  :1;
    ULONG ReservedBits  :28;
  } Attributes;
  struct {
    UCHAR                             PriorityLevelCount;
    BOOLEAN                           MaxPriorityBehavior;
    ULONG                             DirtyThresholdLow;
    ULONG                             DirtyThresholdHigh;
    struct {
      ULONG CacheDisable  :1;
      ULONG SetDirtyThreshold  :1;
      ULONG PriorityDemoteBySize  :1;
      ULONG PriorityChangeByLbaRange  :1;
      ULONG Evict  :1;
      ULONG ReservedBits  :27;
      ULONG MaxEvictCommands;
      ULONG MaxLbaRangeCountForEvict;
      ULONG MaxLbaRangeCountForChangeLba;
    } SupportedCommands;
    NVCACHE_PRIORITY_LEVEL_DESCRIPTOR Priority[];
  } Priorities;
} HYBRID_INFORMATION, *PHYBRID_INFORMATION;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of this structure. Set to HYBRID\_REQUEST\_INFO\_STRUCTURE\_VERSION.

</dd> <dt>

**Size**
</dt> <dd>

The size of this structure. Set to **sizeof**(HYBRID\_INFORMATION).

</dd> <dt>

**HybridSupported**
</dt> <dd>

Miniport supports for hybrid disks. Set to **TRUE** if hybrid disks are supported. Otherwise, **FALSE**.

</dd> <dt>

**Status**
</dt> <dd>

The status of the hybrid disk cache. This contains one of the following values.



| Value                                                                                                                                                                                                                            | Meaning                                                                         |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| <span id="NvCacheStatusUnknown"></span><span id="nvcachestatusunknown"></span><span id="NVCACHESTATUSUNKNOWN"></span><dl> <dt>**NvCacheStatusUnknown**</dt> </dl>         | The miniport driver is not able to report the cache status.<br/>          |
| <span id="NvCacheStatusDisabling"></span><span id="nvcachestatusdisabling"></span><span id="NVCACHESTATUSDISABLING"></span><dl> <dt>**NvCacheStatusDisabling**</dt> </dl> | The cache is currently changing to **NvCacheStatusDisabled** status.<br/> |
| <span id="NvCacheStatusDisabled"></span><span id="nvcachestatusdisabled"></span><span id="NVCACHESTATUSDISABLED"></span><dl> <dt>**NvCacheStatusDisabled**</dt> </dl>     | The cache on the hybrid disk is disabled.<br/>                            |
| <span id="NvCacheStatusEnabled"></span><span id="nvcachestatusenabled"></span><span id="NVCACHESTATUSENABLED"></span><dl> <dt>**NvCacheStatusEnabled**</dt> </dl>         | The cache on the hybrid disk is enabled.<br/>                             |



 

</dd> <dt>

**CacheTypeEffective**
</dt> <dd>

The non-volatile caching type currently set for hybrid disk. The effective cache type is one of the following values.



| Value                                                                                                                                                                                                                                | Meaning                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| <span id="NvCacheTypeUnknown"></span><span id="nvcachetypeunknown"></span><span id="NVCACHETYPEUNKNOWN"></span><dl> <dt>**NvCacheTypeUnknown**</dt> </dl>                     | The miniport driver is not able to report the cache type<br/> |
| <span id="NvCacheNone"></span><span id="nvcachenone"></span><span id="NVCACHENONE"></span><dl> <dt>**NvCacheNone**</dt> </dl>                                                 | The disk does not support a non-volatile cache.<br/>          |
| <span id="NvCacheTypeWriteBack"></span><span id="nvcachetypewriteback"></span><span id="NVCACHETYPEWRITEBACK"></span><dl> <dt>**NvCacheTypeWriteBack**</dt> </dl>             | Write-back caching is supported by hybrid disk.<br/>          |
| <span id="NvCacheTypeWriteThrough"></span><span id="nvcachetypewritethrough"></span><span id="NVCACHETYPEWRITETHROUGH"></span><dl> <dt>**NvCacheTypeWriteThrough**</dt> </dl> | Write-through caching is supported by hybrid disk.<br/>       |



 

</dd> <dt>

**CacheTypeDefault**
</dt> <dd>

The default caching type used by the hybrid disk. The possible values are the same as for **CacheTypeEffective**.

</dd> <dt>

**FractionBase**
</dt> <dd>

The base value for fractional fields in this structure. This value is set to 255.

</dd> <dt>

**CacheSize**
</dt> <dd>

The size, in LBAs, of the non-volatile on the hybrid disk.

</dd> <dt>

**Attributes**
</dt> <dd>

The hybrid disk attributes.

<dl> <dt>

**WriteCacheChangeable**
</dt> <dd>

Support for changes in write caching policy. The value is 1 policy changes are allowed. Otherwise, changes are ignored.

</dd> <dt>

**WriteThroughIoSupported**
</dt> <dd>

Support for individual write operations when write-through caching is used. The value is 1 if individual writes are supported. Otherwise, the values is 0.

</dd> <dt>

**FlushCacheSupported**
</dt> <dd>

Support for non-volatile cache flush. The value is 1 if flushes are supported. Otherwise, the value is 0.

</dd> <dt>

**Removable**
</dt> <dd>

Support of removal of the non-volatile cache from the disk. The value is 1 if the cache is removable. Otherwise, the value is 0.

</dd> <dt>

**ReservedBits**
</dt> <dd>

Reserved.

</dd> </dl> </dd> <dt>

**Priorities**
</dt> <dd>

Priority settings for the hybrid disk.

<dl> <dt>

**PriorityLevelCount**
</dt> <dd>

The number of priority levels supported by the cache. Currently, a non-zero value indicates support for all priorities.

</dd> <dt>

**MaxPriorityBehavior**
</dt> <dd>

If **TRUE**, the disk I/O can fail at maximum priority if the cache is full. Otherwise, if **FALSE**, the operation will complete to disk.

</dd> <dt>

**DirtyThresholdLow**
</dt> <dd>

The low threshold for a cache flush. This value is ratio in the range of **FractionBase**.

</dd> <dt>

**DirtyThresholdHigh**
</dt> <dd>

The low threshold for a cache flush. This value is ratio in the range of **FractionBase**.

</dd> <dt>

**SupportedCommands**
</dt> <dd>

Support for non-volatile cache specific commands to the hybrid disk.

<dl> <dt>

**CacheDisable**
</dt> <dd>

Support for changes in write caching policy. The value is 1 policy changes are allowed. Otherwise, changes are ignored.

</dd> <dt>

**SetDirtyThreshold**
</dt> <dd>

Support for individual write operations when write-through caching is used. The value is 1 if individual writes are supported. Otherwise, the values is 0.

</dd> <dt>

**PriorityDemoteBySize**
</dt> <dd>

Support for non-volatile cache flush. The value is 1 if flushes are supported. Otherwise, the value is 0.

</dd> <dt>

**PriorityChangeByLbaRange**
</dt> <dd>

Support for LBA range priority changes. The value is 1 if priority changes are supported. Otherwise, the value is 0.

</dd> <dt>

**Evict**
</dt> <dd>

Support of removal of the non-volatile cache from the disk. The value is 1 if the cache is removable. Otherwise, the value is 0.

</dd> <dt>

**ReservedBits**
</dt> <dd>

Reserved.

</dd> <dt>

**MaxEvictCommands**
</dt> <dd>

The maximum concurrent Evict commands allowed that are outstanding. This value is valid when **Evict** is set to 1.

</dd> <dt>

**MaxLbaRangeCountForEvict**
</dt> <dd>

The maximum number of LBA ranges possible to associate with an Evict command. This value is valid when **Evict** is set to 1.

</dd> <dt>

**MaxLbaRangeCountForChangeLba**
</dt> <dd>

The maximum number of LBA ranges possible to associate with a Priority Change command. This value is valid when **PriorityChangeByLbaRange** is set to 1.

</dd> </dl> </dd> <dt>

**Priority**
</dt> <dd>

An array of priority level descriptors. The number of descriptors present in the array is set in **PriorityLevelCount**.

</dd> </dl> </dd> </dl>

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.1.<br/>                                                            |
| Header<br/>  | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_SCSI\_MINIPORT\_HYBRID**](ioctl-scsi-miniport-hybrid.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HYBRID_INFORMATION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






