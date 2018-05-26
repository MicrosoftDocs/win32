---
Description: Constructor method.
ms.assetid: e31253fc-b365-4414-9dee-906d4c41d16e
title: CSeekingPassThru.CSeekingPassThru constructor
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CSeekingPassThru.CSeekingPassThru constructor

Constructor method.

## Syntax


```C++
CSeekingPassThru(
   const TCHAR     *pName,
         LPUNKNOWN pUnk,
         HRESULT   *phr
);
```



## Parameters

<dl> <dt>

*pName* 
</dt> <dd>

String containing the name of the object. See [**CBaseObject**](cbaseobject.md) for more information.

</dd> <dt>

*pUnk* 
</dt> <dd>

Pointer to the owner of this object. If the object is aggregated, pass a pointer to the aggregating object's **IUnknown** interface. Otherwise, set this parameter to **NULL**.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to an **HRESULT** value. Ignored.

</dd> </dl>

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Seekpt.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CSeekingPassThru Class**](cseekingpassthru.md)
</dt> </dl>

 

 




