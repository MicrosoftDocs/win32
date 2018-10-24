---
Description: Constructor method.
ms.assetid: 3f758c45-21ec-4728-ba7d-41da7b2fa02f
title: CMsgThread.CMsgThread constructor
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMsgThread.CMsgThread
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMsgThread.CMsgThread constructor

Constructor method.

## Syntax


```C++
CMsgThread();
```



## Parameters

This constructor has no parameters.

## Remarks

Constructing a message thread object does not automatically create the thread. You must call the [**CMsgThread::CreateThread**](cmsgthread-createthread.md) member function to create the thread.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Msgthrd.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMsgThread Class**](cmsgthread.md)
</dt> </dl>

 

 




