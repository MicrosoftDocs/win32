---
title: FEATURE\_DATA\_CD\_AUDIO\_ANALOG\_PLAY structure
description: The FEATURE\_DATA\_CD\_AUDIO\_ANALOG\_PLAY structure holds information about the CD Audio External Play feature.
ms.assetid: 01c34bb8-b164-425d-b81c-7eefc08296e2
keywords:
- FEATURE_DATA_CD_AUDIO_ANALOG_PLAY structure Storage Devices
- PFEATURE_DATA_CD_AUDIO_ANALOG_PLAY structure pointer Storage Devices
topic_type:
- apiref
api_name:
- FEATURE_DATA_CD_AUDIO_ANALOG_PLAY
api_location:
- ntddmmc.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# FEATURE\_DATA\_CD\_AUDIO\_ANALOG\_PLAY structure

The FEATURE\_DATA\_CD\_AUDIO\_ANALOG\_PLAY structure holds information about the CD Audio External Play feature.

## Syntax


```C++
typedef struct _FEATURE_DATA_CD_AUDIO_ANALOG_PLAY {
  FEATURE_HEADER Header;
  UCHAR          SeperateVolume  :1;
  UCHAR          SeperateChannelMute  :1;
  UCHAR          ScanSupported  :1;
  UCHAR          Reserved1  :5;
  UCHAR          Reserved2;
  UCHAR          NumerOfVolumeLevels[2];
} FEATURE_DATA_CD_AUDIO_ANALOG_PLAY, *PFEATURE_DATA_CD_AUDIO_ANALOG_PLAY;
```



## Members

<dl> <dt>

**Header**
</dt> <dd>

Contains a [**FEATURE\_HEADER**](feature-header.md) structure with header information for this feature descriptor.

</dd> <dt>

**SeperateVolume**
</dt> <dd>

Indicates, when set to zero, that all audio channels have the same volume level. When set to 1, it indicates that the volume of each audio channel can be set separately.

</dd> <dt>

**SeperateChannelMute**
</dt> <dd>

Indicates, when set to zero, that all audio channels are muted simultaneously. When set to 1, it indicates that each audio channel can be muted independently.

</dd> <dt>

**ScanSupported**
</dt> <dd>

Indicates, when set to 1, that the SCAN command is supported. See the *SCSI Multimedia 3* (*MMC-3*) specification for a description of the SCAN command.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved.

</dd> <dt>

**NumerOfVolumeLevels**
</dt> <dd></dd> </dl>

## Remarks

This structure holds data for the feature named "CD Audio External Play" by the *MMC-3* specification. Devices that support this feature can play CD audio data and channel it directly to an external output.

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddmmc.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**FEATURE\_HEADER**](feature-header.md)
</dt> <dt>

[**FEATURE\_NUMBER**](feature-number.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20FEATURE_DATA_CD_AUDIO_ANALOG_PLAY%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






