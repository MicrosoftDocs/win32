---
description: Specifies the current input format for the decoder.
ms.assetid: 8fddf8c3-268e-4706-9003-e4bfb03d5278
title: AVDecCommonInputFormat property (Codecapi.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AVDecCommonInputFormat property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Specifies the current input format for the decoder.

This property is read-only.

## Data type

**BSTR** (**VT\_BSTR**)

## Property GUID

**CODECAPI\_AVDecCommonInputFormat**

## Property value

The value of this property is a **BSTR** that contains the string representation of a GUID. The following GUIDs are defined.



| **GUID**                                            | Description                                    |
|-----------------------------------------------------|------------------------------------------------|
| **CODECAPI\_GUID\_AVDecAudioInputAAC**              | Advanced Audio Coding (AAC)                    |
| **CODECAPI\_GUID\_AVDecAudioInputDolbyDigitalPlus** | Dolby Digital Plus audio                       |
| **CODECAPI\_GUID\_AVDecAudioInputDolby**            | Dolby audio                                    |
| **CODECAPI\_GUID\_AVDecAudioInputDTS**              | DTS audio                                      |
| **CODECAPI\_GUID\_AVDecAudioInputHEAAC**            | High-Efficiency Advanced Audio Coding (HE-AAC) |
| **CODECAPI\_GUID\_AVDecAudioInputMPEG**             | MPEG audio                                     |
| **CODECAPI\_GUID\_AVDecAudioInputPCM**              | PCM audio                                      |
| **CODECAPI\_GUID\_AVDecAudioInputWMA**              | Windows Media Audio                            |
| **CODECAPI\_GUID\_AVDecAudioInputWMAPro**           | Windows Media Audio 9 Professional (WMA Pro)   |



 

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

 

 




