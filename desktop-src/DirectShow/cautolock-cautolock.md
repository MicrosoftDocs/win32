---
description: Constructor method. The constructor locks the specified critical section object.
ms.assetid: 5a0d74f9-bb99-4922-9a92-2e7c1863421f
title: CAutoLock.CAutoLock constructor (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAutoLock.CAutoLock
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAutoLock.CAutoLock constructor

Constructor method. The constructor locks the specified critical section object.

## Syntax


```C++
CAutoLock(
   CCritSec *plock
);
```



## Parameters

<dl> <dt>

*plock* 
</dt> <dd>

Pointer to a [**CCritSec**](ccritsec.md) object, which contains a critical section object.

</dd> </dl>

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAutoLock Class**](cautolock.md)
</dt> </dl>

 

 




