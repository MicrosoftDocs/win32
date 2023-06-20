---
description: CSourcePosition is an abstract class for implementing the IMediaPosition interface on a source filter.
ms.assetid: 838d2efd-6870-4412-98e2-fb2628e14bf3
title: CSourcePosition class
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourcePosition
api_type: 
- COM
api_location: 
ms.custom: UpdateFrequency5
---

# CSourcePosition class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

`CSourcePosition` is an abstract class for implementing the [**IMediaPosition**](/windows/desktop/api/Control/nn-control-imediaposition) interface on a source filter.

This class is obsolete. If your source filter is seekable, it should expose the [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking) interface instead of **IMediaPosition**. You can use the [**CSourceSeeking**](csourceseeking.md) base class for this purpose.

 

 



