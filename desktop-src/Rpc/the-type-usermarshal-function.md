---
title: The type_UserMarshal Function
description: The type \_UserMarshal function is a helper function for the \ wire\_marshal\ and \ user\_marshal\ attributes.
ms.assetid: 3cbd78d1-a036-4d0d-bb1d-4c968acfdb36
keywords:
- type_UserMarshal
ms.topic: article
ms.date: 05/31/2018
---

# The type\_UserMarshal Function

The **&lt;type&gt;\_UserMarshal** function is a helper function for the \[ [wire\_marshal](/windows/desktop/Midl/wire-marshal)\] and \[ [user\_marshal](/windows/desktop/Midl/user-marshal)\] attributes. The stubs call this function to marshal data on the client or server side. The function is defined as:

``` syntax
unsigned char __RPC_FAR * __RPC_USER  <type>_UserMarshal(
    unsigned long __RPC_FAR * pFlags,
    unsigned char __RPC_FAR * pBuffer,
    <type>  __RPC_FAR *       pMyObj);
```

The &lt;type&gt; in the function name means the userm-type specified in the **\[wire\_marshal\]** or **\[user\_marshal\]** type definition. This type may be untransmittable or even—when used with the **\[user\_marshal\]** attribute—a type unknown to the MIDL compiler. The wire type name (the name of transmissible type) is not used in the function prototype. Note, however, that the wire type defines the wire layout for the data as specified by OSF DCE.

The *pFlags* parameter is a pointer to an unsigned long flag field. The upper word of the flag contains NDR data representation flags as defined by OSF DCE for floating point, byte order, and character representations. The lower word contains a marshaling context flag as defined by the COM channel. The exact layout of the flags within the field is described in [The type\_UserSize Function](the-type-usersize-function.md).

The *pBuffer* parameter is the current buffer pointer. This pointer may or may not be aligned on entry. Your **&lt;type&gt;\_UserMarshal** function should align the buffer pointer appropriately, marshal the data, and return the new buffer position, which is the address of the first byte after the marshaled object. Keep in mind that the wire type specification determines the actual layout of the data in the buffer.

The *pMyObj* parameter is a pointer to a user type object.

The return value is the new buffer position, which is the address of the first byte after the unmarshaled object.

Buffer overflow can occur when you incorrectly calculate the size of the data and attempt to marshal more data than expected. You should be careful to avoid this situation. You can check against it by using the pointer that **&lt;type&gt;\_UserMarshal** returns. Otherwise, you risk having the NDR engine raise a buffer-overflow exception later.

Exceptions must be caught and handled locally, exceptions must not be allowed to propigated up the call stack.

## Related topics

<dl> <dt>

[Marshaling Rules for user\_marshal and wire\_marshal](marshaling-rules-for-user-marshal-and-wire-marshal.md)
</dt> <dt>

[wire\_marshal](/windows/desktop/Midl/wire-marshal)
</dt> <dt>

[user\_marshal](/windows/desktop/Midl/user-marshal)
</dt> </dl>

 

 
