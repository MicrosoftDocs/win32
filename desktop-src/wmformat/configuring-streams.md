---
title: Configuring Streams
description: Configuring Streams
ms.assetid: d119362f-e23c-4985-aff5-8c084106df30
keywords:
- Windows Media Format SDK,streams
- profiles,streams
- streams,configuring
- codecs,configuring streams
- profiles,IWMStreamConfig interface
- streams,IWMStreamConfig interface
- IWMStreamConfig
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Configuring Streams

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The only thing that is required in a profile is at least one stream. The other options provide access to more advanced features, but with the minimum of one stream you can make an ASF file. It is essential that you understand how to configure streams before creating complex profiles.

For the purpose of profiles, streams can be divided into two types: those that are compressed with Windows Media codecs and arbitrary streams that are not processed with any codecs. Audio streams and video streams are the types that use the Windows Media codecs. Of course, streams can contain audio or video compressed with a third-party codec, but the process of configuring such a stream is a special case. For more information, see [To Create ASF Files Using Third-Party Codecs](to-create-asf-files-using-third-party-codecs.md).

The following list summarizes the process of configuring a stream.

1.  Obtain a stream configuration object for the stream.
    -   If you are creating a stream using one of the Windows Media codecs, you must obtain the stream configuration object as a codec format using the methods of [**IWMCodecInfo3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmcodecinfo3).
    -   If the stream is an arbitrary type, get an empty stream configuration object using [**IWMProfile::CreateNewStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-createnewstream).
2.  Configure the stream to meet your needs.
    -   Streams of all types should be assigned a name, connection name, and stream number.
    -   Streams using Windows Media codecs should be altered only in predefined ways from the codec format. For audio streams, only variable bit rate (VBR) settings for two-pass VBR should be changed. Video streams need to be configured with the desired frame properties.
    -   Arbitrary streams have varying configuration requirements by type. All require a bit rate and buffer window.
3.  Add the stream to the profile by calling [**IWMProfile::AddStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-addstream).

All streams are defined using stream configuration objects. The main interface for a stream configuration object is [**IWMStreamConfig**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamconfig), which provides methods for setting the basic settings of a stream, such as the stream number, bit rate, and so on. **IWMStreamConfig** is inherited by the newer interfaces, [**IWMStreamConfig2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamconfig2) and [**IWMStreamConfig3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamconfig3). As with all numbered interface revisions, you should always retrieve the most recent version using the **QueryInterface** method.

Most settings in a stream are accessed through [**IWMMediaProps**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmmediaprops). These settings are encapsulated in a [**WM\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_media_type) structure. For audio and video, the **WM\_MEDIA\_TYPE** structure points to another structure with further information specific to the type of media. This secondary structure is typically [**WAVEFORMATEX**](/previous-versions/windows/desktop/legacy/dd757720(v=vs.85)) for audio and [**WMVIDEOINFOHEADER**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wmvideoinfoheader) for video. In addition, video streams have a tertiary structure, **BITMAPINFOHEADER**, which describes the characteristics of an individual frame of video. **BITMAPINFOHEADER** is a common structure and can be found in the Graphics Device Interface (GDI) section of the Platform SDK.

The following sections describe how to configure streams.



| Section                                                                                                          | Description                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Configuration Common to All Streams](configuration-common-to-all-streams.md)                                   | Describes the basic stream configuration common to all types of streams.                                                                                        |
| [Getting Stream Configuration Information from Codecs](getting-stream-configuration-information-from-codecs.md) | Describes how to get stream configuration information from the codecs to ensure proper configuration of streams using the Windows Media Audio and Video codecs. |
| [Configuring Audio Streams](configuring-audio-streams.md)                                                       | Describes how to configure audio streams.                                                                                                                       |
| [Configuring Video Streams](configuring-video-streams.md)                                                       | Describes how to configure video streams.                                                                                                                       |
| [Configuring Video Streams for Seeking Performance](configuring-video-streams-for-seeking-performance.md)       | Describes how to configure video streams for which efficient seeking is important.                                                                              |
| [Configuring Screen Capture Streams](configuring-screen-capture-streams.md)                                     | Describes how to configure video streams for screen capture.                                                                                                    |
| [Configuring Image Streams](configuring-image-streams.md)                                                       | Describes how to configure image streams.                                                                                                                       |
| [Using Uncompressed Audio and Video Streams](using-uncompressed-audio-and-video-streams.md)                     | Describes how to set up an uncompressed audio or video stream.                                                                                                  |
| [Configuring Arbitrary Stream Types](configuring-arbitrary-stream-types.md)                                     | Describes how to configure streams to use the predefined arbitrary stream types.                                                                                |
| [Configuring VBR Streams](configuring-vbr-streams.md)                                                           | Describes how to configure streams to use variable bit rate encoding (VBR).                                                                                     |
| [Configuring Data Unit Extensions](configuring-data-unit-extensions.md)                                         | Describes how to configure a stream so that data unit extensions can be attached when the file is written.                                                      |
| [Reusing Stream Configurations](reusing-stream-configurations.md)                                               | Describes the ways in which you can use stream configuration objects from existing profiles to make new profiles.                                               |



 

## Related topics

<dl> <dt>

[**Inputs, Streams and Outputs**](inputs-streams-and-outputs.md)
</dt> <dt>

[**Working with Profiles**](working-with-profiles.md)
</dt> </dl>

 

 