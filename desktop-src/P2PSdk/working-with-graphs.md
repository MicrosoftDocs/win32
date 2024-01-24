---
description: When working with peer graphs, functions must be called in a specific order. The flow of calls depends on whether you are creating or opening a peer graph. This topic identifies the flow of function calls in a simple peer graph application.
ms.assetid: cb4f48d0-d1e2-4a4b-bd5a-6e8f66d03806
title: Working with Graphs
ms.topic: article
ms.date: 05/31/2018
---

# Working with Graphs

When working with peer graphs, functions must be called in a specific order. The flow of calls depends on whether you are creating or opening a peer graph. This topic identifies the flow of function calls in a simple peer graph application.

## Starting Up a Graph

Before an application calls a function in the Peer Graphing API, [**PeerGraphStartup**](/windows/desktop/api/P2P/nf-p2p-peergraphstartup) must be called to initialize the Peer Graphing API for an application, and then set the supported version.

## Creating a Peer Graph

The following procedure identifies the flow of calls for creating a peer graph.

> [!IMPORTANT]
> Only one peer should call [**PeerGraphCreate**](/windows/desktop/api/P2P/nf-p2p-peergraphcreate). All other peers should call [**PeerGraphOpen**](/windows/desktop/api/P2P/nf-p2p-peergraphopen). Multiple calls to **PeerGraphCreate** invalidate a graph.

 

-   Create a peer graph. Call [**PeerGraphCreate**](/windows/desktop/api/P2P/nf-p2p-peergraphcreate).
-   Register for peer events. Call [**PeerGraphRegisterEvent**](/windows/desktop/api/P2P/nf-p2p-peergraphregisterevent).
    > [!Note]  
    > For more information about registering for peer events, see [Events Infrastructure](peer-events-infrastructure.md).

     

-   Listen for connections to a peer graph. Call [**PeerGraphListen**](/windows/desktop/api/P2P/nf-p2p-peergraphlisten).
-   Perform application-dependent functions for the remainder of the running time, for example, process peer events and work with connections.
-   Close the connection to a peer graph. Call [**PeerGraphClose**](/windows/desktop/api/P2P/nf-p2p-peergraphclose).

## Opening a Peer Graph

The flow of function calls to open a peer graph depends on the return value of the call to [**PeerGraphOpen**](/windows/desktop/api/P2P/nf-p2p-peergraphopen). The most important values are **S\_OK** and **PEER\_S\_DATA\_CREATED**, which are explained in the following sections of this topic.

> [!Note]  
> If a call to [**PeerGraphOpen**](/windows/desktop/api/P2P/nf-p2p-peergraphopen) does not return **S\_OK** or **PEER\_S\_DATA\_CREATED**, handle the error.

 

## When PeerGraphOpen Returns S\_OK

When a call to [**PeerGraphOpen**](/windows/desktop/api/P2P/nf-p2p-peergraphopen) returns **S\_OK**, a peer graph and an existing database have been opened. The following procedure identifies what you can do to open a peer graph when a call to **PeerGraphOpen** returns **S\_OK**

-   Register for peer events. Call [**PeerGraphRegisterEvent**](/windows/desktop/api/P2P/nf-p2p-peergraphregisterevent).
    > [!Note]  
    > For more information about registering for events, see [Events Infrastructure](peer-events-infrastructure.md).

     

-   Locate a node. This is a process performed outside of the Peer Graphing Infrastructure, by using a method or application that you identify. The Peer Graphing API does not provide a specific mechanism to find an initial graph node to connect to. An application must use another mechanism, such as the [Peer Name Resolution Protocol (PNRP)](pnrp-namespace-provider-api.md) API, to locate the initial node.
-   If a node is found, connect to it. Call [**PeerGraphConnect**](/windows/desktop/api/P2P/nf-p2p-peergraphconnect), then call [**PeerGraphListen**](/windows/desktop/api/P2P/nf-p2p-peergraphlisten) to listen for connections to the peer graph.
    > [!Note]  
    > If a node is not found, do not call [**PeerGraphConnect**](/windows/desktop/api/P2P/nf-p2p-peergraphconnect) and [**PeerGraphListen**](/windows/desktop/api/P2P/nf-p2p-peergraphlisten).

     

-   Perform application-dependent functions for the remainder of the running time, for example, process peer events and work with connections, depending on whether the node is connected to the peer graph or not. For example, the application can choose to timeout or periodically perform discovery for an active node in the graph.
-   Close the connection to the peer graph. Call [**PeerGraphClose**](/windows/desktop/api/P2P/nf-p2p-peergraphclose).

## When PeerGraphOpen Returns PEER\_S\_DATA\_CREATED

When [**PeerGraphOpen**](/windows/desktop/api/P2P/nf-p2p-peergraphopen) returns **PEER\_S\_DATA\_CREATED**, it means that an existing database for a peer graph is not found, a new database is created, and this is the first time it is opened. To use or listen on a peer graph, a peer must be connected to and synchronized with a peer graph.

The following procedure identifies what you can do to open a peer graph when a call to [**PeerGraphOpen**](/windows/desktop/api/P2P/nf-p2p-peergraphopen) returns **PEER\_S\_DATA\_CREATED**.

-   Open a peer graph. Call [**PeerGraphOpen**](/windows/desktop/api/P2P/nf-p2p-peergraphopen).
-   Register for peer events. Call [**PeerGraphRegisterEvent**](/windows/desktop/api/P2P/nf-p2p-peergraphregisterevent).
    > [!Note]  
    > For more information about registering for peer events, see [Events Infrastructure](peer-events-infrastructure.md).

     

-   Locate a node. This is a process performed outside of the Peer Graphing Infrastructure, by using a method or application that you identify. The Peer Graphing API does not provide a specific mechanism to find an initial graph node to connect to. An application must use another mechanism, such as the [Peer Name Resolution Protocol (PNRP)](pnrp-namespace-provider-api.md) API, to locate the initial node.
-   If a node is found, connect to it. Call [**PeerGraphConnect**](/windows/desktop/api/P2P/nf-p2p-peergraphconnect), then call [**PeerGraphListen**](/windows/desktop/api/P2P/nf-p2p-peergraphlisten) to listen for connections to the peer graph.
    > [!Note]  
    > If a node is not found, do not call [**PeerGraphConnect**](/windows/desktop/api/P2P/nf-p2p-peergraphconnect) and [**PeerGraphListen**](/windows/desktop/api/P2P/nf-p2p-peergraphlisten).

     

-   Perform application-dependent functions for the remainder of the running time, for example, process peer events and work with connections, depending on whether the node is connected to the peer graph or not. For example, the application can choose to timeout or periodically perform discovery for an active node in the graph.
-   Close the connection to the peer graph. Call [**PeerGraphClose**](/windows/desktop/api/P2P/nf-p2p-peergraphclose).

 

 



