---
title: The Versioning Theory for RPC and COM
description: Versioning theory for Remote Procedure Call (RPC) and COM.
ms.assetid: c4df0a7b-e1be-481d-9149-317ffc9179b9
keywords:
- Remote Procedure Call RPC , best practices, versioning
ms.topic: article
ms.date: 05/31/2018
---

# The Versioning Theory for RPC and COM

Only two completely foolproof methods support new functionality without risk of wire compatibility problems:

-   Change the interface version according to the rules; this prevents new clients from communicating with an old server, and may or may not prevent an old client from communicating with the new server. This is clarified later in this section.
-   Introduce a different interface dealing with the new functionality.

A standard RPC interface is identified by a GUID and version number combination; a COM interface is identified by its GUID. The version consists of major and minor parts. For standard interfaces with the same GUID and different version numbers, a connection is possible only when the major version is the same, and the client is not higher than the minor version of the server.

A consequence is that changing the RPC interface GUID breaks wire compatibility, while changing the interface name does not.

In standard RPC, a path for upgrades and extensions is well defined, and basically requires that new methods only be added at the end of the interface, and new types be used only in the new methods. If such additions are needed, the minor version must be increased. Any other change requires a change in the major version, because the client and server software would be incompatible on the wire. Adhering to these rules assures whenever there is a connection between a new client and old server, or vice-versa, both sides are fully compatible.

For a COM interface, the version attribute cannot be used. Creating new interfaces and inheriting from the old interfaces is an equivalent of manipulating the version in RPC. Typically, the best approach in COM is to create a new interface for the expanded functionality. An equivalent of the minor version is the new interface inheriting from the old one. Changing old methods or old data types requires an entirely new COM interface—an interface that does not inherit from the old one.

For COM, the [**QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) function is an established method of checking whether a server supports an interface; hence, the situations where a client can talk to an old or a new version of an interface can be easily resolved.

 

 