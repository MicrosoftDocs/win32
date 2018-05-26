---
title: CDROM\_TOC\_CD\_TEXT\_DATA\_BLOCK structure
description: This structure contains CD text descriptor data used in conjunction with the data in the CDROM\_TOC\_CD\_TEXT\_DATA structure.
ms.assetid: 119386fe-1eff-4dac-b9d5-54baefcf6e12
keywords:
- CDROM_TOC_CD_TEXT_DATA_BLOCK structure Storage Devices
- PCDROM_TOC_CD_TEXT_DATA_BLOCK structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CDROM_TOC_CD_TEXT_DATA_BLOCK
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

# CDROM\_TOC\_CD\_TEXT\_DATA\_BLOCK structure

This structure contains CD text descriptor data used in conjunction with the data in the [**CDROM\_TOC\_CD\_TEXT\_DATA**](cdrom-toc-cd-text-data.md) structure.

## Syntax


```C++
typedef struct _CDROM_TOC_CD_TEXT_DATA_BLOCK {
  UCHAR PackType;
  UCHAR TrackNumber  :7;
  UCHAR ExtensionFlag  :1;
  UCHAR SequenceNumber;
  UCHAR CharacterPosition  :4;
  UCHAR BlockNumber  :3;
  UCHAR Unicode  :1;
  union {
    UCHAR Text[12];
    WCHAR WText[6];
  };
  UCHAR CRC[2];
} CDROM_TOC_CD_TEXT_DATA_BLOCK, *PCDROM_TOC_CD_TEXT_DATA_BLOCK;
```



## Members

<dl> <dt>

**PackType**
</dt> <dd>

Indicates the type of pack data, as follows:

<dl> <dt>

<span id="CDROM_CD_TEXT_PACK_ALBUM_NAME_"></span><span id="cdrom_cd_text_pack_album_name_"></span>CDROM\_CD\_TEXT\_PACK\_ALBUM\_NAME 
</dt> <dd>

Title of album or track.

</dd> </dl>

<dl> <dt>

<span id="CDROM_CD_TEXT_PACK_PERFORMER_"></span><span id="cdrom_cd_text_pack_performer_"></span>CDROM\_CD\_TEXT\_PACK\_PERFORMER 
</dt> <dd>

Names of the performers (in ASCII).

</dd> </dl>

<dl> <dt>

<span id="CDROM_CD_TEXT_PACK_SONGWRITER_"></span><span id="cdrom_cd_text_pack_songwriter_"></span>CDROM\_CD\_TEXT\_PACK\_SONGWRITER 
</dt> <dd>

Names of the songwriters (in ASCII).

</dd> </dl>

<dl> <dt>

<span id="CDROM_CD_TEXT_PACK_COMPOSER_"></span><span id="cdrom_cd_text_pack_composer_"></span>CDROM\_CD\_TEXT\_PACK\_COMPOSER 
</dt> <dd>

Names of the composers (in ASCII).

</dd> </dl>

<dl> <dt>

<span id="CDROM_CD_TEXT_PACK_ARRANGER_"></span><span id="cdrom_cd_text_pack_arranger_"></span>CDROM\_CD\_TEXT\_PACK\_ARRANGER 
</dt> <dd>

Names of the arrangers (in ASCII).

</dd> </dl>

<dl> <dt>

<span id="CDROM_CD_TEXT_PACK_MESSAGES_"></span><span id="cdrom_cd_text_pack_messages_"></span>CDROM\_CD\_TEXT\_PACK\_MESSAGES 
</dt> <dd>

Messages from content provider and/or artist (in ASCII).

</dd> </dl>

<dl> <dt>

<span id="CDROM_CD_TEXT_PACK_DISC_ID"></span><span id="cdrom_cd_text_pack_disc_id"></span>CDROM\_CD\_TEXT\_PACK\_DISC\_ID
</dt> <dd>

Disc identification information.

</dd> </dl>

<dl> <dt>

<span id="CDROM_CD_TEXT_PACK_GENRE_"></span><span id="cdrom_cd_text_pack_genre_"></span>CDROM\_CD\_TEXT\_PACK\_GENRE 
</dt> <dd>

Genre identification and information.

</dd> </dl>

<dl> <dt>

<span id="CDROM_CD_TEXT_PACK_TOC_INFO_"></span><span id="cdrom_cd_text_pack_toc_info_"></span>CDROM\_CD\_TEXT\_PACK\_TOC\_INFO 
</dt> <dd>

Table of contents information.

</dd> </dl>

<dl> <dt>

<span id="CDROM_CD_TEXT_PACK_TOC_INFO2_"></span><span id="cdrom_cd_text_pack_toc_info2_"></span>CDROM\_CD\_TEXT\_PACK\_TOC\_INFO2 
</dt> <dd>

Second table of contents information.

</dd> </dl>

<dl> <dt>

<span id="CDROM_CD_TEXT_PACK_UPC_EAN_"></span><span id="cdrom_cd_text_pack_upc_ean_"></span>CDROM\_CD\_TEXT\_PACK\_UPC\_EAN 
</dt> <dd>

UPC/EAN code of the album and ISRC code of each track.

</dd> </dl>

<dl> <dt>

<span id="CDROM_CD_TEXT_PACK_SIZE_INFO_"></span><span id="cdrom_cd_text_pack_size_info_"></span>CDROM\_CD\_TEXT\_PACK\_SIZE\_INFO 
</dt> <dd>

Size information for the block.

</dd> </dl> </dd> <dt>

**TrackNumber**
</dt> <dd>

See specification *T10/1363-D Revision-02A*, by National Committee for Information Technology Standards (NCITS) For information about the permissible values for this member.

</dd> <dt>

**ExtensionFlag**
</dt> <dd>

Must be set to zero.

</dd> <dt>

**SequenceNumber**
</dt> <dd>

See specification *T10/1363-D Revision-02A*, by National Committee for Information Technology Standards (NCITS) For information about the permissible values for this member.

</dd> <dt>

**CharacterPosition**
</dt> <dd>

See specification *T10/1363-D Revision-02A*, by National Committee for Information Technology Standards (NCITS) For information about the permissible values for this member.

</dd> <dt>

**BlockNumber**
</dt> <dd>

See specification *T10/1363-D Revision-02A*, by National Committee for Information Technology Standards (NCITS) For information about the permissible values for this member.

</dd> <dt>

**Unicode**
</dt> <dd>

Indicates, when set to 1, that the text is stored in Unicode format.

</dd> <dt>

**Text**
</dt> <dd>

Contains text descriptor data in the form of 8-bit ASCII characters.

</dd> <dt>

**WText**
</dt> <dd>

Contains text descriptor data in the form of 16-bit (wide) characters.

</dd> <dt>

**CRC**
</dt> <dd>

Contains the cyclic redundancy check.

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

[**CDROM\_TOC\_CD\_TEXT\_DATA**](cdrom-toc-cd-text-data.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_TOC_CD_TEXT_DATA_BLOCK%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






