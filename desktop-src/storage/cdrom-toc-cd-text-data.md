---
title: CDROM\_TOC\_CD\_TEXT\_DATA structure
description: Device control IRPs with a control code of IOCTL\_CDROM\_READ\_TOC\_EX and a format of CDROM\_READ\_TOC\_EX\_FORMAT\_CDTEXT return their output data in this structure followed by a series of descriptors of type CDROM\_TOC\_CD\_TEXT\_DATA\_BLOCK.
ms.assetid: 92e87c1d-17c4-4ac8-af9d-08863ce84c9e
keywords:
- CDROM_TOC_CD_TEXT_DATA structure Storage Devices
- PCDROM_TOC_CD_TEXT_DATA structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CDROM_TOC_CD_TEXT_DATA
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CDROM\_TOC\_CD\_TEXT\_DATA structure

Device control IRPs with a control code of [**IOCTL\_CDROM\_READ\_TOC\_EX**](ioctl-cdrom-read-toc-ex.md) and a format of CDROM\_READ\_TOC\_EX\_FORMAT\_CDTEXT return their output data in this structure followed by a series of descriptors of type [**CDROM\_TOC\_CD\_TEXT\_DATA\_BLOCK**](cdrom-toc-cd-text-data-block.md).

## Syntax


```C++
typedef struct _CDROM_TOC_CD_TEXT_DATA {
  UCHAR                        Length[2];
  UCHAR                        Reserved1;
  UCHAR                        Reserved2;
  CDROM_TOC_CD_TEXT_DATA_BLOCK Descriptors[];
} CDROM_TOC_CD_TEXT_DATA, *PCDROM_TOC_CD_TEXT_DATA;
```



## Members

<dl> <dt>

**Length**
</dt> <dd>

Indicates the number of bytes to be transferred in response to the IOCTL\_CDROM\_READ\_TOC\_EX IOCTL. This length value does not include the length of the **Length** member itself.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved.

</dd> <dt>

**Descriptors**
</dt> <dd>

Contains zero or more text data block descriptors of type [**CDROM\_TOC\_CD\_TEXT\_DATA\_BLOCK**](cdrom-toc-cd-text-data-block.md).

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CDROM\_READ\_TOC\_EX**](ioctl-cdrom-read-toc-ex.md)
</dt> <dt>

[**CDROM\_READ\_TOC\_EX**](cdrom-read-toc-ex.md)
</dt> <dt>

[**CDROM\_TOC\_CD\_TEXT\_DATA\_BLOCK**](cdrom-toc-cd-text-data-block.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_TOC_CD_TEXT_DATA%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






