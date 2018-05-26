---
title: DVD\_READ\_STRUCTURE structure
description: The DVD\_READ\_STRUCTURE structure is used in conjunction with the IOCTL\_DVD\_READ\_STRUCTURE request to retrieve a DVD descriptor containing information about a DVD disc.
ms.assetid: fe8c55de-e542-4c0d-a96b-31ad39e11dff
keywords:
- DVD_READ_STRUCTURE structure Storage Devices
- PDVD_READ_STRUCTURE structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DVD_READ_STRUCTURE
api_location:
- ntddcdvd.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DVD\_READ\_STRUCTURE structure

The DVD\_READ\_STRUCTURE structure is used in conjunction with the [**IOCTL\_DVD\_READ\_STRUCTURE**](ioctl-dvd-read-structure.md) request to retrieve a DVD descriptor containing information about a DVD disc.

## Syntax


```C++
typedef struct DVD_READ_STRUCTURE {
  LARGE_INTEGER        BlockByteOffset;
  DVD_STRUCTURE_FORMAT Format;
  DVD_SESSION_ID       SessionId;
  UCHAR                LayerNumber;
} DVD_READ_STRUCTURE, *PDVD_READ_STRUCTURE;
```



## Members

<dl> <dt>

**BlockByteOffset**
</dt> <dd>

Contains an offset to the logical block address of the descriptor to be retrieved.

</dd> <dt>

**Format**
</dt> <dd>

Indicates the type of DVD descriptor to retrieve. See the [**DVD\_STRUCTURE\_FORMAT**](dvd-structure-format.md) enumeration type for further information about the values that can be assigned to this member.

</dd> <dt>

**SessionId**
</dt> <dd>

Contains the DVD session ID.

</dd> <dt>

**LayerNumber**
</dt> <dd>

Contains the number of the layer where the descriptor is to be retrieved.

</dd> </dl>

## Remarks

The DVD\_READ\_STRUCTURE structure contains data such as copyright information, or manufacturer-specific information.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_DVD\_READ\_STRUCTURE**](ioctl-dvd-read-structure.md)
</dt> <dt>

[**DVD\_STRUCTURE\_FORMAT**](dvd-structure-format.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DVD_READ_STRUCTURE%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






