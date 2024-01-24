---
description: Specifies the speaker configuration on the client computer.
ms.assetid: a0353e70-0741-4705-95e0-e76ebd8ba977
title: MFPKEY_WMADEC_SPKRCFG Property (Wmcodecdsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_WMADEC\_SPKRCFG Property

Specifies the speaker configuration on the client computer.

## Constant for IPropertyBag

g\_wszWMACSpeakerConfig

## Data Type

**VT\_UI4**

## Default Value

No specific speaker configuration is assumed.

## Remarks

You should set this value to one of the constants or values in the following table. The constants are defined in Microsoft DirectSound, and are listed here for convenience. To resolve these constant names for your compiler, you must include dsound.h.



| Constant             | Value      | Description                                                                  |
|----------------------|------------|------------------------------------------------------------------------------|
| DSSPEAKER\_DIRECTOUT | 0x00000000 | The audio is passed through directly, without being configured for speakers. |
| DSSPEAKER\_HEADPHONE | 0x00000001 | The client computer is equipped with headphones.                             |
| DSSPEAKER\_MONO      | 0x00000002 | The client computer is equipped with a monoaural speaker.                    |
| DSSPEAKER\_QUAD      | 0x00000003 | The client computer is equipped with quadraphonic speakers.                  |
| DSSPEAKER\_STEREO    | 0x00000004 | The client computer is equipped with stereo speakers.                        |
| DSSPEAKER\_SURROUND  | 0x00000005 | The client computer is equipped with four-channel surround-sound speakers.   |
| DSSPEAKER\_5POINT1   | 0x00000006 | The client computer is equipped with five speakers and a subwoofer.          |
| DSSPEAKER\_7POINT1   | 0x00000007 | The client computer is equipped with seven speakers and a subwoofer.         |



 

The value set for this property determines the output formats enumerated by the codec for multichannel audio.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




