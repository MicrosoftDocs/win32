---
description: The TAPI LINE\_PROXYREQUEST message delivers a request to a registered proxy function handler.
ms.assetid: 7f33de55-2482-4558-bd86-ee2ac1e31269
title: LINE_PROXYREQUEST message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_PROXYREQUEST message

The TAPI **LINE\_PROXYREQUEST** message delivers a request to a registered proxy function handler.


```C++
            
```



## Parameters

<dl> <dt>

*hDevice* 
</dt> <dd>

The application's handle to the line device on which the agent status has changed.

</dd> <dt>

*dwCallbackInstance* 
</dt> <dd>

The callback instance supplied when opening the call's line.

</dd> <dt>

*dwParam1* 
</dt> <dd>

Pointer to a [**LINEPROXYREQUEST**](/windows/desktop/api/Tapi/ns-tapi-lineproxyrequest) structure containing the request to be processed by the proxy handler application.

</dd> <dt>

*dwParam2* 
</dt> <dd>

Reserved.

</dd> <dt>

*dwParam3* 
</dt> <dd>

Reserved.

</dd> </dl>

## Return value

No return value.

## Remarks

The **LINE\_PROXYREQUEST** message is sent only to the first application that registered to handle proxy requests of the type being delivered.

The application should process the request contained in the proxy buffer and call [**lineProxyResponse**](/windows/desktop/api/Tapi/nf-tapi-lineproxyresponse) to return data or deliver results. Processing of the request should be done within the context of the application's TAPI callback function only if it can be performed immediately, without waiting for response from any other entity. If the application needs to communicate with other entities (for example, a service provider to handle PBX-based ACD, or any other system service which might result in blocking), then the request should be queued within the application and the callback function exited to avoid delaying the receipt of further TAPI messages by the application.

At the time the **LINE\_PROXYREQUEST** is delivered to the proxy handler, TAPI has already returned a positive *dwRequestID* function result to the original application and unblocked the calling thread to continue execution. The application is awaiting a [**LINE\_REPLY**](line-reply.md) message, which is automatically generated when the proxy handler application calls [**lineProxyResponse**](/windows/desktop/api/Tapi/nf-tapi-lineproxyresponse).

The application shall not free the memory pointed to by *lpProxyRequest*. TAPI frees the memory during the execution of [**lineProxyResponse**](/windows/desktop/api/Tapi/nf-tapi-lineproxyresponse). The application can call [**lineProxyResponse**](/windows/desktop/api/Tapi/nf-tapi-lineproxyresponse) exactly once for each **LINE\_PROXYREQUEST** message.

If the application receives a [**LINE\_CLOSE**](line-close.md) message while it has pending proxy requests, it should call [**lineProxyResponse**](/windows/desktop/api/Tapi/nf-tapi-lineproxyresponse) for each pending request, passing in an appropriate *dwResult* value (such as LINEERR\_OPERATIONFAILED).

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINE\_CLOSE**](line-close.md)
</dt> <dt>

[**LINE\_REPLY**](line-reply.md)
</dt> <dt>

[**LINEPROXYREQUEST**](/windows/desktop/api/Tapi/ns-tapi-lineproxyrequest)
</dt> <dt>

[**lineProxyResponse**](/windows/desktop/api/Tapi/nf-tapi-lineproxyresponse)
</dt> </dl>

 

 




