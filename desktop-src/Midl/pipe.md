---
title: pipe attribute
description: The pipe type constructor makes it possible to transmit an open-ended stream of typed data across a remote procedure call.
ms.assetid: 85b76a55-8df2-4417-9a39-3e3bf49651fc
keywords:
- pipe attribute MIDL
topic_type:
- apiref
api_name:
- pipe
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# pipe attribute

The **pipe** type constructor makes it possible to transmit an open-ended stream of typed data across a remote procedure call.

``` syntax
typedef pipe element-type pipe-declarator;
```

## Parameters

<dl> <dt>

*element-type* 
</dt> <dd>

Defines the size of a single element in the transfer buffer. The *element-type* can be a [base type](midl-base-types.md), predefined\_type, [**struct**](struct.md), [**32b enum**](v1-enum.md), or type identifier. Several restrictions apply to *element\_types*, as described in Remarks, below.

</dd> <dt>

*pipe-declarator* 
</dt> <dd>

Specifies one or more identifiers or pointers to identifiers. Separate multiple declarators with commas.

</dd> </dl>

## Remarks

You can use the **pipe** type constructor to transmit data in both directions. An **\[**[**in**](in.md)**\]** pipe parameter allows the server to pull the data stream from the client during a remote procedure call. An **\[**[**out**](out-idl.md)**\]** pipe parameter allows the server to push the data stream back to the client. You supply the client-side routines to push and pull the data stream and to allocate a global buffer for the data. The client and server stub routines marshal and unmarshal data and pass a reference to the buffer back to the application.

The following restrictions apply to pipes:

-   A pipe element cannot be or contain a pointer, a conformant or varying array, a handle, or a context handle. Also, in the Microsoft implementation of pipes, a pipe element cannot be or contain a [**union**](union.md), a [**16b enum**](enum.md), or an [**\_\_int3264**](--int3264.md).
-   You cannot apply the **\[**[**transmit\_as**](transmit-as.md)**\]**, **\[**[**represent\_as**](represent-as.md)**\]**, **\[**[**wire\_marshal**](wire-marshal.md)**\]**, or **\[**[**user\_marshal**](user-marshal.md)**\]** attributes to a pipe type or to the *element-type*.
-   A pipe type cannot be a member of a structure or union, the target of a pointer, or the base type of an array.
-   A data type declared to be a pipe type can only be used as a parameter of a remote call.
-   You can pass a pipe parameter in either direction by value or by reference (**\[**[**ref**](ref.md)**\]** pointer). However you cannot apply the **\[**[**ptr**](ptr.md)**\]** attribute to a pipe that is passed by reference. You cannot specify a pipe parameter with a **\[**[**unique**](unique.md)**\]** or a full pointer, regardless of direction.
-   You cannot use pipes in **\[**[**object**](object.md)**\]** interfaces.
-   You cannot apply the **\[**[**idempotent**](idempotent.md)**\]** attribute to a routine that has a pipe parameter.
-   You cannot use the serialization attributes, **\[**[**encode**](encode.md)**\]** and **\[**[**decode**](decode.md)**\]** with pipes.
-   You cannot use automatic handles, either by default, or with the **\[**[**auto\_handle**](auto-handle.md)**\]** attribute, with pipes.

> [!Note]  
> The MIDL compiler supports pipes in [**/Oif**](-oi.md) mode only.

 

For more information on implementing routines with pipe parameters, see [Pipes](/windows/desktop/Rpc/pipes) in the RPC Programmer's Guide and Reference.

## Examples

``` syntax
typedef pipe unsigned char UCHAR_PIPE1, UCHAR_PIPE2;
 
//SIMPLE_STRUCT defined elsewhere
typedef pipe SIMPLE_STRUCT SIMPLE_STRUCT_PIPE;
```

## See also

<dl> <dt>

[**auto\_handle**](auto-handle.md)
</dt> <dt>

[MIDL Base Types](midl-base-types.md)
</dt> <dt>

[**decode**](decode.md)
</dt> <dt>

[**encode**](encode.md)
</dt> <dt>

[**enum**](enum.md)
</dt> <dt>

[**idempotent**](idempotent.md)
</dt> <dt>

[**in**](in.md)
</dt> <dt>

[**object**](object.md)
</dt> <dt>

[**out**](out-idl.md)
</dt> <dt>

[**ptr**](ptr.md)
</dt> <dt>

[**ref**](ref.md)
</dt> <dt>

[**represent\_as**](represent-as.md)
</dt> <dt>

[**struct**](struct.md)
</dt> <dt>

[**transmit\_as**](transmit-as.md)
</dt> <dt>

[**unique**](unique.md)
</dt> <dt>

[**user\_marshal**](user-marshal.md)
</dt> <dt>

[**wire\_marshal**](wire-marshal.md)
</dt> </dl>

 

 