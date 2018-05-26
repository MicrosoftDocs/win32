---
title: CDROM\_READ\_TOC\_EX structure
description: When drivers query a target CD-ROM device with IOCTL\_CDROM\_READ\_TOC\_EX they must define the query with this structure.
ms.assetid: 17dbc843-dc65-40d7-9cda-916127e4cfa4
keywords:
- CDROM_READ_TOC_EX structure Storage Devices
- PCDROM_READ_TOC_EX structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CDROM_READ_TOC_EX
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

# CDROM\_READ\_TOC\_EX structure

When drivers query a target CD-ROM device with [**IOCTL\_CDROM\_READ\_TOC\_EX**](ioctl-cdrom-read-toc-ex.md) they must define the query with this structure.

## Syntax


```C++
typedef struct _CDROM_READ_TOC_EX {
  UCHAR Format  :4;
  UCHAR Reserved1  :3;
  UCHAR Msf  :1;
  UCHAR SessionTrack;
  UCHAR Reserved2;
  UCHAR Reserved3;
} CDROM_READ_TOC_EX, *PCDROM_READ_TOC_EX;
```



## Members

<dl> <dt>

**Format**
</dt> <dd>

Specifies table of contents read operation, as follows:

<dl> <dt>

<span id="CDROM_READ_TOC_EX_FORMAT_TOC"></span><span id="cdrom_read_toc_ex_format_toc"></span>CDROM\_READ\_TOC\_EX\_FORMAT\_TOC
</dt> <dd>

Query the device for the table of contents for the specified session(s). The **SessionTrack** member of the structure specifies the starting track number of the session for which the data will be returned. For multisession CD-ROMs, this command will return the table of contents data for all sessions. For track number 0xAA, it returns the lead-out area of the last complete session. The output data is reported in a [**CDROM\_TOC**](cdrom-toc.md) structure.

</dd> </dl>

<dl> <dt>

<span id="CDROM_READ_TOC_EX_FORMAT_SESSION"></span><span id="cdrom_read_toc_ex_format_session"></span>CDROM\_READ\_TOC\_EX\_FORMAT\_SESSION
</dt> <dd>

Query the device for the first complete session number, the last complete session number, and the last complete session starting address. The output data is reported in a [**CDROM\_TOC\_SESSION\_DATA**](cdrom-toc-session-data.md) structure. With this format, the **SessionTrack** member is reserved and must be set to zero. This format provides the initiator with quick access to the last finalized session starting address.

</dd> </dl>

<dl> <dt>

<span id="CDROM_READ_TOC_EX_FORMAT_FULL_TOC"></span><span id="cdrom_read_toc_ex_format_full_toc"></span>CDROM\_READ\_TOC\_EX\_FORMAT\_FULL\_TOC
</dt> <dd>

Query the device for all Q subcode data in the lead-in table of contents areas starting from the session number specified in the **SessionTrack** member. The output data is reported in a header structure, [**CDROM\_TOC\_FULL\_TOC\_DATA**](cdrom-toc-full-toc-data.md), followed by a series of track descriptors defined in [**CDROM\_TOC\_FULL\_TOC\_DATA\_BLOCK**](cdrom-toc-full-toc-data-block.md). In this format, logical block addressing (LBA) is not defined, and the **Msf** member must be set to 1.

</dd> </dl>

<dl> <dt>

<span id="CDROM_READ_TOC_EX_FORMAT_PMA"></span><span id="cdrom_read_toc_ex_format_pma"></span>CDROM\_READ\_TOC\_EX\_FORMAT\_PMA
</dt> <dd>

Query the device for all Q subcode data in the *program memory area* (PMA). The output data is reported in a [**CDROM\_TOC\_PMA\_DATA**](cdrom-toc-pma-data.md) structure. In this format, the **SessionTrack** member is reserved and must be set to zero. Logical block addressing (LBA) is not defined, and the **Msf** member must be set to 1.

</dd> </dl>

<dl> <dt>

<span id="CDROM_READ_TOC_EX_FORMAT_ATIP"></span><span id="cdrom_read_toc_ex_format_atip"></span>CDROM\_READ\_TOC\_EX\_FORMAT\_ATIP
</dt> <dd>

Query the device for *absolute time in pregroove* (ATIP) data. The output data is reported in the [**CDROM\_TOC\_ATIP\_DATA**](cdrom-toc-atip-data.md) structure. In this format, the **SessionTrack** member is reserved and must be set to zero. Logical block addressing (LBA) is not defined, and the **Msf** member must be set to 1.

</dd> </dl>

<dl> <dt>

<span id="CDROM_READ_TOC_EX_FORMAT_CDTEXT"></span><span id="cdrom_read_toc_ex_format_cdtext"></span>CDROM\_READ\_TOC\_EX\_FORMAT\_CDTEXT
</dt> <dd>

Query the device for CD-TEXT information that is recorded in the lead-in area as R-W subchannel data. The output data is reported in a [**CDROM\_TOC\_CD\_TEXT\_DATA**](cdrom-toc-cd-text-data.md) structure with an appended array of [**CDROM\_TOC\_CD\_TEXT\_DATA\_BLOCK**](cdrom-toc-cd-text-data-block.md) structures.

</dd> </dl> </dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**Msf**
</dt> <dd>

Indicates the minute-second-frame bit. When set to one, this bit indicates that minute-second-frame (MSF) addressing must be used. When zero, it indicates that logical block addressing (LBA) must be used.

</dd> <dt>

**SessionTrack**
</dt> <dd>

Specifies the starting track number for which the data will be returned, the session for which the command is targeted, or a reserved field that drivers should set to zero. Which of these values **SessionTrack** takes depends on the value of the **Format** member.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved

</dd> <dt>

**Reserved3**
</dt> <dd>

Reserved

</dd> </dl>

## Remarks

For further information and definitions of terms used in this reference page and in the reference pages of related structures, see specification *T10/1363-D Revision-02A*, by National Committee for Information Technology Standards (NCITS).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CDROM\_READ\_TOC\_EX**](ioctl-cdrom-read-toc-ex.md)
</dt> <dt>

[**CDROM\_TOC**](cdrom-toc.md)
</dt> <dt>

[**CDROM\_TOC\_SESSION\_DATA**](cdrom-toc-session-data.md)
</dt> <dt>

[**CDROM\_TOC\_FULL\_TOC\_DATA**](cdrom-toc-full-toc-data.md)
</dt> <dt>

[**CDROM\_TOC\_FULL\_TOC\_DATA\_BLOCK**](cdrom-toc-full-toc-data-block.md)
</dt> <dt>

[**CDROM\_TOC\_PMA\_DATA**](cdrom-toc-pma-data.md)
</dt> <dt>

[**CDROM\_TOC\_ATIP\_DATA**](cdrom-toc-atip-data.md)
</dt> <dt>

[**CDROM\_TOC\_CD\_TEXT\_DATA**](cdrom-toc-cd-text-data.md)
</dt> <dt>

[**CDROM\_TOC\_CD\_TEXT\_DATA\_BLOCK**](cdrom-toc-cd-text-data-block.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_READ_TOC_EX%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






