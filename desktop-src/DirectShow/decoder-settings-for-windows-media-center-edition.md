---
description: Decoder Settings for Windows Media Center Edition
ms.assetid: 019b063f-f215-44d8-a916-3125bee6af93
title: Decoder Settings for Windows Media Center Edition
ms.topic: article
ms.date: 05/31/2018
---

# Decoder Settings for Windows Media Center Edition

Windows XP Media Center Edition 2005 and later uses the [**ICodecAPI**](/windows/desktop/api/Strmif/nn-strmif-icodecapi) interface to configure the audio decoder filter for television and DVD playback. The following properties are supported.



| Property GUID                   | Description                                      |
|---------------------------------|--------------------------------------------------|
| CODECAPI\_AUDIO\_OUTPUT\_FORMAT | Configures the audio output format. See Remarks. |



 

## Remarks

The value of the CODECAPI\_AUDIO\_OUTPUT\_FORMAT property is a string representation of a GUID, stored as a **BSTR** value. The following GUIDs are defined.



| GUID                                                        | Description                                                                                                                                                                                                    |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CODECAPI\_AUDIO\_OUTPUT\_FORMAT\_PCM\_STEREO\_MATRIXENCODED | The software audio filter should perform software decoding and output a stereo audio stream, with the multichannel audio matrix encoded to the two channels.                                                   |
| CODECAPI\_AUDIO\_OUTPUT\_FORMAT\_PCM\_STEREO                | The software audio filter should perform software decoding and output a stereo audio stream.                                                                                                                   |
| CODECAPI\_AUDIO\_OUTPUT\_FORMAT\_SPDIF\_PCM                 | The software audio filter should perform software audio decoding, even though the physical output from the PC may be a digital interface, such as S/PDIF.                                                      |
| CODECAPI\_AUDIO\_OUTPUT\_FORMAT\_SPDIF\_BITSTREAM           | The software audio filter should not perform software audio decoding, but should pass the raw digital audio bitstream for external processing by a device connected with a digital audio link, such as S/PDIF. |
| CODECAPI\_AUDIO\_OUTPUT\_FORMAT\_PCM\_HEADPHONES            | The software audio filter should perform software audio decoding and should apply proprietary processing to optimize for headphones. Support for this setting is optional.                                     |



 

> [!Note]  
> The **ICodecAPI** interface stores codec properties as key/value pairs, where the key is a GUID and the value is a **VARIANT** type.

 

## Related topics

<dl> <dt>

[Encoder and Decoder Development](encoder-and-decoder-development.md)
</dt> </dl>

 

 



