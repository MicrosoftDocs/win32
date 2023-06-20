---
description: CRenderedInputPin.EndFlush method - The EndFlush method ends a flush operation. This method implements the IPin::EndFlush method.
ms.assetid: 5c27bf76-6886-431d-9958-5064c53909ec
title: CRenderedInputPin.EndFlush method (Amextra.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRenderedInputPin.EndFlush
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CRenderedInputPin.EndFlush method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `EndFlush` method ends a flush operation. This method implements the [**IPin::EndFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-endflush) method.

## Syntax


```C++
HRESULT EndFlush();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK if successful, or an error code otherwise.

## Remarks

This method clears any pending [**EC\_COMPLETE**](ec-complete.md) events.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amextra.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CRenderedInputPin Class**](crenderedinputpin.md)
</dt> </dl>

 

 




