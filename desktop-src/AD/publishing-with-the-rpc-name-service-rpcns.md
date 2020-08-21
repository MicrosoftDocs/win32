---
title: Publishing with the RPC Name Service
description: RPC services can publish their identifiers in a namespace using the RPC name service (RpcNs) APIs.
ms.assetid: 0c8e1207-daeb-4dc8-b83a-a54cd59a46a7
ms.tgt_platform: multiple
keywords:
- Publishing with the RPC Name Service AD
ms.topic: article
ms.date: 05/31/2018
---

# Publishing with the RPC Name Service

RPC services can publish their identifiers in a namespace using the RPC name service (RpcNs) APIs. The RpcNs APIs in Windows 2000 publish the RPC entries in Active Directory Domain Services. Services create RPC bindings and publish them in the namespace as named RPC Server entries with attributes including the unique interface ID, a GUID that is recognized by clients. A client can then search for RPC Servers offering the desired interface, import the binding, and connect to the server.

For more information about publishing an RPC service, see [Server-side Binding](/windows/desktop/Rpc/server-side-binding).

 

 