---
title: The type_UserFree Function
description: The type \_UserFree function is a helper function for the \ wire\_marshal\ and \ user\_marshal\ attributes.
ms.assetid: cc83a074-ea6c-432a-92fe-6397a6dc3c3c
keywords:
- type_UserFree
ms.topic: article
ms.date: 05/31/2018
---

# The type\_UserFree Function

The **&lt;type&gt;\_UserFree** function is a helper function for the \[ [wire\_marshal](/windows/desktop/Midl/wire-marshal)\] and \[ [user\_marshal](/windows/desktop/Midl/user-marshal)\] attributes. The stubs call this function to free the data on the server side. The function is defined as:

``` syntax
void __RPC_USER  <type>_UserFree(
    unsigned long __RPC_FAR * pFlags,
    <type_name>  __RPC_FAR *  pMyObj );
```

The &lt;type&gt; in the function name means the userm-type specified in the **\[wire\_marshal\]** or **\[user\_marshal\]** type definition.

The *pFlags* parameter is a pointer to an **unsigned long** flag field. The upper word of the flag contains NDR data representation flags as defined by OSF DCE for floating point, byte order, and character representations. The lower word contains a marshaling context flag as defined by the COM channel. The exact layout of the flags within the field is described in [The type\_UserSize Function](the-type-usersize-function.md).

The *pMyObj* parameter is a pointer to a user type object. The NDR engine frees the top-level object. You are responsible for freeing any objects to which the top-level object may point.

Exceptions must be caught and handled locally, exceptions must not be allowed to propigated up the call stack.

## Related topics

<dl> <dt>

[Marshaling Rules for user\_marshal and wire\_marshal](marshaling-rules-for-user-marshal-and-wire-marshal.md)
</dt> <dt>

[wire\_marshal](/windows/desktop/Midl/wire-marshal)
</dt> <dt>

[user\_marshal](/windows/desktop/Midl/user-marshal)
</dt> </dl>

 

 
