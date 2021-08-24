---
title: The type_UserUnmarshal Function
description: The type \_UserUnmarshal function is a helper function for the \ wire\_marshal\ and \ user\_marshal\ attributes.
ms.assetid: ee7a0e96-11ec-4d15-9d4b-55cc175fdd55
keywords:
- type_UserMarshal
ms.topic: article
ms.date: 05/31/2018
---

# The type\_UserUnmarshal Function

The **&lt;type&gt;\_UserUnmarshal** function is a helper function for the \[ [wire\_marshal](/windows/desktop/Midl/wire-marshal)\] and \[ [user\_marshal](/windows/desktop/Midl/user-marshal)\] attributes. The stubs call this function to unmarshal data on the client or server side. The function is defined as:

``` syntax
unsigned char __RPC_FAR * __RPC_USER  <type>_UserUnmarshal(
    unsigned long __RPC_FAR * pFlags,
    unsigned char __RPC_FAR * pBuffer,
    <type>  __RPC_FAR *       pMyObj);
```

The &lt;type&gt; in the function name means the userm-type specified in the **\[wire\_marshal\]** or **\[user\_marshal\]** type definition. This type may be untransmittable or even—when used with the **\[user\_marshal\]** attribute—unknown to the MIDL compiler. The wire type name (the name of transmissible type) is not used in the function prototype. Note, however, that the wire type defines the wire layout for the data as specified by OSF DCE.

The *pFlags* parameter is a pointer to an **unsigned long** flag field. The upper word of the flag contains NDR data representation flags as defined by OSF DCE for floating point, byte order, and character representations. The lower word contains a marshaling context flag as defined by the COM channel. The exact layout of the flags within the field is described in [The type\_UserSize Function](the-type-usersize-function.md).

The *pBuffer* parameter is the current buffer pointer. This pointer may or may not be aligned on entry. Your **&lt;type&gt;\_UserUnmarshal** function should align the buffer pointer appropriately, unmarshal the data, and return the new buffer position, which is the address of the first byte after the unmarshaled object.

The *pMyObj* parameter is a pointer to a user-defined type object.

In a heterogeneous environment, the NDR engine performs any data conversion necessary before calling the **&lt;type&gt;\_UserUnmarshal** function. Note that the NDR engine carries out this data conversion according to the wire-type definition supplied for this user data type. The flag indicates the data representation of the sender.

## Related topics

<dl> <dt>

[Marshaling Rules for user\_marshal and wire\_marshal](marshaling-rules-for-user-marshal-and-wire-marshal.md)
</dt> <dt>

[wire\_marshal](/windows/desktop/Midl/wire-marshal)
</dt> <dt>

[user\_marshal](/windows/desktop/Midl/user-marshal)
</dt> </dl>

 

 
