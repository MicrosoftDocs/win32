---
title: Finding Endpoints
description: Server programs listen to endpoints for client requests. The syntax of the endpoint string depends on the protocol sequence you use. For example, the endpoint for TCP/IP is a port number, and the endpoint syntax for named pipes is a valid pipe name.
ms.assetid: 330bbe9f-b7e9-4a5b-86d8-824edec960d2
ms.topic: article
ms.date: 05/31/2018
---

# Finding Endpoints

Server programs listen to endpoints for client requests. The syntax of the endpoint string depends on the protocol sequence you use. For example, the endpoint for TCP/IP is a port number, and the endpoint syntax for named pipes is a valid pipe name.

There are two types of endpoints: well-known and dynamic. Your choice of which type of endpoint your program uses determines whether the distributed application or the run-time library specifies the endpoint.

This section discusses endpoints and presents information on how to find them. It is organized into the following topics:

-   [Using Well-Known Endpoints](#using-well-known-endpoints)
-   [Using Dynamic Endpoints](#using-dynamic-endpoints)
-   [Exporting Well-Known Endpoints Into the Endpoint Map Database](#exporting-well-known-endpoints-into-the-endpoint-map-database)

> [!Note]  
> The terms *static endpoints* and *well-known endpoints* are equivalent, and used interchangeably.

 

It is possible for your client application to use the endpoint map to determine whether or not a server program is currently running. Your client can call [**RpcMgmtInqIfIds**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtinqifids), [**RpcMgmtEpEltInqBegin**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtepeltinqbegin), and [**RpcMgmtEpEltInqDone**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtepeltinqdone) to see if the server has registered the particular interface it requires in the endpoint map.

## Using Well-known Endpoints

Well-known endpoints are pre-assigned endpoints that the server program uses every time it runs. Because the server always listens to that particular endpoint, the client always attempts to connect to it. Well-known endpoints are usually assigned by the authority responsible for the transport protocol. Because server host computers have a finite number of available endpoints, application developers are strongly discouraged from using well-known endpoints. Another advantage of dynamic endpoints is that they simplify long-term management and maintenance of the system.

A distributed application can specify a well-known endpoint in a string and pass that string as a parameter to the function [**RpcServerUseProtseqEp**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseqep). Alternatively, the endpoint string can appear in the IDL file interface header as part of the \[ [endpoint](/windows/desktop/Midl/endpoint)\] interface attribute.

You can use two approaches to implement the well-known endpoint:

-   Specify all information in a string binding
-   Store the well-known endpoint in the name service database

You can write all of the information needed to establish a binding into a distributed application when you develop it. The client can specify the well-known endpoint directly in a string, call [**RpcStringBindingCompose**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcstringbindingcompose) to create a string that contains all the binding information, and supply this string to the function [**RpcBindingFromStringBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingfromstringbinding) to obtain a handle. The client and server can be hard-coded to use a well-known endpoint, or written so that the endpoint information comes from the command line, a data file, a configuration file, or the IDL file.

Your client application can also query a name service database for well-known endpoint information.

## Using Dynamic Endpoints

The number of endpoints for a particular server and a particular protocol sequence are usually limited. For example, when you use the [ncacn\_ip\_tcp](/windows/desktop/Midl/ncacn-ip-tcp) protocol sequence, indicating that RPC network communication occurs using TCP/IP, only a limited number of ports are available (most systems have only the range 1025 through 5000 opened). The RPC run-time libraries allow you to assign endpoints dynamically, as needed. Since the number of possible interface UUIDs is practically unlimited, using the interface UUID to direct the call offers more room for expansion and more flexibility.

By default, the RPC run-time library functions search for endpoint information when they query a name service database. If the endpoint is dynamic, the name service database will not contain endpoint information. However, the query will give your client program the name of a server. It can then search the server's endpoint map.

If the client needs to make a remote procedure call using a dynamic endpoint, the preferred method is to make the call on a partially bound binding handle. The RPC run time resolves the endpoint transparently. This method is superior to using the [**RpcEpResolveBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcepresolvebinding) function, as it allows advanced caching mechanisms in the RPC run time.

If more specific control over endpoint selection is required, clients can search the endpoint map one entry at a time by calling the [**RpcMgmtEpEltInqBegin**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtepeltinqbegin), [**RpcMgmtEpEltInqNext**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtepeltinqnext), and [**RpcMgmtEpEltInqDone**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcmgmtepeltinqdone) functions.

## Exporting Well-known Endpoints into the Endpoint Map Database

It is possible to mix the two approaches to finding endpoints, especially when a distributed system is transitioning from a well-known endpoint model to a dynamic endpoint model. In such transitions, an intermediate version of the server will use a well-known endpoint, but it will also register the well-known endpoint with the endpoint map database. This approach allows clients that use well known endpoint and clients that use a dynamic endpoint to connect. Once all servers are upgraded, a new client version can be deployed that uses dynamic endpoints only. Once all clients are upgraded, a final server version can stop using well-known endpoints and begin using dynamic endpoints only.

This approach allows a transition path for applications that have started with a well-known endpoint but want to migrate to a dynamic endpoint without requiring a simultaneous update of all servers and clients.

 

 