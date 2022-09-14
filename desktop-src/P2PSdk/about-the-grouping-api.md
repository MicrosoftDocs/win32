---
description: The Peer Grouping API combines the technology of the PNRP Name Space Provider API and the Graphing API.
ms.assetid: 0a575efe-968c-48ab-a446-0d910ecb5708
title: About the Grouping API
ms.topic: article
ms.date: 05/31/2018
---

# About the Grouping API

The Peer Grouping API combines the technology of the [PNRP Name Space Provider API](pnrp-namespace-provider-api.md) and the [Graphing API](graphing-api.md). Grouping adds the following two pieces of technology:

-   A multiplexing layer that allows multiple applications to use one graph, one port, and one record database.
-   Security that ensures only peers invited to a group can join and connect throughout the lifetime of a group.

Grouping provides an accessible and easy approach to peer networking because of the straightforward call flow and secure messaging. This API utilizes PNRP for group discovery and a standard PKI-based security provider instead of requiring a developer to implement one. However, if your application demands greater flexibility in terms of security options, consider using the [Graphing API](about-the-graphing-api.md).

The following table identifies the topics in this Grouping API section:

| Topic                                                                | Description                                                                              |
|----------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [How to Work With Groups](how-to-work-with-groups.md)               | Describes the call flow in a Peer Grouping application from startup to shutdown.         |
| [How Group Security Works](how-group-security-works.md)             | Describes how peer group membership and data exchanges are secured.                      |
| [Inviting a Peer to a Group](inviting-a-peer-to-a-group.md)         | Describes the process by which peers are invited and added to a peer group.              |
| [How to Connect to a Peer Group](how-to-connect-to-a-peer-group.md) | Describes how a peer connects to and interacts with a peer group.                        |
| [Managing Group Records](managing-group-records.md)                 | Describes peer group records and how to manage them as a member and as an administrator. |



 

> [!Note]  
> Applications using the Grouping API in an environment with a firewall require exception groups that cover the port specific to the application, as well as port '3587-TCP' for the Grouping API and port '3540-UDP' for PNRP. These exception groups should be enabled whenever the application is running.

 

 

 



