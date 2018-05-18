---
title: VOLUME\_PHYSICAL\_OFFSET structure
description: The VOLUME\_PHYSICAL\_OFFSET structure contains a physical offset into a volume and its accompanying physical disk number and is used with IOCTL\_VOLUME\_PHYSICAL\_TO\_LOGICAL and IOCTL\_VOLUME\_LOGICAL\_TO\_PHYSICAL to request a logical offset equivalent of a physical offset or a physical offset equivalent of a logical offset, respectively.
ms.assetid: '068875e3-4229-4f15-9533-f740239ac873'
keywords: ["VOLUME_PHYSICAL_OFFSET structure Storage Devices", "PVOLUME_PHYSICAL_OFFSET structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- VOLUME_PHYSICAL_OFFSET
api_location:
- ntddvol.h
api_type:
- HeaderDef
---

# VOLUME\_PHYSICAL\_OFFSET structure

The VOLUME\_PHYSICAL\_OFFSET structure contains a physical offset into a volume and its accompanying physical disk number and is used with [**IOCTL\_VOLUME\_PHYSICAL\_TO\_LOGICAL**](ioctl-volume-physical-to-logical.md) and [**IOCTL\_VOLUME\_LOGICAL\_TO\_PHYSICAL**](ioctl-volume-logical-to-physical.md) to request a logical offset equivalent of a physical offset or a physical offset equivalent of a logical offset, respectively.

## Syntax


```C++
typedef struct _VOLUME_PHYSICAL_OFFSET {
  ULONG    DiskNumber;
  LONGLONG Offset;
} VOLUME_PHYSICAL_OFFSET, *PVOLUME_PHYSICAL_OFFSET;
```



## Members

<dl> <dt>

**DiskNumber**
</dt> <dd>

Contains the number of the physical disk.

</dd> <dt>

**Offset**
</dt> <dd>

Contains the physical offset in bytes of the data on the disk.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddvol.h (include Ntddvol.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_VOLUME\_LOGICAL\_TO\_PHYSICAL**](ioctl-volume-logical-to-physical.md)
</dt> <dt>

[**IOCTL\_VOLUME\_PHYSICAL\_TO\_LOGICAL**](ioctl-volume-physical-to-logical.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20VOLUME_PHYSICAL_OFFSET%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






