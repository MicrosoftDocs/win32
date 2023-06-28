---
description: The GetOwner method retrieves a pointer to the IUnknown interface of the owning component. For an aggregated component, the owner is the outer component. Otherwise, the component owns itself.
ms.assetid: 7d8af9d1-52c0-4f2b-9d05-6ddff85ab508
title: CUnknown.GetOwner method (Combase.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CUnknown.GetOwner
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CUnknown.GetOwner method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `GetOwner` method retrieves a pointer to the **IUnknown** interface of the owning component. For an aggregated component, the owner is the outer component. Otherwise, the component owns itself.

## Syntax


```C++
LPUNKNOWN GetOwner();
```



## Parameters

This method has no parameters.

## Return value

Returns a pointer to the controlling **IUnknown** interface.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




