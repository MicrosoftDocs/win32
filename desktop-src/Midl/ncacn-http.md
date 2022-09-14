---
title: ncacn_http attribute
description: The ncacn\_http keyword identifies the Microsoft Internet Information Server (IIS) as the protocol family for the endpoint.
ms.assetid: 92d2b44c-2eab-4474-826b-ccafd26db124
keywords:
- ncacn_http attribute MIDL
topic_type:
- apiref
api_name:
- ncacn_http
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ncacn\_http attribute

The **ncacn\_http** keyword identifies the Microsoft Internet Information Server (IIS) as the protocol family for the endpoint.

``` syntax
ncacn_http:rpc_server[endpoint]
```

## Parameters

<dl> <dt>

*rpc\_server* 
</dt> <dd>

The Internet address or name of the machine that the RPC server process is running on.

</dd> <dt>

*endpoint* 
</dt> <dd>

The well-known (static) TCP/IP port that the RPC server process is listening on.

</dd> </dl>

## Remarks

Identifying the Microsoft Internet Information Server (IIS) as the protocol family allows client and server applications to communicate across the internet by using the Microsoft Internet Information Server (IIS) as a proxy. Because calls are tunneled through an established HTTP port, they can cross firewalls.

Any RPC client and server applications can support the **ncacn\_http** protocol as long as they are networked to an Internet Information Server. The IIS contacts the RPC server and establishes a TCP/IP socket, which it maintains for the client. The IIS negotiates a TCP/IP connection with the RPC server, and once the negotiation is complete, acts as an RPC proxy, forwarding data between the client-side TCP/IP socket and the server-side TCP/IP socket. When the IIS RPC proxy detects a session close on either the client or the server side, it closes the remaining socket.

The client application implicitly uses static binding to the IIS, but the server can use dynamic endpoints, with the server's RPCSS (endpoint mapper) resolving the RPC server port. If the IIS is on a different machine than the RPC server, the IIS receives the remote call, contacts RPCSS on the RPC server machine to get the server process endpoint, and then forwards the call to the appropriate RPC server.

If Internet Explorer is installed, the transport will check the registry to see if there is a configuration for an HTTP proxy. If a proxy exists, the transport will use it.

## Examples

``` syntax
//RPC client accesses an RPC server application, which is listening on //endpoint 2225 of an IIS Web Server named major7.microsoft.com 
[   
    uuid(12345678-1234-1234-1234-123456789ABC), 
    version(1.0), 
    endpoint("ncacn_http:major7.microsoft.com[2225]") 
] 
interface iface
{
    // Interface definition statements.
}

//string binding format. 
//IIS Web server (websvr1)is on a different machine than the RPC
//server, and endpoints are dynamic
"obj_uuid@ncacn_http:major7.microsoft.com
    [,]"

//tells the transport to use proxysvr, port 80, as the outgoing http 
//server:
"obj_uuid@ncacn_http:major7.microsoft.com[,]"
```

## See also

<dl> <dt>

[**endpoint**](endpoint.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**string binding**](/windows/desktop/Rpc/string-binding)
</dt> </dl>

 

 