---
description: The GetPointer method retrieves a read/write pointer to the buffer. This method implements the IMediaSample::GetPointer method.
ms.assetid: dd797ad5-6066-4366-a56f-621132f2e6ea
title: CMediaSample.GetPointer method (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaSample.GetPointer
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaSample.GetPointer method

The `GetPointer` method retrieves a read/write pointer to the buffer. This method implements the [**IMediaSample::GetPointer**](/windows/desktop/api/Strmif/nf-strmif-imediasample-getpointer) method.

## Syntax


```C++
HRESULT GetPointer(
   BYTE **ppBuffer
);
```



## Parameters

<dl> <dt>

*ppBuffer* 
</dt> <dd>

Address of a variable that receives a pointer to the buffer.

</dd> </dl>

## Return value

Returns S\_OK.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




