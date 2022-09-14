---
title: Function Attributes
description: The \ callback\ and \ local\ attributes can be applied as function attributes.
ms.assetid: 05e19164-072c-4a5a-878d-845273975854
ms.topic: article
ms.date: 05/31/2018
---

# Function Attributes

The **\[**[**callback**](/windows/desktop/Midl/callback)**\]** and **\[**[**local**](/windows/desktop/Midl/local)**\]** attributes can be applied as function attributes.

A callback is a remote call from server to client that executes as part of a conceptual single-execution thread. A callback is always issued in the context of a remote call (or callback) and is executed by the thread that issued the original remote call (or callback).

It is often desirable to place a local procedure declaration in the IDL file, since this is the logical place to describe interfaces to a package. The **\[**[**local**](/windows/desktop/Midl/local)**\]** attribute indicates that a procedure declaration is not actually a remote function, but a local procedure. The MIDL compiler does not generate any stubs for functions with the **\[local\]** attribute.

It is important to note that the use of **\[**[**callback**](/windows/desktop/Midl/callback)**\]** is not recommended in multi-thread programming. As a single-thread programming function, it is not equipped to support the security demands a multi-thread environment provides.

 

 