---
description: The EndOfStream method notifies the pin that no additional data is expected. This method implements the IPin::EndOfStream method. Call this method only on input pins.
ms.assetid: 52a71c30-bd68-4152-8901-71ef2e65913a
title: CBasePin.EndOfStream method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.EndOfStream
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBasePin.EndOfStream method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `EndOfStream` method notifies the pin that no additional data is expected. This method implements the [**IPin::EndOfStream**](/windows/desktop/api/Strmif/nf-strmif-ipin-endofstream) method. Call this method only on input pins.

## Syntax


```C++
HRESULT EndOfStream();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

The filter should pass end-of-stream notifications downstream, to the input pins of connected filters. If the filter is a renderer, it should post an [**EC\_COMPLETE**](ec-complete.md) event notification to the filter graph manager. For more information, see [Data Flow in the Filter Graph](data-flow-in-the-filter-graph.md).

In the base class, this method does nothing. Derived classes should override this method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




