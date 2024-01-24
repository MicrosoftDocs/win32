---
description: Using the Sink Writer
ms.assetid: BE89E2E0-711F-4BD5-BB86-AA4CCA2D3E7F
title: Using the Sink Writer
ms.topic: article
ms.date: 05/31/2018
---

# Using the Sink Writer

## Overview

### File Container Types

The sink writer has built-in support for several file container types. For a complete list, see [MF\_TRANSCODE\_CONTAINERTYPE](mf-transcode-containertype.md). You can support additional container types by writing a custom [media sink](media-sinks.md). The file container is specified when you create a new instance of the sink writer.

### Stream Formats

For each stream, the application must specify the following.

-   The *input format* is the format that the application sends to the sink writer.
-   The *output format* is the format that will be written to the file.

The input and output formats can be either compressed or uncompressed. The sink writer supports the following combinations:

-   Uncompressed input with compressed output. This is the typical case, and is used for encoding or transcoding scenarios. A Microsoft Media Foundation encoder must be available that accepts the input type and encodes to the output type.
-   Compressed input with identical output. Use this combination to remux a file without transcoding.
-   Uncompressed input with identical output. Use this combination to write uncompressed audio or video to a file container.

The sink writer does not support video resizing, frame-rate conversion, or audio resampling, unless these functions are provided by the encoder. Otherwise, the application can use [Digital Signal Processors](windowsmediadigitalsignalprocessors.md) to convert the input data, before sending the data to the

## Creating the Sink Writer

There are two functions that create the sink writer:

-   [**MFCreateSinkWriterFromURL**](/windows/desktop/api/mfreadwrite/nf-mfreadwrite-mfcreatesinkwriterfromurl) takes the URL of an output file or a pointer to a byte stream. This function creates the media sink internally.
-   [**MFCreateSinkWriterFromMediaSink**](/windows/desktop/api/mfreadwrite/nf-mfreadwrite-mfcreatesinkwriterfrommediasink) takes a pointer to a media sink that has already been created by the application.

If you are using one of the built-in media sinks, the [**MFCreateSinkWriterFromURL**](/windows/desktop/api/mfreadwrite/nf-mfreadwrite-mfcreatesinkwriterfromurl) function is preferable, because the caller does not need to configure the media sink.

The [**MFCreateSinkWriterFromURL**](/windows/desktop/api/mfreadwrite/nf-mfreadwrite-mfcreatesinkwriterfromurl) method provides several options for specifying the type of file container. In the simplest case, the function uses the file name extension in the URL to select the file container. For details, refer to the function reference page.

For example, the following code specifies the file name "output.wmv" for the URL. Based on the file name extension, the sink writer will load the [ASF Media Sink](asf-media-sinks.md) to create an Advanced Systems Format (ASF) file.


```C++
    HRESULT hr = MFCreateSinkWriterFromURL(L"output.wmv", NULL, NULL, &pSinkWriter);
```



In the case of [**MFCreateSinkWriterFromMediaSink**](/windows/desktop/api/mfreadwrite/nf-mfreadwrite-mfcreatesinkwriterfrommediasink), the file type is determined by the media sink.

## Related topics

<dl> <dt>

[Sink Writer](sink-writer.md)
</dt> </dl>

 

 



