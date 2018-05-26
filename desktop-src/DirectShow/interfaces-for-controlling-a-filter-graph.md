---
Description: Interfaces for Controlling a Filter Graph
ms.assetid: f7de0165-e356-45d5-baed-d127caeebaf6
title: Interfaces for Controlling a Filter Graph
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Interfaces for Controlling a Filter Graph

These interfaces provide methods for controlling a filter graph.



| Interface                                  | Description                                                                                               |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [**IAMClockAdjust**](/windows/win32/Strmif/nn-strmif-iamclockadjust?branch=master)   | Adjust the graph clock.                                                                                   |
| [**IAMGraphStreams**](/windows/win32/Strmif/nn-strmif-iamgraphstreams?branch=master) | Synchronize live streams in a filter graph.                                                               |
| [**IFilterChain**](/windows/win32/Strmif/nn-strmif-ifilterchain?branch=master)       | Control chains of filters.                                                                                |
| [**IMediaControl**](/windows/win32/Control/nn-control-imediacontrol?branch=master)     | Run, pause, and stop the filter graph. (Also provides Automation-compatible methods for building graphs.) |
| [**IMediaEventEx**](/windows/win32/Control/nn-control-imediaeventex?branch=master)     | Respond to events in the graph.                                                                           |
| [**IMediaSeeking**](/windows/win32/Strmif/nn-strmif-imediaseeking?branch=master)     | Seek within a file.                                                                                       |
| [**IQueueCommand**](/windows/win32/Control/nn-control-iqueuecommand?branch=master)     | Queue commands to run at a later time.                                                                    |
| [**IVideoFrameStep**](/windows/win32/Strmif/nn-strmif-ivideoframestep?branch=master) | Frame-step through a video stream.                                                                        |



 

 

 



