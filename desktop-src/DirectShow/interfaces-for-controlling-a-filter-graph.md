---
description: Interfaces for Controlling a Filter Graph
ms.assetid: f7de0165-e356-45d5-baed-d127caeebaf6
title: Interfaces for Controlling a Filter Graph
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Interfaces for Controlling a Filter Graph

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

These interfaces provide methods for controlling a filter graph.



| Interface                                  | Description                                                                                               |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [**IAMClockAdjust**](/windows/desktop/api/Strmif/nn-strmif-iamclockadjust)   | Adjust the graph clock.                                                                                   |
| [**IAMGraphStreams**](/windows/desktop/api/Strmif/nn-strmif-iamgraphstreams) | Synchronize live streams in a filter graph.                                                               |
| [**IFilterChain**](/windows/desktop/api/Strmif/nn-strmif-ifilterchain)       | Control chains of filters.                                                                                |
| [**IMediaControl**](/windows/desktop/api/Control/nn-control-imediacontrol)     | Run, pause, and stop the filter graph. (Also provides Automation-compatible methods for building graphs.) |
| [**IMediaEventEx**](/windows/desktop/api/Control/nn-control-imediaeventex)     | Respond to events in the graph.                                                                           |
| [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking)     | Seek within a file.                                                                                       |
| [**IQueueCommand**](/windows/desktop/api/Control/nn-control-iqueuecommand)     | Queue commands to run at a later time.                                                                    |
| [**IVideoFrameStep**](/windows/desktop/api/Strmif/nn-strmif-ivideoframestep) | Frame-step through a video stream.                                                                        |



 

 

 



