---
description: The REFERENCE\_TIME() operator casts the object to a REFERENCE\_TIME data type.
ms.assetid: 36f51e03-a458-46e6-9657-977b263c127f
title: CRefTime.operator REFERENCE_TIME method (Reftime.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRefTime.operator
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CRefTime.operator REFERENCE\_TIME method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `REFERENCE_TIME()` operator casts the object to a [**REFERENCE\_TIME**](reference-time.md) data type.

## Syntax


```C++
REFERENCE_TIME operator REFERENCE_TIME() const;
```



## Parameters

This method has no parameters.

## Return value

Returns the value of [**CRefTime::m\_time**](creftime-m-time.md).

## Remarks

The following example shows how to use this cast operator:


```C++
CRefTime cRT(1000);
REFERENCE_TIME rt = (REFERENCE_TIME)cRT;
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Reftime.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




