---
description: MPEG-2 Demux Run-Time Modes
ms.assetid: b0d0c725-9220-43a5-af1c-d3c5c72e1ef3
title: MPEG-2 Demux Run-Time Modes
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# MPEG-2 Demux Run-Time Modes

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The [MPEG-2 Demultiplexer](mpeg-2-demultiplexer.md) ("demux") can operate in push mode or pull mode. In push mode, the data comes from a live source, such as a network broadcast. In pull mode, the data comes from a local file.

-   Pull mode is available in Windows XP and later, for program streams only. On down-level platforms, use the [MPEG-2 Splitter](mpeg-2-splitter.md) filter.
-   Push mode is available on all platforms, for both program streams and transport streams.

The demux therefore supports three possible modes: Program streams in pull mode, program streams in push mode, and transport streams in push mode. The demux determines which mode to use at run time. The mode is determined when the input pin connects, or when the first output pin is configured, whichever happens first:

-   When the input pin connects: On Windows XP and later, the demux queries the upstream filter for the [**IAsyncReader**](/windows/desktop/api/Strmif/nn-strmif-iasyncreader) interface; if the upstream filter exposes that interface, the demux configures itself for program streams in pull mode. Otherwise, the demux uses push mode, and the media type determines the stream type (program stream or transport stream). See [**MPEG-2 Demultiplexer Media Types**](mpeg-2-demultiplexer-media-types.md) for a list of input types.
-   When the first output pin is configured: If you create an output pin and query it for [**IMPEG2PIDMap**](/previous-versions/windows/desktop/api/Bdaiface/nn-bdaiface-impeg2pidmap), the demux configures itself for transport streams in push mode. If you query the pin for [**IMPEG2StreamIdMap**](/windows/desktop/api/Strmif/nn-strmif-impeg2streamidmap), the demux configures itself for program streams, also in push mode. Any subsequent queries for the other interface fail, because the demux cannot operate in two modes at once.

Once the demux has configured itself for a particular mode, it remains in that mode. To use a different mode, you must create a new instance of the demux.

## Related topics

<dl> <dt>

[Using the MPEG-2 Demultiplexer](using-the-mpeg-2-demultiplexer.md)
</dt> </dl>

 

 



