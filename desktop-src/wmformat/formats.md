---
title: Formats
description: Formats
ms.assetid: '7c602643-f1fc-4fbd-a739-4296dc758bc9'
keywords:
- Windows Media Format SDK,inputs
- Windows Media Format SDK,streams
- Windows Media Format SDK,outputs
- Windows Media Format SDK,formats
- Advanced Systems Format (ASF),inputs
- ASF (Advanced Systems Format),inputs
- Advanced Systems Format (ASF),streams
- ASF (Advanced Systems Format),streams
- Advanced Systems Format (ASF),outputs
- ASF (Advanced Systems Format),outputs
- Advanced Systems Format (ASF),formats
- ASF (Advanced Systems Format),formats
ms.topic: article
ms.date: 05/31/2018
---

# Formats

The information in a format describes everything you need to know about a particular type of media. Every format has a major type, like audio or video, and may have a subtype. Formats contain different information based on major type. Audio and video formats require much more information than other types.

Just as the objects of the Windows Media Format SDK differentiate between input numbers, stream numbers, and output numbers (see [Inputs, Streams and Outputs](inputs-streams-and-outputs.md)), there are important distinctions between input formats, stream formats, and output formats. These differences are described here:

## Input Formats

An input format describes the digital media that you pass to the writer object. If a stream in an ASF file is compressed with a codec, the codec will support only certain input formats. When using the Windows Media Audio and Video codecs, you can enumerate the supported input formats using the writer object. When writing a file, you are responsible for selecting an input format that matches your input media.

Although the input media format must be supported by the codec that will compress the data, some input format settings need not match the stream format. For example, the input format for a video stream may have a frame size that is different from that defined in the stream format. The codec will perform conversions in these cases.

## Stream Formats

A stream format describes the form of the media as it is stored in the ASF file. The stream format is the format described in the profile, and may or may not be the same as the input format and output format. If a codec is used to compress the data in a stream, the stream format will be different than the input and output formats.

When using the Windows Media Audio and Video codecs, you must obtain a list of supported stream formats from the codec to ensure that you are not attempting to specify a format that the code does not support. Some format settings, such as the size and color depth of a video frame, must be configured manually after the codec format is retrieved.

## Output Formats

An output format describes the digital media that the reader (or synchronous reader) delivers to your application. If a stream in an ASF file is compressed with a codec, the codec will support only certain output formats. When using the Windows Media Audio and Video codecs, you can enumerate the supported output formats by using the reader object. Each of the Windows Media codecs has a default output format, but you can select any supported output format for sample delivery.

Although the output media format must be supported by the codec that compressed the data, some output format settings need not match the stream format. For example, the output format for a video stream may have a frame size that is different from that defined in the stream format. The codec will perform conversions in these cases.

## Related topics

<dl> <dt>

[**Concepts**](concepts.md)
</dt> </dl>

 

 




