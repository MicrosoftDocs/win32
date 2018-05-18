---
title: Strings
description: The \ string\ attribute and Remote Procedure Call (RPC).
ms.assetid: '548283bd-023a-41dd-b1d0-661305d019e9'
---

# Strings

The \[ [string](https://msdn.microsoft.com/library/windows/desktop/aa367270)\] attribute indicates that the parameter is a pointer to an array of type [char](https://msdn.microsoft.com/library/windows/desktop/aa366749), [byte](https://msdn.microsoft.com/library/windows/desktop/aa366743), or **w\_char**. As with a conformant array, the size of a **\[string\]** parameter is determined at run time. Unlike a conformant array, the developer does not have to provide the length associated with the array—the **\[string\]** attribute tells the stub to determine the array size by calling **strlen**. A **\[string\]** attribute cannot be used at the same time as the \[ [length\_is](https://msdn.microsoft.com/library/windows/desktop/aa367068)\] or \[ [last\_is](https://msdn.microsoft.com/library/windows/desktop/aa367066)\] attributes.

The **\[in, string\]** attribute combination directs the stub to pass the string from client to server only. The amount of memory allocated on the server is the same as the transmitted string size plus one.

The \[ [out](https://msdn.microsoft.com/library/windows/desktop/aa367136), **string**\] attributes direct the stub to pass the string from server to client only. The call-by-value design of the C language insists that all **\[out\]** parameters must be pointers.

The **\[out\]** parameter must be a pointer and, by default, all pointer parameters are reference pointers. The reference pointer does not change during the call—it points to the same memory as before the call. For string pointers, the additional constraint of the reference pointer means the client must allocate sufficient valid memory before making the remote procedure call. The stubs transmit the string that the **\[out, string\]** attributes indicate into the memory already allocated on the client side.

The following topics describe the remote procedure parameter prototypes for strings:

-   [\[in, out, string\] Prototype](-in-out-string-prototype.md)
-   [\[in, string\] and \[out, string\] Prototype](-in-string-and-out-string-prototype.md)

 

 




