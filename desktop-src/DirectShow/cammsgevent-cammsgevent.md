---
description: CAMMsgEvent.CAMMsgEvent constructor - Constructor method.
ms.assetid: 7871a624-70c0-4f21-b62a-2c4c2eaa762b
title: CAMMsgEvent.CAMMsgEvent constructor (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMMsgEvent.CAMMsgEvent
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAMMsgEvent.CAMMsgEvent constructor

Constructor method.

## Syntax


```C++
CAMMsgEvent(
   HRESULT *phr
);
```



## Parameters

<dl> <dt>

*phr* 
</dt> <dd>

Pointer to an **HRESULT** value. If the constructor fails, this parameter receives an error code. If this occurs, the object is not in a valid state.

For backward compatibility with earlier versions of strmbase.lib, this parameter defaults to **NULL**. However, passing a non-**NULL** value is preferred, so that the caller can check the status of the object.

</dd> </dl>

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMMsgEvent Class**](cammsgevent.md)
</dt> </dl>

 

 




