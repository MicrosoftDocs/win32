---
Description: Uses the Microsoft Win32 SetThreadPriority function to set the priority of the thread to a new value.
ms.assetid: 5b8ad024-e651-47e5-b32a-c44d56c086cd
title: CMsgThread.SetThreadPriority method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CMsgThread.SetThreadPriority method

Uses the Microsoft Win32 **SetThreadPriority** function to set the priority of the thread to a new value.

## Syntax


```C++
BOOL SetThreadPriority(
   int nPriority
);
```



## Parameters

<dl> <dt>

*nPriority* 
</dt> <dd>

Priority of the thread.

</dd> </dl>

## Return value

Returns one of the following values.



| Return code                                                                              | Description                               |
|------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>****TRUE****</dt> </dl>  | Priority was successfully set.<br/> |
| <dl> <dt>****FALSE****</dt> </dl> | Priority was not set.<br/>          |



 

## Remarks

The client and the worker thread can call this member function.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Msgthrd.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMsgThread Class**](cmsgthread.md)
</dt> </dl>

 

 




