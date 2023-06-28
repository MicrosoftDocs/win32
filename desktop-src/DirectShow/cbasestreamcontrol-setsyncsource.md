---
description: The SetSyncSource method notifies the base class of the current reference clock.
ms.assetid: 056385ac-682c-456e-9a5f-86490bd6e05f
title: CBaseStreamControl.SetSyncSource method (Strmctl.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseStreamControl.SetSyncSource
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBaseStreamControl.SetSyncSource method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `SetSyncSource` method notifies the base class of the current reference clock.

## Syntax


```C++
void SetSyncSource(
   IReferenceClock *pRefClock
);
```



## Parameters

<dl> <dt>

*pRefClock* 
</dt> <dd>

Pointer to the [**IReferenceClock**](/windows/desktop/api/Strmif/nn-strmif-ireferenceclock) interface of the reference clock.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Call this method from inside the filter's [**IMediaFilter::SetSyncSource**](/windows/desktop/api/Strmif/nf-strmif-imediafilter-setsyncsource) method. The **CBaseStreamControl** class uses the **IReferenceClock** interface to ensure that it does not discard samples too quickly.

## Examples


```C++
STDMETHODIMP CMyFilter::SetSyncSource(IReferenceClock *pClock)
{
    // Note: It's OK if pClock is NULL.

    m_pMyPin->SetSyncSource(pClock);
    return CBaseFilter::SetSyncSource(pClock);
}
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Strmctl.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseStreamControl Class**](cbasestreamcontrol.md)
</dt> </dl>

 

 




