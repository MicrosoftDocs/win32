---
Description: The Insert method adds a CDeferredCommand object to the queue.
ms.assetid: 41f9c30c-6267-435a-9089-eb34ae606896
title: CCmdQueue.Insert method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CCmdQueue.Insert method

The `Insert` method adds a [**CDeferredCommand**](cdeferredcommand.md) object to the queue.

## Syntax


```C++
virtual HRESULT Insert(
   CDeferredCommand *pCmd
);
```



## Parameters

<dl> <dt>

*pCmd* 
</dt> <dd>

Pointer to the **CDeferredCommand** object to add to the queue.

</dd> </dl>

## Return value

Returns S\_OK in the default implementation.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CCmdQueue Class**](ccmdqueue.md)
</dt> </dl>

 

 




