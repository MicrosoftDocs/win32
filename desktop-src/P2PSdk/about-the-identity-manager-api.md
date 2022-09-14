---
description: The Peer Identity Manager API allows you to create, enumerate, and manipulate peer identities in a peer application.
ms.assetid: c1b2a587-71c7-4623-a318-4624dad7feba
title: About Identity Manager
ms.topic: article
ms.date: 05/31/2018
---

# About Identity Manager

The Peer Identity Manager API allows you to create, enumerate, and manipulate peer identities in a peer application. You can use the peer identities created using this API as input for the Peer Grouping and Peer Name Resolution Protocol (PNRP) Namespace Provider APIs.

## Peer Identity Manager Best Practices

Each user should have a few peer identities that they can use for the peer activities. For example, a user might have two peer identities for work and leisure.

A well-designed peer application allows a user to select a peer identity to use. A user can create a new peer identity if none of the existing peer identities are appropriate to use with an application.

A well-designed peer application also controls the number of identities that it creates. If an application creates a temporary peer identity, the application must delete the peer identity when the identity is not needed. If an application does not perform this maintenance, the Peer Identity Manager may not be able to create peer identities until some peer identities are removed.

 

 



