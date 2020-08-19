---
title: context_handle_noserialize attribute
description: The \ context\_handle\_noserialize\ ACF attribute guarantees that a context handle will never be serialized, regardless of the application's default behavior.
ms.assetid: aff2484e-639b-41d2-94a9-f34ca4f2343c
keywords:
- context_handle_noserialize attribute MIDL
topic_type:
- apiref
api_name:
- context_handle_noserialize
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# context\_handle\_noserialize attribute

The **\[context\_handle\_noserialize\]** ACF attribute guarantees that a context handle will never be serialized, regardless of the application's default behavior.

``` syntax
typedef [context_handle_noserialize [ , type-acf-attribute-list ] ] context-handle-type

[context_handle_noserialize [, function-acf-attribute-list ] ] function-name( );

function-name (   [context_handle_noserialize 
  [ , parameter-acf-attribute-list ] ] param-name );
```

## Parameters

<dl> <dt>

*type-acf-attribute-list* 
</dt> <dd>

Any other ACF attributes that apply to the type.

</dd> <dt>

*context-handle-type* 
</dt> <dd>

The identifier that specifies the context handle type, as defined in a [**typedef**](typedef.md) declaration. This is the type that receives the [**\[context\_handle\]**](context-handle.md) attribute in the IDL file.

</dd> <dt>

*function-acf-attribute-list* 
</dt> <dd>

Any additional ACF attributes that apply to the function.

</dd> <dt>

*function-name* 
</dt> <dd>

The name of the function as defined in the IDL file.

</dd> <dt>

*parameter-acf-attribute-list* 
</dt> <dd>

Any other ACF attributes that apply to the parameter.

</dd> <dt>

*param-name* 
</dt> <dd>

The name of the parameter as defined in the IDL file.

</dd> </dl>

## Remarks

The [**\[context\_handle\]**](context-handle.md) attribute identifies a binding handle that maintains context, or state information, on the server between remote procedure calls. The attribute can appear as an IDL [**typedef**](typedef.md) type attribute, as a function return type attribute, or as a parameter attribute.

By default, calls on context handles are serialized. An application can call [**RpcSsDontSerializeContext**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcssdontserializecontext) to override this default behavior. Using the [**\[context\_handle\]**](context-handle.md) attribute in an ACF file guarantees that calls on this particular context handle will not be serialized, regardless of the calling application's behavior. Providing a context rundown routine is optional.

This attribute is available in MIDL version 5.0.

**Windows ServerÂ 2003 and WindowsÂ XP or later:** A single interface can accommodate both serialized and nonserialized context handles, enabling one method on an interface to access a context handle exclusively (serialized), while other methods access that context handle in shared mode (nonserialized). These access capabilities are comparable to read/write locking mechanisms; methods using a serialized context handle are exclusive users (writers), whereas methods using a nonserialized context handle are shared users (readers). Methods that destroy or modify the state of a context handle must be serialized. Methods that do not modify the state of a context handle, such as those methods that simply read from a context handle, can be nonserialized. Note that creation methods are implicitly serialized.

## Examples

``` syntax
typedef [context_handle_noserialize] PCONTEXT_HANDLE_TYPE; 
HRESULT RemoteFunc([context_handle_noserialize] pCxHandle);
```

## See also

<dl> <dt>

[ACF Attributes](acf-attributes.md)
</dt> <dt>

[**context\_handle\_serialize**](context-handle-serialize.md)
</dt> <dt>

[**context\_handle**](context-handle.md)
</dt> <dt>

[Context Handles](/windows/desktop/Rpc/context-handles)
</dt> <dt>

[**RpcSsDontSerializeContext**](/windows/desktop/api/rpcdce/nf-rpcdce-rpcssdontserializecontext)
</dt> <dt>

[Server Context Run-down Routine](/windows/desktop/Rpc/server-context-run-down-routine)
</dt> <dt>

[Multithreaded Clients and Context Handles](/windows/desktop/Rpc/multithreaded-clients-and-context-handles)
</dt> <dt>

[**typedef**](typedef.md)
</dt> </dl>

 

 