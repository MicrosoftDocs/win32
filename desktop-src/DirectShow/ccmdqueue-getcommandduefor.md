---
description: The GetCommandDueFor method retrieves a deferred command that is scheduled at a specified time.
ms.assetid: f8a2f9ae-f359-4429-aca5-021b6fe2aa93
title: CCmdQueue.GetCommandDueFor method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CCmdQueue.GetCommandDueFor
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CCmdQueue.GetCommandDueFor method

The `GetCommandDueFor` method retrieves a deferred command that is scheduled at a specified time.

## Syntax


```C++
virtual HRESULT GetCommandDueFor(
   REFERENCE_TIME   tStream,
   CDeferredCommand **ppCmd
);
```



## Parameters

<dl> <dt>

*tStream* 
</dt> <dd>

Time for which the command is scheduled.

</dd> <dt>

*ppCmd* 
</dt> <dd>

Address of a pointer to the deferred command to be carried out at the time specified in the *tStream* parameter.

</dd> </dl>

## Return value

Returns VFW\_E\_NOT\_FOUND if no commands are due; otherwise, returns S\_OK.

## Remarks

This member function takes a stream time and returns the deferred command scheduled at that time. The actual stream-time offset is calculated when the command queue is run. Commands remain queued until run or canceled. This member function will not block.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CCmdQueue Class**](ccmdqueue.md)
</dt> </dl>

 

 




