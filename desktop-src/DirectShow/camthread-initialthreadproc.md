---
description: The InitialThreadProc method calls the main thread procedure.
ms.assetid: 1546c214-7ea9-4484-974b-dbd4b2b3e296
title: CAMThread.InitialThreadProc method (Wxutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAMThread.InitialThreadProc
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CAMThread.InitialThreadProc method

The `InitialThreadProc` method calls the main thread procedure.

## Syntax


```C++
DWORD InitialThreadProc(
   LPVOID pv
);
```



## Parameters

<dl> <dt>

*pv* 
</dt> <dd>

`this` pointer.

</dd> </dl>

## Return value

Returns the **DWORD** returned by [**CAMThread::ThreadProc**](camthread-threadproc.md). The derived class defines this value.

## Remarks

The [**CAMThread::Create**](camthread-create.md) method uses this method for the thread procedure when it creates the thread. It uses the `this` pointer as the thread argument.

This method calls the [**CAMThread::CoInitializeHelper**](camthread-coinitializehelper.md) method and then ThreadProc.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxutil.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CAMThread Class**](camthread.md)
</dt> </dl>

 

 




