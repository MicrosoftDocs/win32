---
title: Media Platform
description: Media Foundation and DirectShow provide the basis for media support in Windows.
ms.assetid: 020f009c-7432-432b-a39b-9295dd784d2e
ms.topic: article
ms.date: 05/31/2018
---

# Media Platform

[Media Foundation](/windows/desktop/medfound/microsoft-media-foundation-sdk) and [DirectShow](/windows/desktop/DirectShow/directshow) provide the basis for media support in Windows. Media Foundation was introduced in Windows Vista as the replacement for DirectShow. In Windows 7, Media Foundation has been enhanced to provide better format support, including *MPEG-4*, as well as support for video capture devices and hardware codecs.

## Format Support

In Windows 7, [Media Foundation](/windows/desktop/medfound/microsoft-media-foundation-sdk) provides extensive format support that includes codecs for *H.264* video, *MJPEG*, and *MP3*; new sources for *MP4*, *3GP*, *AAC* audio, and *AVI*; and new file sinks for *MP4*, *3GP*, and *MP3*. (See [Supported Media Formats in Media Foundation](../medfound/supported-media-formats-in-media-foundation.md).)

## Hardware Devices

[Media Foundation](/windows/desktop/medfound/microsoft-media-foundation-sdk) now supports the following types of hardware devices in the audio/video pipeline:

-   *UVC 1.1* video capture devices, such as webcams
-   Audio capture devices
-   Hardware encoders and decoders
-   Hardware video processors, such as color-space converters

Hardware codecs can perform very fast video transcoding. For example, suppose you want to transfer a *Windows Media Video (WMV)* file to a cell phone that supports only *3GP* files. With a hardware encoder, the file can be transcoded "as needed," immediately before transferring it to the device.

Hardware devices are represented in [Media Foundation](/windows/desktop/medfound/microsoft-media-foundation-sdk) by a proxy object, and are used in the pipeline just like software-based components. (See [What's New for Media Foundation](../medfound/whats-new-for-media-foundation.md).)

## Simplified Programming Model

In Windows Vista, [Media Foundation](/windows/desktop/medfound/microsoft-media-foundation-sdk) exposed a relatively low-level set of APIs. These APIs are flexible, but may not be appropriate for performing tasks. Windows 7 adds new high-level APIs that make it simpler to write media applications in *C++*. These new high-level APIs include:

-   **MFPlay**. These APIs are designed for audio and video playback. They support the typical playback operations (stop, pause, play, seek, rate control, audio volume, and so forth), while hiding the details of the low-level APIs (the session and topology layers).
-   **Source Reader**. You can use these APIs to pull raw or decoded data from a media file, without knowing anything about the underlying format. For example, you can get a thumbnail bitmap from a video file or get live video frames from a webcam.
-   **Sink Writer**. You can use these APIs to author media files by passing in uncompressed or encoded data. For example, you can re-encode or remix a video file.
-   **Transcode**. These APIs target the most common audio and video encoding scenarios.

## Platform Improvements

Windows 7 includes numerous enhancements to the underlying [Media Foundation](/windows/desktop/medfound/microsoft-media-foundation-sdk) platform APIs. Advanced applications can use these APIs directly; other applications will get the benefits indirectly. These benefits include:

-   Improvements in the video pipeline to reduce power consumption and video memory usage.
-   New *DVXA* video processing APIs, which use a more flexible compositing model and are better suited for *HD* video formats.
-   Improvements to the way in which plug-ins (sources and decoders) are enumerated and managed.

## Related topics

<dl> <dt>

[What's New for Media Foundation](../medfound/whats-new-for-media-foundation.md)
</dt> </dl>

 

 