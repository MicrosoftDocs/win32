---
description: About the Render Engines
ms.assetid: 80299b1a-09bf-4660-95d3-41a2b0074745
title: About the Render Engines
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About the Render Engines

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[This API is not supported and may be altered or unavailable in the future.\]

This article describes how [DirectShow Editing Services](directshow-editing-services.md) (DES) renders a video editing project.

In DES, a project is represented as a timeline. The timeline is useful because it simplifies the most common tasks in video editing, such as rearranging source clips and adding video effects. The DirectShow stream architecture, on the other hand, requires a filter graph. Thus, to render your project, you must translate a timeline into a filter graph. The component that does this is called a *render engine*. DirectShow provides two render engines:

-   Basic render engine: Builds a filter graph that delivers uncompressed output.
-   Smart render engine: Builds a filter graph that delivers compressed output.

The smart render engine uses smart recompression to improve performance. With smart recompression, source files are recompressed only when the original file format differs from the final output format. If the formats match, the source is never decompressed. Smart recompression is supported only for video compression, not for audio compression.

For preview, use the basic render engine. The smart render engine can also preview, but less efficiently because it has to decompress the compressed stream. For writing files, use the smart render engine if you want smart recompression. Otherwise, use the basic render engine. Smart recompression can greatly reduce the time it takes to write the file.

> [!IMPORTANT]
> Do not use the smart render engine to read or write Windows Media files.

 

> [!IMPORTANT]
> Both render engines create an invisible window that processes messages. The thread that creates the render engine must have a message loop, to dispatch messages. Also, that thread must not exit until the Render Engine and the Filter Graph Manager are released. Otherwise, the application might deadlock.

 

Constructing the Filter Graph

The filter graph is built in two stages. In the first stage, the render engine constructs a "front end," which is a partial filter graph. The following diagram illustrates a typical front end:

![filter graph front end](images/rendeng1.png)

The subsystems contain various specialized filters, which the render engine assembles automatically. The front end contains one output pin for each group in the timeline. The output pins deliver uncompressed data if you use the basic render engine, or compressed data if you use the smart render engine.

In the second step, the output pins are connected to rendering filters. For preview, the rendering filters are video and audio renderers. For file writing, the rendering filters are multiplexer (mux) filters and file-writer filters.

![completing the filter graph](images/rendeng2.png)

## Related topics

<dl> <dt>

[Previewing a Project](previewing-a-project.md)
</dt> <dt>

[Writing a Project to a File](writing-a-project-to-a-file.md)
</dt> </dl>

 

 



