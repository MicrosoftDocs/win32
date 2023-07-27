---
description: The following table lists the globally unique identifiers (GUIDs) defined for Microsoft DirectX Media Object (DMO) categories. These GUIDs are defined in the header file Dmoreg.h and exported by the Dmoguids.lib library.
ms.assetid: d67debd0-8ecb-41ab-bc6c-b27cba97c65a
title: DMO GUIDs (Dmoreg.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# DMO GUIDs

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following table lists the globally unique identifiers (GUIDs) defined for Microsoft DirectX Media Object (DMO) categories. These GUIDs are defined in the header file Dmoreg.h and exported by the Dmoguids.lib library.

To enumerate the DMOs registered in a category, pass the corresponding GUID to the [**DMOEnum**](/previous-versions/windows/desktop/api/Dmoreg/nf-dmoreg-dmoenum) function.



| GUID                                                                                                                                                                                                                     | Description                     |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------|
| <span id="DMOCATEGORY_AUDIO_DECODER"></span><span id="dmocategory_audio_decoder"></span><dl> <dt>**DMOCATEGORY\_AUDIO\_DECODER**</dt> </dl>                       | Audio decoder<br/>        |
| <span id="DMOCATEGORY_AUDIO_EFFECT"></span><span id="dmocategory_audio_effect"></span><dl> <dt>**DMOCATEGORY\_AUDIO\_EFFECT**</dt> </dl>                          | Audio effect<br/>         |
| <span id="DMOCATEGORY_AUDIO_ENCODER"></span><span id="dmocategory_audio_encoder"></span><dl> <dt>**DMOCATEGORY\_AUDIO\_ENCODER**</dt> </dl>                       | Audio encoder<br/>        |
| <span id="DMOCATEGORY_VIDEO_DECODER"></span><span id="dmocategory_video_decoder"></span><dl> <dt>**DMOCATEGORY\_VIDEO\_DECODER**</dt> </dl>                       | Video decoder<br/>        |
| <span id="DMOCATEGORY_VIDEO_EFFECT"></span><span id="dmocategory_video_effect"></span><dl> <dt>**DMOCATEGORY\_VIDEO\_EFFECT**</dt> </dl>                          | Video effect<br/>         |
| <span id="DMOCATEGORY_VIDEO_ENCODER"></span><span id="dmocategory_video_encoder"></span><dl> <dt>**DMOCATEGORY\_VIDEO\_ENCODER**</dt> </dl>                       | Video encoder<br/>        |
| <span id="DMOCATEGORY_AUDIO_CAPTURE_EFFECT"></span><span id="dmocategory_audio_capture_effect"></span><dl> <dt>**DMOCATEGORY\_AUDIO\_CAPTURE\_EFFECT**</dt> </dl> | Audio capture effect<br/> |



## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dmoreg.h</dt> </dl> |



## See also

<dl> <dt>

[DMO Constants](dmo-constants.md)
</dt> </dl>

 

 




