---
title: Binding Handle Functions
description: The following table contains the list of RPC run-time routines that operate on binding handles and specifies the type of binding handle allowed.
ms.assetid: 16effe59-ebe2-48c3-b97a-90656b6d3b51
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Binding Handle Functions

The following table contains the list of RPC run-time routines that operate on binding handles and specifies the type of binding handle allowed.



| Routine                                                            | Input argument   | Output argument |
|--------------------------------------------------------------------|------------------|-----------------|
| [**RpcBindingCopy**](/windows/win32/Rpcdce/nf-rpcdce-rpcbindingcopy?branch=master)                           | Server           | Server          |
| [**RpcBindingFree**](/windows/win32/Rpcdce/nf-rpcdce-rpcbindingfree?branch=master)                           | Server           | None            |
| [**RpcBindingFromStringBinding**](/windows/win32/Rpcdce/nf-rpcdce-rpcbindingfromstringbinding?branch=master) | None             | Server          |
| [**RpcBindingInqAuthClient**](/windows/win32/Rpcdce/nf-rpcdce-rpcbindinginqauthclient?branch=master)         | Client           | None            |
| [**RpcBindingInqAuthInfo**](/windows/win32/Rpcdce/nf-rpcdce-rpcbindinginqauthinfo?branch=master)             | Server           | None            |
| [**RpcBindingInqObject**](/windows/win32/Rpcdce/nf-rpcdce-rpcbindinginqobject?branch=master)                 | Server or client | None            |
| [**RpcBindingReset**](/windows/win32/Rpcdce/nf-rpcdce-rpcbindingreset?branch=master)                         | Server           | None            |
| [**RpcBindingSetAuthInfo**](/windows/win32/Rpcdce/nf-rpcdce-rpcbindingsetauthinfo?branch=master)             | Server           | None            |
| [**RpcBindingSetObject**](/windows/win32/Rpcdce/nf-rpcdce-rpcbindingsetobject?branch=master)                 | Server           | None            |
| [**RpcBindingToStringBinding**](/windows/win32/Rpcdce/nf-rpcdce-rpcbindingtostringbinding?branch=master)     | Server or client | None            |
| [**RpcBindingVectorFree**](/windows/win32/Rpcdce/nf-rpcdce-rpcbindingvectorfree?branch=master)               | Server           | None            |
| [**RpcNsBindingExport**](/windows/win32/Rpcnsi/nf-rpcnsi-rpcnsbindingexporta?branch=master)                   | Server           | None            |
| [**RpcNsBindingImportNext**](/windows/win32/Rpcnsi/nf-rpcnsi-rpcnsbindingimportnext?branch=master)           | None             | Server          |
| [**RpcNsBindingLookupNext**](/windows/win32/Rpcnsi/nf-rpcnsi-rpcnsbindinglookupnext?branch=master)           | None             | Server          |
| [**RpcNsBindingSelect**](/windows/win32/Rpcnsi/nf-rpcnsi-rpcnsbindingselect?branch=master)                   | Server           | Server          |
| [**RpcServerInqBindings**](/windows/win32/Rpcdce/nf-rpcdce-rpcserverinqbindings?branch=master)               | None             | Server          |



 

 

 




