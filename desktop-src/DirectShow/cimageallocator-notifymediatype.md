---
description: The NotifyMediaType method informs the object of the current media type.
ms.assetid: 6fb708ff-e968-4867-baca-ebe2515c9fab
title: CImageAllocator.NotifyMediaType method (Winutil.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImageAllocator.NotifyMediaType
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CImageAllocator.NotifyMediaType method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `NotifyMediaType` method informs the object of the current media type.

## Syntax


```C++
void NotifyMediaType(
   CMediaType *pMediaType
);
```



## Parameters

<dl> <dt>

*pMediaType* 
</dt> <dd>

Pointer to a [**CMediaType**](cmediatype.md) object, or **NULL** to clear the media type.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

The owning filter should call this method whenever the media type changes. Typically this occurs when the pin first connects, and after a dynamic format change. The allocator uses the media type to validate proposed allocator properties, and also when it creates media samples.

The **CImageAllocator** object stores the *pMediaType* pointer in the **m\_pMediaType** member variable. Therefore, if the caller needs to release the **CMediaType** object, it should update the allocator by calling this method again, either with a new pointer or with a **NULL** value. Otherwise, an error can occur when the allocator attempts to reference the old pointer.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImageAllocator Class**](cimageallocator.md)
</dt> </dl>

 

 




