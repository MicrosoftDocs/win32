---
title: Asynchronous Call State
description: This page describes the Asynchronous Call State for RPC calls.
ms.assetid: 4a594dad-a8a1-44e9-8648-ddc2539c234c
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous Call State

This page describes the Asynchronous Call State for RPC calls.

## Client Behavior



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>State</th>
<th>State name</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>C</td>
<td>Make the call</td>
<td>Make the RPC
<ul>
<li>On success go to state WComp</li>
<li>On exception go to End</li>
</ul>
To fail: go to Can<br/></td>
</tr>
<tr class="even">
<td>Can</td>
<td>Cancel the call</td>
<td>Call <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccancelcall"><strong>RpcAsyncCancelCall</strong></a>Go to WComp<br/></td>
</tr>
<tr class="odd">
<td>WComp</td>
<td>Wait for completion</td>
<td>Wait for notificationCall-complete notification should be received<br/> Go to Comp<br/></td>
</tr>
<tr class="even">
<td>Comp</td>
<td>Completion</td>
<td>Issue <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall"><strong>RpcAsyncCompleteCall</strong></a>Go to End<br/></td>
</tr>
<tr class="odd">
<td>End</td>


</tr>
</tbody>
</table>



 

## Server Behavior



| State | State name     | Action                                                                                                                                                                                                              |
|-------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D     | Dispatch       | The call is dispatched by the RPC runtimeProcess<br/> Go to Comp<br/> To fail fatally (while executing on the RPC thread): Raise exception; go to End<br/> To fail gracefully: go to A<br/> |
| A     | Abort the call | Call [**RpcAsyncAbortCall**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasyncabortcall)Go to End<br/>                                                                                                                                             |
| Comp  | Completion     | Issue [**RpcAsyncCompleteCall**](/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall)Go to End<br/>                                                                                                                                      |
| End   |                |                                                                                                                                                                                                                     |



 

 

 





