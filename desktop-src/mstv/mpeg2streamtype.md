---
title: MPEG2StreamType enumeration
description: Specifies the MPEG2 stream type.
ms.assetid: 10df5a9e-965c-4118-8ece-2d8ee353cd10
keywords:
- MPEG2StreamType enumeration Microsoft TV Technologies
- MPEG2StreamType enumeration Microsoft TV Technologies
topic_type:
- apiref
api_name:
- MPEG2StreamType
api_location:
- bdatypes.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# MPEG2StreamType enumeration

Specifies the MPEG2 stream type. The values in this enumeration correspond to the value of the stream\_type field in the program map table (PMT). The list is not exhaustive; other values may be possible.

## Syntax


```C++
typedef enum MPEG2StreamType { 
  BDA_UNITIALIZED_MPEG2STREAMTYPE  = -1,
  Reserved1                        = 0x00,
  ISO_IEC_11172_2_VIDEO            = 0x01,
  ISO_IEC_13818_2_VIDEO            = 0x02,
  ISO_IEC_11172_3_AUDIO            = 0x03,
  ISO_IEC_13818_3_AUDIO            = 0x04,
  ISO_IEC_13818_1_PRIVATE_SECTION  = 0x05,
  ISO_IEC_13818_1_PES              = 0x06,
  ISO_IEC_13522_MHEG               = 0x07,
  ANNEX_A_DSM_CC                   = 0x08,
  ITU_T_REC_H_222_1                = 0x09,
  ISO_IEC_13818_6_TYPE_A           = 0x0A,
  ISO_IEC_13818_6_TYPE_B           = 0x0B,
  ISO_IEC_13818_6_TYPE_C           = 0x0C,
  ISO_IEC_13818_6_TYPE_D           = 0x0D,
  ISO_IEC_13818_1_AUXILIARY        = 0x0E,
  ISO_IEC_13818_1_RESERVED         = 0x0F,
  USER_PRIVATE                     = 0x10,
  ISO_IEC_USER_PRIVATE             = 0x80,
  DOLBY_AC3_AUDIO                  = 0x81
} MPEG2StreamType;
```



## Constants

<dl> <dt>

<span id="BDA_UNITIALIZED_MPEG2STREAMTYPE"></span><span id="bda_unitialized_mpeg2streamtype"></span>**BDA\_UNITIALIZED\_MPEG2STREAMTYPE**
</dt> <dd>

MPEG-2 un-initialized streams.

</dd> <dt>

<span id="Reserved1"></span><span id="reserved1"></span><span id="RESERVED1"></span>**Reserved1**
</dt> <dd>

Reserved for future use.

</dd> <dt>

<span id="ISO_IEC_11172_2_VIDEO"></span><span id="iso_iec_11172_2_video"></span>**ISO\_IEC\_11172\_2\_VIDEO**
</dt> <dd>

MPEG-1 video stream. (ISO/IEC 11172 video.)

</dd> <dt>

<span id="ISO_IEC_13818_2_VIDEO"></span><span id="iso_iec_13818_2_video"></span>**ISO\_IEC\_13818\_2\_VIDEO**
</dt> <dd>

MPEG-2 video stream. (ISO/IEC 13818-2 video.)

</dd> <dt>

<span id="ISO_IEC_11172_3_AUDIO"></span><span id="iso_iec_11172_3_audio"></span>**ISO\_IEC\_11172\_3\_AUDIO**
</dt> <dd>

MPEG-1 audio stream. (ISO/IEC 11172 audio.)

</dd> <dt>

<span id="ISO_IEC_13818_3_AUDIO"></span><span id="iso_iec_13818_3_audio"></span>**ISO\_IEC\_13818\_3\_AUDIO**
</dt> <dd>

MPEG-2 audio stream. (ISO/IEC 13818-3 audio.)

</dd> <dt>

<span id="ISO_IEC_13818_1_PRIVATE_SECTION"></span><span id="iso_iec_13818_1_private_section"></span>**ISO\_IEC\_13818\_1\_PRIVATE\_SECTION**
</dt> <dd>

MPEG-2 private sections. (ISO/IEC 13818-1 private sections.)

</dd> <dt>

