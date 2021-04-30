---
description: The Peer Infrastructure is a set of several APIs that are powerful and flexible.
ms.assetid: aed7585a-88e5-4ca3-a8c3-e2ccfe13d35d
title: What is the Peer Infrastructure?
ms.topic: article
ms.date: 05/31/2018
---

# What is the Peer Infrastructure?

The Peer Infrastructure is a set of several APIs that are powerful and flexible. The major components include the following:

-   [Peer Graphing API](#peer-graphing-api)
-   [Peer Grouping API](#peer-grouping-api)
-   [Peer Identity Manager API](#peer-identity-manager-api)
-   [PNRP Namespace Provider API](#pnrp-namespace-provider-api)

## Peer Graphing API

The Peer Infrastructure provides a graphing technology that can pass information efficiently and reliably between peers in a peer graph. The [Peer Graphing API](graphing-api.md) ensures that each node has a consistent view of the data in a graph.

You can use the [Peer Graphing API](graphing-api.md) to do the following:

-   Create and manage peer graphs
-   Enumerate and interact with other peers in a peer graph
-   Send data in the form of a [record](records.md) to each node in a peer graph

## Peer Grouping API

The [Peer Grouping API](grouping-api.md) combines and enhances the Peer [PNRP](#pnrp-namespace-provider-api) and [Graphing](#peer-graphing-api) APIs, and adds the following two components:

-   A multiplexing layer that allows multiple applications running on one peer entity to connect to a group
-   A specific security model that ensures only peers invited to a group can connect to the group through the lifetime of the group

You can use the Peer Grouping API to do the following:

-   Create and manage secure peer groups
-   Enumerate and interact with other peers in a group
-   Send data in the form of a [record](records.md) to each node in a peer group

## Peer Identity Manager API

By using the [Peer Identity Manager API](identity-manager-api.md) you can create secure [peer names](peer-names.md) that PNRP can use to ensure that a person publishing a name officially owns the name. Peer names are also called identities, and they are used in the Peer Grouping API to identify the individuals in a group.

You can use the [Peer Identity Manager API](identity-manager-api.md) to do the following:

-   Create, enumerate, and manage peer identities.

## PNRP Namespace Provider API

The Peer Infrastructure provides a serverless name resolution technology called the [PNRP Namespace Provider API](pnrp-namespace-provider-api.md). By using the Winsock 2 PNRP Namespace Provider API, a peer, service, computing device, and peer group endpoint can manage, register, unregister, and resolve another endpoint in a PNRP [cloud](clouds.md).

> [!Note]  
> PNRP is an acronym for **peer name resolution protocol**.

 

 

 



