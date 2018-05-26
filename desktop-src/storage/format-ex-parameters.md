---
title: FORMAT\_EX\_PARAMETERS structure
description: The FORMAT\_EX\_PARAMETERS structure is used in conjunction with the IOCTL\_DISK\_FORMAT\_TRACKS\_EX request to format the specified set of contiguous tracks on the disk.
ms.assetid: 0c87a0b8-f355-48a4-a119-11e047e159d0
keywords:
- FORMAT_EX_PARAMETERS structure Storage Devices
- PFORMAT_EX_PARAMETERS structure pointer Storage Devices
topic_type:
- apiref
api_name:
- FORMAT_EX_PARAMETERS
api_location:
- ntdddisk.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FORMAT\_EX\_PARAMETERS structure

The FORMAT\_EX\_PARAMETERS structure is used in conjunction with the [**IOCTL\_DISK\_FORMAT\_TRACKS\_EX**](ioctl-disk-format-tracks-ex.md) request to format the specified set of contiguous tracks on the disk.

## Syntax


```C++
typedef struct _FORMAT_EX_PARAMETERS {
  MEDIA_TYPE MediaType;
  ULONG      StartCylinderNumber;
  ULONG      EndCylinderNumber;
  ULONG      StartHeadNumber;
  ULONG      EndHeadNumber;
  USHORT     FormatGapLength;
  USHORT     SectorsPerTrack;
  USHORT     SectorNumber[1];
} FORMAT_EX_PARAMETERS, *PFORMAT_EX_PARAMETERS;
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

</dd> <dt>

**FormatGapLength**
</dt> <dd>

Indicates the length in bytes of a format gap.

</dd> <dt>

**SectorsPerTrack**
</dt> <dd>

Indicates the number of sectors per track.

</dd> <dt>

**SectorNumber**
</dt> <dd>

Contains an array whose first element indicates the number of the sector where the formatting should begin.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntdddisk.h (include Ntdddisk.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_DISK\_FORMAT\_TRACKS\_EX**](ioctl-disk-format-tracks-ex.md)
</dt> <dt>

[**IOCTL\_DISK\_FORMAT\_TRACKS**](ioctl-disk-format-tracks.md)
</dt> <dt>

[**FORMAT\_PARAMETERS**](format-parameters.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FORMAT_EX_PARAMETERS%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






