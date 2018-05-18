---
Description: WavSource Sample
ms.assetid: '905fbba5-0a04-4048-80bd-f8707c4879da'
title: WavSource Sample
---

# WavSource Sample

Shows how to create a custom media source in Microsoft Media Foundation. The sample implements a media source that parses .wav audio files.

This sample is a relatively simple example of a media source:

-   There is only one stream, so there is no code to implement stream selection.
-   The media source does not implement rate control (that is, fast forward or reverse playback).
-   All source and stream methods are implemented as synchronous methods.
-   Because the data portion of a .wav file is a single block of uncompressed PCM audio, the media source does not need to read packet headers or otherwise parse the stream during playback, other than reading the initial [**WAVEFORMAT**](multimedia.waveformat) header.

For a more advanced example of a media source, see the [MPEG1Source Sample](mpeg1source-sample.md).

## APIs Demonstrated

This sample demonstrates the following Media Foundation interfaces:

-   [**IMFByteStreamHandler**](imfbytestreamhandler.md)
-   [**IMFMediaSource**](imfmediasource.md)
-   [**IMFMediaStream**](imfmediastream.md)

## Usage

The WavSource sample builds a DLL that is a COM server for both the media source and media source's byte-stream handler. Before using the media source, you must register the DLL.

To use the media source, you can run the [BasicPlayback](mf.basicplayback_sample). The source resolver will automatically load the media source if you select a .wav file for playback. (If an error occurs, make sure that you successfully registered the WavSource DLL.)

You can also use the TopoEdit tool to build a playback topology that contains the media source. For more information about TopoEdit, see [TopoEdit](topoedit.md).

## Requirements



| Product                                                        | Version   |
|----------------------------------------------------------------|-----------|
| [Windows SDK](http://go.microsoft.com/fwlink/p/?linkid=129787) | Windows 7 |



 

## Downloading the Sample

This sample is available in the [Windows classic samples github repository](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/multimedia/mediafoundation/wavsource).

## Related topics

<dl> <dt>

[Media Foundation SDK Samples](media-foundation-sdk-samples.md)
</dt> <dt>

[Media Sources](media-sources.md)
</dt> <dt>

[MPEG1Source Sample](mpeg1source-sample.md)
</dt> <dt>

[Scheme Handlers and Byte-Stream Handlers](scheme-handlers-and-byte-stream-handlers.md)
</dt> <dt>

[Writing a Custom Media Source](writing-a-custom-media-source.md)
</dt> </dl>

 

 



