---
title: SUB\_Q\_CHANNEL\_DATA union
description: Device control IRPs with a control code of IOCTL\_CDROM\_READ\_Q\_CHANNEL return their output data in this union.
ms.assetid: d0304ac7-cb19-499c-81af-98be33312951
keywords:
- SUB_Q_CHANNEL_DATA union Storage Devices
- PSUB_Q_CHANNEL_DATA union pointer Storage Devices
topic_type:
- apiref
api_name:
- SUB_Q_CHANNEL_DATA
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

# SUB\_Q\_CHANNEL\_DATA union

Device control IRPs with a control code of IOCTL\_CDROM\_READ\_Q\_CHANNEL return their output data in this union.

## Syntax


```C++
typedef union _SUB_Q_CHANNEL_DATA {
  SUB_Q_CURRENT_POSITION     CurrentPosition;
  SUB_Q_MEDIA_CATALOG_NUMBER MediaCatalog;
  SUB_Q_TRACK_ISRC           TrackIsrc;
} SUB_Q_CHANNEL_DATA, *PSUB_Q_CHANNEL_DATA;
```



## Members

<dl> <dt>

**CurrentPosition**
</dt> <dd>

Contains position information, such as the absolute and relative addresses, in a [**SUB\_Q\_CURRENT\_POSITION**](sub-q-current-position.md) structure.

</dd> <dt>

**MediaCatalog**
</dt> <dd>

Contains the media catalog number in a [**SUB\_Q\_MEDIA\_CATALOG\_NUMBER**](sub-q-media-catalog-number.md) structure.

</dd> <dt>

**TrackIsrc**
</dt> <dd>

Contains the TrackIsrc code in a [**SUB\_Q\_TRACK\_ISRC**](sub-q-track-isrc.md) structure.

</dd> </dl>

## Remarks

The value of the **Format** member of the CDROM\_SUB\_Q\_DATA\_FORMAT structure that is passed as input with IOCTL\_CDROM\_READ\_Q\_CHANNEL determines which member of this union is used to return the output data. See [**CDROM\_SUB\_Q\_DATA\_FORMAT**](cdrom-sub-q-data-format.md) for a detailed explanation.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CDROM\_READ\_Q\_CHANNEL**](ioctl-cdrom-read-q-channel.md)
</dt> <dt>

[**CDROM\_SUB\_Q\_DATA\_FORMAT**](cdrom-sub-q-data-format.md)
</dt> <dt>

[**SUB\_Q\_CURRENT\_POSITION**](sub-q-current-position.md)
</dt> <dt>

[**SUB\_Q\_MEDIA\_CATALOG\_NUMBER**](sub-q-media-catalog-number.md)
</dt> <dt>

[**SUB\_Q\_TRACK\_ISRC**](sub-q-track-isrc.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SUB_Q_CHANNEL_DATA%20union%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






