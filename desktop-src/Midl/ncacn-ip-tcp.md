---
title: ncacn_ip_tcp attribute
description: The ncacn\_ip\_tcp keyword identifies TCP/IP as the protocol family for the endpoint.
ms.assetid: 8142c667-9a5f-4066-a36d-1bb5ce551d21
keywords:
- ncacn_ip_tcp attribute MIDL
topic_type:
- apiref
api_name:
- ncacn_ip_tcp
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ncacn\_ip\_tcp attribute

The **ncacn\_ip\_tcp** keyword identifies TCP/IP as the protocol family for the endpoint.

``` syntax
endpoint("ncacn_ip_tcp:server-name[port-name]")
```

## Parameters

<dl> <dt>

*server-name* 
</dt> <dd>

Specifies the name or Internet address for the server, or host, computer. The name is a character string. The Internet address is a common Internet address notation.

</dd> <dt>

*port-name* 
</dt> <dd>

Specifies an optional 16-bit number. Values of less than 1024 are usually reserved. If no value is specified, the endpoint-mapping service selects a valid *port-name* value.

</dd> </dl>

## Remarks

The syntax of the TCP/IP transport port string, like all port strings, is defined independently of the IDL specification. The compiler performs some syntax checking but does not guarantee that the endpoint specification is correct. Some errors may be reported at run time rather than at compile time.

## Examples

``` syntax
[   
    uuid(12345678-4000-2006-0000-20000000001a), 
    version(1.1), 
    endpoint("ncacn_ip_tcp:rainier[1404]") 
]
interface iface
{
    // Interface definition statements.
}

 
endpoint("ncacn_ip_tcp:128.10.2.30[1404]")
```

## See also

<dl> <dt>

[**endpoint**](endpoint.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**ncacn\_nb\_tcp**](ncacn-nb-tcp.md)
</dt> <dt>

[**ncacn\_np**](ncacn-np.md)
</dt> <dt>

[**ncacn\_spx**](ncacn-spx.md)
</dt> <dt>

[**ncalrpc**](ncalrpc.md)
</dt> <dt>

[**string binding**](/windows/desktop/Rpc/string-binding)
</dt> </dl>

 

 