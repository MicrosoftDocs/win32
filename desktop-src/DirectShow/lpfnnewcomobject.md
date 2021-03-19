---
description: Pointer to a function that creates an instance of the object.
ms.assetid: 8c9dab82-a080-4733-8c62-d090b28306e0
title: LPFNNewCOMObject function pointer (Combase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LPFNNewCOMObject
api_type: 
- UserDefined
api_location: 
- Combase.h
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



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Combase.h (include Streams.h)</dt> </dl> |



## See also

<dl> <dt>

[**CFactoryTemplate Class**](cfactorytemplate.md)
</dt> </dl>

 

 




