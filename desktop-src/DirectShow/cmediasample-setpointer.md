---
description: The SetPointer method sets the pointer to the memory buffer.
ms.assetid: 60627600-c982-462e-b540-327a58e57615
title: CMediaSample.SetPointer method (Amfilter.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaSample.SetPointer
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
ms.custom: UpdateFrequency5
---

# CMediaSample.SetPointer method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The `SetPointer` method sets the pointer to the memory buffer.

## Syntax


```C++
HRESULT SetPointer(
   BYTE *ptr,
   LONG cBytes
);
```



## Parameters

<dl> <dt>

*ptr* 
</dt> <dd>

Pointer to a memory buffer allocated by the caller, of size *cBytes*.

</dd> <dt>

*cBytes* 
</dt> <dd>

Length of the buffer, in bytes.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

This method enables the allocator to set a new pointer for the sample.

This method is not available through the [**IMediaSample**](/windows/desktop/api/Strmif/nn-strmif-imediasample) interface. The object that creates the sample can access this method (through **CMediaSample**), but other objects cannot.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




