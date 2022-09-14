---
description: MPEG1Source Sample
ms.assetid: c9f131ff-0b79-487c-9a46-a9b1350553a1
title: MPEG1Source Sample
ms.topic: article
ms.date: 05/31/2018
---

# MPEG1Source Sample

Shows how to write a custom media source in Microsoft Media Foundation. The sample implements a media source that parses MPEG-1 systems-layer streams and generates samples that contain MPEG-1 payloads.

## APIs Demonstrated

This sample demonstrates the following Media Foundation interfaces:

-   [**IMFByteStreamHandler**](/windows/desktop/api/mfidl/nn-mfidl-imfbytestreamhandler)
-   [**IMFMediaSource**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasource)
-   [**IMFMediaStream**](/windows/desktop/api/mfidl/nn-mfidl-imfmediastream)

Before examining this sample, you might want to review the [WavSource Sample](wavsource-sample.md), which provides a simpler implementation of a media source. The MPEG1Source sample adds some features that would be found in most real-world implementations of a media source:

-   Multiple streams
-   Asynchronous methods
-   Asynchronous I/O

In the Windows SDK for Windows Server 2008, this sample also includes a sample MPEG-1 video decoder that displays the time code for each video frame. (It does not actually decode the MPEG-1 bitstream.)

Starting in the Windows SDK for Windows 7, the decoder has been moved to a separate sample. See [Decoder Sample](decoder-sample.md).

## Usage

The MPEG1Source sample builds a DLL that is a COM server for the media source, media source's byte-stream handler, and the decoder MFT. Before using the media source, you must register the DLL.

To use the media source, you can run the [BasicPlayback Sample](/previous-versions//bb970475(v=vs.85)). The source resolver will automatically load the media source if you select an MPEG-1 file for playback. (If an error occurs, make sure that you successfully registered the MPEG1Source DLL.)

You can also use the TopoEdit tool to build a playback topology that contains the media source. For more information about TopoEdit, see [TopoEdit](topoedit.md).

## Requirements



| Product                                                        | Version   |
|----------------------------------------------------------------|-----------|
| [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx) | Windows 7 |



 

## Downloading the Sample

This sample is available in the [Windows classic samples github repository](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/multimedia/mediafoundation/mpeg1source).

## Related topics

<dl> <dt>

[Media Foundation SDK Samples](media-foundation-sdk-samples.md)
</dt> <dt>

[Media Sources](media-sources.md)
</dt> <dt>

[Scheme Handlers and Byte-Stream Handlers](scheme-handlers-and-byte-stream-handlers.md)
</dt> <dt>

[Tutorial: Writing a Custom Media Source](tutorial--writing-a-custom-media-source.md)
</dt> <dt>

[WavSource Sample](wavsource-sample.md)
</dt> </dl>

 

 
