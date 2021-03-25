---
description: Constructor method.
ms.assetid: 8c215b16-98e5-42fb-a95b-b6df1ade180e
title: CImageAllocator.CImageAllocator constructor (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImageAllocator.CImageAllocator
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CImageAllocator.CImageAllocator constructor

Constructor method.

## Syntax


```C++
CImageAllocator(
   CBaseFilter *pFilter,
   TCHAR       *pName,
   HRESULT     *phr
);
```



## Parameters

<dl> <dt>

*pFilter* 
</dt> <dd>

Pointer to the owning filter.

</dd> <dt>

*pName* 
</dt> <dd>

Pointer to a string containing the debug name of the allocator. For more information, see [**CBaseObject**](cbaseobject.md).

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to an **HRESULT** value. Set the value to S\_OK before creating the object. If the constructor fails, the value is set to an error code.

</dd> </dl>

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImageAllocator Class**](cimageallocator.md)
</dt> </dl>

 

 




