---
title: VOLUME\_LOGICAL\_OFFSET structure
description: The VOLUME\_LOGICAL\_OFFSET structure contains a logical offset into a volume.
ms.assetid: 4b0a982b-63ae-4109-a4be-2dd82824e75a
keywords:
- VOLUME_LOGICAL_OFFSET structure Storage Devices
- PVOLUME_LOGICAL_OFFSET structure pointer Storage Devices
topic_type:
- apiref
api_name:
- VOLUME_LOGICAL_OFFSET
api_location:
- ntddvol.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# VOLUME\_LOGICAL\_OFFSET structure

The VOLUME\_LOGICAL\_OFFSET structure contains a logical offset into a volume.

## Syntax


```C++
typedef struct _VOLUME_LOGICAL_OFFSET {
  LONGLONG LogicalOffset;
} VOLUME_LOGICAL_OFFSET, *PVOLUME_LOGICAL_OFFSET;
```



## Members

<dl> <dt>

**LogicalOffset**
</dt> <dd>

Contains a logical offset in bytes into a volume.

</dd> </dl>

## Remarks

The VOLUME\_LOGICAL\_OFFSET structure is used with [**IOCTL\_VOLUME\_PHYSICAL\_TO\_LOGICAL**](ioctl-volume-physical-to-logical.md) and [**IOCTL\_VOLUME\_LOGICAL\_TO\_PHYSICAL**](ioctl-volume-logical-to-physical.md) to request a logical offset equivalent of a physical offset or a physical offset equivalent of a logical offset, respectively.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20VOLUME_LOGICAL_OFFSET%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






