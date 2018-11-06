---
title: Binding Handle Functions
description: The following table contains the list of RPC run-time routines that operate on binding handles and specifies the type of binding handle allowed.
ms.assetid: 16effe59-ebe2-48c3-b97a-90656b6d3b51
ms.topic: article
ms.date: 05/31/2018
---

# Binding Handle Functions

The following table contains the list of RPC run-time routines that operate on binding handles and specifies the type of binding handle allowed.



| Routine                                                            | Input argument   | Output argument |
|--------------------------------------------------------------------|------------------|-----------------|
| [**RpcBindingCopy**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingcopy)                           | Server           | Server          |
| [**RpcBindingFree**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingfree)                           | Server           | None            |
| [**RpcBindingFromStringBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingfromstringbinding) | None             | Server          |
| [**RpcBindingInqAuthClient**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindinginqauthclient)         | Client           | None            |
| [**RpcBindingInqAuthInfo**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindinginqauthinfo)             | Server           | None            |
| [**RpcBindingInqObject**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindinginqobject)                 | Server or client | None            |
| [**RpcBindingReset**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingreset)                         | Server           | None            |
| [**RpcBindingSetAuthInfo**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetauthinfo)             | Server           | None            |
| [**RpcBindingSetObject**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetobject)                 | Server           | None            |
| [**RpcBindingToStringBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingtostringbinding)     | Server or client | None            |
| [**RpcBindingVectorFree**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingvectorfree)               | Server           | None            |
| [**RpcNsBindingExport**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindingexporta)                   | Server           | None            |
| [**RpcNsBindingImportNext**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindingimportnext)           | None             | Server          |
| [**RpcNsBindingLookupNext**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindinglookupnext)           | None             | Server          |
| [**RpcNsBindingSelect**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindingselect)                   | Server           | Server          |
| [**RpcServerInqBindings**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverinqbindings)               | None             | Server          |



 

 

 




