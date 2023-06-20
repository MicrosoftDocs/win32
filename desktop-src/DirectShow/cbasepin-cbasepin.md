---
description: CBasePin.CBasePin constructor - Constructor method.
ms.assetid: e8cb5f1d-171f-4bf8-8ab6-6e547c4678d2
title: CBasePin.CBasePin constructor (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBasePin.CBasePin
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CBasePin.CBasePin constructor

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Constructor method.

## Syntax


```C++
CBasePin(
   TCHAR         *pObjectName,
   CBaseFilter   *pFilter,
   CCritSec      *pLock,
   HRESULT       *phr,
   LPCWSTR       pName,
   PIN_DIRECTION dir
);
```



## Parameters

<dl> <dt>

*pObjectName* 
</dt> <dd>

String containing the debug name for the object. For more information, see [**CBaseObject**](cbaseobject.md).

</dd> <dt>

*pFilter* 
</dt> <dd>

Pointer to the filter that created this pin.

</dd> <dt>

*pLock* 
</dt> <dd>

Pointer to a [**CCritSec**](ccritsec.md) lock, used to serialize state changes. Can be the same critical section as the filter lock, [**CBaseFilter::m\_pLock**](cbasefilter-m-plock.md).

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to a variable that receives an **HRESULT** value indicating the success or failure of the method. Initialize the value to S\_OK before creating the object. The value is changed only if an error occurs.

</dd> <dt>

*pName* 
</dt> <dd>

Wide-character string containing the name of the pin. For more information, see [**CBasePin::QueryPinInfo**](cbasepin-querypininfo.md).

</dd> <dt>

*dir* 
</dt> <dd>

Member of the [**PIN\_DIRECTION**](/windows/win32/api/strmif/ne-strmif-pin_direction) enumeration specifying the direction of the pin.

</dd> </dl>

## Remarks

The critical section specified by *pLock* serializes the pin's state, including its connection status, choice of allocator, media type, and the status of flush operations. Do not use this critical section to serialize streaming operations. For more information, see [Data Flow in the Filter Graph](data-flow-in-the-filter-graph.md).

A filter might create pins in its constructor method, so at this point the *pFilter* pointer might not refer to a valid object. Store the pointer, but do not dereference it while inside the pin's constructor.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




