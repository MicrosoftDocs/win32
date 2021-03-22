---
description: Constructor method.
ms.assetid: 3ee67cfd-a968-4b7c-9c7b-1c28ddb9c343
title: CMediaSample.CMediaSample constructor (Amfilter.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaSample.CMediaSample
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaSample.CMediaSample constructor

Constructor method.

## Syntax


```C++
CMediaSample(
   TCHAR          *pName,
   CBaseAllocator *pAllocator,
   HRESULT        *phr,
   LPBYTE         pBuffer = NULL,
   LONG           length = 0
);
```



## Parameters

<dl> <dt>

*pName* 
</dt> <dd>

Ignored.

</dd> <dt>

*pAllocator* 
</dt> <dd>

Pointer to the [**CBaseAllocator**](cbaseallocator.md) object that created this sample.

</dd> <dt>

*phr* 
</dt> <dd>

Ignored.

</dd> <dt>

*pBuffer* 
</dt> <dd>

Pointer to a memory buffer allocated by the caller, of size *length*.

</dd> <dt>

*length* 
</dt> <dd>

Length of the memory buffer.

</dd> </dl>

## Remarks

The base class does not modify the **HRESULT** value passed in the *phr* parameter.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaSample Class**](cmediasample.md)
</dt> </dl>

 

 




