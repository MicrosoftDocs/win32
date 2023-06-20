---
description: The GetState method retrieves the filters's state (running, stopped, or paused).
ms.assetid: 5d35824c-2509-499a-bbb1-1fb916b51808
title: CBaseRenderer.GetState method (Renbase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.GetState
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseRenderer.GetState method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `GetState` method retrieves the filters's state (running, stopped, or paused).

## Syntax


```C++
HRESULT GetState(
   DWORD        dwMilliSecsTimeout,
   FILTER_STATE *State
);
```



## Parameters

<dl> <dt>

*dwMilliSecsTimeout* 
</dt> <dd>

Time-out interval, in milliseconds.

</dd> <dt>

*State* 
</dt> <dd>

Pointer to a variable that receives a member of the [**FILTER\_STATE**](/windows/win32/api/strmif/ne-strmif-filter_state) enumerated type, indicating the filter's state.

</dd> </dl>

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                                                | Description                                                    |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | Success.<br/>                                            |
| <dl> <dt>**VFW\_S\_STATE\_INTERMEDIATE**</dt> </dl> | The filter is transitioning to the indicated state.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>                  | **NULL** pointer argument.<br/>                          |



 

## Remarks

This method overrides the [**CBaseFilter::GetState**](cbasefilter-getstate.md) method. When the renderer is paused, it does not complete the state transition until it receives a sample to render. If the time-out expires before the state transition is complete, the method returns VFW\_S\_STATE\_INTERMEDIATE.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




