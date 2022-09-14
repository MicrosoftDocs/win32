---
description: CVideoTransformFilter.CVideoTransformFilter constructor - Constructor method.
ms.assetid: 4dad635f-4637-4f40-9f02-a91b59d05278
title: CVideoTransformFilter.CVideoTransformFilter constructor (Vtrans.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CVideoTransformFilter.CVideoTransformFilter
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CVideoTransformFilter.CVideoTransformFilter constructor

Constructor method.

## Syntax


```C++
CVideoTransformFilter(
   TCHAR     *pName,
   LPUNKNOWN pUnk,
   REFCLSID  clsid
);
```



## Parameters

<dl> <dt>

*pName* 
</dt> <dd>

String containing the debug name of the filter. For more information, see [**CBaseObject::CBaseObject**](cbaseobject-cbaseobject.md).

</dd> <dt>

*pUnk* 
</dt> <dd>

Pointer to the owner of this object. If the object is aggregated, pass a pointer to the aggregating object's **IUnknown** interface. Otherwise, set this parameter to **NULL**.

</dd> <dt>

*clsid* 
</dt> <dd>

Class identifier of the filter.

</dd> </dl>

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Vtrans.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CVideoTransformFilter Class**](cvideotransformfilter.md)
</dt> </dl>

 

 




