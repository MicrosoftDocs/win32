---
title: Interface Marshaling
description: Interface Marshaling
ms.assetid: 71069bd3-5f90-406a-be78-bb1af9b1c1c0
ms.topic: article
ms.date: 05/31/2018
---

# Interface Marshaling

Unless you know beyond all doubt that your interface will never be used across apartment, thread, or process boundaries, you need to decide how to provide marshaling support for your interfaces. There are three ways to provide marshaling support:

-   Write your own proxy/stub code that calls the COM channel, which in turn calls the RPC run-time libraries. Theoretically, it is possible to do this, but in practice it is almost impossible to do without a significant amount of effort.
-   Describe your interfaces in an interface definition language (IDL) file and use the MIDL compiler to generate a proxy/stub DLL. This method provides the best performance and the most flexibility in terms of acceptable data types. Using MIDL-generated proxy stubs, you can control not only memory management but even the marshaling and unmarshaling of complex data types across different platforms.
-   Use MIDL to generate a type library that the system uses to provide marshaling support at run time. This is the easiest way to implement marshaling support. All you have to do is generate a type library and register it. Your interfaces must be Automation-compatible (either [**oleautomation**](/windows/desktop/Midl/oleautomation) or [**dual**](/windows/desktop/Midl/dual)), which places some restrictions on the kinds of data types you can use as method parameters. However, in most cases, the advantage of having your interfaces accessible to programs written in other languages, such as Microsoft Visual Basic and Java, outweighs the limitations on data types.

## Related topics

<dl> <dt>

[Inter-Object Communication](inter-object-communication.md)
</dt> </dl>

 

 