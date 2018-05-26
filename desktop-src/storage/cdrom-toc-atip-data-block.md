---
title: CDROM\_TOC\_ATIP\_DATA\_BLOCK structure
description: Device control IRPs with a control code of IOCTL\_CDROM\_READ\_TOC\_EX and a format of CDROM\_READ\_TOC\_EX\_FORMAT\_ATIP return their output data in a header structure of type CDROM\_TOC\_ATIP\_DATA followed by a series of ATIP data block descriptors defined by CDROM\_TOC\_ATIP\_DATA\_BLOCK.
ms.assetid: b98d0ba9-9c32-44ed-b6c3-db6de26a1663
keywords:
- CDROM_TOC_ATIP_DATA_BLOCK structure Storage Devices
- PCDROM_TOC_ATIP_DATA_BLOCK structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CDROM_TOC_ATIP_DATA_BLOCK
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

# CDROM\_TOC\_ATIP\_DATA\_BLOCK structure

Device control IRPs with a control code of [**IOCTL\_CDROM\_READ\_TOC\_EX**](ioctl-cdrom-read-toc-ex.md) and a format of CDROM\_READ\_TOC\_EX\_FORMAT\_ATIP return their output data in a header structure of type [**CDROM\_TOC\_ATIP\_DATA**](cdrom-toc-atip-data.md) followed by a series of ATIP data block descriptors defined by **CDROM\_TOC\_ATIP\_DATA\_BLOCK**.

## Syntax


```C++
typedef struct _CDROM_TOC_ATIP_DATA_BLOCK {
  UCHAR CdrwReferenceSpeed  :3;
  UCHAR Reserved3  :1;
  UCHAR WritePower  :3;
  UCHAR True1  :1;
  UCHAR Reserved4  :6;
  UCHAR UnrestrictedUse  :1;
  UCHAR Reserved5  :1;
  UCHAR A3Valid  :1;
  UCHAR A2Valid  :1;
  UCHAR A1Valid  :1;
  UCHAR DiscSubType  :3;
  UCHAR IsCdrw  :1;
  UCHAR True2  :1;
  UCHAR Reserved7;
  UCHAR LeadInMsf[3];
  UCHAR Reserved8;
  UCHAR LeadOutMsf[3];
  UCHAR Reserved9;
  UCHAR A1Values[3];
  UCHAR Reserved10;
  UCHAR A2Values[3];
  UCHAR Reserved11;
  UCHAR A3Values[3];
  UCHAR Reserved12;
} CDROM_TOC_ATIP_DATA_BLOCK, *PCDROM_TOC_ATIP_DATA_BLOCK;
```



## Members

<dl> <dt>

**CdrwReferenceSpeed**
</dt> <dd>

Indicates the recommended write speed for the media. Values 0x00 to 0x01 are reserved. A value of 0x02 indicates a CD-ROM speed of 4X. A value of 0x03 indicates a CD-ROM speed of 8X. Values 0x04 to 0x07 are reserved.

</dd> <dt>

**Reserved3**
</dt> <dd>

Reserved.

</dd> <dt>

**WritePower**
</dt> <dd>

Indicates media's recommended initial laser power setting. The high order bit must be set to 1. The setting of the other bits varies between CD-R and CD-RW media. For an explanation of the values these bits can have, see the *SCSI Multimedia Commands - 3* (MMC-3) specification.

</dd> <dt>

**True1**
</dt> <dd>

Must be set to 1.

</dd> <dt>

**Reserved4**
</dt> <dd>

Reserved.

</dd> <dt>

**UnrestrictedUse**
</dt> <dd>

Indicates, when set to 1, that the mounted disc is defined for unrestricted use. When set to zero, indicates that the mounted disc is defined for restricted use.

</dd> <dt>

**Reserved5**
</dt> <dd>

Reserved.

</dd> <dt>

**A3Valid**
</dt> <dd>

Indicates that bytes 16-18 (bytes 12-14 of the ATIP descriptor) are valid when set to 1. When set to zero, indicates that bytes 16-18 are invalid.

</dd> <dt>

**A2Valid**
</dt> <dd>

Indicates that A2 values field is valid when set to 1. When set to zero, indicates that the A2 values field is invalid.

</dd> <dt>

**A1Valid**
</dt> <dd>

Indicates that A3 values field is valid when set to 1. When set to zero, indicates that the A3 values field is invalid.

</dd> <dt>

**DiscSubType**
</dt> <dd>

Must be set to zero.

</dd> <dt>

**IsCdrw**
</dt> <dd>

Indicates the media is rewritable (CD-RW) when set to 1. When set to zero, indicates the media is write-once (CD-R).

</dd> <dt>

**True2**
</dt> <dd>

Must be set to 1.

</dd> <dt>

**Reserved7**
</dt> <dd>

Reserved.

</dd> <dt>

**LeadInMsf**
</dt> <dd>

Indicates the ATIP start time of lead-in, in terms of minutes, seconds, and frames. Valid values of the first byte are from 0x50 to 0x63. For an explanation of the values that the second and third bytes can have, see the *SCSI Multimedia Commands - 3* (MMC-3) specification.

</dd> <dt>

**Reserved8**
</dt> <dd>

Reserved.

</dd> <dt>

**LeadOutMsf**
</dt> <dd>

Indicates the ATIP last possible start time of lead-out in terms of minutes, seconds, and frames. Valid values of the first byte are from 0x0 to 0x04F. For an explanation of the values that the second and third bytes can have, see the *SCSI Multimedia Commands - 3* (MMC-3) specification.

</dd> <dt>

**Reserved9**
</dt> <dd>

Reserved.

</dd> <dt>

**A1Values**
</dt> <dd>

See specification *T10/1363-D Revision-02A*, by National Committee for Information Technology Standards (NCITS) For information about the permissible values for this member.

</dd> <dt>

**Reserved10**
</dt> <dd>

Reserved.

</dd> <dt>

**A2Values**
</dt> <dd>

Reserved.

</dd> <dt>

**Reserved11**
</dt> <dd>

Reserved.

</dd> <dt>

**A3Values**
</dt> <dd>

Reserved.

</dd> <dt>

**Reserved12**
</dt> <dd>

Reserved.

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

[**CDROM\_TOC\_ATIP\_DATA**](cdrom-toc-atip-data.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_TOC_ATIP_DATA_BLOCK%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






