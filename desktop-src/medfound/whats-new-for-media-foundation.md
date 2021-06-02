---
description: Microsoft Media Foundation was introduced in Windows Vista as the replacement for DirectShow. Of course, DirectShow is still supported in Windows 7, but developers are encouraged to use Media Foundation in their new digital media applications.
ms.assetid: c345c0d9-5325-4f73-b9ec-1673ad10e3e4
title: Whats New for Media Foundation
ms.topic: article
ms.date: 05/31/2018
---

# What's New for Media Foundation

Microsoft Media Foundation was introduced in Windows Vista as the replacement for DirectShow. Of course, DirectShow is still supported in Windows 7, but developers are encouraged to use Media Foundation in their new digital media applications.

The improvements to Media Foundation can be summarized as follows:

-   Better format support, including MPEG-4
-   Support for capture devices and hardware codecs
-   A simplified programming model
-   Improvements to the platform

## Better Format Support

The Media Foundation audio/video pipeline was implemented in Windows Vista, but it supported a limited set of formats and file containers, which meant that some applications needed to fall back on older technologies such as DirectShow. In Windows 7, Media Foundation includes the following new codecs, media sources, and media sinks:

-   AAC decoder
-   AAC encoder
-   AVI/WAVE file source
-   DV video decoder
-   H.264 video decoder
-   H.264 video encoder
-   MJPEG decoder
-   MP3 file sink\*
-   MP4/3GP file source
-   MP4/3GP file sink

> [!Note]  
> The MP3 file sink does not include an MP3 audio encoder.

 

For more information, see [Supported Media Formats in Media Foundation](supported-media-formats-in-media-foundation.md).

## Hardware Device Support

Media Foundation now supports the following types of hardware devices in the audio/video pipeline:

-   UVC 1.1 video capture devices, such as webcams
-   Audio capture devices
-   Hardware encoders and decoders
-   Hardware video processors, such as color-space converters

Hardware codecs can perform very fast video transcoding. For example, an application might transfer Windows Media Video (WMV) files to a cell phone that supports only 3GP files. Using a hardware encoder, the application can transcode the file in the backgound, just before transferring it to the device.

Hardware devices are represented in Media Foundation by a proxy object, and are used in the pipeline just like software-based components.

## Simplified Programming Model

In Windows Vista, Media Foundation exposed a relatively low-level set of APIs. These APIs are flexible, but too complex for simple tasks. Windows 7 adds new high-level APIs that make it simpler to write media applications in C++. These new high-level APIs include the following.



| API                                | Description                                                                                                                                                                                                                                                                                                    |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Source Reader](source-reader.md) | The source reader pulls raw or decoded data from a media file. For example, you can use the source reader to get thumbnail bitmaps from a video file, or to analyze the waveform data in an audio file. You can also use the source reader to get live data from an audio or video capture device. <br/> |
| [Sink Writer](sink-writer.md)     | The sink writer enables you to author media files by passing in uncompressed or encoded data. For example, you can use it to re-encode a video file, or to capture live video from a webcam to a file.                                                                                                         |
| [Transcode API](transcode-api.md) | This feature supports the most common audio/video encoding scenarios.<br/>                                                                                                                                                                                                                               |



 

You can still use the low-level APIs in Media Foundation. You might do so if you need more control over the audio/video pipeline.

## Platform Improvements

Windows 7 includes numerous enhancements to the underlying Media Foundation platform APIs. Advanced applications can use these APIs directly; other applications will get the benefits indirectly. The improvements include:

-   Changes in the video pipeline to reduce power consumption and video memory usage.
-   [DXVA-HD](dxva-hd.md): Microsoft DirectX Video Acceleration High Definition (DXVA-HD) is a new API for hardware-accelerated video processing. DXVA-HD offers a more flexible compositing model than the previous DXVA video processing API, and is better suited for high-definition video formats..
-   A new mechanism for enumerating sources and decoders, which includes merit values and a preferred/blocked list. This feature improves the overall reliability of the system. For more information, see the following topics:
    -   [**MFTEnumEx**](/windows/desktop/api/mfapi/nf-mfapi-mftenumex)
    -   [**IMFPluginControl**](/windows/desktop/api/mfobjects/nn-mfobjects-imfplugincontrol)
    -   [Codec Merit](codec-merit.md)

