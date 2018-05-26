---
Description: Constructor method. The constructor locks the specified critical section object.
ms.assetid: 5a0d74f9-bb99-4922-9a92-2e7c1863421f
title: CAutoLock.CAutoLock constructor
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAutoLock Class**](cautolock.md)
</dt> </dl>

 

 




