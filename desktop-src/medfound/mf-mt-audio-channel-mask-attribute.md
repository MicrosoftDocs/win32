---
description: In an audio media type, specifies the assignment of audio channels to speaker positions.
ms.assetid: fa5f6baa-0a21-4162-8870-38e71763aba0
title: MF_MT_AUDIO_CHANNEL_MASK attribute (Mfapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_AUDIO\_CHANNEL\_MASK attribute

In an audio media type, specifies the assignment of audio channels to speaker positions.

## Data type

**UINT32**

The value of this attribute is a bitwise **OR** of the following flags, which are defined in the header file mmreg.h.

<dl> <dt>

<span id="SPEAKER_FRONT_LEFT"></span><span id="speaker_front_left"></span>**SPEAKER\_FRONT\_LEFT** (0x1)
</dt> <dt>

<span id="SPEAKER_FRONT_RIGHT"></span><span id="speaker_front_right"></span>**SPEAKER\_FRONT\_RIGHT** (0x2)
</dt> <dt>

<span id="SPEAKER_FRONT_CENTER"></span><span id="speaker_front_center"></span>**SPEAKER\_FRONT\_CENTER** (0x4)
</dt> <dt>

<span id="SPEAKER_LOW_FREQUENCY"></span><span id="speaker_low_frequency"></span>**SPEAKER\_LOW\_FREQUENCY** (0x8)
</dt> <dt>

<span id="SPEAKER_BACK_LEFT"></span><span id="speaker_back_left"></span>**SPEAKER\_BACK\_LEFT** (0x10)
</dt> <dt>

<span id="SPEAKER_BACK_RIGHT"></span><span id="speaker_back_right"></span>**SPEAKER\_BACK\_RIGHT** (0x20)
</dt> <dt>

<span id="SPEAKER_FRONT_LEFT_OF_CENTER"></span><span id="speaker_front_left_of_center"></span>**SPEAKER\_FRONT\_LEFT\_OF\_CENTER** (0x40)
</dt> <dt>

<span id="SPEAKER_FRONT_RIGHT_OF_CENTER"></span><span id="speaker_front_right_of_center"></span>**SPEAKER\_FRONT\_RIGHT\_OF\_CENTER** (0x80)
</dt> <dt>

<span id="SPEAKER_BACK_CENTER"></span><span id="speaker_back_center"></span>**SPEAKER\_BACK\_CENTER** (0x100)
</dt> <dt>

<span id="SPEAKER_SIDE_LEFT"></span><span id="speaker_side_left"></span>**SPEAKER\_SIDE\_LEFT** (0x200)
</dt> <dt>

<span id="SPEAKER_SIDE_RIGHT"></span><span id="speaker_side_right"></span>**SPEAKER\_SIDE\_RIGHT** (0x400)
</dt> <dt>

<span id="SPEAKER_TOP_CENTER"></span><span id="speaker_top_center"></span>**SPEAKER\_TOP\_CENTER** (0x800)
</dt> <dt>

<span id="SPEAKER_TOP_FRONT_LEFT"></span><span id="speaker_top_front_left"></span>**SPEAKER\_TOP\_FRONT\_LEFT** (0x1000)
</dt> <dt>

<span id="SPEAKER_TOP_FRONT_CENTER"></span><span id="speaker_top_front_center"></span>**SPEAKER\_TOP\_FRONT\_CENTER** (0x2000)
</dt> <dt>

<span id="SPEAKER_TOP_FRONT_RIGHT"></span><span id="speaker_top_front_right"></span>**SPEAKER\_TOP\_FRONT\_RIGHT** (0x4000)
</dt> <dt>

<span id="SPEAKER_TOP_BACK_LEFT"></span><span id="speaker_top_back_left"></span>**SPEAKER\_TOP\_BACK\_LEFT** (0x8000)
</dt> <dt>

<span id="SPEAKER_TOP_BACK_CENTER"></span><span id="speaker_top_back_center"></span>**SPEAKER\_TOP\_BACK\_CENTER** (0x10000)
</dt> <dt>

<span id="SPEAKER_TOP_BACK_RIGHT"></span><span id="speaker_top_back_right"></span>**SPEAKER\_TOP\_BACK\_RIGHT** (0x20000)
</dt> </dl>

## Remarks

This attribute corresponds to the **dwChannelMask** member of the [**WAVEFORMATEXTENSIBLE**](/windows/win32/api/mmreg/ns-mmreg-waveformatextensible) structure.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**IMFMediaType**](/windows/desktop/api/mfobjects/nn-mfobjects-imfmediatype)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 
