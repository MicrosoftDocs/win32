---
description: CBasePin.Active method - The Active method notifies the pin that the filter is now active.
ms.assetid: 1054f8cf-a5fb-4de6-abf2-c3740ce47787
title: CBasePin.Active method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.Active
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBasePin.Active method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `Active` method notifies the pin that the filter is now active.

## Syntax


```C++
virtual HRESULT Active();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

When the filter goes from stopped to paused, the [**CBaseFilter**](cbasefilter.md) class calls this method on all of the filter's connected pins.

This method does nothing in the base class. Derived classes can override this method; for example, a pin might commit allocators or obtain hardware resources.

The filter graph manager's internal state is not updated until after this member function returns, so do not test the state from this method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




