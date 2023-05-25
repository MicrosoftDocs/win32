---
title: Custom File and Stream Handlers
description: Custom File and Stream Handlers
ms.assetid: 'c61e0118-d405-4c1e-9ae8-ed6a145a5d6b'
keywords:
- Video for Windows (VFW),custom file handlers
- Video for Windows (VFW),custom stream handlers
- Video for Windows (VFW),file handlers
- Video for Windows (VFW),stream handlers
- VFW (Video for Windows),custom file handlers
- VFW (Video for Windows),custom stream handlers
- VFW (Video for Windows),file handlers
- VFW (Video for Windows),stream handlers
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Custom File and Stream Handlers

\[The feature associated with this page, [Custom File and Stream Handlers](/windows/win32/multimedia/custom-file-and-stream-handlers), is a legacy feature. It has been superseded by [MediaStreamSource class](/uwp/api/Windows.Media.Core.MediaStreamSource). **MediaStreamSource class** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaStreamSource class** instead of **Custom File and Stream Handlers**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

File and stream handlers are drivers that provide consistent interfaces to an application that controls multimedia data. The file and stream handlers included in the operating system use video and waveform-audio data stored in audio-video interleaved (AVI) and waveform-audio files.

You can write handlers to allow your application to write or access multimedia data from another source, such as a file using a proprietary format, an AVI file that has been expanded to contain additional data streams, or a handler that generates its own multimedia data. If you have a custom file format for AVI data that you would like to use with the [AVIFile Functions and Macros](avifile-functions-and-macros.md), you need to write a custom handler.

-   [About Custom File and Stream Handlers](about-custom-file-and-stream-handlers.md)
-   [Using Custom File and Stream Handlers](using-custom-file-and-stream-handlers.md)
-   [Custom File and Stream Handler Reference](custom-file-and-stream-handler-reference.md)

 

 




