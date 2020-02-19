---
title: Asynchronous Pipe State
description: This page describes the Asynchronous Pipe State for RPC calls.
ms.assetid: af937eba-6b70-447a-af76-a8e27f5754e3
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous Pipe State

This page describes the Asynchronous Pipe State for RPC calls.

## IN Pipe

Client Behavior

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>State</th>
<th>State Name</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>C</td>
<td>Make the call</td>
<td>Make the RPC
<ul>
<li>On success go to state WS</li>
<li>On exception go to End</li>
</ul>
To fail: go to Can<br/></td>
</tr>
<tr class="even">
<td>P</td>
<td>Push</td>
<td>Make a push
<ul>
<li>On failure go to End</li>
<li>On success go to WS</li>
</ul>
To fail: go to Can<br/></td>
</tr>
<tr class="odd">
<td>WS</td>
<td>Wait for Send</td>
<td>Wait for notification
<ul>
<li>On failure to get a notification go to Can</li>
<li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcSendComplete</strong></a> is received and more data needs to be sent go to P</li>
<li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcSendComplete</strong></a> is received and more data does not need to be sent go to NP</li>
<li>If a failure <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcCallComplete</strong></a> is received go Comp</li>
</ul>
To fail: go to Can<br/></td>
</tr>
<tr class="even">
<td>NP</td>
<td>Null Push</td>
<td>Push 0 bytes (null push)
<ul>
<li>On failure go to End</li>
<li>On success go to WComp</li>
</ul>
To fail: go to Can<br/></td>
</tr>
<tr class="odd">
<td>Can</td>
<td>Cancel the Call</td>
<td>Call <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccancelcall"><strong>RpcAsyncCancelCall</strong></a>Go to WComp<br/></td>
</tr>
<tr class="even">
<td>WComp</td>
<td>Wait for Completion</td>
<td>Wait for notificationCall-complete notification should be received.<br/> Go to Comp<br/></td>
</tr>
<tr class="odd">
<td>Comp</td>
<td>Completion</td>
<td>Issue <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall"><strong>RpcAsyncCompleteCall</strong></a>Go to End<br/></td>
</tr>
<tr class="even">
<td>End</td>


</tr>
</tbody>
</table>



 

Server Behavior

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>State</th>
<th>State Name</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>D</td>
<td>Dispatch</td>
<td>The call is dispatched by the RPC runtime Go to P<br/> To fail fatally (while executing on the RPC thread): Raise exception; go to End<br/> To fail gracefully: Go to A<br/></td>
</tr>
<tr class="even">
<td>P</td>
<td>Pull</td>
<td>Make a pull
<ul>
<li>On failure go to End</li>
<li>On success and synchronous completion with non-zero bytes read go to P</li>
<li>On success and synchronous completion with zero bytes read (null pull) go to Comp</li>
<li>On success and asynchronous completion (ERROR_IO_PENDING is returned) go to WP</li>
</ul>
To fail: go to A<br/></td>
</tr>
<tr class="odd">
<td>WP</td>
<td>Wait for Pull</td>
<td>Wait for notification
<ul>
<li>On failure to get a completion go to A</li>
<li>If a failure <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received go to A</li>
<li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received with non-zero bytes read go to P</li>
<li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received with zero bytes read (null pull) go to Comp</li>
<li>If a failure is received go to A</li>
</ul>
To fail: go to A<br/></td>
</tr>
<tr class="even">
<td>A</td>
<td>Abort the Call</td>
<td>Call <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasyncabortcall"><strong>RpcAsyncAbortCall</strong></a>Go to End<br/></td>
</tr>
<tr class="odd">
<td>Comp</td>
<td>Completion</td>
<td>Call <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall"><strong>RpcAsyncCompleteCall</strong></a>Go to End<br/></td>
</tr>
<tr class="even">
<td>End</td>


</tr>
</tbody>
</table>



 

## OUT Pipe

