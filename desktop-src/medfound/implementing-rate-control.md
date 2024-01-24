---
description: This topic describes how custom pipeline objects can support variable playback rates, including reverse playback. For information about using rate control from an application, see Rate Control.
ms.assetid: 077678db-ca5a-423b-9430-93497113d639
title: Implementing Rate Control
ms.topic: article
ms.date: 05/31/2018
---

# Implementing Rate Control

This topic describes how custom pipeline objects can support variable playback rates, including reverse playback. For information about using rate control from an application, see [Rate Control](rate-control.md).

This topic contains the following sections:

-   [Media Sources](#media-sources)
-   [Media Foundation Transforms](#media-foundation-transforms)
    -   [Reverse Playback](#reverse-playback)
-   [Media Sinks](#media-sinks)
-   [Related topics](#related-topics)

If you are writing a Microsoft Media Foundation pipeline object (a media source, transform, or media sink), you might need to support variable playback rates. To do so, implement the following interfaces:

1.  Implement the [**IMFGetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice) interface.
2.  Support the **MF\_RATE\_CONTROL\_SERVICE** service. (See [Service Interfaces](service-interfaces.md).)
3.  Implement the [**IMFRateSupport**](/windows/desktop/api/mfidl/nn-mfidl-imfratesupport) interface, which gets the playback rates supported by the object.
4.  Implement the [**IMFRateControl**](/windows/desktop/api/mfidl/nn-mfidl-imfratecontrol) interface, which gets or sets the playback rate.

## Media Sources

If a media source supports rate control, it should implement both [**IMFRateSupport**](/windows/desktop/api/mfidl/nn-mfidl-imfratesupport) and [**IMFRateControl**](/windows/desktop/api/mfidl/nn-mfidl-imfratecontrol). Otherwise, the Media Session reports that the minimum and maximum playback rate is 1.0, regardless of what other components are in the pipeline.

The playback rate does not affect the presentation times of the samples, so the media source should not adjust its time stamps. Instead, the presentation clock runs at a faster or slower speed. For reverse playback, the source delivers samples in reverse order, with decreasing time stamps.

The *fThin* parameter of the [**IMFRateControl::SetRate**](/windows/desktop/api/mfidl/nf-mfidl-imfratecontrol-setrate) method indicates whether media source should *thin* the content. Thinning applies primarily to video streams. In thinned mode, the source drops delta frames and deliver only key frames. At very high playback rates, the source might skip some key frames (for example, deliver every other key frame).

The source does not have to drop audio samples in thinned mode. At very high playback rates, however, the source might not be able to read data fast nough to fill the pipeline's sample requests. In that case, the source might need to drop some audio data. If so, it should attempt to deliver audio samples that are close in time to the video samples (assuming that the source has both types of stream).

When a stream transitions between thinned and non-thinned mode, it sends an [MEStreamThinMode](mestreamthinmode.md) event.

When the media source completes a call to [**SetRate**](/windows/desktop/api/mfidl/nf-mfidl-imfratecontrol-setrate), it sends the [MESourceRateChanged](mesourceratechanged.md) event.

During reverse playback:

-   The media source delivers samples in reverse order, without adjusting the time stamps.
-   Time stamps within a stream should monotonically decrease.
-   The beginning of the content is considered the end of the stream. After each media stream delivers the first sample in the stream (that is, presentation time = 0), it sends the [MEEndOfStream](meendofstream.md) event.

## Media Foundation Transforms

In general, a Media Foundation transform (MFT) does not need explicit support for rate control, unless the MFT implements non-thinned reverse playback.

If an MFT does not implement the [**IMFRateSupport**](/windows/desktop/api/mfidl/nn-mfidl-imfratesupport) interface, the Media Session assumes the following:

-   The MFT supports arbitary playback rates for forward playback, both thinned and non-thinned.
-   The MFT supports thinned reverse playback, but does not support non-thinned reverse playback.

If either of these conditions is not true, the MFT should implement [**IMFRateSupport**](/windows/desktop/api/mfidl/nn-mfidl-imfratesupport) and [**IMFRateControl**](/windows/desktop/api/mfidl/nn-mfidl-imfratecontrol).

### Reverse Playback

The Media Session can play in reverse even if one or more transforms in the pipeline do not explicitly support reverse playback.

If an MFT does not expose the [**IMFRateSupport**](/windows/desktop/api/mfidl/nn-mfidl-imfratesupport) interface, the Media Session uses *thinning* for reverse playback, as follows:

-   The Media Session sends key frames to the MFT in the usual way, by calling [**IMFTransform::ProcessInput**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processinput).

-   The Media Session drops delta frames and replaces them with [MEStreamTick](mestreamtick.md) events.

-   Between each sample, the Media Session flushes the MFT, to avoid any errors caused by the fact that the time stamps are decreasing.

A sample is considered a key frame if it has the [MFSampleExtension\_CleanPoint](mfsampleextension-cleanpoint-attribute.md) attribute set to **TRUE**, and is considered a delta frame if this attribute is **FALSE** or not set.

If the MFT implements [**IMFRateSupport**](/windows/desktop/api/mfidl/nn-mfidl-imfratesupport), the Media Session uses this interface to discover whether the MFT supports non-thinned reverse playback. If the MFT supports non-thinned reverse playback, the Media Session delivers all of the samples, in reverse order, without dropping samples or flushing the MFT.

If an MFT supports non-thinned reverse playback, it should implement the [**IMFRateControl**](/windows/desktop/api/mfidl/nn-mfidl-imfratecontrol) interface. The Media Session will use this interface to notify the MFT when reverse playback occurs. At that point, the MFT must be prepared for the time stamps to decrease and for delta frames to arrive in reverse order. A decoder will typically need to buffer samples until it has received an entire group of pictures (GOP), then decode the entire GOP and output the decoded frames in the correct (reverse) order.

## Media Sinks

If a media sink is *rateless*, the Media Session assumes that media sink can handle any playback rate. The media sink does not need to implement [**IMFRateSupport**](/windows/desktop/api/mfidl/nn-mfidl-imfratesupport). (A rateless media sink returns the MEDIASINK\_RATELESS flag from the [**IMFMediaSink::GetCharacteristics**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasink-getcharacteristics) method.)

Otherwise, a media sink should implement [**IMFRateSupport**](/windows/desktop/api/mfidl/nn-mfidl-imfratesupport) if it can handle playback rates other than 1.0.

Media sinks should not implement [**IMFRateControl**](/windows/desktop/api/mfidl/nn-mfidl-imfratecontrol). When the playback rate changes, the presentation clock calls the media sink's [**IMFClockStateSink::OnClockSetRate**](/windows/desktop/api/mfidl/nf-mfidl-imfclockstatesink-onclocksetrate) method.

## Related topics

<dl> <dt>

[Rate Control](rate-control.md)
</dt> <dt>

[Seeking, Fast Forward, and Reverse Play](seeking--fast-forward--and-reverse-play.md)
</dt> </dl>

 

 



