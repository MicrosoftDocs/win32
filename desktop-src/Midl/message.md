---
title: message attribute
description: The \ message\ attribute indicates that the remote procedure call is to be treated as a message from the client to the server.
ms.assetid: ec616bf5-a845-4e7e-9f39-20947d2074f7
keywords:
- message attribute MIDL
topic_type:
- apiref
api_name:
- message
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# message attribute

The **\[message\]** attribute indicates that the remote procedure call is to be treated as a message from the client to the server.

``` syntax
[message, optional-attribute-list] void function-name(
    [in, optional-parameter-attributes] param-name,. . .);
```

## Parameters

<dl> <dt>

*optional-attribute-list* 
</dt> <dd>

Other attributes that apply to the function. Only the **\[**[**local**](local.md)**\]**, **\[**[**nocode**](nocode.md)**\]**, **\[**[**code**](code.md)**\],** and **\[**[**optimize**](optimize.md)**\]** attributes may be used with the **\[message\]** attribute.

</dd> <dt>

*function-name* 
</dt> <dd>

The name of the function as defined in the IDL file.

</dd> <dt>

*optional-parameter-attributes* 
</dt> <dd>

Zero or more MIDL attributes that will be applied to the parameter.

</dd> <dt>

*param-name* 
</dt> <dd>

The name of the parameter as defined in the IDL file.

</dd> </dl>

## Remarks

As messages from the client, remote procedure calls with the **\[message\]** attribute are delivered to the server asynchronously over the [**ncadg\_mq**](ncadg-mq.md) message-queuing transport. You can indicate synchronous-mode messaging by specifying the **ncadg\_mq** transport protocol without using the **\[message\]** attribute.

By specifying asynchronous-mode messaging, the **\[message\]** attribute allows the client to make the remote procedure call and return immediately, even when the server application is not responding. If the target server is not available, the call will be stored until the server becomes available.

In addition, asynchronous-mode messaging lets you control message-queue properties of the receive queue for the server. See [**RpcBindingSetOption**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcbindingsetoption) for more information on selecting quality of service, call priority, and call lifetime for the server process.

The following restrictions also apply to the **\[message\]** attribute:

-   Microsoft Message Queuing must be implemented in the client and server systems and the systems must be visible to each other as determined by the scope of the message queue installation.
-   The binding must use well-known endpoints and the [**ncadg\_mq**](ncadg-mq.md) transport protocol.
-   The function cannot contain output parameters or a return type other than [**void**](void.md). Note that the latter restriction makes the **\[message\]** attribute unsuitable for COM (object) interface methods, at this time. The next release of MIDL will permit **\[message\]** functions to return error\_status\_t or HRESULT.
-   Any interface that contains at least one **\[message\]** call must be registered by calling [**RpcServerRegisterIf**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcserverregisterif) or [**RpcServerRegisterIfEx**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcserverregisterifex) before calling [**RpcServerUseProtseqEpEx(ncadg\_mq)**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcserveruseprotseqepex). Otherwise, calls that were waiting on the queue for the server will be read before the interface is registered, and the calls will fail.

## Examples

``` syntax
[message] void DisplayString(
    [in, string] char * p1);
 
[message] void VarDataArray(
    [in, size_is(iSize)] ARRAY_TYPE lpMyArray,
    [in] int iSize,
    [in] unsigned long ulChksum);
```

## See also

<dl> <dt>

[**code**](code.md)
</dt> <dt>

[**local**](local.md)
</dt> <dt>

[**ncadg\_mq**](ncadg-mq.md)
</dt> <dt>

[**nocode**](nocode.md)
</dt> <dt>

[**optimize**](optimize.md)
</dt> <dt>

[RPC Message Queuing](/windows/desktop/Rpc/rpc-message-queuing)
</dt> <dt>

[**RpcBindingSetOption**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcbindingsetoption)
</dt> <dt>

[**RpcBindingInqOption**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcbindinginqoption)
</dt> <dt>

[**void**](void.md)
</dt> </dl>

 

 