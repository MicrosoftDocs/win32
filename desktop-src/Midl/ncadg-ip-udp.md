---
title: ncadg_ip_udp attribute
description: The ncadg\_ip\_udp keyword identifies the datagram version of TCP/IP as the protocol family for the endpoint. This protocol family is obsolete and should not be used in new applications.
ms.assetid: c9133fcc-6dc2-49da-9c6f-5ce3c51090d5
keywords:
- ncadg_ip_udp attribute MIDL
topic_type:
- apiref
api_name:
- ncadg_ip_udp
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ncadg\_ip\_udp attribute

The **ncadg\_ip\_udp** keyword identifies the datagram version of TCP/IP as the protocol family for the endpoint. This protocol family is obsolete and should not be used in new applications.

``` syntax
endpoint("ncadg_ip_udp:server-name[port-name]")
```

## Parameters

<dl> <dt>

*server-name* 
</dt> <dd>

Specifies the name or internet address for the server, or host, computer. The name is a character string and may be a fully qualified domain name. The internet address is a common internet address notation.

</dd> <dt>

*port-name* 
</dt> <dd>

Specifies an optional 16-bit number. Values of less than 1024 are usually reserved. If no value is specified, the endpoint-mapping service selects a valid *port-name* value.

</dd> </dl>

## Remarks

The following restrictions apply to the datagram protocols, [**ncadg\_ipx**](ncadg-ipx.md) and **ncadg\_ip\_udp**:

-   They do not support callbacks. Any functions using the **\[**[**callback**](callback.md)**\]** attribute will fail.
-   They do not support use of the [**pipe**](pipe.md) type constructor.

The syntax of the TCP/IP transport port string, like all port strings, is defined independently of the IDL specification. The compiler performs some syntax checking but does not guarantee that the endpoint specification is correct. Some errors may be reported at run time rather than at compile time.

## Examples

``` syntax
[
    uuid(12345678-4000-2006-0000-20000000001a), 
    version(1.1), 
    endpoint("ncadg_ip_udp:rainier[1404]") 
]
interface iface1
{
    // Interface definition statements.
}

[
    uuid(87654321-4000-2006-0000-20000000001a), 
    version(1.1), 
    endpoint("ncadg_ip_udp:128.10.2.30[1404]") 
]
interface iface2
{
    // Interface definition statements.
}
```

## See also

<dl> <dt>

[**endpoint**](endpoint.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**ncacn\_at\_dsp**](ncacn-at-dsp.md)
</dt> <dt>

[**ncacn\_dnet\_nsp**](ncacn-dnet-nsp.md)
</dt> <dt>

[**ncacn\_ip\_tcp**](ncacn-ip-tcp.md)
</dt> <dt>

[**ncacn\_nb\_ipx**](ncacn-nb-ipx.md)
</dt> <dt>

[**ncacn\_spx**](ncacn-spx.md)
</dt> <dt>

[**ncacn\_nb\_nb**](ncacn-nb-nb.md)
</dt> <dt>

[**ncacn\_nb\_tcp**](ncacn-nb-tcp.md)
</dt> <dt>

[**ncacn\_np**](ncacn-np.md)
</dt> <dt>

[**ncacn\_vns\_spp**](ncacn-vns-spp.md)
</dt> <dt>

[**ncalrpc**](ncalrpc.md)
</dt> <dt>

[**ncadg\_ipx**](ncadg-ipx.md)
</dt> <dt>

[String Binding](/windows/desktop/Rpc/string-binding)
</dt> </dl>

 

 