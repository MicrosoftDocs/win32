---
title: Binding Handles
description: Binding is the process of creating a logical connection between a client program and a server program. The information that composes the binding between client and server is represented by a structure called a binding handle.
ms.assetid: '802e6da7-a329-4010-91bd-003ad2169121'
ms.topic: article
ms.date: 05/31/2018
---

# Binding Handles

Binding is the process of creating a logical connection between a client program and a server program. The information that composes the binding between client and server is represented by a structure called a binding handle.

A binding handle is analogous to a file handle that the fopen C run-time library function returns, or a window handle that the function [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa) returns.

As with these handles, your application cannot directly access and manipulate the information in the binding handle. The information in a binding handle data structure is available only to the RPC run-time libraries. You provide the handle, the run-time libraries access and manipulate the appropriate data.

This section presents a discussion on binding handles in the following topics:

-   [Types of Binding Handles](types-of-binding-handles.md)
-   [Client-Side Binding](client-side-binding.md)
-   [Server-Side Binding](server-side-binding.md)
-   [Fully and Partially Bound Handles](fully-and-partially-bound-handles.md)
-   [Interpreting Binding Information](interpreting-binding-information.md)
-   [Microsoft RPC Binding-Handle Extensions](microsoft-rpc-binding-handle-extensions.md)
-   [Binding-Handle Functions](binding-handle-functions.md)
-   [The RPC Name Service Database](the-rpc-name-service-database.md)

 

 