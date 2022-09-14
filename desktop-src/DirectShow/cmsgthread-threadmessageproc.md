---
description: Processes requests. This is a pure virtual member function.
ms.assetid: ffdbc287-ca17-44e4-b00a-d72a2367f510
title: CMsgThread.ThreadMessageProc method (Msgthrd.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CMsgThread.ThreadMessageProc
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CMsgThread.ThreadMessageProc method

Processes requests. This is a pure virtual member function.

## Syntax


```C++
virtual LRESULT ThreadMessageProc(
   UINT     uMsg,
   DWORD    dwFlags,
   LPVOID   lpParam,
   CAMEvent *pEvent
);
```



## Parameters

<dl> <dt>

*uMsg* 
</dt> <dd>

Request code.

</dd> <dt>

*dwFlags* 
</dt> <dd>

Optional flag parameter to request.

</dd> <dt>

*lpParam* 
</dt> <dd>

Optional pointer to extra data or a return data block.

</dd> <dt>

*pEvent* 
</dt> <dd>

Optional pointer to an event object.

</dd> </dl>

## Return value

Any nonzero return causes the thread to exit. Returns zero unless an exit request has been processed recently.

## Remarks

This pure virtual function must be overridden in your derived class. It will be called once for each request queued by a call to the [**CMsgThread::PutThreadMsg**](cmsgthread-putthreadmsg.md) member function.

The member function defines the four parameters. Typically, use the *uMsg* parameter to indicate the request, and the other three parameters will be optional additional parameters. The calling application can supply a pointer to a [**CAMEvent**](camevent.md) object in the *pEvent* parameter if your application requires it. You must set this event after processing the event by using an expression such as:


```C++
pEvent->SetEvent
```



One request code must be set aside to tell the worker thread to exit. Upon receiving this request, return 1 from this member function. Return 0 if you do not want the worker thread to exit.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Msgthrd.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMsgThread Class**](cmsgthread.md)
</dt> </dl>

 

 




