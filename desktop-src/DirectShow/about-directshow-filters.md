---
description: About DirectShow Filters
ms.assetid: 57b7d32e-2073-46a2-91ec-a34072134489
title: About DirectShow Filters
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About DirectShow Filters

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

DirectShow uses a modular architecture, where each stage of processing is done by a COM object called a filter. DirectShow provides a set of standard filters for applications to use, and developers can write their own custom filters that extend the functionality of DirectShow. To illustrate, here are the steps needed to play an AVI video file, along with the filters that perform each step:

-   Read the raw data from the file as a byte stream (File Source filter).
-   Examine the AVI headers, and parse the byte stream into separate video frames and audio samples (AVI Splitter filter).
-   Decode the video frames (various decoder filters, depending on the compression format).
-   Draw the video frames (Video Renderer filter).
-   Send the audio samples to the sound card (Default DirectSound Device filter).

These filters are shown in the following diagram.

![filter graph for playing back an avi file with compressed video](images/avi-filter-graph.png)

As the diagram shows, each filter is connected to one or more other filters. The connection points are also COM objects, called *pins*. Filters use pins to move data from one filter the next. The arrows in the diagram show the direction in which the data travels. In DirectShow, a set of filters is called a *filter graph*.

Filters have three possible states: running, stopped, and paused. When a filter is running, it processes media data. When it is stopped, it stops processing data. The paused state is used to cue data before running; the section [Data Flow in the Filter Graph](data-flow-in-the-filter-graph.md) describes this concept in more detail. With very rare exceptions, state changes are coordinated throughout the entire filter graph; all the filters in the graph switch states in unison. Thus, the entire filter graph is also said to be running, stopped, or paused.

Filters can be grouped into several broad categories:

-   A *source* filter introduces data into the graph. The data might come from a file, a network, a camera, or anywhere else. Each source filter handles a different type of data source.
-   A *transform* filter takes an input stream, processes the data, and creates an output stream. Encoders and decoders are examples of transform filters.
-   *Renderer* filters sit at the end of the chain. They receive data and present it to the user. For example, a video renderer draws video frames on the display; an audio renderer sends audio data to the sound card; and a file-writer filter writes data to a file.
-   A *splitter* filter splits an input stream into two or more outputs, typically parsing the input stream along the way. For example, the AVI Splitter parses a byte stream into separate video and audio streams.
-   A *mux* filter takes multiple inputs and combines them into a single stream. For example, the AVI Mux performs the inverse operation of the AVI Splitter. It takes audio and video streams and produces an AVI-formatted byte stream.

The distinctions between these categories are not absolute. For example, the ASF Reader filter acts as both a source filter and a splitter filter.

All DirectShow filters expose the [**IBaseFilter**](/windows/desktop/api/Strmif/nn-strmif-ibasefilter) interface, and all pins expose the [**IPin**](/windows/desktop/api/Strmif/nn-strmif-ipin) interface. DirectShow also defines many other interfaces that support more specific functionality.

## Related topics

<dl> <dt>

[About the Filter Graph Manager](about-the-filter-graph-manager.md)
</dt> <dt>

[Data Flow in the Filter Graph](data-flow-in-the-filter-graph.md)
</dt> <dt>

[DirectShow Filters](directshow-filters.md)
</dt> </dl>

 

 



