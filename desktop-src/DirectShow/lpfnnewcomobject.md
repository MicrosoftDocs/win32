---
Description: Pointer to a function that creates an instance of the object.
ms.assetid: 8c9dab82-a080-4733-8c62-d090b28306e0
title: LPFNNewCOMObject function pointer
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LPFNNewCOMObject function pointer

Pointer to a function that creates an instance of the object.

## Syntax


```C++
typedef CUnknown* ( CALLBACK *LPFNNewCOMObject)(
   LPUNKNOWN pUnkOuter,
   HRESULT   *phr
);
```



## Parameters

<dl> <dt>

*pUnkOuter* 
</dt> <dd>

Pointer to the **IUnknown** interface of the object that aggregates the new object, if any. This pointer can be **NULL**.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to an **HRESULT** value. If the constructor fails, this parameter receives an error code.

</dd> </dl>

## Return value

Returns a pointer to a new instance of the object.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Combase.h (include Streams.h)</dt> </dl> |



## See also

<dl> <dt>

[**CFactoryTemplate Class**](cfactorytemplate.md)
</dt> </dl>

 

 




