---
Description: Constructor method.
ms.assetid: facc2c9d-034a-4fed-b6fe-77a40e36c305
title: CSystemClock.CSystemClock constructor
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CSystemClock.CSystemClock constructor

Constructor method.

## Syntax


```C++
CSystemClock(
   TCHAR     *pName,
   LPUNKNOWN pUnk,
   HRESULT   *phr
);
```



## Parameters

<dl> <dt>

*pName* 
</dt> <dd>

String containing the debug name of the object. For more information, see [**CBaseObject**](cbaseobject.md).

</dd> <dt>

*pUnk* 
</dt> <dd>

Pointer to the owner of this object. If the object is aggregated, pass a pointer to the aggregating object's **IUnknown** interface. Otherwise, set this parameter to **NULL**.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to the **HRESULT** value. If an error occurs, the method returns an error code in this parameter.

</dd> </dl>

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Sysclock.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 




