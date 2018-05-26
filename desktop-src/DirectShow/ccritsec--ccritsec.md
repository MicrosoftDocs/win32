---
Description: Destructor method.
ms.assetid: cade850c-391c-41dc-adfe-56de8b2bbfff
title: CCritSec.~CCritSec destructor
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CCritSec.~CCritSec destructor

Destructor method.

## Syntax


```C++
~CCritSec();
```



## Remarks

This method calls the [**DeleteCriticalSection**](https://msdn.microsoft.com/library/windows/desktop/ms682552) function to delete the critical section.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CCritSec Class**](ccritsec.md)
</dt> </dl>

 

 




