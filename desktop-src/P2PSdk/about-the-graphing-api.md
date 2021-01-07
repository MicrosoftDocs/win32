---
description: The Peer Graphing API allows applications to pass data between peers efficiently and reliably. The core concepts of peer graph technology are the nodes of a peer graph, and event notices.
ms.assetid: c3530134-bde3-4a9a-b433-4f198430a607
title: About the Graphing API
ms.topic: article
ms.date: 05/31/2018
---

# About the Graphing API

The Peer Graphing API allows applications to pass data between peers efficiently and reliably. The core concepts of peer graph technology are the **nodes** of a peer graph, and event notices.

## Nodes

A node represents a specific instance of a peer on a network. The Peer Graphing API infrastructure ensures that each node has a consistent view of the data in a graph. A node has the following features:

-   Can connect to a different node, and form an interrelated network called a peer graph.
-   Can share data with other nodes in a graph in the form of a [record](records.md).
-   Can create direct connections separate from the peer graphs established by using the Peer [Grouping API](about-the-grouping-api.md).
    > [!Note]  
    > Direct connections allow nodes to send private data to each other.

     

## Event Notices

The Peer Graphing API has an event infrastructure that allows an application to register and receive notice of a peer event within the Peer Graphing API infrastructure. When something changes within a peer graph, an application sends an event notice to identify that a change has occurred.

 

 



