---
Description: The GetClassID method retrieves the class identifier. This method implements the IPersistGetClassID method.
ms.assetid: 95038b11-b56f-4ab9-aefa-4735651c3731
title: CBaseMediaFilter.GetClassID method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseMediaFilter.GetClassID method

The `GetClassID` method retrieves the class identifier. This method implements the **IPersist::GetClassID** method.

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

Pointer to a variable that receives the class identifier.

</dd> </dl>

## Return value

Returns S\_OK or E\_POINTER.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseMediaFilter Class**](cbasemediafilter.md)
</dt> </dl>

 

 




