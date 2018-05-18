---
title: WRITE\_CACHE\_CHANGE enumeration
description: The WRITE\_CACHE\_CHANGE enumeration indicates whether the write cache features of a device are changeable or not.
ms.assetid: '4293e7a6-117e-47bb-85d6-20de8277abad'
keywords: ["WRITE_CACHE_CHANGE enumeration Storage Devices"]
topic_type:
- apiref
api_name:
- WRITE_CACHE_CHANGE
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# WRITE\_CACHE\_CHANGE enumeration

The WRITE\_CACHE\_CHANGE enumeration indicates whether the write cache features of a device are changeable or not.

## Syntax


```C++
typedef enum _WRITE_CACHE_CHANGE { 
  WriteCacheChangeUnknown  = 0,
  WriteCacheNotChangeable  = 1,
  WriteCacheChangeable     = 2
} WRITE_CACHE_CHANGE;
```



## Constants

<dl> <dt>

<span id="WriteCacheChangeUnknown"></span><span id="writecachechangeunknown"></span><span id="WRITECACHECHANGEUNKNOWN"></span>**WriteCacheChangeUnknown**
</dt> <dd>

The system cannot report the write cache change capability of the device.

</dd> <dt>

<span id="WriteCacheNotChangeable"></span><span id="writecachenotchangeable"></span><span id="WRITECACHENOTCHANGEABLE"></span>**WriteCacheNotChangeable**
</dt> <dd>

Host software cannot change the characteristics of the device's write cache

</dd> <dt>

<span id="WriteCacheChangeable"></span><span id="writecachechangeable"></span><span id="WRITECACHECHANGEABLE"></span>**WriteCacheChangeable**
</dt> <dd>

Host software can change the characteristics of the device's write cache

</dd> </dl>

## Remarks

The [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)

request reports a WRITE\_CACHE\_CHANGE value in the [**STORAGE\_WRITE\_CACHE\_PROPERTY**](storage-write-cache-property.md) structure.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20WRITE_CACHE_CHANGE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






