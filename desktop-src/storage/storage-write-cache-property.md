---
title: STORAGE\_WRITE\_CACHE\_PROPERTY structure
description: The STORAGE\_WRITE\_CACHE\_PROPERTY structure is used with the IOCTL\_STORAGE\_QUERY\_PROPERTY request to retrieve information about a devices write cache property.
ms.assetid: 4abc44ab-1729-46c3-befd-5f917e10953c
keywords:
- STORAGE_WRITE_CACHE_PROPERTY structure Storage Devices
- PSTORAGE_WRITE_CACHE_PROPERTY structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_WRITE_CACHE_PROPERTY
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# STORAGE\_WRITE\_CACHE\_PROPERTY structure

The STORAGE\_WRITE\_CACHE\_PROPERTY structure is used with the [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) request to retrieve information about a device's write cache property.

## Syntax


```C++
typedef struct _STORAGE_WRITE_CACHE_PROPERTY {
  ULONG              Version;
  ULONG              Size;
  WRITE_CACHE_TYPE   WriteCacheType;
  WRITE_CACHE_ENABLE WriteCacheEnabled;
  WRITE_CACHE_CHANGE WriteCacheChangeable;
  WRITE_THROUGH      WriteThroughSupported;
  BOOLEAN            FlushCacheSupported;
  BOOLEAN            UserDefinedPowerProtection;
  BOOLEAN            NVCacheEnabled;
} STORAGE_WRITE_CACHE_PROPERTY, *PSTORAGE_WRITE_CACHE_PROPERTY;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version number of the write cache property.

</dd> <dt>

**Size**
</dt> <dd>

The size, in bytes, of the STORAGE\_WRITE\_CACHE\_PROPERTY structure.

</dd> <dt>

**WriteCacheType**
</dt> <dd>

A [**WRITE\_CACHE\_TYPE**](write-cache-type.md)-typed value that indicates the current write cache type

</dd> <dt>

**WriteCacheEnabled**
</dt> <dd>

A [**WRITE\_CACHE\_ENABLE**](write-cache-enable.md)-typed value that indicates whether the write cache is enabled.

</dd> <dt>

**WriteCacheChangeable**
</dt> <dd>

A [**WRITE\_CACHE\_CHANGE**](write-cache-change.md)-typed value that indicates whether if the host can change the write cache characteristics.

</dd> <dt>

**WriteThroughSupported**
</dt> <dd>

A [**WRITE\_THROUGH**](write-through.md)-typed value that indicates whether the device supports write-through caching.

</dd> <dt>

**FlushCacheSupported**
</dt> <dd>

A Boolean value that indicates whether the device allows host software to flush the device cache. If **TRUE**, the device allows host software to flush the device cache. If **FALSE**, host software cannot flush the device cache.

</dd> <dt>

**UserDefinedPowerProtection**
</dt> <dd>

A Boolean value that indicates whether a user can configure the device's power protection characteristics in the registry. If **TRUE**, a user can configure the device's power protection characteristics in the registry. If **FALSE**, the user cannot configure the device's power protection characteristics in the registry.

</dd> <dt>

**NVCacheEnabled**
</dt> <dd>

A Boolean value that indicates whether the device has a battery backup for the write cache. If **TRUE**, the device has a battery backup for the write cache. If **FALSE**, the device does not have a battery backup for the writer cache.

</dd> </dl>

## Remarks

All of the parameter values that are described in this topic refer to the output of the [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) request.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_WRITE_CACHE_PROPERTY%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