<span id="ISO_IEC_13818_1_PES"></span><span id="iso_iec_13818_1_pes"></span>**ISO\_IEC\_13818\_1\_PES**
</dt> <dd>

MPEG-2 Packetized Elementary Stream (PES) packets containing private data. (ISO/IEC 13818-1 PES).

</dd> <dt>

<span id="ISO_IEC_13522_MHEG"></span><span id="iso_iec_13522_mheg"></span>**ISO\_IEC\_13522\_MHEG**
</dt> <dd>

MHEG-5 Audio-Visual streams. (ISO/IEC 13522 MHEG.)

</dd> <dt>

<span id="ANNEX_A_DSM_CC"></span><span id="annex_a_dsm_cc"></span>**ANNEX\_A\_DSM\_CC**
</dt> <dd>

Digital Storage Media Command and Control (DSM-CC) stream. (ISO/IEC 13818-1 Annex A.)

</dd> <dt>

<span id="ITU_T_REC_H_222_1"></span><span id="itu_t_rec_h_222_1"></span>**ITU\_T\_REC\_H\_222\_1**
</dt> <dd>

ITU-T Satellite Audio-Visual streams. (ITU-T Rec. H.222.1.)

</dd> <dt>

<span id="ISO_IEC_13818_6_TYPE_A"></span><span id="iso_iec_13818_6_type_a"></span>**ISO\_IEC\_13818\_6\_TYPE\_A**
</dt> <dd>

MPEG-2 Video Clip A streams. (ISO/IEC 13818-6 type A.)

</dd> <dt>

<span id="ISO_IEC_13818_6_TYPE_B"></span><span id="iso_iec_13818_6_type_b"></span>**ISO\_IEC\_13818\_6\_TYPE\_B**
</dt> <dd>

MPEG-2 Video Clip B streams. (ISO/IEC 13818-6 type B.)

</dd> <dt>

<span id="ISO_IEC_13818_6_TYPE_C"></span><span id="iso_iec_13818_6_type_c"></span>**ISO\_IEC\_13818\_6\_TYPE\_C**
</dt> <dd>

MPEG-2 Video Clip C streams. (ISO/IEC 13818-6 type C.)

</dd> <dt>

<span id="ISO_IEC_13818_6_TYPE_D"></span><span id="iso_iec_13818_6_type_d"></span>**ISO\_IEC\_13818\_6\_TYPE\_D**
</dt> <dd>

MPEG-2 Video Clip D streams. (ISO/IEC 13818-6 type D.)

</dd> <dt>

<span id="ISO_IEC_13818_1_AUXILIARY"></span><span id="iso_iec_13818_1_auxiliary"></span>**ISO\_IEC\_13818\_1\_AUXILIARY**
</dt> <dd>

MPEG-2 Auxiliary streams. (ISO/IEC 13818-1 auxiliary.)

</dd> <dt>

<span id="ISO_IEC_13818_1_RESERVED"></span><span id="iso_iec_13818_1_reserved"></span>**ISO\_IEC\_13818\_1\_RESERVED**
</dt> <dd>

MPEG-2 Reserved streams.

</dd> <dt>

<span id="USER_PRIVATE"></span><span id="user_private"></span>**USER\_PRIVATE**
</dt> <dd>

This constant is not supported; use ISO\_IEC\_USER\_PRIVATE instead.

**Windows Server 2008, Windows Vista and earlier:** User proprietary streams.

</dd> <dt>

<span id="ISO_IEC_USER_PRIVATE"></span><span id="iso_iec_user_private"></span>**ISO\_IEC\_USER\_PRIVATE**
</dt> <dd>

User proprietary streams. This enumeration value matches the value given in ISO/IEC 13818-1.

</dd> <dt>

<span id="DOLBY_AC3_AUDIO"></span><span id="dolby_ac3_audio"></span>**DOLBY\_AC3\_AUDIO**
</dt> <dd>

Dolby AC3 audio.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Bdatypes.h (include Bdaiface.h)</dt> </dl> |



## See also

<dl> <dt>

[**IMPEG2ComponentType::get\_StreamType**](/previous-versions/windows/desktop/api/tuner/nf-tuner-impeg2componenttype-get_streamtype)
</dt> <dt>

[Tuning Model Enumerations](tuning-model-enumerations.md)
</dt> </dl>

 

 





