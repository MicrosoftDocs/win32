---
title: Configuring Audio Streams
description: Configuring Audio Streams
ms.assetid: 6ddd9bc1-3fde-4098-afce-fdda461ced62
keywords:
- streams,configuring audio streams
- codecs,configuring audio streams
- audio streams,configuring
- codecs,formats
- streams,IWMCodecInfo interface
- IWMCodecInfo,audio streams
- streams,A/V synchronization
- audio streams,A/V synchronization
- A/V synchronization
- streams,synchronizing A/V
- audio streams,synchronizing A/V
- streams,low-delay audio formats
- audio streams,low-delay audio formats
- codecs,low-delay audio formats
- streams,variable bit rate (VBR)
- audio streams,variable bit rate (VBR)
- codecs,variable bit rate (VBR)
- variable bit rate (VBR),configuring
- VBR (variable bit rate),configuring
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Configuring Audio Streams

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Audio streams are generally the most straightforward to configure. Get a stream configuration from the codec using the methods of [**IWMCodecInfo**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmcodecinfo) as described in [Getting Stream Configuration Information from Codecs](getting-stream-configuration-information-from-codecs.md). Under most circumstances, you should not alter the settings from those retrieved.

The codec format that you select from those enumerated depends upon the intended use of the ASF files made with the profile. The codec format description retrieved by [**IWMCodecInfo2::GetCodecFormatDesc**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmcodecinfo2-getcodecformatdesc) summarizes the characteristics of the format. If your application does not display the descriptions to choose between them, you can call **QueryInterface** on the [**IWMStreamConfig**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamconfig) interface of the codec format to get the [**IWMMediaProps**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmmediaprops) interface. Then you can retrieve the [**WM\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_media_type) structure by calling [**IWMMediaProps::GetMediaType**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmmediaprops-getmediatype). By examining the **WM\_MEDIA\_TYPE** structure and the [**WAVEFORMATEX**](/previous-versions/windows/desktop/legacy/dd757720(v=vs.85)) structure it points to, you can determine the settings of the codec format and compare them to your requirements.

## Getting Audio Formats for A/V Synchronization

The Windows Media Audio codec and Windows Media Audio Professional codec both support formats for audio-only files and for audio/video files. The audio-only formats are optimized for files containing only audio data, while the audio/video formats are optimized for audio that is in a file with a video stream. When enumerating codec formats for these codecs, the audio/video formats come after the audio-only formats. The audio/video format descriptions all contain the string "(A/V)". You can identify the formats designed for audio/video synchronization programmatically by checking the number of packets per second. Formats for synchronization have 5 or more packets per second if the bit rate is greater than or equal to 32,000 bits per second. Formats with bit rates less than 32,000 bits per second can be used with synchronized video if they use 3 or more packets per second. The code example in the [To Find Audio Formats](to-find-audio-formats.md) topic contains the code required to make this check:


```C++
if((pWave->nAvgBytesPerSec / pWave->nBlockAlign) >= 
       ((pWave->nAvgBytesPerSec >= 4000) ? 5.0 : 3.0))
{
    // Set this stream configuration as the new best match.
}
```



## Getting Low-Delay Audio Formats

The Windows Media 9.1 codec and the Windows Media Audio 9.1 Professional codec both support low-delay formats. These formats have a smaller buffer window than other audio formats. Low-delay audio is intended to improve performance in scenarios where files or streams will be switched frequently; for example, an application that lists a number of songs for streaming in the user interface and allows users to arbitrarily switch between them.

Low-delay formats are available only in CBR mode (one-pass or two-pass). The low-delay format descriptions all contain the string "Low Delay". You can identify the formats programmatically by checking the bit-rate value of the format. The low-delay formats are assigned bit rates that are 1 kilobit less than the bit rates of the equivalent normal format. For example, the Windows Media Audio 9.1 codec supports a single-pass CBR format with a bit rate of 192 kbps. The equivalent low-delay format has a bit rate of 191 kbps. In addition, with the exception of the 5 kbps mono format supported by the Windows Media Audio 9.1 codec, the low-delay formats are the only formats that have an odd bit-rate value.

## Configuring Variable Bit Rate Audio

When you need a variable bit rate (VBR) format for one of the Windows Media audio codecs, you can get it by setting the enumeration settings in the [**IWMCodecInfo3::SetCodecEnumerationSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmcodecinfo3-setcodecenumerationsetting) method. Set g\_wszVBREnabled to True, and set g\_wszNumPasses to 1 for quality-based VBR or 2 for two-pass VBR (constrained or unconstrained). If you are using constrained two-pass VBR, you must manually set the maximum bit rate and buffer window for the stream using the methods of [**IWMPropertyVault**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmpropertyvault) as described in [Configuring VBR Streams](configuring-vbr-streams.md).

In quality-based VBR profiles, the **nAvgBytesPerSec** member of the **WAVEFORMATEX** structure contains the quality level (1 through 100) in the low-order byte and the three high-order bytes are set to 0x7fffff. Do not attempt to modify the quality setting by modifying this value manually; you must use the format as it is retrieved from the codec. To use a different quality value, you must enumerate formats until you find one that meets your needs. Also, **nAvgBytesPerSec** will not be preserved in the ASF file; when you obtain the **WAVEFORMATEX** structure for a file that has been opened with the reader object, **nAvgBytesPerSec** contains an approximate value representing the average number of bytes per second.

> [!Note]  
> When configuring audio streams, you should never have an audio buffer window value that is greater than the value for any video streams in the file. Normally this is not an issue, as audio buffer window values should range between 1.5 and 3 seconds and video values should range between 3 and 5 seconds. If an audio buffer window is greater than a video buffer window, the file will play back with the streams slightly out of synchronization.

 

## Related topics

<dl> <dt>

[**Configuration Common to All Streams**](configuration-common-to-all-streams.md)
</dt> <dt>

[**Configuring Streams**](configuring-streams.md)
</dt> <dt>

[**To Find Audio Formats**](to-find-audio-formats.md)
</dt> </dl>

 

 