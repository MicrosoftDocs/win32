---
description: Ball Filter Sample
ms.assetid: 80a6db64-ef13-46a2-8f2a-e39095e874b2
title: Ball Filter Sample
ms.topic: article
ms.date: 05/31/2018
---

# Ball Filter Sample

## Description

The Ball Filter is a video source filter that produces an image of a bouncing ball. This sample illustrates format negotiation and the use of the source filter base classes [**CSource**](csource.md) and [**CSourceStream**](csourcestream.md).

The code in Fball.h and Fball.cpp manages the filter interfaces. Those two files contain approximately the minimum code required for a source filter. The Ball.h and Ball.cpp files contain the code that bounces the ball.

This filter has a single output pin, which provides a video stream that shows a ball bouncing around in the frame. The Ball filter also accepts quality management requests from the downstream filter, which illustrates a simple quality management strategy. This filter implements the [**IQualityControl**](/windows/desktop/api/Strmif/nn-strmif-iqualitycontrol) interface for that purpose.

## Downloading the Sample

To download the DirectShow SDK samples, install the latest version of the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx).

This sample is installed under the following path: \[*SDK Root*\]\\Samples\\Multimedia\\DirectShow\\Filters\\Ball.

## Related topics

<dl> <dt>

[DirectShow Samples](directshow-samples.md)
</dt> </dl>

 

 



