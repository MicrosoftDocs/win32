---
description: Decrements the reference count on the object. This method implements the INonDelegatingUnknown::NonDelegatingRelease method.
ms.assetid: 58610f7d-5524-450f-a0f8-b299944abc78
title: CUnknown.NonDelegatingRelease method (Combase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CUnknown.NonDelegatingRelease
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CUnknown.NonDelegatingRelease method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Decrements the reference count on the object. This method implements the **INonDelegatingUnknown::NonDelegatingRelease** method.

## Syntax


```C++
ULONG NonDelegatingRelease();
```



## Parameters

This method has no parameters.

## Return value

Returns the reference count.

## Remarks

When the reference count reaches zero, the object deletes itself.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




