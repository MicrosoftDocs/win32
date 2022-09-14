---
title: string attribute (RPC)
description: The \ string\ attribute and Remote Procedure Call (RPC).
ms.assetid: '794e03f2-b1e9-42dc-8536-9ced5c0e3dad'
ms.topic: article
ms.date: 05/31/2018
---

# string attribute (RPC)

The \[ [string](/windows/desktop/Midl/string)\] attribute indicates that the parameter is a pointer to an array of type [char](/windows/desktop/Midl/char-idl), [byte](/windows/desktop/Midl/byte), or **w\_char**. As with a conformant array, the size of a **\[string\]** parameter is determined at run time. Unlike a conformant array, the developer does not have to provide the length associated with the array—the **\[string\]** attribute tells the stub to determine the array size by calling **strlen**. A **\[string\]** attribute cannot be used at the same time as the \[ [length\_is](/windows/desktop/Midl/length-is)\] or \[ [last\_is](/windows/desktop/Midl/last-is)\] attributes.

The **\[in, string\]** attribute combination directs the stub to pass the string from client to server only. The amount of memory allocated on the server is the same as the transmitted string size plus one.

The \[ [out](/windows/desktop/Midl/out-idl), **string**\] attributes direct the stub to pass the string from server to client only. The call-by-value design of the C language insists that all **\[out\]** parameters must be pointers.

The **\[out\]** parameter must be a pointer and, by default, all pointer parameters are reference pointers. The reference pointer does not change during the call—it points to the same memory as before the call. For string pointers, the additional constraint of the reference pointer means the client must allocate sufficient valid memory before making the remote procedure call. The stubs transmit the string that the **\[out, string\]** attributes indicate into the memory already allocated on the client side.

The following topics describe the remote procedure parameter prototypes for strings:

-   [\[in, out, string\] Prototype](-in-out-string-prototype.md)
-   [\[in, string\] and \[out, string\] Prototype](-in-string-and-out-string-prototype.md)

 

 