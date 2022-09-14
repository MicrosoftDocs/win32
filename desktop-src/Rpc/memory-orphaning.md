---
title: Memory Orphaning
description: If your distributed application uses an \ in, out, unique\ or \ in, out, ptr\ pointer parameter, the server side of the application can change the value of the pointer parameter to null.
ms.assetid: 65588b4d-6bf4-44f7-994c-29a5b185c6b9
ms.topic: article
ms.date: 05/31/2018
---

# Memory Orphaning

If your distributed application uses an \[ [in](/windows/desktop/Midl/in), [out](/windows/desktop/Midl/out-idl), [unique](/windows/desktop/Midl/unique)\] or \[**in**, **out**, [ptr](/windows/desktop/Midl/ptr)\] pointer parameter, the server side of the application can change the value of the pointer parameter to null. When the server subsequently returns the null value to the client, memory referenced by the pointer before the remote procedure call is still present on the client side, but is no longer accessible from that pointer (except in the case of an aliased full pointer). This memory is said to be *orphaned*. This is also termed a *memory leak*. Repeated orphaning of memory on the client causes the client to run out of available memory resources.

Memory can also be orphaned whenever the server changes an embedded pointer to a null value. For example, if the parameter points to a complex data structure such as a tree, the server side of the application can delete nodes of the tree and set pointers inside the tree to null.

Another situation that can lead to a memory leak involves conformant, varying, and open arrays containing pointers. When the server application modifies the parameter that specifies the array size or transmitted range so that it represents a smaller value, the stubs use the smaller value(s) to free memory. The array elements with indices larger than the size parameter are orphaned. Your application must free elements outside the transmitted range.

 

 