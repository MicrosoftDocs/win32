---
title: CDROM\_SUB\_Q\_DATA\_FORMAT structure
description: The CDROM\_SUB\_Q\_DATA\_FORMAT structure is used with device control IRPs of type IOCTL\_CDROM\_READ\_Q\_CHANNEL.
ms.assetid: 0eac3cc1-9c1c-4438-ab20-51c65018cea0
keywords:
- CDROM_SUB_Q_DATA_FORMAT structure Storage Devices
- PCDROM_SUB_Q_DATA_FORMAT structure pointer Storage Devices
topic_type:
- apiref
api_name:
- CDROM_SUB_Q_DATA_FORMAT
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# CDROM\_SUB\_Q\_DATA\_FORMAT structure

The CDROM\_SUB\_Q\_DATA\_FORMAT structure is used with device control IRPs of type [**IOCTL\_CDROM\_READ\_Q\_CHANNEL**](ioctl-cdrom-read-q-channel.md).

## Syntax


```C++
typedef struct _CDROM_SUB_Q_DATA_FORMAT {
  UCHAR Format;
  UCHAR Track;
} CDROM_SUB_Q_DATA_FORMAT, *PCDROM_SUB_Q_DATA_FORMAT;
```



## Members

<dl> <dt>

**Format**
</dt> <dd>

Specifies which subset of the Q data the read operation should return, as follows:

<dl> <dt>

<span id="IOCTL_CDROM_CURRENT_POSITION_"></span><span id="ioctl_cdrom_current_position_"></span>IOCTL\_CDROM\_CURRENT\_POSITION 
</dt> <dd>

Indicates that the read operation should return position information such as the track number, the index number, the absolute address, and the track relative address. If the IOCTL\_CDROM\_Q\_CHANNEL device control IRP specifies this format, the information is returned in the [**SUB\_Q\_CURRENT\_POSITION**](sub-q-current-position.md) member of the [**SUB\_Q\_CHANNEL\_DATA**](sub-q-channel-data.md) structure.

</dd> </dl>

<dl> <dt>

<span id="IOCTL_CDROM_MEDIA_CATALOG"></span><span id="ioctl_cdrom_media_catalog"></span>IOCTL\_CDROM\_MEDIA\_CATALOG
</dt> <dd>

Indicates that the read operation should return the media catalog number. If the IOCTL\_CDROM\_Q\_CHANNEL device control IRP specifies this format, the information is returned in the [**SUB\_Q\_MEDIA\_CATALOG\_NUMBER**](sub-q-media-catalog-number.md) member of the [**SUB\_Q\_CHANNEL\_DATA**](sub-q-channel-data.md) structure.

</dd> </dl>

<dl> <dt>

<span id="IOCTL_CDROM_TRACK_ISRC"></span><span id="ioctl_cdrom_track_isrc"></span>IOCTL\_CDROM\_TRACK\_ISRC
</dt> <dd>

Indicates that the read operation should return the ISO/IEC 3901 Track International Standard Recording Code (ISRC). This code gives a unique number to an audio track. If the IOCTL\_CDROM\_Q\_CHANNEL device control IRP specifies this format, the information is returned in the [**SUB\_Q\_TRACK\_ISRC**](sub-q-track-isrc.md) member of the [**SUB\_Q\_CHANNEL\_DATA**](sub-q-channel-data.md) structure.

</dd> </dl> </dd> <dt>

**Track**
</dt> <dd>

Indicates the track number where the CD-ROM driver must read the Q subchannel data. If **Format** is set to IOCTL\_CDROM\_MEDIA\_CATALOG, then the **Track** member must be set to zero.

</dd> </dl>

## Remarks

The CDROM\_SUB\_Q\_DATA\_FORMAT structure indicates the track from which to read the Q part of the subchannel data and the format of the read.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CDROM\_READ\_Q\_CHANNEL**](ioctl-cdrom-read-q-channel.md)
</dt> <dt>

[**SUB\_Q\_CHANNEL\_DATA**](sub-q-channel-data.md)
</dt> <dt>

[**SUB\_Q\_CURRENT\_POSITION**](sub-q-current-position.md)
</dt> <dt>

[**SUB\_Q\_MEDIA\_CATALOG\_NUMBER**](sub-q-media-catalog-number.md)
</dt> <dt>

[**SUB\_Q\_TRACK\_ISRC**](sub-q-track-isrc.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_SUB_Q_DATA_FORMAT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






