---
title: callback attribute
description: The \ callback\ attribute declares a static callback function that exists on the client side of the distributed application. Callback functions provide a way for the server to execute code on the client.
ms.assetid: c78947ae-614c-4f33-9ab7-1231e5031f80
keywords:
- callback attribute MIDL
topic_type:
- apiref
api_name:
- callback
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# callback attribute

The **\[callback\]** attribute declares a static callback function that exists on the client side of the distributed application. Callback functions provide a way for the server to execute code on the client.

``` syntax
[callback [ , function-attr-list] ] type-specifier [ptr-declarator] function-name(
        [ [attribute-list] ] type-specifier [declarator]
        , ...);
```

## Parameters

<dl> <dt>

*function-attr-list* 
</dt> <dd>

Specifies zero or more attributes that apply to the function. Valid function attributes are **\[**[**local**](local.md)**\]**; the pointer attribute **\[**[**ref**](ref.md)**\]**, **\[**[**unique**](unique.md)**\]**, or **\[**[**ptr**](ptr.md)**\]**; and the usage attributes **\[**[**string**](string.md)**\]**, **\[**[**ignore**](ignore.md)**\]**, and **\[**[**context\_handle**](context-handle.md)**\]**. Separate multiple attributes with commas.

</dd> <dt>

*type-specifier* 
</dt> <dd>

Specifies a [base\_type](midl-base-types.md), [**struct**](struct.md), [**union**](union.md), [**enum**](enum.md) type, or type identifier. An optional storage specification can precede *type-specifier*.

</dd> <dt>

*ptr-declarator* 
</dt> <dd>

Specifies zero or more pointer declarators. A pointer declarator is the same as the pointer declarator used in C; it is constructed from the \* designator, modifiers such as **far**, and the qualifier [**const**](const.md).

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the remote procedure.

</dd> <dt>

*attribute-list* 
</dt> <dd>

Specifies zero or more directional attributes, field attributes, usage attributes, and pointer attributes appropriate for the specified parameter type. Separate multiple attributes with commas.

</dd> <dt>

*declarator* 
</dt> <dd>

Specifies a standard C declarator such as identifiers, pointer declarators, and array declarators. For more information, see [Array and Sized-Pointer Attributes](array-and-sized-pointer-attributes.md), [**arrays**](arrays-1.md), and [Arrays and Pointers](/windows/desktop/Rpc/arrays-and-pointers). The parameter-name identifier is optional.

</dd> </dl>

## Remarks

The **\[callback\]** function is useful when the server must obtain information from the client. If server applications were supported on Windows 3.*x*, the server could make a call to a remote procedure on the Windows 3.*x* server to obtain the needed information. The callback function accomplishes the same purpose and lets the server query the client for information in the context of the original call.

Callbacks are special cases of remote calls that execute as part of a single thread. A callback is issued in the context of a remote call. Any remote procedure defined as part of the same interface as the static callback function can call the callback function.

It is important to note that the use of \[callback\] is not recommended in multi-thread programming. As a single-thread programming function, it is not equipped to support the security demands a multi-thread environment provides.

The **RpcCancelThread** function cannot be used to cancel a call that may dispatch a static callback. If a particular remote procedure call will never result in a callback, then it can be canceled. Otherwise, a call can be canceled only if it can be guaranteed that a callback for it has not been issued.

Only the connection-oriented and local-protocol sequences support the callback attribute. The size of the \[out\] data for callbacks over the local-protocol sequence is limited to 150 bytes. If an RPC interface uses a connectionless (datagram) protocol sequence, calls to procedures with the callback attribute will fail.

Handles cannot be used as parameters in callback functions. Because callbacks always execute in the context of a call, the binding handle used by the client to make the call to the server is also used as the binding handle from the server to the client.

Callbacks can nest to any depth.

## Examples

``` syntax
[callback] HRESULT DisplayString([in, string] char * p1);
```

## See also

<dl> <dt>

[**arrays**](arrays-1.md)
</dt> <dt>

[MIDL Base Types](midl-base-types.md)
</dt> <dt>

[**const**](const.md)
</dt> <dt>

[**context\_handle**](context-handle.md)
</dt> <dt>

[**enum**](enum.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**ignore**](ignore.md)
</dt> <dt>

[**local**](local.md)
</dt> <dt>

[**/osf**](-osf.md)
</dt> <dt>

[**ref**](ref.md)
</dt> <dt>

[**ptr**](ptr.md)
</dt> <dt>

[**string**](string.md)
</dt> <dt>

[**struct**](struct.md)
</dt> <dt>

[**union**](union.md)
</dt> <dt>

[**unique**](unique.md)
</dt> <dt>

[**RpcCancelThread**](/windows/desktop/api/rpcdce/nf-rpcdce-rpccancelthread)
</dt> </dl>

 

 