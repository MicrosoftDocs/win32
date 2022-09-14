---
title: Criteria for Name Service Entries
description: Criteria for Name Service Entries with Remote Procedure Call (RPC).
ms.assetid: f9a7b935-7104-489c-93a8-0c3793d17348
ms.topic: article
ms.date: 05/31/2018
---

# Criteria for Name Service Entries

The following criteria are used when processing name service entries:

-   If you provide a non-**NULL** entry name for [**RpcNsBindingLookupBegin**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindinglookupbegina), that entry will be the only entry searched for binding handles. If you pass **NULL**, all entries in your logon domain will be searched. Note that this does not include trusted domains.
-   If you provide an interface handle, binding handles are returned from an entry only if the interface section of the entry contains a compatible version of that interface UUID. That is, the major version number must be the same as your interface UUID, while the minor version number must be equal to or greater than yours.
-   If you provide an object UUID, binding handles are returned from an entry only if the object UUID section of the entry contains that particular object UUID.

If a name service entry survives the criteria described above, all the binding handles from those entries are gathered. Handles with a protocol sequence that is unsupported by the client are discarded and the remaining handles are returned to you as the output from [**RpcNsBindingLookupNext**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindinglookupnext).

 

 




