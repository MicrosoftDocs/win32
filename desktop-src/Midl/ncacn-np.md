---
title: ncacn_np attribute
description: The ncacn\_np keyword identifies named pipes as the protocol family for the endpoint.
ms.assetid: 02961bb8-faf0-42e5-b134-dd2983e6d146
keywords:
- ncacn_np attribute MIDL
topic_type:
- apiref
api_name:
- ncacn_np
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ncacn\_np attribute

The **ncacn\_np** keyword identifies named pipes as the protocol family for the endpoint.

``` syntax
endpoint("ncacn_np:server-name[\\pipe\\pipe-name]")
```

## Parameters

<dl> <dt>

*server-name* 
</dt> <dd>

Optional. Specifies the name of the server. Backslash characters are optional.

</dd> <dt>

*pipe-name* 
</dt> <dd>

Specifies a valid pipe name. A valid pipe name is a string containing identifiers separated by backslash characters. The first identifier must be [**pipe**](pipe.md). Each identifier must be separated by two backslash characters.

</dd> </dl>

## Remarks

A server creates an instance of a named pipe that is then available to any client. When a client attempts to connect, the existing instance is associated with that client. Before another client can connect, the server must create another instance of the named pipe. If a client tries to bind to the server before the new instance is created, the binding call, [**RpcBindingFromStringBinding**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcbindingfromstringbinding), may fail with the error message RPC\_S\_SERVER\_TOO\_BUSY. Therefore, you need to make sure that your client application handles the case where the server is too busy to accept a connection. The client should automatically retry, prompt the user for a course of action, or fail gracefully.

The syntax of the named-pipe port string, like all port strings, is defined by the transport implementation and is independent of the IDL specification. The MIDL compiler performs limited syntax checking but does not guarantee that the endpoint specification is correct. Some classes of errors may be reported at run time rather than at compile time.

## Examples

``` syntax
[
    uuid(12345678-4000-2006-0000-20000000001a), 
    version(1.1), 
    endpoint("ncacn_np:[\\pipe\\stove\\hat]") 
] 
interface iface1
{
    // Interface definition statements.
}

[
    uuid(87654321-4000-2006-0000-20000000001b), 
    version(1.1), 
    endpoint("ncacn_np:\\\\myotherserver[\\pipe\\corncob]") 
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

[**ncacn\_vns\_spp**](ncacn-vns-spp.md)
</dt> <dt>

[**ncalrpc**](ncalrpc.md)
</dt> <dt>

[**ncadg\_ipx**](ncadg-ipx.md)
</dt> <dt>

[**ncadg\_ip\_udp**](ncadg-ip-udp.md)
</dt> <dt>

[**string binding**](/windows/desktop/Rpc/string-binding)
</dt> </dl>

 

 