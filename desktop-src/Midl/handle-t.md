---
title: handle_t attribute
description: The handle\_t keyword declares an object to be of the primitive handle type handle\_t. A primitive binding handle is a data object that can be used by the application to represent the binding.
ms.assetid: 94962ed6-5c17-43e7-853f-1e9c4b3118a7
keywords:
- handle_t attribute MIDL
topic_type:
- apiref
api_name:
- handle_t
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# handle\_t attribute

The **handle\_t** keyword declares an object to be of the primitive handle type **handle\_t**. A primitive binding handle is a data object that can be used by the application to represent the binding.

``` syntax
typedef RPC_BINDING_HANDLE handle_t;
```

## Parameters

This attribute has no parameters.

## Remarks

The **handle\_t** type is one of the predefined types of the interface definition language (IDL). It can appear as a type specifier in [**typedef**](typedef.md) declarations, general declarations, and function declarators (as a function-return-type specifier and a parameter-type specifier). For the context in which type specifiers appear, see [Interface Definition (IDL) File](interface-definition-idl-file.md).

In Microsoft RPC, parameters of type **handle\_t** can occur only as **\[**[**in**](in.md)**\]** parameters. Primitive handles cannot have the **\[**[**unique**](unique.md)**\]** or **\[**[**ptr**](ptr.md)**\]** attribute.

Parameters of type **handle\_t** (primitive handle parameters) are not transmitted on the network.

## See also

<dl> <dt>

[MIDL Base Types](midl-base-types.md)
</dt> <dt>

[Binding and Handles](/windows/desktop/Rpc/binding-and-handles)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**in**](in.md)
</dt> <dt>

[**typedef**](typedef.md)
</dt> <dt>

[**ptr**](ptr.md)
</dt> <dt>

[**unique**](unique.md)
</dt> </dl>

 

 