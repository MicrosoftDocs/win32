---
title: type_strict_context_handle attribute
description: Use the \ type\_strict\_context\_handle\ in an ACF file to set restrictions on context handles.
ms.assetid: b67caad2-e87d-4eba-8555-8f347aadd515
keywords:
- type_strict_context_handle attribute MIDL
topic_type:
- apiref
api_name:
- type_strict_context_handle
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# type\_strict\_context\_handle attribute

Use the **\[type\_strict\_context\_handle\]** in an ACF file to set restrictions on context handles.

``` syntax
[ 
    type_strict_context_handle 
    [, interface-attribute-list] 
] 
interface interface-name
{
    interface-definition-statements
}
```

## Parameters

<dl> <dt>

*interface-attribute-list* 
</dt> <dd>

Other ACF attributes that apply to the interface as a whole. Valid attributes include [**auto\_handle**](auto-handle.md), [**implicit\_handle**](implicit-handle.md), [**explicit\_handle**](explicit-handle.md), and [**optimize**](optimize.md), [**code**](code.md), or [**nocode**](nocode.md). Separate multiple attributes with commas.

</dd> <dt>

*interface-name* 
</dt> <dd>

The name of the interface.

</dd> <dt>

*interface-definition-statements* 
</dt> <dd>

One or more MIDL statements that define the elements of the [**interface**](interface.md).

</dd> </dl>

## Remarks

In order to use this attribute, the -target flag must be set to NT60 (or higher) when running midl.exe.

\[type\_strict\_context\_handle\] is a functional superset of \[strict\_context\_handle\]. In \[strict\_context\_handle\], the type ID of the handle is always 0; in \[type\_strict\_context\_handle\], a unique type ID is assigned by the MIDL compiler.

It is recommended to use \[type\_strict\_context\_handle\] rather than \[strict\_context\_handle\]. Context handles are not associated with a specific type by default. When multiple types of context handles are used in the same process, it is possible for a malicious client to pass a context handle in place of another to produce undesirable results. The use of \[type\_strict\_context\_handle\] allows applications to enforce context handle type consistency and prevent any mismatched context handle type usage.

A context handle attributed with \[type\_strict\_context\_handle\] cannot also be attributed with \[strict\_context\_handle\].

## See also

<dl> <dt>

[Application Configuration File (ACF)](application-configuration-file-acf-.md)
</dt> <dt>

[**code**](code.md)
</dt> <dt>

[Context Handles](/windows/desktop/Rpc/context-handles)
</dt> <dt>

[**context\_handle\_serialize**](context-handle-serialize.md)
</dt> <dt>

[**context\_handle\_noserialize**](context-handle-noserialize.md)
</dt> <dt>

[**explicit\_handle**](explicit-handle.md)
</dt> <dt>

[**implicit\_handle**](implicit-handle.md)
</dt> <dt>

[**nocode**](nocode.md)
</dt> <dt>

[**optimize**](optimize.md)
</dt> <dt>

[strict\_context\_handle](strict-context-handle.md)
</dt> </dl>

 

 