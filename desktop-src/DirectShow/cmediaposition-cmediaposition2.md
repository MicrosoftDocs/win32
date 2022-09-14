---
description: "Learn about the CMediaPosition.CMediaPosition (Ctlutil.h) constructor method. This method uses 'pName', 'pUnk', and 'phr' parameters."
ms.assetid: 4074f513-d1e7-4311-8732-4d755e621e55
title: CMediaPosition.CMediaPosition constructor (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMediaPosition.CMediaPosition
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMediaPosition.CMediaPosition constructor (Ctlutil.h) - pName, pUnk, phr parameters

Constructor method.

## Syntax


```C++
CMediaPosition(
   const TCHAR     *pName,
         LPUNKNOWN pUnk,
         HRESULT   *phr
);
```



## Parameters

<dl> <dt>

*pName* 
</dt> <dd>

Pointer to the name of the object, for debugging purposes. Allocate this parameter in static memory.

</dd> <dt>

*pUnk* 
</dt> <dd>

Pointer to the owner of this object, or **NULL** if the object is not aggregated.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to an **HRESULT** value.

</dd> </dl>

## Requirements

| Requirement | Value |
|-|-|
| Header | Ctlutil.h (include Streams.h) |
| Library| Strmbase.lib (retail builds); Strmbasd.lib (debug builds) |

## See also

<dl> <dt>

[**CMediaPosition Class**](cmediaposition.md)
</dt> </dl>

 

 




