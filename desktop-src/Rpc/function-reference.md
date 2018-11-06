---
title: Function Reference
description: This section documents the Remote Procedure Call (RPC) run-time functions supported in Microsoft RPC.
ms.assetid: 135bef8d-1794-420e-a111-604d02dbcc06
ms.topic: article
ms.date: 05/31/2018
---

# Function Reference

This section documents the Remote Procedure Call (RPC) run-time functions supported in Microsoft RPC. This section describes each function's purpose, syntax, input parameters, and return values. It also provides additional information to help you use RPC functions in an application.

All pointers passed to RPC functions must include the **\_ \_RPC\_FAR** attribute. For example, the pointer **RPC\_BINDING\_HANDLE \*** becomes **RPC\_BINDING\_HANDLE \_ \_RPC\_FAR \*** and **char \* \*** *Ptr* becomes **char \_ \_RPC\_FAR \* \_ \_RPC\_FAR \*** *Ptr*.

This section presents the function references in the following groups:

-   [RPC Functions](rpc-functions.md)
-   [RPC Callback and Notification Functions](rpc-callback-and-notification-functions.md)

 

 




