---
description: The Remove method removes the CDeferredCommand object from the queue.
ms.assetid: b3cff57d-9625-40db-b815-9529ac706f45
title: CCmdQueue.Remove method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CCmdQueue.Remove
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CCmdQueue.Remove method

The `Remove` method removes the [**CDeferredCommand**](cdeferredcommand.md) object from the queue.

## Syntax


```C++
virtual HRESULT Remove(
   CDeferredCommand *pCmd
);
```



## Parameters

<dl> <dt>

*pCmd* 
</dt> <dd>

Pointer to the **CDeferredCommand** object to remove from the queue.

</dd> </dl>

## Return value

Returns VFW\_E\_NOT\_FOUND if the object is not found in the queue. Otherwise, returns S\_OK.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CCmdQueue Class**](ccmdqueue.md)
</dt> </dl>

 

 




