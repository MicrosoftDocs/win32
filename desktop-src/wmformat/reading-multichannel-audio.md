---
title: Reading Multichannel Audio
description: Reading Multichannel Audio
ms.assetid: 9d577c5c-7275-493e-8a77-318c264b59b3
keywords:
- Windows Media Format SDK,reading multichannel audio
- Advanced Systems Format (ASF),reading multichannel audio
- ASF (Advanced Systems Format),reading multichannel audio
- Advanced Systems Format (ASF),multichannel audio
- ASF (Advanced Systems Format),multichannel audio
- codecs,reading multichannel audio
- multichannel audio,reading
ms.topic: article
ms.date: 05/31/2018
---

# Reading Multichannel Audio

The Windows Media Audio 9 Professional codec can encode multichannel audio (more than two channels). When reading a file with multichannel audio, you must configure the output properly or the audio will be delivered at a lower quality and in stereo. To set an output for multichannel audio delivery, you must set two output settings: g\_wszEnableDiscreteOutput and g\_wszSpeakerConfig.

Setting g\_wszEnableDiscreteOutput to **TRUE** sets the codec to deliver high-definition audio output. High-definition audio is encoded by the Windows Media Audio 9 codec with 24-bit samples in stereo or multiple channels. If this setting is **FALSE**, only 16-bit stereo output will be delivered.

The number of speakers on the playing computer is set with g\_wszSpeakerConfig. This setting is a **DWORD** value set to one of the DirectSound speaker constants listed in the following table. To resolve these constant names for your compiler, you must include dsound.h.



| Constant             | Value      | Description                                                                  |
|----------------------|------------|------------------------------------------------------------------------------|
| DSSPEAKER\_DIRECTOUT | 0x00000000 | The audio is passed through directly, without being configured for speakers. |
| DSSPEAKER\_HEADPHONE | 0x00000001 | The client computer is equipped with headphones.                             |
| DSSPEAKER\_MONO      | 0x00000002 | The client computer is equipped with a monaural speaker.                     |
| DSSPEAKER\_QUAD      | 0x00000003 | The client computer is equipped with quadraphonic speakers.                  |
| DSSPEAKER\_STEREO    | 0x00000004 | The client computer is equipped with stereo speakers.                        |
| DSSPEAKER\_SURROUND  | 0x00000005 | The client computer is equipped with four-channel surround-sound speakers.   |
| DSSPEAKER\_5POINT1   | 0x00000006 | The client computer is equipped with five speakers and a subwoofer.          |
| DSSPEAKER\_7POINT1   | 0x00000007 | The client computer is equipped with seven speakers and a subwoofer.         |



 

To set these settings, use [**IWMReaderAdvanced2::SetOutputSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-setoutputsetting).

Finally, for the channels to be output discretely, with no fold-down to stereo, you must set the correct media type on the output by following these steps:

1.  Call [**IWMReader::GetOutputFormatCount**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmreader-getoutputformatcount) to get the number of supported formats for the relevant audio output. Output format indexes are zero-based.
2.  For each supported format, call [**IWMReader::GetOutputFormat**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-getoutputformat) to retrieve the [**IWMOutputMediaProps**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmoutputmediaprops) interface on the output media properties object.
3.  Call [**IWMMediaProps::GetMediaType**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmmediaprops-getmediatype) to retrieve the media type.
4.  If the retrieved media type is the desired multichannel type, then set it by calling [**IWMReader::SetOutputProps**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-setoutputprops).

After you have set discrete output and the speaker configuration, the output formats enumerated by the reader should include multichannel formats that use the [**WAVEFORMATEXTENSIBLE**](/previous-versions/windows/desktop/legacy/dd757721(v=vs.85)) structure. If you enumerate the output formats before setting the properties, only formats with 1 or 2 channels and a maximum of 16 bits per channel will be included. As with other audio formats, you should use only the formats enumerated by the reader; do not configure your own.

> [!Note]  
> You can output multichannel audio only if your application is running on Microsoft Windows XP or a later version of Microsoft Windows.

 

## Related topics

<dl> <dt>

[**Inputs, Streams and Outputs**](inputs-streams-and-outputs.md)
</dt> <dt>

[**Reading ASF Files**](reading-asf-files.md)
</dt> <dt>

[**Output Settings**](output-settings.md)
</dt> <dt>

[**Working with High-Resolution PCM Audio**](working-with-high-resolution-pcm-audio.md)
</dt> </dl>

 

 