---
Description: Destructor method.
ms.assetid: cade850c-391c-41dc-adfe-56de8b2bbfff
title: CCritSec.~CCritSec destructor
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CCritSec.~CCritSec
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
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

 

 




