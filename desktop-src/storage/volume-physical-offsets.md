---
title: VOLUME\_PHYSICAL\_OFFSETS structure
description: The VOLUME\_PHYSICAL\_OFFSETS structure contains an array of physical offsets and accompanying physical disk numbers and is used with IOCTL\_VOLUME\_LOGICAL\_TO\_PHYSICAL to request a series of pairs of physical offsets and disk numbers that correspond to a single logical offset.
ms.assetid: 876cb283-ce0d-44ed-b515-d4ee31089b88
keywords:
- VOLUME_PHYSICAL_OFFSETS structure Storage Devices
- PVOLUME_PHYSICAL_OFFSETS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- VOLUME_PHYSICAL_OFFSETS
api_location:
- ntddvol.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# VOLUME\_PHYSICAL\_OFFSETS structure

The VOLUME\_PHYSICAL\_OFFSETS structure contains an array of physical offsets and accompanying physical disk numbers and is used with [**IOCTL\_VOLUME\_LOGICAL\_TO\_PHYSICAL**](ioctl-volume-logical-to-physical.md) to request a series of pairs of physical offsets and disk numbers that correspond to a single logical offset.

## Syntax


```C++
typedef struct _VOLUME_PHYSICAL_OFFSETS {
  ULONG                  NumberOfPhysicalOffsets;
  VOLUME_PHYSICAL_OFFSET PhysicalOffset[ANYSIZE_ARRAY];
} VOLUME_PHYSICAL_OFFSETS, *PVOLUME_PHYSICAL_OFFSETS;
```



## Members

<dl> <dt>

**NumberOfPhysicalOffsets**
</dt> <dd>

Contains the number of physical offsets returned by the call to [**IOCTL\_VOLUME\_LOGICAL\_TO\_PHYSICAL**](ioctl-volume-logical-to-physical.md).

</dd> <dt>

**PhysicalOffset**
</dt> <dd>

Contains an array of structures of type [**VOLUME\_PHYSICAL\_OFFSET**](volume-physical-offset.md). Each element of the array contains a pair consisting of a physical disk number and an accompanying physical offset &lt;disk number, disk offset&gt;.

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
</dt> <dt>

[**VOLUME\_PHYSICAL\_OFFSET**](volume-physical-offset.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20VOLUME_PHYSICAL_OFFSETS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






