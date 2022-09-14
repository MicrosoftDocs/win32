---
title: Configuring Video Streams
description: Configuring Video Streams
ms.assetid: caffdfc1-3c35-4b7b-8643-5a9095cc11f6
keywords:
- streams,configuring video streams
- codecs,configuring video streams
- video streams,configuring
ms.topic: article
ms.date: 05/31/2018
---

# Configuring Video Streams

Video streams are more flexible in their configuration than audio streams. This is because the properties of the frames that make up the video can vary widely from one file to the next. When you retrieve the codec format for the codec you are using, you must set the following values for video stream configuration objects.



| Value                                 | Description                                                                                                                                                                                                                                                                 |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bit rate                              | Call [**IWMStreamConfig::SetBitrate**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstreamconfig-setbitrate) to set to the desired value. The video codec will try to compress the media to meet your specifications. If your values are too low, the resulting compressed video will be very degraded.           |
| Buffer window                         | Call [**IWMStreamConfig::SetBufferWindow**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstreamconfig-setbufferwindow) to set to the desired value. The video codec will try to compress the media to meet your specifications. If your values are too low, the resulting compressed video will be very degraded. |
| **WMVIDEOINFOHEADER.rcSource**        | The upper left corner must be set to 0,0. The lower right corner must be set to the frame dimensions. For example, in a 640x480 stream, these settings would be 0,0,640,480.                                                                                                |
| **WMVIDEOINFOHEADER.rcTarget**        | Must match **rcSource**.                                                                                                                                                                                                                                                    |
| **WMVIDEOINFOHEADER.dwBitRate**       | Must match the bit rate set for the stream.                                                                                                                                                                                                                                 |
| **WMVIDEOINFOHEADER.AvgTimePerFrame** | Set to the approximate time per frame.                                                                                                                                                                                                                                      |
| **BITMAPINFOHEADER.biWidth**          | Set to the width, in pixels, of the desired frame size.                                                                                                                                                                                                                     |
| **BITMAPINFOHEADER.biHeight**         | Set to the height, in pixels, of the desired frame size.                                                                                                                                                                                                                    |



 

Video content does not play correctly unless it is encoded to a size that is a multiple of four for both width and height. The exception is [*RGB*](wmformat-glossary.md) uncompressed video, which can be any size. If you try to set a size that is not a multiple of four, one of the following errors will be returned by the writer:

-   NS\_E\_INVALID\_INPUT\_FORMAT
-   NS\_E\_INVALID\_OUTPUT\_FORMAT
-   NS\_E\_INVALIDPROFILE

If you are using variable bit rate encoding, you may need to make other adjustments. For more information, see [Configuring VBR Streams](configuring-vbr-streams.md).

Some Windows Media Video codecs support multiple complexity levels. Complexity levels determine the algorithms that the codec will use when encoding a video stream. Using a high complexity level will require more processing power for encoding and decoding.

Each codec that supports complexity settings exposes the following settings that you can retrieve with the [**IWMCodecInfo3::GetCodecProp**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmcodecinfo3-getcodecprop) method.



| Setting                 | Description                                         |
|-------------------------|-----------------------------------------------------|
| g\_wszComplexityMax     | The maximum quality level supported by the codec.   |
| g\_wszComplexityOffline | The suggested quality level for offline playback.   |
| g\_wszComplexityLive    | The suggested quality level for streaming playback. |



 

To set the complexity for a video stream in a profile, use the [**IWMPropertyVault::SetProperty**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmpropertyvault-setproperty) method using the property g\_wszComplexity. The value you set must be less than or equal to the maximum supported complexity for the codec.

## Related topics

<dl> <dt>

[**Configuration Common to All Streams**](configuration-common-to-all-streams.md)
</dt> <dt>

[**Configuring Streams**](configuring-streams.md)
</dt> <dt>

[**Video Complexity Settings**](video-complexity-settings.md)
</dt> </dl>

 

 




