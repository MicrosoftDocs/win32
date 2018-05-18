---
title: CDROM\_PLAY\_AUDIO\_MSF structure
description: Device control IRPs with a control code of IOCTL\_CDROM\_PLAY\_AUDIO\_MSF use this structure to play an audio CD.
ms.assetid: '73589397-9b2b-4d49-9860-cb2eb6a26632'
keywords: ["CDROM_PLAY_AUDIO_MSF structure Storage Devices", "PCDROM_PLAY_AUDIO_MSF structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- CDROM_PLAY_AUDIO_MSF
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
---

# CDROM\_PLAY\_AUDIO\_MSF structure

Device control IRPs with a control code of [**IOCTL\_CDROM\_PLAY\_AUDIO\_MSF**](ioctl-cdrom-play-audio-msf.md) use this structure to play an audio CD.

## Syntax


```C++
typedef struct _CDROM_PLAY_AUDIO_MSF {
  UCHAR StartingM;
  UCHAR StartingS;
  UCHAR StartingF;
  UCHAR EndingM;
  UCHAR EndingS;
  UCHAR EndingF;
} CDROM_PLAY_AUDIO_MSF, *PCDROM_PLAY_AUDIO_MSF;
```



## Members

<dl> <dt>

**StartingM**
</dt> <dd>

Contains an integer between 0 and 74 that indicates the starting minute.

</dd> <dt>

**StartingS**
</dt> <dd>

Contains an integer between 0 and 59 that indicates the starting second.

</dd> <dt>

**StartingF**
</dt> <dd>

Contains an integer between 0 and 74 that indicates the starting frame.

</dd> <dt>

**EndingM**
</dt> <dd>

Contains an integer between 0 and 74 that indicates the ending minute.

</dd> <dt>

**EndingS**
</dt> <dd>

Contains an integer between 0 and 59 that indicates the ending second.

</dd> <dt>

**EndingF**
</dt> <dd>

Contains an integer between 0 and 74 that indicates the ending frame.

</dd> </dl>

## Remarks

Device control IRPs with a control code of IOCTL\_CDROM\_PLAY\_AUDIO\_MSF use this structure to play an audio CD and to indicate where to begin playing and where to stop. Starting and ending points are indicated in terms of minutes, seconds, and frames.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_CDROM\_PLAY\_AUDIO\_MSF**](ioctl-cdrom-play-audio-msf.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CDROM_PLAY_AUDIO_MSF%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






