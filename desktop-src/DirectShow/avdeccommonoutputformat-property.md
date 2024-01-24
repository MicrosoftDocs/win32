---
description: Specifies the output format for the decoder.
ms.assetid: fdccdbfa-2814-4d21-9a7f-4121b79718e6
title: AVDecCommonOutputFormat property (Codecapi.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AVDecCommonOutputFormat property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Specifies the output format for the decoder.

This property is read/write.

## Data type

**BSTR** (**VT\_BSTR**)

## Property GUID

**CODECAPI\_AVDecCommonOutputFormat**

## Property value



| GUID                                                               | Description                                                                                                                                                                                                         |
|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CODECAPI\_GUID\_AVDecAudioOutputFormat\_PCM                        | PCM audio, using any number of channels                                                                                                                                                                             |
| CODECAPI\_GUID\_AVDecAudioOutputFormat\_PCM\_Headphones            | Stereo PCM audio, using left-only/right-only (Lo/Ro) downmix                                                                                                                                                        |
| CODECAPI\_GUID\_AVDecAudioOutputFormat\_PCM\_Stereo\_Auto          | Stereo PCM audio, using automatic selection of the stereo downmix mode (Lo/Ro or Lt/Rt). You can use this value for audio formats in which the input stream defines the preferred downmix mode, such as Dolby AC-3. |
| CODECAPI\_GUID\_AVDecAudioOutputFormat\_PCM\_Stereo\_MatrixEncoded | Stereo PCM audio, using matrix-encoded stereo downmix (Lt/Rt)                                                                                                                                                       |
| CODECAPI\_GUID\_AVDecAudioOutputFormat\_SPDIF\_Bitstream           | S/PDIF (Sony/Philips Digital Interface Format) compressed bitstream, as defined by IEC-60958                                                                                                                        |
| CODECAPI\_GUID\_AVDecAudioOutputFormat\_SPDIF\_PCM                 | S/PDIF PCM stereo, as defined by IEC-60958                                                                                                                                                                          |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Codec API Properties](codec-api-properties.md)
</dt> <dt>

[**ICodecAPI Interface**](/windows/desktop/api/Strmif/nn-strmif-icodecapi)
</dt> </dl>

 

 




