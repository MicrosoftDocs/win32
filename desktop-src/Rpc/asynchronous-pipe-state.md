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


| State | State Name | Action | 
|-------|------------|--------|
| C | Make the call | Make the RPC<ul><li>On success go to state WS</li><li>On exception go to End</li></ul>To fail: go to Can<br /> | 
| P | Push | Make a push<ul><li>On failure go to End</li><li>On success go to WS</li></ul>To fail: go to Can<br /> | 
| WS | Wait for Send | Wait for notification<ul><li>On failure to get a notification go to Can</li><li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcSendComplete</strong></a> is received and more data needs to be sent go to P</li><li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcSendComplete</strong></a> is received and more data does not need to be sent go to NP</li><li>If a failure <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcCallComplete</strong></a> is received go Comp</li></ul>To fail: go to Can<br /> | 
| NP | Null Push | Push 0 bytes (null push)<ul><li>On failure go to End</li><li>On success go to WComp</li></ul>To fail: go to Can<br /> | 
| Can | Cancel the Call | Call <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccancelcall"><strong>RpcAsyncCancelCall</strong></a>Go to WComp<br /> | 
| WComp | Wait for Completion | Wait for notificationCall-complete notification should be received.<br /> Go to Comp<br /> | 
| Comp | Completion | Issue <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall"><strong>RpcAsyncCompleteCall</strong></a>Go to End<br /> | 
| End | 




 

Server Behavior


| State | State Name | Action | 
|-------|------------|--------|
| D | Dispatch | The call is dispatched by the RPC runtime Go to P<br /> To fail fatally (while executing on the RPC thread): Raise exception; go to End<br /> To fail gracefully: Go to A<br /> | 
| P | Pull | Make a pull<ul><li>On failure go to End</li><li>On success and synchronous completion with non-zero bytes read go to P</li><li>On success and synchronous completion with zero bytes read (null pull) go to Comp</li><li>On success and asynchronous completion (ERROR_IO_PENDING is returned) go to WP</li></ul>To fail: go to A<br /> | 
| WP | Wait for Pull | Wait for notification<ul><li>On failure to get a completion go to A</li><li>If a failure <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received go to A</li><li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received with non-zero bytes read go to P</li><li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received with zero bytes read (null pull) go to Comp</li><li>If a failure is received go to A</li></ul>To fail: go to A<br /> | 
| A | Abort the Call | Call <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasyncabortcall"><strong>RpcAsyncAbortCall</strong></a>Go to End<br /> | 
| Comp | Completion | Call <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall"><strong>RpcAsyncCompleteCall</strong></a>Go to End<br /> | 
| End | 




 

## OUT Pipe

Client Behavior


| State | State Name | Action | 
|-------|------------|--------|
| C | Make the call | Make the RPC<ul><li>On success go to P</li><li>On failure go to Comp</li></ul>To fail: go to Can<br /> | 
| P | Pull | Make a pull<ul><li>On failure go to End</li><li>On success and synchronous completion with non-zero bytes read go to P</li><li>On success and synchronous completion with zero bytes read (null pull) go to WComp</li><li>On success and asynchronous completion (ERROR_IO_PENDING is returned) go to WP</li></ul>To fail: go to Can<br /> | 
| WP | Wait for Pull | Wait for notification<ul><li>On failure to get a completion go to Can</li><li>If a failure <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received go to Can</li><li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received with non-zero bytes read go to P</li><li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received with zero bytes read (null pull) go to Comp</li><li>If a failure is received go Can</li></ul>To fail: go to Can<br /> | 
| Can | Cancel the Call | Call <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccancelcall"><strong>RpcAsyncCancelCall</strong></a>Go to WComp<br /> | 
| WComp | Wait for Completion | Wait for notification. Call-complete notification should be received.<br /> Go to Comp<br /> | 
| Comp | Completion | Issue <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall"><strong>RpcAsyncCompleteCall</strong></a>Go to End<br /> | 
| End | 




 

Server Behavior


| State | State Name | Action | 
|-------|------------|--------|
| D | Dispatch | The call is dispatched by the RPC runtime Go to P<br /> To fail fatally (while executing on the RPC thread): Raise exception; go to End<br /> To fail gracefully: Go to A<br /> | 
| P | Push | Make a push<ul><li>On success go to WP</li><li>On failure go to End</li></ul>To fail: go to A<br /> | 
| WP | Wait for Push | Wait for notification<ul><li>On failure to get a completion go to A</li><li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcSendComplete</strong></a> is received and more data needs to be sent go to P</li><li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcSendComplete</strong></a> is received and more data does not need to be sent go to NP</li><li>If a failure is received go Comp</li></ul>To fail: go to A<br /> | 
| NP | Null Push | Push 0 bytes<ul><li>on success go to WNP</li><li>on failure go to Comp</li></ul>To fail: go to A<br /> | 
| WNP | Wait for Null Push | Wait for notification<ul><li>On failure to get a completion go to A</li><li>If a failure is received go Comp</li><li>If a success is received go Comp</li></ul> | 
| A | Abort the Call | Call <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasyncabortcall"><strong>RpcAsyncAbortCall</strong></a>; go to End | 
| Comp | Completion | Issue <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall"><strong>RpcAsyncCompleteCall</strong></a>; go to End | 
| End | 




 

