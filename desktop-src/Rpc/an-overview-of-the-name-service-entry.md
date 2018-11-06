---
title: An Overview of the Name Service Entry
description: The name service entry consists of three distinct sections.
ms.assetid: 3059a9a9-174d-4d04-8565-e4558f17f465
ms.topic: article
ms.date: 05/31/2018
---

# An Overview of the Name Service Entry

The name service entry consists of three distinct sections. The first section is for interfaces (UUID + version), the second section contains the object UUIDs, and the third section is for binding handles. You provide a name for the entry that will serve as a way to identify it.

When calling [**RpcNsBindingExport**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindingexporta), the server specifies the name of the entry in which to place the exported information. This newly exported interface is then added to the interface section of the name service entry. Any interfaces that are already present in the name service entry remain as well. This same process is followed for object UUIDs and binding handles.

The client calls [**RpcNsBindingLookupBegin**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindinglookupbegina) (or [**RpcNsBindingImportBegin**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindingimportbegina)) to search for an appropriate binding handle. The entry name, interface handle, and an object UUID are extracted. These restrict the entries from which binding handles are returned. If an entry matches the search criteria, all the binding handles in that entry are returned from [**RpcNsBindingImportNext**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindingimportnext).

 

 




