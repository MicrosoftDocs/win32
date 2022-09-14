---
title: Writing Backward Compatible Clients and Servers
description: In theory, the versioning scheme of RPC helps prevent miscommunication between modified servers and clients and their deployed counterparts.
ms.assetid: 0c7d6716-e4ed-447e-bf64-906d55bec907
keywords:
- Remote Procedure Call RPC , best practices, backward compatibility
ms.topic: article
ms.date: 05/31/2018
---

# Writing Backward Compatible Clients and Servers

In theory, the versioning scheme of RPC helps prevent miscommunication between modified servers and clients and their deployed counterparts. In practice, however, developers frequently must introduce changes to existing interfaces without modifying the version, because previous clients and servers must be able to communicate with new ones. This is a larger issue for standard RPC than for COM; querying is a natural way of searching for supported interfaces in COM, while in RPC exception handling must be used for equivalent coverage.

This section discusses the best RPC programming practices for addressing these situations. This section is divided into the following topics:

-   [The Versioning Theory for RPC and COM](the-versioning-theory-for-rpc-and-com.md)
-   [Changing Interfaces in a Backward Compatible Manner](changing-interfaces-in-a-backward-compatible-manner.md)
-   [Examples of Incompatible Changes](examples-of-incompatible-changes.md)

 

 




