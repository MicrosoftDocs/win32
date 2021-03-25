---
description: Constructor method.
ms.assetid: d7550c38-d728-41b2-80a6-20728abf6012
title: CImageSample.CImageSample constructor (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImageSample.CImageSample
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CImageSample.CImageSample constructor

Constructor method.

## Syntax


```C++
CImageSample(
   CBaseAllocator *pAllocator,
   TCHAR          *pName,
   HRESULT        *phr,
   LPBYTE         pBuffer,
   LONG           length
);
```



## Parameters

<dl> <dt>

*pAllocator* 
</dt> <dd>

Pointer to the allocator that created this sample.

</dd> <dt>

*pName* 
</dt> <dd>

Ignored.

</dd> <dt>

*phr* 
</dt> <dd>

Ignored.

</dd> <dt>

*pBuffer* 
</dt> <dd>

Pointer to a memory buffer allocated by the caller, of size *length*. The buffer should contain a GDI device-independent bitmap (DIB).

</dd> <dt>

*length* 
</dt> <dd>

Length of the buffer.

</dd> </dl>

## Remarks

The [**CImageAllocator**](cimageallocator.md) class creates a DIB using a file-mapping object that is backed by the operating-system paging file. The handle to the file-mapping object is stored in the **hMapping** member of the **m\_DibData** structure.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImageSample Class**](cimagesample.md)
</dt> </dl>

 

 




