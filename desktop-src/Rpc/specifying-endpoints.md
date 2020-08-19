---
title: Specifying Endpoints
description: Specifying well-known and dynamic endpoints in Remote Procedure Call (RPC).
ms.assetid: fc39b527-11e6-45a7-b3b5-8bcf469633d8
ms.topic: article
ms.date: 05/31/2018
---

# Specifying Endpoints

An endpoint is a network-specific address of a server process for remote procedure calls. The actual name of the endpoint depends on the protocol sequence used. For example, TCP, UDP, and HTTP use ports. Named pipes uses a named pipe name. Client/server applications can use a well-known endpoint or a dynamic endpoint. This section presents the techniques that server programs use to specify well-known and dynamic endpoints. The information is discussed in the following topics:

-   [Specifying Well-known Endpoints](#specifying-well-known-endpoints)
-   [Specifying Dynamic Endpoints](#specifying-dynamic-endpoints)

## Specifying Well-known Endpoints

When your server uses a well-known endpoint, it can include the endpoint data as part of its name service database entry. If it does, the client's binding handle contains a complete server address that includes the well-known endpoint when the client imports the binding handle from the server entry.

Your server program can also specify well-known endpoints at the same time it specifies protocol sequences. Invoke either the [**RpcServerUseProtseqEp**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseqep) or [**RpcServerUseProtseqEpEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseqepex) function. The difference between the two is that the latter function has an extra parameter your server can use to control dynamic port allocation.

If your server program specifies its endpoint information in this way, it should also call the [**RpcEpRegister**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcepregister) function to register the endpoint in the endpoint map. Even though the endpoint is always the same, the client may use the endpoint map to find the server.

Like protocol sequences, an application can specify endpoint information in its IDL file. When it does, it should register both the protocol sequences and endpoints at the same time by invoking the [**RpcServerUseAllProtseqsIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseallprotseqsif) or [**RpcServerUseAllProtseqsIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseallprotseqsifex) function. In this case, the client has access to the endpoint information through the interface specification in the IDL file. Therefore, it is not necessary to call the [**RpcEpRegister**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcepregister) function.

## Specifying Dynamic Endpoints

A dynamic endpoint is an endpoint that the server host computer assigns when the server begins execution. Most server applications use dynamic endpoints to avoid conflict with other programs over the limited number of ports that are available on the server host computer system. However, programs using named pipes or the [**ncalrpc**](/windows/desktop/Midl/ncalrpc) protocol sequence have a very large endpoint name space. They benefit less from dynamic endpoints than programs using other transports.

Server programs register dynamic endpoints in an endpoint map database. If you want the server to use any available endpoint, call [**RpcServerUseAllProtSeqs**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseallprotseqs), [**RpcServerUseAllProtseqsEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseallprotseqsex), [**RpcServerUseProtseq**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseq) or [**RpcServerUseProtseqEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseqex). This sets the RPC run-time library to use all or one valid protocol sequence(s) with dynamic endpoints. The server should then call [**RpcServerInqBindings**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverinqbindings) to obtain a set of valid binding handles. The server passes the set of binding handles, or binding vector, to the function [**RpcEpRegister**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcepregister) to register all suitable endpoints in the endpoint map. For each call your server makes to **RpcEpRegister**, there should be a corresponding call to [**RpcBindingVectorFree**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingvectorfree) to release the memory that the binding vector uses.

Note that server programs can use the [**RpcEpRegisterNoReplace**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcepregisternoreplace) function rather than [**RpcEpRegister**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcepregister). Programs typically use **RpcEpRegisterNoReplace** when multiple copies of a server program must run on a server host system.

Both the [**RpcEpRegister**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcepregister) and [**RpcEpRegisterNoReplace**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcepregisternoreplace) functions add the server's interfaces and binding handles to the endpoint mapper database. When the client makes a remote procedure call using a partially bound handle, the client's run-time library asks the server computer's endpoint mapper for the endpoint of a compatible server instance. The client library supplies the interface UUID, protocol sequence, and, if present, the object UUID in the client binding handle. The endpoint mapper looks for a database entry that matches the client's information. The client/server interface UUID, the interface major version, and protocol sequence must all match exactly. In addition, the server's interface minor version must be greater than or equal to the client's minor version.

If all tests are successful, the endpoint mapper returns the valid endpoint and the client run-time library updates the endpoint in the binding handle.

Dynamic endpoints are automatically purged from the endpoint mapper database when the server process stops running. You can either remove the endpoint from the endpoint mapper database before the server program exits using the [**RpcEpUnregister**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcepunregister) function, or you can allow automatic cleanup to manage removal of the endpoint.

 

 