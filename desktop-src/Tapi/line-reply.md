---
description: The TAPI LINE\_REPLY message is sent to report the results of function calls that completed asynchronously.
ms.assetid: 5d98ed8b-b75e-49f8-aba3-c6eee89e91c1
title: LINE_REPLY message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_REPLY message

The TAPI **LINE\_REPLY** message is sent to report the results of function calls that completed asynchronously.


```C++
            
```



## Parameters

<dl> <dt>

*hDevice* 
</dt> <dd>

Not used.

</dd> <dt>

*dwCallbackInstance* 
</dt> <dd>

Returns the application's callback instance.

</dd> <dt>

*dwParam1* 
</dt> <dd>

The request identifier for which this is the reply.

</dd> <dt>

*dwParam2* 
</dt> <dd>

The success or error indication. The application should cast this parameter into a LONG. Zero indicates success; a negative number indicates an error.

</dd> <dt>

*dwParam3* 
</dt> <dd>

Unused.

</dd> </dl>

## Return value

No return value.

## Remarks

Functions that operate asynchronously return a positive request identifier value to the application. This request identifier is returned with the reply message to identify the request that was completed. The other parameter for the **LINE\_REPLY** message carries the success or failure indication. Possible errors are the same as those defined by the corresponding function. This message cannot be disabled.

In some cases, an application may fail to receive the **LINE\_REPLY** message corresponding to a call to an asynchronous function. This occurs if the corresponding call handle is deallocated before the message has been received.

> [!Note]  
> When an application invokes any asynchronous operation that writes data back into application memory, the application must keep that memory available for writing until a **LINE\_REPLY** or [**LINE\_GATHERDIGITS**](line-gatherdigits.md) message is received.

 

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINE\_GATHERDIGITS**](line-gatherdigits.md)
</dt> </dl>

 

 




