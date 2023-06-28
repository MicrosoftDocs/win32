---
description: Specifies which audio channel is mapped to channel N in the encoded audio stream.
ms.assetid: 996c97d6-e4c6-4189-89cb-912d28327453
title: AVEncAudioMapDestChannelN property (Codecapi.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AVEncAudioMapDestChannelN property

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Specifies which audio channel is mapped to channel *N* in the encoded audio stream.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**See Remarks.**

## Remarks

This reference topic describes a set of related properties. Each property maps an input channel to a specified output channel. The following properties are defined.



| Property GUID                            | Description             |
|------------------------------------------|-------------------------|
| **CODECAPI\_AVEncAudioMapDestChannel0**  | Destination channel 0.  |
| **CODECAPI\_AVEncAudioMapDestChannel1**  | Destination channel 1.  |
| **CODECAPI\_AVEncAudioMapDestChannel2**  | Destination channel 2.  |
| **CODECAPI\_AVEncAudioMapDestChannel3**  | Destination channel 3.  |
| **CODECAPI\_AVEncAudioMapDestChannel4**  | Destination channel 4.  |
| **CODECAPI\_AVEncAudioMapDestChannel5**  | Destination channel 5.  |
| **CODECAPI\_AVEncAudioMapDestChannel6**  | Destination channel 6.  |
| **CODECAPI\_AVEncAudioMapDestChannel7**  | Destination channel 7.  |
| **CODECAPI\_AVEncAudioMapDestChannel8**  | Destination channel 8.  |
| **CODECAPI\_AVEncAudioMapDestChannel9**  | Destination channel 9.  |
| **CODECAPI\_AVEncAudioMapDestChannel10** | Destination channel 10. |
| **CODECAPI\_AVEncAudioMapDestChannel11** | Destination channel 11. |
| **CODECAPI\_AVEncAudioMapDestChannel12** | Destination channel 12. |
| **CODECAPI\_AVEncAudioMapDestChannel13** | Destination channel 13. |
| **CODECAPI\_AVEncAudioMapDestChannel14** | Destination channel 14. |
| **CODECAPI\_AVEncAudioMapDestChannel15** | Destination channel 15. |



 

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

 

 