Client Behavior

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>State</th>
<th>State Name</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>C</td>
<td>Make the call</td>
<td>Make the RPC
<ul>
<li>On success go to P</li>
<li>On failure go to Comp</li>
</ul>
To fail: go to Can<br/></td>
</tr>
<tr class="even">
<td>P</td>
<td>Pull</td>
<td>Make a pull
<ul>
<li>On failure go to End</li>
<li>On success and synchronous completion with non-zero bytes read go to P</li>
<li>On success and synchronous completion with zero bytes read (null pull) go to WComp</li>
<li>On success and asynchronous completion (ERROR_IO_PENDING is returned) go to WP</li>
</ul>
To fail: go to Can<br/></td>
</tr>
<tr class="odd">
<td>WP</td>
<td>Wait for Pull</td>
<td>Wait for notification
<ul>
<li>On failure to get a completion go to Can</li>
<li>If a failure <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received go to Can</li>
<li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received with non-zero bytes read go to P</li>
<li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received with zero bytes read (null pull) go to Comp</li>
<li>If a failure is received go Can</li>
</ul>
To fail: go to Can<br/></td>
</tr>
<tr class="even">
<td>Can</td>
<td>Cancel the Call</td>
<td>Call <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccancelcall"><strong>RpcAsyncCancelCall</strong></a>Go to WComp<br/></td>
</tr>
<tr class="odd">
<td>WComp</td>
<td>Wait for Completion</td>
<td>Wait for notification. Call-complete notification should be received.<br/> Go to Comp<br/></td>
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



 

Server Behavior

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>State</th>
<th>State Name</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>D</td>
<td>Dispatch</td>
<td>The call is dispatched by the RPC runtime Go to P<br/> To fail fatally (while executing on the RPC thread): Raise exception; go to End<br/> To fail gracefully: Go to A<br/></td>
</tr>
<tr class="even">
<td>P</td>
<td>Push</td>
<td>Make a push
<ul>
<li>On success go to WP</li>
<li>On failure go to End</li>
</ul>
To fail: go to A<br/></td>
</tr>
<tr class="odd">
<td>WP</td>
<td>Wait for Push</td>
<td>Wait for notification
<ul>
<li>On failure to get a completion go to A</li>
<li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcSendComplete</strong></a> is received and more data needs to be sent go to P</li>
<li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcSendComplete</strong></a> is received and more data does not need to be sent go to NP</li>
<li>If a failure is received go Comp</li>
</ul>
To fail: go to A<br/></td>
</tr>
<tr class="even">
<td>NP</td>
<td>Null Push</td>
<td>Push 0 bytes
<ul>
<li>on success go to WNP</li>
<li>on failure go to Comp</li>
</ul>
To fail: go to A<br/></td>
</tr>
<tr class="odd">
<td>WNP</td>
<td>Wait for Null Push</td>
<td>Wait for notification
<ul>
<li>On failure to get a completion go to A</li>
<li>If a failure is received go Comp</li>
<li>If a success is received go Comp</li>
</ul></td>
</tr>
<tr class="even">
<td>A</td>
<td>Abort the Call</td>
<td>Call <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasyncabortcall"><strong>RpcAsyncAbortCall</strong></a>; go to End</td>
</tr>
<tr class="odd">
<td>Comp</td>
<td>Completion</td>
<td>Issue <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall"><strong>RpcAsyncCompleteCall</strong></a>; go to End</td>
</tr>
<tr class="even">
<td>End</td>


</tr>
</tbody>
</table>



 

## IN-OUT Pipe

