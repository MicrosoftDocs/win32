---
title: VERIFY\_INFORMATION structure
description: The VERIFY\_INFORMATION structure provides information used to verify the existence of a disk extent.
ms.assetid: '7bb5c2ff-9bdb-4958-b290-9edb18d02668'
keywords: ["VERIFY_INFORMATION structure Storage Devices", "PVERIFY_INFORMATION structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- VERIFY_INFORMATION
api_location:
- ntdddisk.h
api_type:
- HeaderDef
---

# VERIFY\_INFORMATION structure

The VERIFY\_INFORMATION structure provides information used to verify the existence of a disk extent.

## Syntax


```C++
typedef struct _VERIFY_INFORMATION {
  LARGE_INTEGER StartingOffset;
  ULONG         Length;
} VERIFY_INFORMATION, *PVERIFY_INFORMATION;
```



## Members

<dl> <dt>

**StartingOffset**
</dt> <dd>

Specifies the starting offset, in bytes, of the disk extent.

</dd> <dt>

**Length**
</dt> <dd>

Indicates the length, in bytes, of the disk extent.

</dd> </dl>

## Remarks

VERIFY\_INFORMATION is the output buffer for the [**IOCTL\_DISK\_VERIFY**](ioctl-disk-verify.md) control code.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_DISK\_VERIFY**](ioctl-disk-verify.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20VERIFY_INFORMATION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






