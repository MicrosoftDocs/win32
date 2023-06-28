---
description: The CTransformInputPin class implements an input pin that is used by the CTransformFilter class.
ms.assetid: 032da1bb-448d-48ea-ab3d-f721d790637f
title: CTransformInputPin class (Transfrm.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformInputPin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CTransformInputPin class

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

![ctransforminputpin class hierarchy](images/tfrm01.png)

The `CTransformInputPin` class implements an input pin that is used by the [**CTransformFilter**](ctransformfilter.md) class.

Typically, you do not need to derive from this class. Most of the methods in this class call corresponding methods on the **CTransformFilter** class, which you can override. If you derive from this class, you must override the filter's [**CTransformFilter::GetPin**](ctransformfilter-getpin.md) method to create instances of your derived class.



| Protected Member Variables                                           | Description                                                                            |
|----------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**m\_pTransformFilter**](ctransforminputpin-m-ptransformfilter.md) | Pointer to the owning filter.                                                          |
| Public Methods                                                       | Description                                                                            |
| [**CTransformInputPin**](ctransforminputpin-ctransforminputpin.md)  | Constructor method.                                                                    |
| [**CheckConnect**](ctransforminputpin-checkconnect.md)              | Determines whether a pin connection is suitable.                                       |
| [**BreakConnect**](ctransforminputpin-breakconnect.md)              | Releases the pin from a connection.                                                    |
| [**CompleteConnect**](ctransforminputpin-completeconnect.md)        | Completes a connection to another pin.                                                 |
| [**CheckMediaType**](ctransforminputpin-checkmediatype.md)          | Determines if the pin accepts a specific media type.                                   |
| [**SetMediaType**](ctransforminputpin-setmediatype.md)              | Sets the media type for the connection.                                                |
| [**CheckStreaming**](ctransforminputpin-checkstreaming.md)          | Determines whether the pin can accept samples. Virtual.                                |
| [**CurrentMediaType**](ctransforminputpin-currentmediatype.md)      | Retrieves the media type for the current pin connection.                               |
| IPin Methods                                                         | Description                                                                            |
| [**QueryId**](ctransforminputpin-queryid.md)                        | Retrieves an identifier for the pin.                                                   |
| [**EndOfStream**](ctransforminputpin-endofstream.md)                | Notifies the pin that no additional data is expected.                                  |
| [**BeginFlush**](ctransforminputpin-beginflush.md)                  | Begins a flush operation.                                                              |
| [**EndFlush**](ctransforminputpin-endflush.md)                      | Ends a flush operation.                                                                |
| [**NewSegment**](ctransforminputpin-newsegment.md)                  | Notifies the pin that media samples received after this call are grouped as a segment. |
| IMemInputPin Methods                                                 | Description                                                                            |
| [**Receive**](ctransforminputpin-receive.md)                        | Receives the next media sample in the stream.                                          |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




