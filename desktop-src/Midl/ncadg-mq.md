---
title: ncadg_mq attribute
description: The ncadg\_mq keyword identifies Microsoft Message Queuing Services (MSMQ) as the transport protocol for the endpoint. This protocol is obsolete and should not be used in new applications.
ms.assetid: 7472fc47-c1f0-4578-8aef-b655505e0563
keywords:
- ncadg_mq attribute MIDL
topic_type:
- apiref
api_name:
- ncadg_mq
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ncadg\_mq attribute

The **ncadg\_mq** keyword identifies Microsoft Message Queuing Services (MSMQ) as the transport protocol for the endpoint. This protocol is obsolete and should not be used in new applications.

``` syntax
endpoint("ncadg_mq:server-name")
```

## Parameters

<dl> <dt>

*server-name* 
</dt> <dd>

Specifies the name of the server, or host, computer. The name is a character string and may be a fully qualified domain name.

</dd> </dl>

## Remarks

In order to use the **ncadg\_mq** transport protocol, the MSMQ components must be fully installed and the client and server systems must be reachable through the MQ protocols.

The **ncadg\_mq** protocol does not support dynamic endpoints or [**broadcast**](broadcast.md) calls. As with other datagram protocols, **ncadg\_mq** does not support callbacks; any functions using the [**callback**](callback.md) attribute will fail.

> [!Note]  
> This protocol family is not supported in WindowsÂ XP.

 

## Examples

The syntax of the message-queue protocol is defined independently of the IDL specification. The MIDL compiler performs some syntax checking but does not guarantee that the endpoint specification is correct. Some errors may be reported at run time rather than during compilation.

``` syntax
[
    uuid(12345678-4000-2006-0000-20000000001a), 
    version(1.1), 
    endpoint("ncadg_mq:rainier") 
]
interface iface
{
    // Interface definition statements.
}
```

## See also

<dl> <dt>

[**broadcast**](broadcast.md)
</dt> <dt>

[**callback**](callback.md)
</dt> <dt>

[**endpoint**](endpoint.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**message**](message.md)
</dt> <dt>

[RPC Message Queuing](/windows/desktop/Rpc/rpc-message-queuing)
</dt> <dt>

[String Binding](/windows/desktop/Rpc/string-binding)
</dt> </dl>

 

 