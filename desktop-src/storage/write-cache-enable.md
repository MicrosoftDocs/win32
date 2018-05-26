---
title: WRITE\_CACHE\_ENABLE enumeration
description: The WRITE\_CACHE\_ENABLE enumeration indicates whether the write cache is enabled or disabled.
ms.assetid: 29cdf3a0-19f4-45b4-b85c-ad1754a0ec84
keywords:
- WRITE_CACHE_ENABLE enumeration Storage Devices
topic_type:
- apiref
api_name:
- WRITE_CACHE_ENABLE
api_location:
- ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WRITE\_CACHE\_ENABLE enumeration

The WRITE\_CACHE\_ENABLE enumeration indicates whether the write cache is enabled or disabled.

## Syntax


```C++
typedef enum _WRITE_CACHE_ENABLE { 
  WriteCacheEnableUnknown  = 0,
  WriteCacheDisabled       = 1,
  WriteCacheEnabled        = 2
} WRITE_CACHE_ENABLE;
```



## Constants

<dl> <dt>

<span id="WriteCacheEnableUnknown"></span><span id="writecacheenableunknown"></span><span id="WRITECACHEENABLEUNKNOWN"></span>**WriteCacheEnableUnknown**
</dt> <dd>

The system cannot report whether the device's write cache is enabled or disabled.

</dd> <dt>

<span id="WriteCacheDisabled"></span><span id="writecachedisabled"></span><span id="WRITECACHEDISABLED"></span>**WriteCacheDisabled**
</dt> <dd>

The device's write cache is disabled.

</dd> <dt>

<span id="WriteCacheEnabled"></span><span id="writecacheenabled"></span><span id="WRITECACHEENABLED"></span>**WriteCacheEnabled**
</dt> <dd>

The device's write cache is enabled.

</dd> </dl>

## Remarks

The [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)

request reports a WRITE\_CACHE\_ENABLE value in the [**STORAGE\_WRITE\_CACHE\_PROPERTY**](storage-write-cache-property.md) structure.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20WRITE_CACHE_ENABLE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