## IN-OUT Pipe

Client Behavior


| State | State Name | Action | 
|-------|------------|--------|
| C | Make the call | Make the RPC<ul><li>On success go to WS</li><li>On exception go to End</li></ul>To fail: go to Can<br /> | 
| PS | Push | Make a push<ul><li>On failure go to End</li><li>On success go to WS</li></ul>To fail: go to Can<br /> | 
| WS | Wait for Send | Wait for notification<ul><li>On failure to get a notification go to Can</li><li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcSendComplete</strong></a> is received and more data needs to be sent go to PS</li><li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcSendComplete</strong></a> is received and more data does not need to be sent go to NP</li><li>If a failure <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcCallComplete</strong></a> is received go Comp</li></ul>To fail: go to Can<br /> | 
| NP | Null Push | Push 0 bytes (null push)<ul><li>On failure go to End</li><li>On success go to PL</li></ul>To fail: go to Can<br /> | 
| PL | Pull | Make a pull<ul><li>On failure go to End</li><li>On success and synchronous completion with non-zero bytes read go to PL</li><li>On success and synchronous completion with zero bytes read (null pull) go to WComp</li><li>On success and asynchronous completion (ERROR_IO_PENDING is returned) go to WPL</li></ul>To fail: go to Can<br /> | 
| WPL | Wait for Pull | Wait for notification<ul><li>On failure to get a completion go to Can</li><li>If a failure <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received go to Can</li><li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received with non-zero bytes read go to PL</li><li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received with zero bytes read go to Comp</li><li>If a failure is received go Can</li></ul>To fail: go to Can<br /> | 
| Can | Cancel the Call | Call <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccancelcall"><strong>RpcAsyncCancelCall</strong></a>Go to WComp<br /> | 
| WComp | Wait for Completion | Wait for notification. CallComplete notification should be received.<br /> Go to Comp<br /> | 
| Comp | Completion | Issue <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall"><strong>RpcAsyncCompleteCall</strong></a>Go to End<br /> | 
| End | 




 

Server Behavior


| State | State Name | Action | 
|-------|------------|--------|
| D | Dispatch | The call is dispatched by the RPC runtimeGo to PL<br /> To fail fatally (while executing on the RPC thread): Raise exception; go to End<br /> To fail gracefully: Go to A<br /> | 
| PL | Pull | Make a pull<ul><li>On failure go to End</li><li>On success and synchronous completion with non-zero bytes read go to PL</li><li>On success and synchronous completion with zero bytes read (null pull) go to PS</li><li>On success and asynchronous completion (ERROR_IO_PENDING is returned) go to WPL</li></ul>To fail: go to A<br /> | 
| WPL | Wait for Pull | Wait for notification<ul><li>On failure to get a completion go to A</li><li>If a failure <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received go to A</li><li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received with non-zero bytes read go to PL</li><li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcReceiveComplete</strong></a> is received with zero bytes read go to PS</li><li>If a failure is received go A</li></ul>To fail: go to A<br /> | 
| PS | Push | Make a push<ul><li>On success go to WPS</li><li>On failure go to End</li></ul>To fail: go to A<br /> | 
| WPS | Wait for Push | Wait for notification<ul><li>On failure to get a completion go to A</li><li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcSendComplete</strong></a> is received and more data needs to be sent go to PS</li><li>If a success <a href="/windows/desktop/api/Rpcasync/ne-rpcasync-rpc_async_event"><strong>RpcSendComplete</strong></a> is received and more data does not need to be sent go to NP</li><li>If a failure is received go Comp</li></ul>To fail: go to A<br /> | 
| NP | Null Push | Push 0 bytes<ul><li>on success go to WNP</li><li>on failure go to Comp</li></ul>To fail: go to A<br /> | 
| WNP | Wait for Null Push | Wait for notification<ul><li>On failure to get a completion go to A</li><li>If a failure is received go Comp</li><li>If a success is received go Comp</li></ul><br /> | 
| A | Abort the Call | Call <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasyncabortcall"><strong>RpcAsyncAbortCall</strong></a>; go to End | 
| Comp | Completion | Issue <a href="/windows/desktop/api/Rpcasync/nf-rpcasync-rpcasynccompletecall"><strong>RpcAsyncCompleteCall</strong></a>; go to End | 
| End | 




 

 

 





