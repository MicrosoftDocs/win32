---
title: CDROM\_TOC\_FULL\_TOC\_DATA\_BLOCK structure
description: The CDROM\_TOC\_FULL\_TOC\_DATA\_BLOCK structure contains track descriptor data used in conjunction with the data from the CDROM\_TOC\_FULL\_TOC\_DATA structure.
ms.assetid: '8d6d1283-b64e-4c3b-8a45-376cfe76a19d'
keywords: ["CDROM_TOC_FULL_TOC_DATA_BLOCK structure Storage Devices", "PCDROM_TOC_FULL_TOC_DATA_BLOCK structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- CDROM_TOC_FULL_TOC_DATA_BLOCK
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
---

# CDROM\_TOC\_FULL\_TOC\_DATA\_BLOCK structure

The CDROM\_TOC\_FULL\_TOC\_DATA\_BLOCK structure contains track descriptor data used in conjunction with the data from the [**CDROM\_TOC\_FULL\_TOC\_DATA**](cdrom-toc-full-toc-data.md) structure.

## Syntax


```C++
typedef struct _CDROM_TOC_FULL_TOC_DATA_BLOCK {
  UCHAR SessionNumber;
  UCHAR Control  :4;
  UCHAR Adr  :4;
  UCHAR Reserved1;
  UCHAR Point;
  UCHAR MsfExtra[3];
  UCHAR Zero;
  UCHAR Msf[3];
} CDROM_TOC_FULL_TOC_DATA_BLOCK, *PCDROM_TOC_FULL_TOC_DATA_BLOCK;
```



## Members

<dl> <dt>

**SessionNumber**
</dt> <dd>

Contains the number of the session that the track belongs to.

</dd> <dt>

**Control**
</dt> <dd>

Indicates the attributes of the track.

<dl> <dt>

<span id="AUDIO_WITH_PREEMPHASIS"></span><span id="audio_with_preemphasis"></span>AUDIO\_WITH\_PREEMPHASIS
</dt> <dd>

Indicates two audio channels with preemphasis of 50/15 microseconds have been added.

</dd> </dl>

<dl> <dt>

<span id="DIGITAL_COPY_PERMITTED"></span><span id="digital_copy_permitted"></span>DIGITAL\_COPY\_PERMITTED
</dt> <dd>

Indicates digital copying is allowed.

</dd> </dl>

<dl> <dt>

<span id="AUDIO_DATA_TRACK"></span><span id="audio_data_track"></span>AUDIO\_DATA\_TRACK
</dt> <dd>

Indicates that the track contains nonaudio data.

</dd> </dl>

<dl> <dt>

<span id="TWO_FOUR_CHANNEL_AUDIO"></span><span id="two_four_channel_audio"></span>TWO\_FOUR\_CHANNEL\_AUDIO
</dt> <dd>

Indicates that the track contains four channels of audio data.

</dd> </dl> </dd> <dt>

**Adr**
</dt> <dd>

Indicates the type of information encoded in the Q subchannel of the block where this table of contents entry was found.

<dl> <dt>

<span id="ADR_NO_MODE_INFORMATION"></span><span id="adr_no_mode_information"></span>ADR\_NO\_MODE\_INFORMATION
</dt> <dd>

Q subchannel mode information not supplied.

</dd> </dl>

<dl> <dt>

<span id="ADR_ENCODES_CURRENT_POSITION"></span><span id="adr_encodes_current_position"></span>ADR\_ENCODES\_CURRENT\_POSITION
</dt> <dd> <dl> <dt>

Q subchannel encodes current position data
</dt> <dt>

(that is, track, index, absolute address, relative address). 
</dt> </dl> </dd> </dl>

<dl> <dt>

<span id="ADR_ENCODES_MEDIA_CATALOG"></span><span id="adr_encodes_media_catalog"></span>ADR\_ENCODES\_MEDIA\_CATALOG
</dt> <dd>

Q subchannel encodes media catalog number.

</dd> </dl>

<dl> <dt>

<span id="ADR_ENCODES_ISRC_"></span><span id="adr_encodes_isrc_"></span>ADR\_ENCODES\_ISRC 
</dt> <dd>

Q subchannel encodes ISRC.

</dd> </dl> </dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**Point**
</dt> <dd>

Defines various types of information within the table of contents lead-in area. For information about the permissible values for this member, see specification *T10/1363-D Revision-02A*, by National Committee for Information Technology Standards (NCITS).

</dd> <dt>

**MsfExtra**
</dt> <dd>

See specification *T10/1363-D Revision-02A*, by National Committee for Information Technology Standards (NCITS) For information about the permissible values for this member.

</dd> <dt>

**Zero**
</dt> <dd>

Contains the value of the zero bit.

</dd> <dt>

**Msf**
</dt> <dd>

Contains the minute, second, and frame. Msf\[0\] contains the minutes field. Msf\[1\] contains the seconds field, and Msf\[2\] contains the frames field. MSF is a format similar to logical block addressing.

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

[**CDROM\_TOC\_FULL\_TOC\_DATA**](cdrom-toc-full-toc-data.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_TOC_FULL_TOC_DATA_BLOCK%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






