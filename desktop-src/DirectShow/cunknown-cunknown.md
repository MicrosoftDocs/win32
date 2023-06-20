---
description: CUnknown.CUnknown constructor - Constructor method.
ms.assetid: dafe0d5c-b4c8-4efb-8c47-a8c5db6e8aed
title: CUnknown.CUnknown constructor (Combase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CUnknown.CUnknown
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CUnknown.CUnknown constructor

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Constructor method.

## Syntax


```C++
CUnknown(
   const TCHAR     *pName,
         LPUNKNOWN pUnk
);
```



## Parameters

<dl> <dt>

*pName* 
</dt> <dd>

String containing the name of the object; used in the [**CBaseObject**](cbaseobject.md) constructor for debugging.

</dd> <dt>

*pUnk* 
</dt> <dd>

Pointer to the owner of this object. If the object is aggregated, pass a pointer to the aggregating object's IUnknown interface. Otherwise, set this parameter to **NULL**.

</dd> </dl>

## Remarks

The object is initialized with a reference count of zero.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




