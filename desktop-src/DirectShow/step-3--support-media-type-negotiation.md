---
description: Implement support for media type negotiation as part of writing a transform filter. The media type describes the format of the data.
ms.assetid: b2b5dafc-d38d-4ec3-a390-55229495b4f9
title: Step 3. Support Media Type Negotiation
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Step 3. Support Media Type Negotiation

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This is step 3 of the tutorial [Writing Transform Filters](writing-transform-filters.md).

When two pins connect, they must agree on a media type for the connection. The media type describes the format of the data. Without the media type, a filter might deliver one kind of data, only to have another filter treat it as something else.

The basic mechanism for negotiating media types is the [**IPin::ReceiveConnection**](/windows/desktop/api/Strmif/nf-strmif-ipin-receiveconnection) method. The output pin calls this method on the input pin with a proposed media type. The input pin accepts the connection or rejects it. If it rejects the connection, the output pin can try another media type. If no suitable types are found, the connection fails. Optionally, the input pin can advertise a list of types that it prefers, through the [**IPin::EnumMediaTypes**](/windows/desktop/api/Strmif/nf-strmif-ipin-enummediatypes) method. The output pin can use this list when it proposes media types, although it does not have to.

The **CTransformFilter** class implements a general framework for this process, as follows:

-   The input pin has no preferred media types. It relies entirely on the upstream filter to propose the media type. For video data, this makes sense, because the media type includes the image size and the frame rate. Typically, that information must be supplied by an upstream source filter or parser filter. In the case of audio data, the set of possible formats is smaller, so it may be practical for the input pin to offer some preferred types. In that case, override [**CBasePin::GetMediaType**](cbasepin-getmediatype.md) on the input pin.
-   When the upstream filter proposes a media type, the input pin calls the [**CTransformFilter::CheckInputType**](ctransformfilter-checkinputtype.md) method, which accepts or rejects the type.
-   The output pin will not connect unless the input pin is connected first. This behavior is typical for transform filters. In most cases, the filter must determine the input type before it can set the output type.
-   When the output pin does connect, it has a list of media types that it proposes to the downstream filter. It calls the [**CTransformFilter::GetMediaType**](ctransformfilter-getmediatype.md) method to generate this list. The output pin will also try any media types that the downstream filter proposes.
-   To check whether a particular output type is compatible with the input type, the output pin calls the [**CTransformFilter::CheckTransform**](ctransformfilter-checktransform.md) method.

The three **CTransformFilter** methods listed previously are pure virtual methods, so your derived class must implement them. None of these methods belongs to a COM interface; they are simply part of the implementation provided by the base classes.

The following sections describe each method in more detail:

-   [Step 3A. Implement the CheckInputType Method](step-3a--implement-the-checkinputtype-method.md)
-   [Step 3B. Implement the GetMediaType Method](step-3b--implement-the-getmediatype-method.md)
-   [Step 3C. Implement the CheckTransform Method](step-3c--implement-the-checktransform-method.md)

## Related topics

<dl> <dt>

[How Filters Connect](how-filters-connect.md)
</dt> <dt>

[Writing DirectShow Filters](writing-directshow-filters.md)
</dt> </dl>

 

 



