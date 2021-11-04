---
description: This topic is an overview of the file encoding APIs provided in Microsoft Media Foundation.
ms.assetid: 69dbef63-e272-4ad2-8d04-ae9366f79b33
title: Overview of Encoding in Media Foundation
ms.topic: article
ms.date: 05/31/2018
---

# Overview of Encoding in Media Foundation

This topic is an overview of the file encoding APIs provided in Microsoft Media Foundation.

## Terminology

*Encoding* is a general term that covers several distinct processes:

1.  Encoding an audio or video stream into a compressed formats. For example, encoding a video stream to H.264 video.
2.  Multiplexing ("muxing") one or more streams into a single byte stream. Typically, the incoming streams are encoded first. This step might involve packetizing the encoded streams.
3.  Writing a multiplexed byte stream to a file, such as an MP4 or Advanced Systems Format (ASF) file. Alternatively, the multiplexed stream can be sent over the network.

The following diagram shows these three processes:

![diagram showing the encoding and multiplexing processes](images/encoding03.png)

Variations of this process include transcoding and remuxing:

-   *Transcoding* means decoding an existing file, re-encoding the streams, and re-multiplexing the encoded streams. Transcoding might be done to convert a file from one encoding type to another; for example, to convert H.264 video to Windows Media Video (WMV). It can also be done to change the encoded bit rate; the video frame size; the frame rate; or other format parameters.
-   *Remultiplexing* or *remuxing* means demultiplexing a file and re-multiplexing the streams, with no decode/encode step. This might be done to change how the audio/video packets are multiplexed, to remove a stream, or to combine streams from two different source files.
-   *Transrating* is a special case of transcoding, where the bit-rate is changed without changing the compression type. For example, you might convert a high-bit-rate file to a lower bit-rate. A typical scenario in which transrating might be used is when synchronizing media content from a PC to a portable device. If the portable device does not support a high bit rate, the file might be transrated before it is copied to the portable device.

The following block diagram shows the transcoding process.

![diagram showing the transcoding process](images/encoding05.png)

The following block diagram shows the remuxing process.

![diagram showing the remuxing process](images/encoding06.png)

This documentation sometimes uses the term *encoding* to include both transcoding and remuxing. When it is important to distinguish between them, the documentation will note the difference.

See also: [Media Foundation: Essential Concepts](media-foundation-programming--essential-concepts.md).

## Media Foundation Encoding Architecture

At the lowest layer of the Media Foundation architecture, the following types of component are used for encoding:

-   For transcoding, [Media Sources](media-sources.md) are used to demultiplex the source file.
-   For the encoding process, [Media Foundation Transforms](media-foundation-transforms.md) are used to decode and encode streams.
-   For the multiplexing process, [Media Sinks](media-sinks.md) are used to multiplex the streams and write the multiplexed stream to a file or network.

The following diagram shows the data flow between these components in a transcoding scenario:

![diagram showing the components used in transcoding](images/encoding04.png)

Most applications will not use these components directly. Instead, an application will use higher-level APIs that manage these lower-level components. Media Foundation provides two higher-level APIs for encoding:

<dl> <dt>

<span id="Media_Session"></span><span id="media_session"></span><span id="MEDIA_SESSION"></span>[Media Session](media-session.md)
</dt> <dd>

The Media Session provides an end-to-end pipeline that moves data from the media source, through the codecs, and finally to the media sink. The application controls the Media Session and receives status events from the Media Session.

</dd> <dt>

<span id="Source_Reader_plus_Sink_Writer"></span><span id="source_reader_plus_sink_writer"></span><span id="SOURCE_READER_PLUS_SINK_WRITER"></span>[Source Reader](source-reader.md) plus [Sink Writer](sink-writer.md)
</dt> <dd>

The Source Reader wraps the media source and optionally the decoders. It delivers either encoded or decoded samples the application. The Sink Writer wraps the media sink and optionally the encoders. The application passes samples to the Sink Writer.

</dd> </dl>

The following diagram shows the Media Session:

![diagram showing how the media session performs transcoding](images/encoding01.png)

The [Transcode API](transcode-api.md) (the blue shaded box) is a set of APIs introduced in Windows 7, which make it easier to configure the Media Session for encoding.

The next diagram shows the Source Reader and Sink Writer:

![diagram showing transcoding with the source reader and sink writer](images/encoding02.png)

## Related topics

<dl> <dt>

[Encoding and File Authoring](encoding-and-file-authoring.md)
</dt> <dt>

[Media Foundation Programming: Essential Concepts](media-foundation-programming--essential-concepts.md)
</dt> </dl>

 

 



