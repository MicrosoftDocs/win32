---
title: Authorization Functions
description: Each time a server program receives a client request for access to one of the management remote procedures, the RPC run-time library invokes a default authorization function.
ms.assetid: e3edbf6f-2876-49ac-a93e-14fd0b5adf53
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Authorization Functions

Each time a server program receives a client request for access to one of the management remote procedures, the RPC run-time library invokes a default authorization function. This function uses the SSP to check the client's credentials and authorize or reject the request.

Your server program can override the authorization function that the SSP provides. Invoke the function [**RpcMgmtSetAuthorizationFn**](/windows/win32/Rpcdce/nf-rpcdce-rpcmgmtsetauthorizationfn?branch=master) and pass it to the address of your authorization function. Once the server program sets the authorization function, the RPC run-time library calls it every time the server program receives a client request to one of the management functions. For more information, see [**RpcMgmtIsServerListening**](/windows/win32/Rpcdce/nf-rpcdce-rpcmgmtisserverlistening?branch=master), [**RpcMgmtStopServerListening**](/windows/win32/Rpcdce/nf-rpcdce-rpcmgmtstopserverlistening?branch=master), [**RpcMgmtInqIfIds**](/windows/win32/Rpcdce/nf-rpcdce-rpcmgmtinqifids?branch=master), [**RpcMgmtInqServerPrincName**](/windows/win32/Rpcdce/nf-rpcdce-rpcmgmtinqserverprincname?branch=master), and [**RpcMgmtInqStats**](/windows/win32/Rpcdce/nf-rpcdce-rpcmgmtinqstats?branch=master).

 

 




