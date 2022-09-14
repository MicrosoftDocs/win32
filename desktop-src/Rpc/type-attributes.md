---
title: Type Attributes
description: Remote Procedure Call (RPC) and the MIDL type attributes that can be applied to type declarations.
ms.assetid: cd7fd582-6162-4154-9dff-6c86c344b9ae
ms.topic: article
ms.date: 05/31/2018
---

# Type Attributes

Type attributes are the MIDL attributes that can be applied to type declarations:

-   **\[**[**handle**](/windows/desktop/Midl/handle)**\]**
-   **\[**[**context\_handle**](/windows/desktop/Midl/context-handle)**\]**
-   **\[**[**switch\_type**](/windows/desktop/Midl/switch-type)**\]**
-   [pointer type attributes](three-pointer-types.md)

The **\[switch\_type\]** attribute designates the type of a union discriminator. This attribute applies only to a nonencapsulated union.

A context handle is a pointer with a **\[context\_handle\]** attribute. The **\[context\_handle\]** attribute allows you to write procedures that maintain state information between remote procedure calls. A context handle with a non-null value represents saved context and serves two purposes:

-   On the client side, it contains the information needed by the RPC run-time library to direct the call to the server.
-   On the server side, it serves as a handle on active context.

The **\[**[**handle**](/windows/desktop/Midl/handle)**\]** attribute specifies that a type can occur as a user-defined (generic) handle. This feature permits the design of handles that are meaningful to the application. The user must provide binding and unbinding routines to convert between the user-defined handle type and the RPC primitive handle type, **handle\_t**. A primitive handle contains destination information meaningful to the RPC run-time libraries. A user-defined handle can only be defined in a type declaration, not in a function declaration. A parameter with the **\[handle\]** attribute has a double purpose. It is used to determine the binding for the call, and it is transmitted to the called procedure as a normal data parameter.

 

 