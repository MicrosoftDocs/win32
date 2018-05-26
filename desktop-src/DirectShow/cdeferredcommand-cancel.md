---
Description: The Cancel method cancels a previously queued CDeferredCommandInvoke request.
ms.assetid: 77671f6b-db50-4d8a-b727-aeed365f0303
title: CDeferredCommand.Cancel method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CDeferredCommand.Cancel method

The `Cancel` method cancels a previously queued [**CDeferredCommand::Invoke**](cdeferredcommand-invoke.md) request.

## Syntax


```C++
HRESULT Cancel();
```



## Parameters

This method has no parameters.

## Return value

Returns VFW\_E\_ALREADY\_CANCELLED if **m\_pQueue** is **NULL**. Returns an **HRESULT** from [**CCmdQueue::Remove**](ccmdqueue-remove.md) if the call generates an error. Returns S\_OK if successful.

## Remarks

This member function implements the [**IDeferredCommand::Cancel**](/windows/win32/Control/nf-control-ideferredcommand-cancel?branch=master) method.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDeferredCommand Class**](cdeferredcommand.md)
</dt> </dl>

 

 




