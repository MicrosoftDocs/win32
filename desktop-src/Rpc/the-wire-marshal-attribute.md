---
title: The wire_marshal Attribute
description: The \ wire\_marshal\ attribute is an IDL-type attribute similar in syntax to \ transmit\_as\ , but providing a more efficient way to marshal data across a network.
ms.assetid: b764ca2b-7bbc-4266-836c-0d70033e9c62
keywords:
- Remote Procedure Call RPC , attributes, wire_marshal
- wire_marshal
ms.topic: article
ms.date: 05/31/2018
---

# The wire\_marshal Attribute

The \[ [wire\_marshal](/windows/desktop/Midl/wire-marshal)\] attribute is an IDL-type attribute similar in syntax to \[ [transmit\_as](/windows/desktop/Midl/transmit-as)\], but providing a more efficient way to marshal data across a network.

You use the \[**wire\_marshal**\] attribute to specify a data type that will be transmitted in place of the application-specific data type. Each application-specific type has a corresponding transmittable type that defines the wire representation (the representation used on the network).The application-specific type need not be transmittable, but it must be a type that MIDL recognizes. To marshal a type unknown to MIDL, use the ACF attribute \[ [user\_marshal](/windows/desktop/Midl/user-marshal)\].

Your application-specific type can be a simple, composite, or pointer type. The main restriction is that the type instance must have a fixed, well-defined memory size. If the size of your type instance needs to change, use a pointer field rather than a conformant array. Alternatively, you can define a pointer to the changeable type.

You must supply the routines for sizing, marshaling, and unmarshaling the data as well as freeing the associated memory. The following table describes the four user-supplied routine names. The &lt;type&gt; is the userm-type specified in the \[**wire\_marshal**\] type definition.



| Routine                                                            | Description                                                               |
|--------------------------------------------------------------------|---------------------------------------------------------------------------|
| [&lt;type&gt;\_UserSize](the-type-usersize-function.md)           | Sizes the RPC data buffer before marshaling on the client or server side. |
| [&lt;type&gt;\_UserMarshal](the-type-usermarshal-function.md)     | Marshals the data on the client or server side.                           |
| [&lt;type&gt;\_UserUnmarshal](the-type-userunmarshal-function.md) | Unmarshals the data on the client or server side.                         |
| [&lt;type&gt;\_UserFree](the-type-userfree-function.md)           | Frees the data on the server side.                                        |



 

These programmer-supplied routines are provided by either the client or the server application based on the directional attributes.

If the parameter is \[ [in](/windows/desktop/Midl/in)\] only, the client transmits to the server. The client needs the **&lt;type&gt;\_UserSize** and **&lt;type&gt;\_UserMarshal** functions. The server needs the **&lt;type&gt;\_UserUnmarshal**, and **&lt;type&gt;\_UserFree** functions.

For an \[ [out](/windows/desktop/Midl/out-idl)\]-only parameter, the server transmits to the client. The server needs the **&lt;type&gt;\_UserSize** and **&lt;type&gt;\_UserMarshal** functions, while the client needs the **&lt;type&gt;\_UserMarshal** function.

## Related topics

<dl> <dt>

[The user\_marshal Attribute](the-user-marshal-attribute.md)
</dt> <dt>

[Marshaling Rules for user\_marshal and wire\_marshal](marshaling-rules-for-user-marshal-and-wire-marshal.md)
</dt> <dt>

[wire\_marshal](/windows/desktop/Midl/wire-marshal)
</dt> <dt>

[user\_marshal](/windows/desktop/Midl/user-marshal)
</dt> <dt>

[**NdrGetUserMarshalInfo**](/windows/desktop/api/Rpcndr/nf-rpcndr-ndrgetusermarshalinfo)
</dt> </dl>

 

 
