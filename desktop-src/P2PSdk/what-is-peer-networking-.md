---
description: Peer-to-peer networking is a serverless networking technology that allows several network devices to share resources and communicate directly with each other.
ms.assetid: d2a43d3b-2782-4777-8c65-05e2c52930d0
title: What is Peer Networking?
ms.topic: article
ms.date: 05/31/2018
---

# What is Peer Networking?

Peer-to-peer networking is a serverless networking technology that allows several network devices to share resources and communicate directly with each other. This technology is available for Windows XP with Service Pack 1 (SP1) and later clients that run the Advanced Networking Pack for the Peer-to-Peer Infrastructure.

The Peer-to-Peer Infrastructure is a set of networking APIs to help you develop decentralized networking applications that use the collective power of computers on a network. For example, peer-to-peer applications can be collaborative communications, content distribution technologies, and so on.

The Peer-to-Peer Infrastructure provides a solid networking infrastructure so that you can concentrate on developing applications, because the infrastructure is developed for you.

The Peer-to-Peer Infrastructure includes the following major components:

-   [Scalable and secure peer name resolution](#scalable-and-secure-peer-name-resolution)
-   [Efficient multipoint communication](#efficient-multipoint-communication)
-   [Distributed data management](#distributed-data-management)
-   [Secure peer identities](#secure-peer-identities)
-   [Secure Peer-to-Peer groups](#secure-peer-to-peer-groups)

## Scalable and Secure Peer Name Resolution

The [Peer Name Resolution Protocol (PNRP) Namespace Provider API](pnrp-namespace-provider-api.md) is a name-to-IP resolution protocol. The IPv6 scope or context that includes all participating peers is called a [cloud](clouds.md). PNRP allows peers to interact with each other within a cloud.

## Efficient Multipoint Communication

The Peer-to-Peer Infrastructure includes the [Graphing API](graphing-api.md) that provides efficient multipoint communication. Like PNRP, peer-to-peer graphing allows a set of nodes to interact, and pass data to and from each other in the form of a [record](records.md). Each record that a peer generates or updates is sent to all nodes in a graph.

## Distributed Data Management

Distributed data management automatically stores all records sent to a peer-to-peer graph until the specified expiration time for each record. Peer-to-peer networking ensures that each node in a peer-to-peer graph has a similar view of the record database. If a peer-to-peer graph has a security model associated with it, the graph contains the following information:

-   Who can and cannot connect to a graph
-   Who can secure and validate records based on externally defined criteria

## Secure Peer Identities

The Peer-to-Peer Infrastructure provides a Peer-to-Peer [Identity Manager API](identity-manager-api.md) that allows you to create, manage, and manipulate the peer identities. Peer identities are used to define names for secure endpoints in PNRP, and can represent any resource that participates in a peer-to-peer network, including secure peer-to-peer groups and services.

## Secure Peer-to-Peer Groups

The Peer-to-Peer [Grouping API](grouping-api.md) combines the Peer-to-Peer Graphing, Identity Manager, and PNRP APIs to form a cohesive and convenient solution for peer-to-peer networking application development. The Peer-to-Peer Grouping API uses the Peer-to-Peer Identity Manager API and a self-signed certificate scheme to ensure security within the graphing infrastructure. Each group can be resolved and registered through PNRP, which allows for the name resolution of random peers within a registered peer-to-peer group. A group can be an endpoint in PNRP, just like a peer.


For an overview of the APIs in the Peer-to-Peer Infrastructure, see the topic [What is the Peer Infrastructure?](what-is-the-peer-infrastructure-.md).

 

 



