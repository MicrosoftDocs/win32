---
Description: The Run method switches to running mode so that commands that are deferred by the stream time can be run.
ms.assetid: c529ae84-c9b7-46f1-a1e4-716fc9e9df13
title: CCmdQueue.Run method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CCmdQueue.Run method

The `Run` method switches to running mode so that commands that are deferred by the stream time can be run.

## Syntax


```C++
virtual HRESULT Run(
   REFERENCE_TIME tStreamTimeOffset
);
```



## Parameters

<dl> <dt>

*tStreamTimeOffset* 
</dt> <dd>

Offset time.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

During running mode, stream-time-to-presentation-time mapping is known.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CCmdQueue Class**](ccmdqueue.md)
</dt> </dl>

 

 




