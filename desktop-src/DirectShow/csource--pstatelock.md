---
description: The pStateLock method retrieves a pointer to the filter's critical section object.
ms.assetid: 10a2e74b-a5aa-4d68-958e-d86f4b78037e
title: CSource.pStateLock method (Source.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSource.pStateLock
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CSource.pStateLock method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **pStateLock** method retrieves a pointer to the filter's critical section object.

> [!Note]  
> Although named like a member variable, **pStateLock** is a method.

 

## Syntax


```C++
CCritSec* pStateLock();
```



## Parameters

This method has no parameters.

## Return value

Returns a pointer to the [**CSource::m\_cStateLock**](csource-m-cstatelock.md) member variable.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Source.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSource Class**](csource.md)
</dt> </dl>

 

 




