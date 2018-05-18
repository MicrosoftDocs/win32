---
title: DISK\_CACHE\_RETENTION\_PRIORITY enumeration
description: The DISK\_CACHE\_RETENTION\_PRIORITY enumeration is used in conjunction with the IOCTL\_DISK\_GET\_CACHE\_INFORMATION request and the structure DISK\_CACHE\_INFORMATION to indicate which kinds data are to be held in the cache on a preferential basis.
ms.assetid: '238d0b22-bd35-4e8d-9bb5-283af2bbb75b'
keywords: ["DISK_CACHE_RETENTION_PRIORITY enumeration Storage Devices"]
topic_type:
- apiref
api_name:
- DISK_CACHE_RETENTION_PRIORITY
api_location:
- ntdddisk.h
api_type:
- HeaderDef
---

# DISK\_CACHE\_RETENTION\_PRIORITY enumeration

The DISK\_CACHE\_RETENTION\_PRIORITY enumeration is used in conjunction with the [**IOCTL\_DISK\_GET\_CACHE\_INFORMATION**](ioctl-disk-get-cache-information.md) request and the structure [**DISK\_CACHE\_INFORMATION**](disk-cache-information.md) to indicate which kinds data are to be held in the cache on a preferential basis.

## Syntax


```C++
typedef enum  { 
  EqualPriority       = 0,
  KeepPrefetchedData  = 1,
  KeepReadData        = 2
} DISK_CACHE_RETENTION_PRIORITY;
```



## Constants

<dl> <dt>

<span id="EqualPriority"></span><span id="equalpriority"></span><span id="EQUALPRIORITY"></span>**EqualPriority**
</dt> <dd>

Indicates that no data is held in the cache on a preferential basis. All types of data have equal access to cache memory.

</dd> <dt>

<span id="KeepPrefetchedData"></span><span id="keepprefetcheddata"></span><span id="KEEPPREFETCHEDDATA"></span>**KeepPrefetchedData**
</dt> <dd>

Indicates that a preference is to be given to prefetched data.

</dd> <dt>

<span id="KeepReadData"></span><span id="keepreaddata"></span><span id="KEEPREADDATA"></span>**KeepReadData**
</dt> <dd>

Indicates that a preference is to be given to data cached from a READ operation.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**DISK\_CACHE\_INFORMATION**](disk-cache-information.md)
</dt> <dt>

[**IOCTL\_DISK\_GET\_CACHE\_INFORMATION**](ioctl-disk-get-cache-information.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DISK_CACHE_RETENTION_PRIORITY%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






