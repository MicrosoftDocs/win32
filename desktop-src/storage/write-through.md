---
title: WRITE\_THROUGH enumeration
description: The WRITE\_THROUGH enumeration specifies whether a storage device supports write-through caching.
ms.assetid: 'b5060a4f-4d11-4a69-9025-5c7036dea558'
keywords: ["WRITE_THROUGH enumeration Storage Devices"]
topic_type:
- apiref
api_name:
- WRITE_THROUGH
api_location:
- ntddstor.h
api_type:
- HeaderDef
---

# WRITE\_THROUGH enumeration

The WRITE\_THROUGH enumeration specifies whether a storage device supports write-through caching.

## Syntax


```C++
typedef enum _WRITE_THROUGH { 
  WriteThroughUnknown       = 0,
  WriteThroughNotSupported  = 1,
  WriteThroughSupported     = 2
} WRITE_THROUGH;
```



## Constants

<dl> <dt>

<span id="WriteThroughUnknown"></span><span id="writethroughunknown"></span><span id="WRITETHROUGHUNKNOWN"></span>**WriteThroughUnknown**
</dt> <dd>

Indicates that no information is available concerning the writethrough capabilities of the device.

</dd> <dt>

<span id="WriteThroughNotSupported"></span><span id="writethroughnotsupported"></span><span id="WRITETHROUGHNOTSUPPORTED"></span>**WriteThroughNotSupported**
</dt> <dd>

Indicates that the device does not support writethrough operations.

</dd> <dt>

<span id="WriteThroughSupported"></span><span id="writethroughsupported"></span><span id="WRITETHROUGHSUPPORTED"></span>**WriteThroughSupported**
</dt> <dd>

Indicates that the device supports writethrough operations.

</dd> </dl>

## Remarks

The [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)

request reports this value in the [**STORAGE\_WRITE\_CACHE\_PROPERTY**](storage-write-cache-property.md) structure.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20WRITE_THROUGH%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






