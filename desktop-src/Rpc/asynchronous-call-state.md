---
title: Asynchronous Call State
description: This page describes the Asynchronous Call State for RPC calls.
ms.assetid: 4a594dad-a8a1-44e9-8648-ddc2539c234c
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous Call State

This page describes the Asynchronous Call State for RPC calls.

## Client Behavior




| State | State name | Action | 
|-------|------------|--------|
| C | Make the call | Make the RPC<ul><li>On success go to state WComp</li><li>On exception go to End</li></ul>To fail: go to Can<br /> | 
| Can | Cancel the call | Call <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccancelcall"><strong>RpcAsyncCancelCall</strong></a>Go to WComp<br /> | 
| WComp | Wait for completion | Wait for notificationCall-complete notification should be received<br /> Go to Comp<br /> | 
| Comp | Completion | Issue <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall"><strong>RpcAsyncCompleteCall</strong></a>Go to End<br /> | 
| End | 




 

## Server Behavior



| State | State name     | Action                                                                                                                                                                                                              |
|-------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D     | Dispatch       | The call is dispatched by the RPC runtimeProcess<br/> Go to Comp<br/> To fail fatally (while executing on the RPC thread): Raise exception; go to End<br/> To fail gracefully: go to A<br/> |
| A     | Abort the call | Call [**RpcAsyncAbortCall**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasyncabortcall)Go to End<br/>                                                                                                                                             |
| Comp  | Completion     | Issue [**RpcAsyncCompleteCall**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall)Go to End<br/>                                                                                                                                      |
| End   |                |                                                                                                                                                                                                                     |



 

 

 





