---
title: RPC Load Balancing
description: RPC Load Balancing
ms.assetid: c646f748-d5f2-422d-8305-1f86c0dc61b4
ms.topic: article
ms.date: 05/31/2018
---

# RPC Load Balancing

Microsoft RPC Load Balancing is intended to provide a scalable solution for scenarios which demand a high load of [RPC over HTTP](remote-procedure-calls-using-rpc-over-http.md) traffic. The RPC Load Balancer’s primary purpose is to ensure RPC/HTTP traffic can be serviced by a server farm to improve scalability. To achieve this, RPC must ensure that all connections from a client process are serviced by the same server endpoint in the server farm. The RPC Load Balancer is implemented as a service which runs in conjunction with the RPC over HTTP Proxy service.

To enable load balancing, the RPC Load Balancing service running on each of the servers communicates with each other to determine the preferred server for the initial client connection. This process is called arbitration and it occurs at the time of the initial client connection. To reduce cross server traffic, the RPC Load Balancing service chooses the local endpoint to service the connection if the client is not already associated with a server. For a given client connection, the outcome of arbitration is one of two possibilities:

-   If the client has already made a connection, the server to first receive the connection will handle the subsequent connections.
-   If this is the first connection from the client, arbitration will result in the local server handling the connection, and thus all connections from the client. This information, once determined, will be committed to the other RPC Load Balancer services in the server farm, thus informing them of the server handling all of the client’s requests.

This section provides an overview of RPC Load Balancing in the following topics:

-   [Deploying Load Balancing](deploying-load-balancing.md)
-   [Configuring Load Balancing](configuring-load-balancing.md)
-   [Load Balancing Best Practices](load-balancing-best-practices.md)

## Requirements

The RPC Load Balancing service is supported on servers running Windows Server 2008 R2 or later and clients running Windows 7 or later versions of Windows.

The RPC Proxy service, the RPC Load Balancing service and the server endpoints must all be running on the same machine. Additionally, all servers in the server farm must be capable of servicing the requested endpoint. For information on configuring the RPC Proxy service and the RPC Load Balancing service, see [Configuring Computers for RPC over HTTP](configuring-computers-for-rpc-over-http.md) and [Configuring Load Balancing](configuring-load-balancing.md), respectively.

## Limitations

At this time, RPC Load Balancing supports only one server farm per resource. All servers in all server farms must be capable of servicing all resources as well.

 

 