## SDK Changes

-   New headers and library files: [Media Foundation Headers and Libraries](media-foundation-headers-and-libraries.md)
-   DLL and .lib changes: [Library Changes in Windows 7](media-foundation-headers-and-libraries.md)
-   New SDK Samples:
    -   [Audio Clip Sample](audio-clip-sample.md)
    -   [DXVA-HD Sample](dxva-hd-sample.md)
    -   [MFCaptureD3D Sample](mfcaptured3d-sample.md)
    -   [MFCaptureToFile Sample](mfcapturetofile-sample.md)
    -   [Transcode Sample](transcode-sample.md)
    -   [VideoThumbnail Sample](videothumbnail-sample.md)
-   Improvements to [TopoEdit](topoedit.md):
    -   Support for transcoding. See Building a [Transcode Topology with TopoEdit](building-a-transcode-topology-with-topoedit.md).
    -   Support for audio and video capture. See [Topology Menu](topology-menu.md).

## New in Windows 8

Some of the new updates to Media Foundation with Windows 8 are:

-   The [**IMFCaptureEngine**](/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcaptureengine) controls one or more capture devices. See the [Capture Engine Attributes](capture-engine-attributes.md) for a list of attributes. Other new media capture related interfaces are [**IMFCapturePhotoSink**](/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcapturephotosink), [**IMFCapturePreviewSink**](/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcapturepreviewsink), [**IMFCaptureRecordSink**](/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcapturerecordsink), [**IMFCaptureSink**](/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcapturesink), and [**IMFCaptureSource**](/windows/desktop/api/mfcaptureengine/nn-mfcaptureengine-imfcapturesource).
-   The following Media Foundation class extensions are new for Windows 8:
    -   [**IMFMediaEngineEx**](/windows/desktop/api/mfmediaengine/nn-mfmediaengine-imfmediaengineex)
    -   [**IMFMediaSourceEx**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasourceex)
    -   [**IMFRealTimeClientEx**](/windows/desktop/api/mfidl/nn-mfidl-imfrealtimeclientex)
    -   [**IMFSinkWriterEx**](/windows/desktop/api/mfreadwrite/nn-mfreadwrite-imfsinkwriterex)
    -   [**IMFSourceReaderEx**](/windows/desktop/api/mfreadwrite/nn-mfreadwrite-imfsourcereaderex)
    -   [**IMFVideoSampleAllocatorEx**](/windows/desktop/api/mfidl/nn-mfidl-imfvideosampleallocatorex)
    -   [**IMFWorkQueueServicesEx**](/windows/desktop/api/mfidl/nn-mfidl-imfworkqueueservicesex)
-   [Direct3D 11 Video API](direct3d-11-video-apis.md) are new for Windows 8. Windows 8 Desktop apps can still use [Direct3D 9 Video API](direct3d-video-apis.md), but Windows Store apps must use the new Direct3D 11 Video API. For info more info on Microsoft Direct3D 11 Video see [Supporting Direct3D 11 Video Decoding in Media Foundation](supporting-direct3d-11-video-decoding-in-media-foundation.md).
-   There have been updates and improvements to Media Foundation work queues. See [Work Queue and Threading Improvements](media-foundation-work-queue-and-threading-improvements.md) for more info.
-   [H.264 UVC 1.5 camera encoders](camera-encoder-h264-uvc-1-5.md).
-   For a list of the Media Foundation API which can be used with Windows Store apps see [Win32 and COM for Windows Store apps (multimedia)](media-foundation-headers-and-libraries.md).
-   Media Foundation is not included with the N and KN editions of Windows 8. For more information, see [Microsoft Windows Media Feature Pack for N and KN Versions of all Windows 8 Editions](https://support.microsoft.com/kb/2703761).

## Related topics

<dl> <dt>

[About Media Foundation](about-the-media-foundation-sdk.md)
</dt> <dt>

[Microsoft Media Foundation](microsoft-media-foundation-sdk.md)
</dt> </dl>

 

 




