---
title: WRITE\_CACHE\_TYPE enumeration
description: The WRITE\_CACHE\_TYPE enumeration specifies the cache type.
ms.assetid: 'c8e5017a-b5ec-456a-a33d-0a84b92c71bf'
keywords: ["WRITE_CACHE_TYPE enumeration Storage Devices"]
topic_type:
- apiref
api_name:
- WRITE_CACHE_TYPE
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# WRITE\_CACHE\_TYPE enumeration

The WRITE\_CACHE\_TYPE enumeration specifies the cache type.

## Syntax


```C++
typedef enum _WRITE_CACHE_TYPE { 
  WriteCacheTypeUnknown       = 0,
  WriteCacheTypeNone          = 1,
  WriteCacheTypeWriteBack     = 2,
  WriteCacheTypeWriteThrough  = 3
} WRITE_CACHE_TYPE;
```



## Constants

<dl> <dt>

<span id="WriteCacheTypeUnknown"></span><span id="writecachetypeunknown"></span><span id="WRITECACHETYPEUNKNOWN"></span>**WriteCacheTypeUnknown**
</dt> <dd>

The system cannot report the type of the write cache.

</dd> <dt>

<span id="WriteCacheTypeNone"></span><span id="writecachetypenone"></span><span id="WRITECACHETYPENONE"></span>**WriteCacheTypeNone**
</dt> <dd>

The device does not have a write cache.

</dd> <dt>

<span id="WriteCacheTypeWriteBack"></span><span id="writecachetypewriteback"></span><span id="WRITECACHETYPEWRITEBACK"></span>**WriteCacheTypeWriteBack**
</dt> <dd>

The device has a write back cache.

</dd> <dt>

<span id="WriteCacheTypeWriteThrough"></span><span id="writecachetypewritethrough"></span><span id="WRITECACHETYPEWRITETHROUGH"></span>**WriteCacheTypeWriteThrough**
</dt> <dd>

The device has a write through cache.

</dd> </dl>

## Remarks

There are two main types of write cache: *write back* and *write through*. With a write-back cache, the device does not copy cache data to nonvolatile media until absolutely necessary. This type of operation improves the performance of write operations. With a write-through cache, the device writes data to the cache and the media in parallel. This type of operation does not improve write performance, but it makes subsequent read operations faster.

The [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)

request reports a WRITE\_CACHE\_TYPE value in the [**STORAGE\_WRITE\_CACHE\_PROPERTY**](storage-write-cache-property.md) structure.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> <dt>

[**STORAGE\_WRITE\_CACHE\_PROPERTY**](storage-write-cache-property.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20WRITE_CACHE_TYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






