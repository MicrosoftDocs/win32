---
description: About Rate Control
ms.assetid: 509b2cc8-6017-41a9-ae80-9af21dce9367
title: About Rate Control
ms.topic: article
ms.date: 05/31/2018
---

# About Rate Control

In Media Foundation, the *playback rate* is expressed as the ratio of the current playback rate to the normal playback rate. For example, a rate of 2.0 is twice normal speed, and 0.5 is half normal speed. Negative values indicate reverse playback. A playback rate of -2.0 plays backward through the stream at twice the normal speed. A rate of zero causes one frame to be rendered; after that, the presentation clock does not advance. To get another frame at the rate of zero, the application must seek to a new position.

Applications use the following interfaces to control the playback rate.

-   [**IMFRateSupport**](/windows/desktop/api/mfidl/nn-mfidl-imfratesupport). Used to find out the fastest and slowest playback rates that are possible.
-   [**IMFRateControl**](/windows/desktop/api/mfidl/nn-mfidl-imfratecontrol). Used to change the playback rate.

To get these two interfaces, call [**IMFGetService::GetService**](/windows/desktop/api/mfidl/nf-mfidl-imfgetservice-getservice) on the Media Session. The service identifier is MF\_RATE\_CONTROL\_SERVICE.

By using the rate control service, an application can implement fast forward and reverse playback.

## Thinning

*Thinning* is any process that reduces the number of samples in a stream, to reduce the overall bit rate. For video, thinning is generally accomplished by dropping the delta frames and delivering only the key frames. Often the pipeline can support faster playback rates using thinned playback, because the data rate is lower because delta frames are not decoded.

Thinning does not change the time stamps or durations on the samples. For example, if the nominal rate of the video stream is 25 frames per second, the duration of each frame is still marked as 40 milliseconds, even if the media source is dropping all of the delta frames. That means there will be a time gap between the end of one frame and the start of the next.

## Scrubbing

*Scrubbing* is the process of instantaneously seeking to specific points in the stream by interacting with a scrollbar, timeline, or other visual representation of time. The term comes from the era of reel-to-reel tape players when rocking a reel back and forth to locate a section was like scrubbing the playback head with the tape.

Scrubbing is implemented in Media Foundation by setting the playback rate to zero. For more information, see [How to Perform Scrubbing](how-to-perform-scrubbing.md).

## Related topics

<dl> <dt>

[Rate Control](rate-control.md)
</dt> <dt>

[Seeking, Fast Forward, and Reverse Play](seeking--fast-forward--and-reverse-play.md)
</dt> <dt>

[Service Interfaces](service-interfaces.md)
</dt> </dl>

 

 



