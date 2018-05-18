---
title: STORAGE\_SET\_READ\_AHEAD structure
description: The STORAGE\_SET\_READ\_AHEAD structure is used in conjunction with the IOCTL\_STORAGE\_SET\_READ\_AHEAD request to instruct the device to skip to the target address upon reaching the trigger address.
ms.assetid: 'a7ed65f3-40a9-4b08-b59d-7c65c250d5cb'
keywords: ["STORAGE_SET_READ_AHEAD structure Storage Devices", "PSTORAGE_SET_READ_AHEAD structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- STORAGE_SET_READ_AHEAD
api_location:
- ntddcdvd.h
api_type:
- HeaderDef
---

# STORAGE\_SET\_READ\_AHEAD structure

The STORAGE\_SET\_READ\_AHEAD structure is used in conjunction with the [**IOCTL\_STORAGE\_SET\_READ\_AHEAD**](ioctl-storage-set-read-ahead.md) request to instruct the device to skip to the target address upon reaching the trigger address.

## Syntax


```C++
typedef struct _STORAGE_SET_READ_AHEAD {
  LARGE_INTEGER TriggerAddress;
  LARGE_INTEGER TargetAddress;
} STORAGE_SET_READ_AHEAD, *PSTORAGE_SET_READ_AHEAD;
```



## Members

<dl> <dt>

**TriggerAddress**
</dt> <dd>

Indicates the address at which the device jumps to the target address.

</dd> <dt>

**TargetAddress**
</dt> <dd>

Indicates the address to jump to.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_SET\_READ\_AHEAD**](ioctl-storage-set-read-ahead.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_SET_READ_AHEAD%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






