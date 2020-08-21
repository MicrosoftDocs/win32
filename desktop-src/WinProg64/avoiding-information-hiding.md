---
title: Avoiding Information Hiding
description: Occasionally, programs deliberately or inadvertently hide information from the RPC marshaling engine.
ms.assetid: 016b9221-092d-4c25-a396-4f41dcdfb3cf
keywords:
- backward compatibility 64-bit Windows Programming
- compatibility problems 64-bit Windows Programming
ms.topic: article
ms.date: 05/31/2018
---

# Avoiding Information Hiding

Occasionally, programs deliberately or inadvertently hide information from the RPC marshaling engine. Some examples are as follows:

-   Sending a data structure as an undifferentiated block of bytes
-   Leveraging performance by using a side effect from a method to channel additional data across the wire
-   Attempting to disguise a handle by passing it as a **DWORD** or a **ULONG**

These techniques are almost guaranteed to introduce compatibility problems even before you port your application to 64-bit Windows.

Instead of sending a server context as a **DWORD** in a standard remote procedure call, use a context handle to provide an opaque handle to a server context that is held on behalf of a client. Contexts are identified by GUIDs defined by the RPC run time when a server creates a context handle for a client. No pointer is used over the wire and the operation is completely transparent across 32- or 64-bit boundaries. For more information on using context handles, see [Context Handles](/windows/desktop/Rpc/context-handles).

DCOM interfaces cannot use context handles because COM provides its own context management. Instead of creating a context handle, you can pass an interface pointer to the COM object. Then you can call the methods directly through the interface pointer or place the pointer inside other calls. To release the server object, the client calls the interface's **Release** method through the interface pointer.

Again, there may be times when you cannot change the original design of the code that you are porting. If there is no way to avoid sending a pointer across the wire as a **DWORD**, you will have to implement some form of server-side mapping between **DWORD** values and pointers. One way to do this is to change the pointers in the client side application to pointer-precision types, such as **ULONG\_PTR** or **DWORD\_PTR**. Then use the MIDL \[[**call\_as**](/windows/desktop/Midl/call-as)\] attribute to put the pointers on the wire as **DWORD** values. The client-side wrapper need only pass the arguments along. The server-side wrapper handles the mapping between both types. In a similar way, you can use either the \[[**transmit\_as**](/windows/desktop/Midl/transmit-as)\] attribute or the \[[**represent\_as**](/windows/desktop/Midl/represent-as)\] attribute to convert your data to a backward-compatible format for wire representation.

If backward-wire compatibility is not an issue or if the handle is not used for remote calls and you are sure that remote calls between 32- and 64-bit processes will never happen, you can redefine an argument as a **ULONG64**. If necessary, you can modify the 32-bit application to pass a **DWORD** to the user. Alternatively, you can build separate stubs from separate IDL files for each platform using a **DWORD** on 32-bit Windows and a **ULONG64** on 64-bit Windows.

 

 