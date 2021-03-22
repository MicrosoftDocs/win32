---
description: The GetClassID method retrieves the class identifier (CLSID) of the object. This method implements the IPersist::GetClassID method.
ms.assetid: 3d2cc6a3-67d1-4dd9-916b-7c350ce6a542
title: CSystemClock.GetClassID method (Sysclock.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSystemClock.GetClassID
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CSystemClock.GetClassID method

The `GetClassID` method retrieves the class identifier (CLSID) of the object. This method implements the **IPersist::GetClassID** method.

## Syntax


```C++
HRESULT GetClassID(
   CLSID *pClsID
);
```



## Parameters

<dl> <dt>

*pClsID* 
</dt> <dd>

Pointer to a variable that receives the value CLSID\_SystemClock.

</dd> </dl>

## Return value

Returns S\_OK or E\_POINTER.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | CSystemClock Class<br/>                                                                                                                                                              |
| Header<br/>  | <dl> <dt>Sysclock.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




