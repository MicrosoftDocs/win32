---
title: Multithreaded Clients and Context Handles
description: When you have a multithreaded client where multiple threads are using the same context handle instance, access to the context handle instance is serialized at the server by default.
ms.assetid: 192be467-b1e0-422b-878a-738cb7d72b5b
ms.topic: article
ms.date: 05/31/2018
---

# Multithreaded Clients and Context Handles

When you have a multithreaded client where multiple threads are using the same context handle instance, access to the context handle instance is serialized at the server by default. This saves the server manager from having to guard against another thread from the same client changing the context or the context running down while a call is dispatched. However, in certain cases serialization may impact performance.

Consider the following: two client threads invoke a remote procedure call that does not change the state of the context (for example, the call simply obtains some values from it). Such calls do not need to be serialized.

For such situations, Windows XP offers a mixed mode serialization model, where each method may be declared to have exclusive or shared access to a context handle. See [context\_handle\_serialize](/windows/desktop/Midl/context-handle-serialize) and [context\_handle\_noserialize](/windows/desktop/Midl/context-handle-noserialize) for details.

In versions of Windows prior to Windows XP, the only means of allowing concurrent access to a context handle is to call the [**RpcSsDontSerializeContext**](/previous-versions/aa378473(v=vs.80)) function to allow multiple calls to be dispatched on a single context handle. Calling the **RpcSsDontSerializeContext** function does not disable serialization entirely; when a context run-down occurs, the context run-down routine runs only when all outstanding client requests have completed. A call to **RpcScDontSerializeContext** affects the entire process, and is not revertible. Using **RpcScDontSerializeContext** in Windows XP and later versions is not recommended; it makes server code very complicated when dealing reliably with race conditions inherent in completely non-serialized environments.

 

 