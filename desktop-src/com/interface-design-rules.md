---
title: Interface Design Rules
description: This section provides a short summary of interface design rules and guidelines.
ms.assetid: c43fc385-bcd6-45fc-91b2-ad9827fdb15c
ms.topic: article
ms.date: 05/31/2018
---

# Interface Design Rules

This section provides a short summary of interface design rules and guidelines. Some of these rules are specific to the COM architecture, while others are restrictions imposed by the interface design language, MIDL. For details of COM interface design, see [Anatomy of an IDL File](anatomy-of-an-idl-file.md).

By definition, an object is not a COM object unless it implements either the [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) interface or an interface that is derived from **IUnknown**. In addition, the following rules apply to all interfaces implemented on a COM object:

-   They must have a unique interface identifier (IID).
-   They must be immutable. Once they are created and published, no part of their definition may change.
-   All interface methods must return an **HRESULT** value so that the portions of the system that handle remote processing can report RPC errors.
-   All string parameters in interface methods must be Unicode.
-   Your data types must be remotable. If you cannot convert a data type to a remotable type, you will have to create your own marshaling and unmarshaling routines. Also, **LPVOID**, or **void \***, has no meaning on a remote computer. Use a pointer to [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown), if necessary.

> [!Note]  
> The current implementation of MIDL does not handle function overloading or multiple inheritance.

 

## Other Interface Design Considerations

Use pointers to data very carefully. To re-create the data in the address space of the process that is called, the RPC run time must know the exact size of the data. If, for example, a **CHAR \*** parameter points to a buffer of characters rather than to a single character, the data cannot be correctly re-created. Use the syntax available with MIDL to accurately describe the data structures represented by your type definitions.

Initialization is essential for pointers that are embedded in arrays and structures and passed across process boundaries. Uninitialized pointers may work when passed to a program in the same process space, but proxies and stubs assume that all pointers are initialized with valid addresses or are null.

Be careful when aliasing pointers (allowing pointers to point to the same piece of memory). If the aliasing is intentional, these pointers should be declared aliased in the IDL file. Pointers declared as nonaliased should never alias each other.

Pay attention to how you allocate and free memory. Remember that, unless you explicitly tell a COM object (by using the [**allocate**](/windows/desktop/Midl/allocate) attribute) not to free a data structure that was created during an out-of-process call, that structure will be destroyed when the call completes. Also, consider the potentially destructive overhead created by inefficient allocation of data structures that now need to be marshaled and unmarshaled.

Finally, be careful when defining your **HRESULT** return values so that you don't create error codes that conflict with COM-defined FACILITY\_ITF codes (values between 0x0000 and 0x01FF are reserved) or that conflict with other **HRESULT** values with the same value. Whenever possible, use the universal COM success and failure return values, and use an [**out**](/windows/desktop/Midl/out-idl) parameter, rather than an **HRESULT**, to return information specific to the function call.

For more information, see the following topics:

-   [Designing Remotable Interfaces](designing-remotable-interfaces.md)
-   [Using a COM Interface](using-a-com-interface.md)

## Related topics

<dl> <dt>

[Interface Definitions and Type Libraries](/windows/desktop/Midl/interface-definitions-and-type-libraries)
</dt> </dl>

 

 