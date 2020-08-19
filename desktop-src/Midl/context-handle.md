---
title: context_handle attribute
description: The \ context\_handle\ attribute identifies a binding handle that maintains context, or state information, on the server between remote procedure calls.
ms.assetid: ab1aee44-4add-4816-a7ef-38bbf7b38918
keywords:
- context_handle attribute MIDL
topic_type:
- apiref
api_name:
- context_handle
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# context\_handle attribute

The **\[context\_handle\]** attribute identifies a binding handle that maintains context, or state information, on the server between remote procedure calls.

``` syntax
typedef [context_handle [ , type-attribute-list ] ] type-specifier declarator-list;

[context_handle [, function-attr-list ] ] type-specifier [ptr-decl] function-name(
    [ [parameter-attribute-list] ] type-specifier [declarator], ...);

[ [ function-attr-list ] ] type-specifier [ ptr-decl ] function-name(
    [context_handle [ , parameter-attribute-list ] ] type-specifier [declarator], ...);

[ void __RPC_USER context-handle-type_rundown (
  context-handle-type); ]
```

## Parameters

<dl> <dt>

*type-attribute-list* 
</dt> <dd>

Specifies one or more attributes that apply to the type.

</dd> <dt>

*type-specifier* 
</dt> <dd>

Specifies a pointer type or a type identifier. An optional storage specification can precede *type-specifier*.

</dd> <dt>

*declarator and declarator-list* 
</dt> <dd>

Specifies standard C declarators, such as identifiers, pointer declarators, and array declarators. The declarator for a context handle must include at least one pointer declarator. For more information, see [Array and Sized-Pointer Attributes](array-and-sized-pointer-attributes.md), [**arrays**](arrays-1.md), and [Arrays and Pointers](/windows/desktop/Rpc/arrays-and-pointers). The *declarator-list* consists of one or more declarators, separated by commas. The parameter-name identifier in the function declarator is optional.

</dd> <dt>

*function-attr-list* 
</dt> <dd>

Specifies zero or more attributes that apply to the function. Valid function attributes are **\[**[**callback**](callback.md)**\]**, **\[**[**local**](local.md)**\]**; the pointer attribute **\[**[**ref**](ref.md)**\]**, **\[**[**unique**](unique.md)**\]**, or **\[**[**ptr**](ptr.md)**\]**; and the usage attributes **\[**[**string**](string.md)**\]**, **\[**[**ignore**](ignore.md)**\]**, and **\[context\_handle\]**.

</dd> <dt>

*ptr-decl* 
</dt> <dd>

Specifies zero or more pointer declarators. A pointer declarator is the same as the pointer declarator used in C; it is constructed from the **\*** designator, modifiers such as **far**, and the qualifier [**const**](const.md).

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the remote procedure.

</dd> <dt>

*parameter-attribute-list* 
</dt> <dd>

Specifies zero or more directional attributes, field attributes, usage attributes, and pointer attributes appropriate for the specified parameter type. Separate multiple attributes with commas.

</dd> <dt>

*context-handle-type* 
</dt> <dd>

Specifies the identifier that specifies the context handle type as defined in a [**typedef**](typedef.md) declaration that takes the **\[context\_handle\]** attribute. The rundown routine is optional.

**Windows ServerÂ 2003 and WindowsÂ XP:** A single interface can accommodate both serialized and nonserialized context handles, enabling one method on an interface to access a context handle exclusively (serialized), while other methods access that context handle in shared mode (nonserialized). These access capabilities are comparable to read/write locking mechanisms; methods using a serialized context handle are exclusive users (writers), whereas methods using a nonserialized context handle are shared users (readers). Methods that destroy or modify the state of a context handle must be serialized. Methods that do not modify the state of a context handle, such as those methods that simply read from a context handle, can be nonserialized. Note that creation methods are implicitly serialized.

</dd> </dl>

## Remarks

The **\[context\_handle\]** attribute can appear as an IDL [**typedef**](typedef.md) type attribute, as a function return type attribute, or as a parameter attribute. When you apply the **\[context\_handle\]** attribute to a type definition, you must also provide a context rundown routine. See [Server Context Run-down Routine](/windows/desktop/Rpc/server-context-run-down-routine) for details.

When you use the MIDL compiler in default ([**/ms\_ext**](-ms-ext.md)) mode, a context handle can be any pointer type selected by the user, as long as it complies with the requirements for context handles described here. The data associated with such a context handle type is not transmitted on the network and should only be manipulated by the server application. DCE IDL compilers restrict context handles to pointers of type [**void**](void.md) **\***. Therefore this feature is not available when you use the MIDL compiler [**/osf**](-osf.md) switch.

As with other handle types, the context handle is opaque to the client application, and any data associated with it is not transmitted. On the server, the context handle serves as a handle on active context, and all data associated with the context handle type is accessible.

