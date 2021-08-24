---
title: The type_UserSize Function
description: The type \_UserSize function is a helper function for the \ wire\_marshal\ and \ user\_marshal\ attributes.
ms.assetid: 74a46418-1a02-47ed-a3ab-35f3364cc38f
keywords:
- type_UserSize
ms.topic: article
ms.date: 05/31/2018
---

# The type\_UserSize Function

The **&lt;type&gt;\_UserSize** function is a helper function for the \[ [wire\_marshal](/windows/desktop/Midl/wire-marshal)\] and \[ [user\_marshal](/windows/desktop/Midl/user-marshal)\] attributes. The stubs call this function to size the RPC data buffer for the user data object before the data is marshaled on the client or server side. The function is defined as:

``` syntax
unsigned long __RPC_USER  <type>_UserSize(
    unsigned long __RPC_FAR * pFlags,
    unsigned long StartingSize,
    <type>  __RPC_FAR *pMyObj);
```

The &lt;type&gt; in the function name means the userm-type, as specified in the **\[wire\_marshal\]** or **\[user\_marshal\]** type definition. This type may be untransmittable or even—when used with the **\[user\_marshal\]** attribute— unknown to the MIDL compiler. The wire type name (the name of the type transmitted across the network) is not used in the function prototype. Note, however, that the wire type defines the layout for the data as specified by OSF DCE. All data must be converted to network data representation (NDR) format.

The *pFlags* parameter is a pointer to an **unsigned long** flag field. The upper word of the flag contains NDR format flags as defined by OSF DCE for floating point, byte order, and character representations. The lower word contains a marshaling context flag as defined by the COM channel. The exact layout of the flags within the field is shown in the following table.



| Bits  | Flag                                  | Value                                                                                     |
|-------|---------------------------------------|-------------------------------------------------------------------------------------------|
| 31-24 | Floating-point representation         | 0 = IEEE 1 = VAX 2 = Cray 3 = IBM                                                         |
| 23-20 | Integer and floating-point byte order | 0 = Big-endian 1 = Little-endian                                                          |
| 19-16 | Character representation              | 0 = ASCII 1 = EBCDIC                                                                      |
| 15-0  | Marshaling context flag               | 0 = MSHCTX\_LOCAL 1 = MSHCTX\_NOSHAREDMEM 2 = MSHCTX\_DIFFERENTMACHINE 3 = MSHCTX\_INPROC |



 

The marshaling context flag makes it possible to alter the behavior of your routine depending on the context for the RPC call. For example, if you have a handle (**long**) to a block of data, you could send the handle for an in-process call, but you would send the actual data for a call to a different machine. The marshaling context flag and its values are defined in the Wtypes.h and Wtypes.idl files in the Platform Software Development Kit (SDK).

> [!Note]  
> When the wire type is properly defined, you do not have to use the NDR format flags, as the NDR engine performs the necessary conversions.

 

The *StartingSize* a parameter is the current buffer offset. The starting size indicates the buffer offset for the user object, and it may or may not be aligned properly. Your routine should account for whatever padding is necessary.

The *pMyObj* parameter is a pointer to a user type object.

The return value is the new offset or buffer position. The function should return the cumulative size, which is the starting size plus possible padding plus the data size.

The **&lt;type&gt;\_UserSize** function can return an overestimate of the size needed. The actual size of the sent buffer is defined by the data size, not by the buffer allocation size.

The **&lt;type&gt;\_UserSize** function is not called if the wire size can be computed at compile time. Note that for most unions, even if there are no pointers, the actual size of the wire representation can be determined only at run time.

## Related topics

<dl> <dt>

[Marshaling rules for user\_marshal and wire\_marshal](marshaling-rules-for-user-marshal-and-wire-marshal.md)
</dt> <dt>

[user\_marshal](/windows/desktop/Midl/user-marshal)
</dt> <dt>

[wire\_marshal](/windows/desktop/Midl/wire-marshal)
</dt> </dl>

 

 
