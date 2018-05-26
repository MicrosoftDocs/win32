---
Description: Constructor method.
ms.assetid: e8e9138a-6c39-41de-a7f8-d9e9c4fe5ab6
title: CCritSec.CCritSec constructor
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CCritSec.CCritSec constructor

Constructor method.

## Syntax


```C++
CCritSec();
```



## Parameters

This constructor has no parameters.

## Remarks

This method calls the [**InitializeCriticalSection**](https://msdn.microsoft.com/library/windows/desktop/ms683472) function to initialize the critical section.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CCritSec Class**](ccritsec.md)
</dt> </dl>

 

 




