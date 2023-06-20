---
description: CTransformFilter.CTransformFilter constructor - Constructor method.
ms.assetid: a64c3e29-91f2-455f-aac1-1e4ecce6958d
title: CTransformFilter.CTransformFilter constructor (Transfrm.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformFilter.CTransformFilter
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CTransformFilter.CTransformFilter constructor

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Constructor method.

## Syntax


```C++
CTransformFilter(
   TCHAR     *pObjectName,
   LPUNKNOWN lpUnk,
   CLSID     clsid
);
```



## Parameters

<dl> <dt>

*pObjectName* 
</dt> <dd>

String containing the debug name of the filter. For more information, see [**CBaseObject**](cbaseobject.md).

</dd> <dt>

*lpUnk* 
</dt> <dd>

Pointer to the owner of this object. If the object is aggregated, pass a pointer to the aggregating object's **IUnknown** interface. Otherwise, set this parameter to **NULL**.

</dd> <dt>

*clsid* 
</dt> <dd>

Class identifier of the filter.

</dd> </dl>

## Remarks

The constructor does not create the filter's pins. That happens during the first call to the [**GetPin**](ctransformfilter-getpin.md) method. The constructor initializes the [**m\_pInput**](ctransformfilter-m-pinput.md) and [**m\_pOutput**](ctransformfilter-m-poutput.md) member variables to **NULL**.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




