---
description: Constructor method.
ms.assetid: 20c3c4af-b22f-4b74-a6b6-5ee309de4eef
title: CBaseObject.CBaseObject constructor (Combase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseObject.CBaseObject
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseObject.CBaseObject constructor

Constructor method.

## Syntax


```C++
CBaseObject(
   const TCHAR *pName
);
```



## Parameters

<dl> <dt>

*pName* 
</dt> <dd>

String that contains the name of the object, for debugging purposes.

</dd> </dl>

## Remarks

This method increments the active-object count. (See [**CBaseObject::ObjectsActive**](cbaseobject-objectsactive.md).)

Allocate the *pName* parameter in static memory:


```C++
// Correct.
CBaseObject *pObject = new CBaseObject(NAME("My Object"));

// Incorrect.
TCHAR ObjectName[] = TEXT("My Object");
CBaseObject *pObject = new CObject(ObjectName);
```



The [**NAME**](name.md) macro compiles to **NULL** in retail builds, so that static strings appear only in debug builds. For more information, see [**DbgDumpObjectRegister**](dbgdumpobjectregister.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Combase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseObject Class**](cbaseobject.md)
</dt> </dl>

 

 




