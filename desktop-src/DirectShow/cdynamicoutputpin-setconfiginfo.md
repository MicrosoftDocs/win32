---
description: The SetConfigInfo method specifies the IGraphConfig pointer and the stop event.
ms.assetid: 938fe8be-5622-4954-9ba3-31fc68fbfa31
title: CDynamicOutputPin.SetConfigInfo method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDynamicOutputPin.SetConfigInfo
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CDynamicOutputPin.SetConfigInfo method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `SetConfigInfo` method specifies the [**IGraphConfig**](/windows/desktop/api/Strmif/nn-strmif-igraphconfig) pointer and the stop event.

## Syntax


```C++
void SetConfigInfo(
   IGraphConfig *pGraphConfig,
   HANDLE       hStopEvent
);
```



## Parameters

<dl> <dt>

*pGraphConfig* 
</dt> <dd>

Pointer to the [**IGraphConfig**](/windows/desktop/api/Strmif/nn-strmif-igraphconfig) interface, or **NULL**.

</dd> <dt>

*hStopEvent* 
</dt> <dd>

Handle to an event that is signaled when the filter stops, or **NULL**.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The filter must call this method when it joins the filter graph. The filter graph manager supports **IGraphConfig**. For the *hStopEvent* parameter, create a manual-reset event. When the filter leaves the filter graph, call this method again with **NULL** for both parameters.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 