To create a context handle, the client passes to the server an **\[**[**out**](out-idl.md)**\]**, **\[**[**ref**](ref.md)**\]** pointer to a context handle. (The context handle itself can have a **NULL** or non-**NULL** value—as long as its value is consistent with its pointer attributes. For example, when the context handle type has the **\[**[**ref**](ref.md)**\]** attribute applied to it, it cannot have a **NULL** value.) Another binding handle must be supplied to accomplish the binding until the context handle is created. When no explicit handle is specified, implicit binding is used. When no **\[**[**implicit\_handle**](implicit-handle.md)**\]** attribute is present, an auto handle is used.

The remote procedure on the server creates an active context handle. The client must use that context handle as an **\[**[**in**](in.md)**\]** or **\[in**, **out\]** parameter in subsequent calls. An **\[in\]**-only context handle can be used as a binding handle, so it must have a non-**NULL** value. An **\[in\]**-only context handle does not reflect state changes on the server.

On the server, the called procedure can interpret the context handle as needed. For example, the called procedure can allocate heap storage and use the context handle as a pointer to this storage.

To close a context handle, the client passes the context handle as an **\[**[**in**](in.md)**\]**, **\[**[**out**](out-idl.md)**\]** argument. The server must return a **NULL** context handle when it is no longer maintaining context on behalf of the caller. For example, if the context handle represents an open file and the call closes the file, the server must set the context handle to **NULL** and return it to the client. A **NULL** value is invalid as a binding handle on subsequent calls.

A context handle is only valid for one server. When a function has two handle parameters and the context handle is not **NULL**, the binding handles must refer to the same address space.

When a function has an **\[**[**in**](in.md)**\]** or an **\[in**, **out\]** context handle, its context handle can be used as the binding handle. In this case, implicit binding is not used and the **\[**[**implicit\_handle**](implicit-handle.md)**\]** or **\[**[**auto\_handle**](auto-handle.md)**\]** attribute is ignored.

The following restrictions apply to context handles:

-   Context handles cannot be array elements, structure members, or union members. They can only be parameters.
-   Context handles cannot have the **\[**[**transmit\_as**](transmit-as.md)**\]** or **\[**[**represent\_as**](represent-as.md)**\]** attribute.
-   Parameters that are pointers to **\[**[**out**](out-idl.md)**\]** context handles must be **\[**[**ref**](ref.md)**\]** pointers.
-   An **\[**[**in**](in.md)**\]** context handle can be used as the binding handle and cannot be **NULL**.
-   An **\[in**, [**out**](out-idl.md) context handle can be **NULL** on input, but only if the procedure has another explicit handle parameter. If there are no other explicit non-**NULL** context handle parameters, the **\[in**, **out\]** context handle cannot be **NULL**.
-   A context handle cannot be used with callbacks.

## Examples

``` syntax
typedef [context_handle] void * PCONTEXT_HANDLE_TYPE; 
short RemoteFunc1([out] PCONTEXT_HANDLE_TYPE * pCxHandle); 
short RemoteFunc2([in, out] PCONTEXT_HANDLE_TYPE * pCxHandle); 
void __RPC_USER PCONTEXT_HANDLE_TYPE_rundown (PCONTEXT_HANDLE_TYPE);
```

## See also

<dl> <dt>

[**arrays**](arrays-1.md)
</dt> <dt>

[**auto\_handle**](auto-handle.md)
</dt> <dt>

[**callback**](callback.md)
</dt> <dt>

[Client Context Reset](/windows/desktop/Rpc/client-context-reset)
</dt> <dt>

[**const**](const.md)
</dt> <dt>

[Context Handles](/windows/desktop/Rpc/context-handles)
</dt> <dt>

[**handle**](handle.md)
</dt> <dt>

[Binding and Handles](/windows/desktop/Rpc/binding-and-handles)
</dt> <dt>

[**ignore**](ignore.md)
</dt> <dt>

[**implicit\_handle**](implicit-handle.md)
</dt> <dt>

[**in**](in.md)
</dt> <dt>

[**local**](local.md)
</dt> <dt>

[Multithreaded Clients and Context Handles](/windows/desktop/Rpc/multithreaded-clients-and-context-handles)
</dt> <dt>

[**/ms\_ext**](-ms-ext.md)
</dt> <dt>

[**out**](out-idl.md)
</dt> <dt>

[**ptr**](ptr.md)
</dt> <dt>

[**ref**](ref.md)
</dt> <dt>

[**represent\_as**](represent-as.md)
</dt> <dt>

[**RpcSsDestroyClientContext**](/windows/desktop/api/rpcndr/nf-rpcndr-rpcssdestroyclientcontext)
</dt> <dt>

[Server Context Run-down Routine](/windows/desktop/Rpc/server-context-run-down-routine)
</dt> <dt>

[**string**](string.md)
</dt> <dt>

[**transmit\_as**](transmit-as.md)
</dt> <dt>

[**typedef**](typedef.md)
</dt> <dt>

[**unique**](unique.md)
</dt> <dt>

[**void**](void.md)
</dt> </dl>

 

 