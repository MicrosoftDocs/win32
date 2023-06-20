---
description: The WaitForRenderTime method waits for the current sample's presentation time.
ms.assetid: a6acb780-48df-4f73-adcb-cfa4e54b19ac
title: CBaseRenderer.WaitForRenderTime method (Renbase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.WaitForRenderTime
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseRenderer.WaitForRenderTime method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `WaitForRenderTime` method waits for the current sample's presentation time.

## Syntax


```C++
virtual HRESULT WaitForRenderTime();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the following **HRESULT** values.



| Return code                                                                                           | Description                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                  | Success.<br/>                                                       |
| <dl> <dt>**VFW\_E\_STATE\_CHANGED**</dt> </dl> | The filter state changed before the presentation time arrived.<br/> |



 

## Remarks

This method waits until one of the following occurs:

-   The sample's presentation time arrives, at which point the sample can be rendered.
-   The filter stops or begins flushing data.

If the presentation time arrives, the [**CBaseRenderer::m\_RenderEvent**](cbaserenderer-m-renderevent.md) event is signaled. If the state changes, the [**CBaseRenderer::m\_ThreadSignal**](cbaserenderer-m-threadsignal.md) event is signaled. This method waits on both events. The derived class can override this method to wait on additional events, if necessary.

This method calls the [**CBaseRenderer::OnWaitStart**](cbaserenderer-onwaitstart.md) method when the wait begins, and the [**CBaseRenderer::OnWaitEnd**](cbaserenderer-onwaitend.md) method when the wait is done. Neither method does anything in the base class, but the derived class can override them.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




