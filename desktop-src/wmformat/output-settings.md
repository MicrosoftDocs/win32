---
title: Output Settings
description: Output Settings
ms.assetid: effe6c07-e6df-45b0-b865-2a025c466d6f
keywords:
- Windows Media Format SDK,global constants
- Advanced Systems Format (ASF),global constants
- ASF (Advanced Systems Format),global constants
- global constants,list of
- Windows Media Format SDK,constants
- Advanced Systems Format (ASF),constants
- ASF (Advanced Systems Format),constants
- constants,list of
- Windows Media Format SDK,output settings
- Advanced Systems Format (ASF),output settings
- ASF (Advanced Systems Format),output settings
- output settings
- synchronous readers,output settings
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Output Settings

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following global constants are used to identify output settings for the reader and synchronous reader object.



| Global constant                | WMT\_ATTR\_DATATYPE  | Description of *pValue*                                                                                                                                                                                                                                                                                                    |
|--------------------------------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| g\_wszAllowInterlacedOutput    | **WMT\_TYPE\_BOOL**  | If True, the reader will deliver interlaced frames, if supported by the output.                                                                                                                                                                                                                                            |
| g\_wszDedicatedDeliveryThread  | **WMT\_TYPE\_BOOL**  | If True, this output will have a dedicated thread created for delivery of its samples. Not supported on the synchronous reader.                                                                                                                                                                                            |
| g\_wszDeliverOnReceive         | **WMT\_TYPE\_BOOL**  | If True, samples for this output will be delivered as soon as they are available from the reader. This can result in samples from this output being delivered out of order and before corresponding samples from other outputs.                                                                                            |
| g\_wszDynamicRangeControl      | **WMT\_TYPE\_DWORD** | Specifies the level of dynamic range control to use for the output. Set to a value from 0 to 2, where 0 indicates no dynamic range control (the default), and 2 is the maximum level of dynamic range control (the smallest dynamic range).                                                                                |
| g\_wszEarlyDataDelivery        | **WMT\_TYPE\_DWORD** | Time, in milliseconds, which specifies how much earlier to deliver the samples. If greater than zero, the samples from this output will be retrieved and decoded so that the samples are delivered earlier than the samples for other outputs. Normally the reader delivers samples in order of presentation time.         |
| g\_wszEnableDiscreteOutput     | **WMT\_TYPE\_BOOL**  | If True, the reader will enable high-definition, multichannel audio output. This setting is only valid for audio streams encoded with the Windows Media Audio 9 Professional codec. If this setting is set to true, you must also specify the speaker configuration of the client computer by setting g\_wszSpeakerConfig. |
| g\_wszEnableFrameInterpolation | **WMT\_TYPE\_BOOL**  | If True, the codec will deliver the video stream at a higher [*frame rate*](wmformat-glossary.md), interpolating the frames algorithmically.                                                                                                                                                          |
| g\_wszJustInTimeDecode         | **WMT\_TYPE\_BOOL**  | If True, the data must be decoded as late as possible. Not supported in the synchronous reader.                                                                                                                                                                                                                            |
| g\_wszNeedsPreviousSample      | **WMT\_TYPE\_BOOL**  | If true, the sample requires the previous sample to be decompressed. This setting only applies to delta frames in compressed video and is read only.                                                                                                                                                                       |
| g\_wszScrambledAudio           | **WMT\_TYPE\_BOOL**  | If True, this output will use the scrambled audio error concealment scheme. This is a valid setting for audio outputs only.                                                                                                                                                                                                |
| g\_wszSingleOutputBuffer       | **WMT\_TYPE\_BOOL**  | If True, a single output buffer must be used (for example, a DirectDraw® video buffer). Not supported in the synchronous reader.                                                                                                                                                                                           |
| g\_wszSoftwareScaling          | **WMT\_TYPE\_BOOL**  | If False, video is not scaled. (There must be no change to the resolution.)                                                                                                                                                                                                                                                |
| g\_wszSpeakerConfig            | **WMT\_TYPE\_DWORD** | If multichannel audio decoding is enabled by setting g\_wszEnableDiscreteOutput, this setting specifies the speaker configuration of the client computer. Set to one of the DirectSound speaker configuration constants.                                                                                                   |
| g\_wszStreamLanguage           | **WMT\_TYPE\_WORD**  | The index in the language list of the language to be delivered for this output. Used for outputs representing streams mutually exclusive by language.                                                                                                                                                                      |
| g\_wszVideoSampleDurations     | **WMT\_TYPE\_BOOL**  | If True, the reader will deliver accurate sample durations.                                                                                                                                                                                                                                                                |
| g\_wszEnableWMAProSPDIFOutput  | **WMT\_TYPE\_BOOL**  | If True, the reader will include the Sony/Phillips Digital Interface format (S/PDIF) in the enumerated output types.                                                                                                                                                                                                       |



 

## Related topics

<dl> <dt>

[**IWMReaderAdvanced2::GetOutputSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-getoutputsetting)
</dt> <dt>

[**IWMReaderAdvanced2::SetOutputSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-setoutputsetting)
</dt> <dt>

[**IWMSyncReader::GetOutputSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-getoutputsetting)
</dt> <dt>

[**IWMSyncReader::SetOutputSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-setoutputsetting)
</dt> </dl>

 

 




