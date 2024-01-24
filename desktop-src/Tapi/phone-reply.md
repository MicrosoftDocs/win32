---
description: The TAPI PHONE\_REPLY message is sent to an application to report the results of function call that completed asynchronously.
ms.assetid: 434f37d6-f385-4cc9-9658-2b683cab532c
title: PHONE_REPLY message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PHONE\_REPLY message

The TAPI **PHONE\_REPLY** message is sent to an application to report the results of function call that completed asynchronously.


```C++
            
```



## Parameters

<dl> <dt>

*hPhone* 
</dt> <dd>

Unused.

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

Functions that operate asynchronously return a positive request identifier value to the application. This request identifier is returned with the reply message to identify the request that was completed. The other parameter for the **PHONE\_REPLY** message carries the success or failure indication. Possible errors are the same as those defined by the corresponding function. This message cannot be disabled.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