Client Behavior

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>State</th>
<th>State Name</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>C</td>
<td>Make the call</td>
<td>Make the RPC
<ul>
<li>On success go to WS</li>
<li>On exception go to End</li>
</ul>
To fail: go to Can<br/></td>
</tr>
<tr class="even">
<td>PS</td>
<td>Push</td>
<td>Make a push
<ul>
<li>On failure go to End</li>
<li>On success go to WS</li>
</ul>
To fail: go to Can<br/></td>
</tr>
<tr class="odd">
<td>WS</td>
<td>Wait for Send</td>
<td>Wait for notification
<ul>
<li>On failure to get a notification go to Can</li>
<li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcSendComplete</strong></a> is received and more data needs to be sent go to PS</li>
<li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcSendComplete</strong></a> is received and more data does not need to be sent go to NP</li>
<li>If a failure <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcCallComplete</strong></a> is received go Comp</li>
</ul>
To fail: go to Can<br/></td>
</tr>
<tr class="even">
<td>NP</td>
<td>Null Push</td>
<td>Push 0 bytes (null push)
<ul>
<li>On failure go to End</li>
<li>On success go to PL</li>
</ul>
To fail: go to Can<br/></td>
</tr>
<tr class="odd">
<td>PL</td>
<td>Pull</td>
<td>Make a pull
<ul>
<li>On failure go to End</li>
<li>On success and synchronous completion with non-zero bytes read go to PL</li>
<li>On success and synchronous completion with zero bytes read (null pull) go to WComp</li>
<li>On success and asynchronous completion (ERROR_IO_PENDING is returned) go to WPL</li>
</ul>
To fail: go to Can<br/></td>
</tr>
<tr class="even">
<td>WPL</td>
<td>Wait for Pull</td>
<td>Wait for notification
<ul>
<li>On failure to get a completion go to Can</li>
<li>If a failure <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received go to Can</li>
<li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received with non-zero bytes read go to PL</li>
<li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received with zero bytes read go to Comp</li>
<li>If a failure is received go Can</li>
</ul>
To fail: go to Can<br/></td>
</tr>
<tr class="odd">
<td>Can</td>
<td>Cancel the Call</td>
<td>Call <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccancelcall"><strong>RpcAsyncCancelCall</strong></a>Go to WComp<br/></td>
</tr>
<tr class="even">
<td>WComp</td>
<td>Wait for Completion</td>
<td>Wait for notification. CallComplete notification should be received.<br/> Go to Comp<br/></td>
</tr>
<tr class="odd">
<td>Comp</td>
<td>Completion</td>
<td>Issue <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall"><strong>RpcAsyncCompleteCall</strong></a>Go to End<br/></td>
</tr>
<tr class="even">
<td>End</td>


</tr>
</tbody>
</table>



 

Server Behavior

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>State</th>
<th>State Name</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>D</td>
<td>Dispatch</td>
<td>The call is dispatched by the RPC runtimeGo to PL<br/> To fail fatally (while executing on the RPC thread): Raise exception; go to End<br/> To fail gracefully: Go to A<br/></td>
</tr>
<tr class="even">
<td>PL</td>
<td>Pull</td>
<td>Make a pull
<ul>
<li>On failure go to End</li>
<li>On success and synchronous completion with non-zero bytes read go to PL</li>
<li>On success and synchronous completion with zero bytes read (null pull) go to PS</li>
<li>On success and asynchronous completion (ERROR_IO_PENDING is returned) go to WPL</li>
</ul>
To fail: go to A<br/></td>
</tr>
<tr class="odd">
<td>WPL</td>
<td>Wait for Pull</td>
<td>Wait for notification
<ul>
<li>On failure to get a completion go to A</li>
<li>If a failure <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received go to A</li>
<li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received with non-zero bytes read go to PL</li>
<li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received with zero bytes read go to PS</li>
<li>If a failure is received go A</li>
</ul>
To fail: go to A<br/></td>
</tr>
<tr class="even">
<td>PS</td>
<td>Push</td>
<td>Make a push
<ul>
<li>On success go to WPS</li>
<li>On failure go to End</li>
</ul>
To fail: go to A<br/></td>
</tr>
<tr class="odd">
<td>WPS</td>
<td>Wait for Push</td>
<td>Wait for notification
<ul>
<li>On failure to get a completion go to A</li>
<li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcSendComplete</strong></a> is received and more data needs to be sent go to PS</li>
<li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcSendComplete</strong></a> is received and more data does not need to be sent go to NP</li>
<li>If a failure is received go Comp</li>
</ul>
To fail: go to A<br/></td>
</tr>
<tr class="even">
<td>NP</td>
<td>Null Push</td>
<td>Push 0 bytes
<ul>
<li>on success go to WNP</li>
<li>on failure go to Comp</li>
</ul>
To fail: go to A<br/></td>
</tr>
<tr class="odd">
<td>WNP</td>
<td>Wait for Null Push</td>
<td>Wait for notification
<ul>
<li>On failure to get a completion go to A</li>
<li>If a failure is received go Comp</li>
<li>If a success is received go Comp</li>
</ul>
<br/></td>
</tr>
<tr class="even">
<td>A</td>
<td>Abort the Call</td>
<td>Call <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasyncabortcall"><strong>RpcAsyncAbortCall</strong></a>; go to End</td>
</tr>
<tr class="odd">
<td>Comp</td>
<td>Completion</td>
<td>Issue <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall"><strong>RpcAsyncCompleteCall</strong></a>; go to End</td>
</tr>
<tr class="even">
<td>End</td>


</tr>
</tbody>
</table>



 

 

 





