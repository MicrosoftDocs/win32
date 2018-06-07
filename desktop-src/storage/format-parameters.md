---
title: FORMAT\_PARAMETERS structure
description: The FORMAT\_PARAMETERS structure is used in conjunction with the IOCTL\_DISK\_FORMAT\_TRACKS request to format the specified set of contiguous tracks on the disk.
ms.assetid: 9c92e010-35d7-40ff-8025-51e945861b9c
keywords:
- FORMAT_PARAMETERS structure Storage Devices
- PFORMAT_PARAMETERS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- FORMAT_PARAMETERS
api_location:
- ntdddisk.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# FORMAT\_PARAMETERS structure

The FORMAT\_PARAMETERS structure is used in conjunction with the [**IOCTL\_DISK\_FORMAT\_TRACKS**](ioctl-disk-format-tracks.md) request to format the specified set of contiguous tracks on the disk.

## Syntax


```C++
typedef struct _FORMAT_PARAMETERS {
  MEDIA_TYPE MediaType;
  ULONG      StartCylinderNumber;
  ULONG      EndCylinderNumber;
  ULONG      StartHeadNumber;
  ULONG      EndHeadNumber;
} FORMAT_PARAMETERS, *PFORMAT_PARAMETERS;
```



## Members

<dl> <dt>

**MediaType**
</dt> <dd>

Indicates format information, such as the disk size and the number of bytes per sector. For a list of the values that can be assigned to this member, see [**MEDIA\_TYPE**](media-type.md).

</dd> <dt>

**StartCylinderNumber**
</dt> <dd>

Indicates the number of the cylinder where the formatting should begin.

</dd> <dt>

**EndCylinderNumber**
</dt> <dd>

Indicates the number of the cylinder where the formatting should end.

</dd> <dt>

**StartHeadNumber**
</dt> <dd>

Indicates the number of the head where the formatting should begin.

</dd> <dt>

**EndHeadNumber**
</dt> <dd>

Indicates the number of the head where the formatting should end.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_DISK\_FORMAT\_TRACKS**](ioctl-disk-format-tracks.md)
</dt> <dt>

[**MEDIA\_TYPE**](media-type.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FORMAT_PARAMETERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






