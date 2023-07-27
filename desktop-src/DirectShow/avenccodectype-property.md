---
description: Specifies the encoding scheme.
ms.assetid: a26951d6-67fb-43fb-849f-331416e9d7c2
title: AVEncCodecType property (Codecapi.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AVEncCodecType property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Specifies the encoding scheme.

This property is read/write.

## Data type

**BSTR** (**VT\_BSTR**)

## Property GUID

**CODECAPI\_AVEncCodecType**

## Property value

The value of this property is a **BSTR** that contains the string representation of a GUID. The following GUIDs are defined.



| GUID                                      | Description                                        |
|-------------------------------------------|----------------------------------------------------|
| CODECAPI\_GUID\_AVEncDolbyDigitalConsumer | Dolby Digital Consumer audio                       |
| CODECAPI\_GUID\_AVEncDolbyDigitalPlus     | Dolby Digital Plus audio                           |
| CODECAPI\_GUID\_AVEncDolbyDigitalPro      | Dolby Digital Pro audio                            |
| CODECAPI\_GUID\_AVEncDTS                  | DTS audio                                          |
| CODECAPI\_GUID\_AVEncDTSHD                | DTS-HD audio                                       |
| CODECAPI\_GUID\_AVEncDV                   | DV video                                           |
| CODECAPI\_GUID\_AVEncH264Video            | H.264 video                                        |
| CODECAPI\_GUID\_AVEncMLP                  | Meridian Lossless Packing (MLP) audio              |
| CODECAPI\_GUID\_AVEncMPEG1Audio           | MPEG-1 audio                                       |
| CODECAPI\_GUID\_AVEncMPEG1Video           | MPEG-1 video                                       |
| CODECAPI\_GUID\_AVEncMPEG2Audio           | MPEG-2 audio                                       |
| CODECAPI\_GUID\_AVEncMPEG2Video           | MPEG-2 video                                       |
| CODECAPI\_GUID\_AVEncPCM                  | PCM audio                                          |
| CODECAPI\_GUID\_AVEncSDDS                 | Sony Dynamic Digital Sound (SDDS) audio            |
| CODECAPI\_GUID\_AVEncWMALossless          | Windows Media Audio 9 Lossless audio               |
| CODECAPI\_GUID\_AVEncWMAPro               | Windows Media Audio 9 Professional (WMA Pro) audio |
| CODECAPI\_GUID\_AVEncWMAVoice             | Windows Media Audio 9 Voice audio                  |
| CODECAPI\_GUID\_AVEncWMV                  | Windows Media Video                                |
| CODECAPI\_GUID\_AVEndMPEG4Video           | MPEG-4 video                                       |



 

## Remarks

Applications can set this property to specify which encoding scheme to use. Codecs can also return this property as a capability.

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

 

 




