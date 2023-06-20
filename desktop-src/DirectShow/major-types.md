---
description: The following table describes the major media types.
ms.assetid: 718a07f6-e2e4-4670-b9cf-982b53abffd2
title: Major Types (Dshow.h)
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Major Types

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following table describes the major media types.



| GUID                                                                                                                                                                                                                                  | Description                                                                                               |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------|
| <span id="MEDIATYPE_AnalogAudio"></span><span id="mediatype_analogaudio"></span><span id="MEDIATYPE_ANALOGAUDIO"></span><dl> <dt>**MEDIATYPE\_AnalogAudio**</dt> </dl>         | Analog audio.<br/>                                                                                  |
| <span id="MEDIATYPE_AnalogVideo"></span><span id="mediatype_analogvideo"></span><span id="MEDIATYPE_ANALOGVIDEO"></span><dl> <dt>**MEDIATYPE\_AnalogVideo**</dt> </dl>         | Analog video.<br/>                                                                                  |
| <span id="MEDIATYPE_Audio"></span><span id="mediatype_audio"></span><span id="MEDIATYPE_AUDIO"></span><dl> <dt>**MEDIATYPE\_Audio**</dt> </dl>                                 | Audio. See [Audio Subtypes](audio-subtypes.md).<br/>                                               |
| <span id="MEDIATYPE_AUXLine21Data"></span><span id="mediatype_auxline21data"></span><span id="MEDIATYPE_AUXLINE21DATA"></span><dl> <dt>**MEDIATYPE\_AUXLine21Data**</dt> </dl> | Line 21 data. Used by closed captions. See [**Line 21 Media Types**](line-21-media-types.md).<br/> |
| <span id="MEDIATYPE_File"></span><span id="mediatype_file"></span><span id="MEDIATYPE_FILE"></span><dl> <dt>**MEDIATYPE\_File**</dt> </dl>                                     | File. (Obsolete)<br/>                                                                               |
| <span id="MEDIATYPE_Interleaved"></span><span id="mediatype_interleaved"></span><span id="MEDIATYPE_INTERLEAVED"></span><dl> <dt>**MEDIATYPE\_Interleaved**</dt> </dl>         | Interleaved audio and video. Used for Digital Video (DV).<br/>                                      |
| <span id="MEDIATYPE_LMRT"></span><span id="mediatype_lmrt"></span><dl> <dt>**MEDIATYPE\_LMRT**</dt> </dl>                                                                      | Obsolete. Do not use.<br/>                                                                          |
| <span id="MEDIATYPE_Midi"></span><span id="mediatype_midi"></span><span id="MEDIATYPE_MIDI"></span><dl> <dt>**MEDIATYPE\_Midi**</dt> </dl>                                     | MIDI format.<br/>                                                                                   |
| <span id="MEDIATYPE_MPEG2_PES"></span><span id="mediatype_mpeg2_pes"></span><dl> <dt>**MEDIATYPE\_MPEG2\_PES**</dt> </dl>                                                      | MPEG-2 PES packets. See [MPEG-2 Media Types](mpeg-2-media-types.md).<br/>                          |
| <span id="MEDIATYPE_MPEG2_SECTIONS"></span><span id="mediatype_mpeg2_sections"></span><dl> <dt>**MEDIATYPE\_MPEG2\_SECTIONS**</dt> </dl>                                       | MPEG-2 section data. See [MPEG-2 Media Types](mpeg-2-media-types.md).<br/>                         |
| <span id="MEDIATYPE_ScriptCommand"></span><span id="mediatype_scriptcommand"></span><span id="MEDIATYPE_SCRIPTCOMMAND"></span><dl> <dt>**MEDIATYPE\_ScriptCommand**</dt> </dl> | Data is a script command, used by closed captions.<br/>                                             |
| <span id="MEDIATYPE_Stream"></span><span id="mediatype_stream"></span><span id="MEDIATYPE_STREAM"></span><dl> <dt>**MEDIATYPE\_Stream**</dt> </dl>                             | Byte stream with no time stamps. See [**Stream Subtypes**](stream-subtypes.md).<br/>               |
| <span id="MEDIATYPE_Text"></span><span id="mediatype_text"></span><span id="MEDIATYPE_TEXT"></span><dl> <dt>**MEDIATYPE\_Text**</dt> </dl>                                     | Text.<br/>                                                                                          |
| <span id="MEDIATYPE_Timecode"></span><span id="mediatype_timecode"></span><span id="MEDIATYPE_TIMECODE"></span><dl> <dt>**MEDIATYPE\_Timecode**</dt> </dl>                     | Timecode data. Note: DirectShow does not provide any filters that support this media type.<br/>     |
| <span id="MEDIATYPE_URL_STREAM"></span><span id="mediatype_url_stream"></span><dl> <dt>**MEDIATYPE\_URL\_STREAM**</dt> </dl>                                                   | Obsolete. Do not use.<br/>                                                                          |
| <span id="MEDIATYPE_VBI"></span><span id="mediatype_vbi"></span><dl> <dt>**MEDIATYPE\_VBI**</dt> </dl>                                                                         | Vertical blanking interval (VBI) data (for television). Same as KSDATAFORMAT\_TYPE\_VBI.<br/>       |
| <span id="MEDIATYPE_Video"></span><span id="mediatype_video"></span><span id="MEDIATYPE_VIDEO"></span><dl> <dt>**MEDIATYPE\_Video**</dt> </dl>                                 | Video. See [Video Subtypes](video-subtypes.md).<br/>                                               |



## Remarks

The subtype GUID further defines the format. For some formats, the subtype GUID might be MEDIASUBTYPE\_None, which means the format does not require a subtype.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Dshow.h</dt> </dl> |



## See also

<dl> <dt>

[Media Types](media-types.md)
</dt> </dl>

 

 




