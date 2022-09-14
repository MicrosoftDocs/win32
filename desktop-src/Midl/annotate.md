---
title: annotate attribute
description: The \ annotate\ attribute allows you to specify a SAL annotation string for the specified method, parameter, or structure field.
ms.assetid: D0A35DCD-BD2F-455B-A040-5D63E4572D83
keywords:
- annotate attribute MIDL
topic_type:
- apiref
api_name:
- annotate
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# annotate attribute

The **\[annotate\]** attribute allows you to specify a SAL annotation string for the specified method, parameter, or structure field.

``` syntax
[ annotation(â€œstringâ€0,  [, function-attribute-list] ] function-declarator ;
[ [function-attribute-list] ] type-specifier [pointer-declarator] function-name(
    [ annotation(â€œstringâ€) [ , parameter-attribute-list ] ] type-specifier [declarator]
    , ...);
```

## Parameters

<dl> <dt>

*string* 
</dt> <dd>

Specified SAL annotation string.

</dd> <dt>

*function-attribute-list* 
</dt> <dd>

Specifies zero or more attributes that apply to the function. Valid function attributes include [**\[callback\]**](callback.md); the pointer attributes [**\[ref\]**](ref.md), [**\[unique\]**](unique.md), or [**\[ptr\]**](ptr.md); and the usage attributes [**\[string\]**](string.md), [**\[ignore\]**](ignore.md), and [**\[context\_handle\]**](context-handle.md). Multiple attributes must be separated by commas.

</dd> <dt>

*function-declarator* 
</dt> <dd>

Specifies the type specifier, function name, and parameter list for the function.

</dd> <dt>

*type-specifier* 
</dt> <dd>

Specifies a **base\_type**, [**\[struct\]**](struct.md), [**union**](union.md), or [**\[enum\]**](enum.md) type or type identifier. An optional storage specification can precede *type-specifier*.

</dd> <dt>

*pointer-declarator* 
</dt> <dd>

Specifies zero or more pointer declarators. A pointer declarator is the same as a pointer declarator used in C; it is constructed from the \* designator, modifiers such as **far**, and the qualifier [**\[const\]**](const.md).

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the remote procedure.

</dd> <dt>

*parameter-attribute-list* 
</dt> <dd>

Specifies zero or more attributes appropriate for the parameter type. Parameter attributes with the [**\[in\]**](in.md) attribute can also take the directional attribute [**\[out\]**](out-idl.md); the field attributes [**\[first\_is\]**](first-is.md), [**\[last\_is\]**](last-is.md), [**\[length\_is\]**](length-is.md), [**\[max\_is\]**](max-is.md), [**\[size\_is\]**](size-is.md), and [**\[switch\_type\]**](switch-type.md); the pointer attributes [**\[ref\]**](ref.md), [**\[unique\]**](unique.md), or [**\[ptr\]**](ptr.md); and the usage attributes [**\[context\_handle\]**](context-handle.md) and [**\[string\]**](string.md). The usage attribute [**\[ignore\]**](ignore.md) cannot be used as a parameter attribute. Multiple attributes must be separated by commas.

</dd> <dt>

*declarator* 
</dt> <dd>

Specifies standard C declarators, such as identifiers, pointer declarators, and array declarators. For more information, see [Array and Sized-Pointer Attributes](array-and-sized-pointer-attributes.md), [**\[arrays\]**](../rpc/arrays.md), and [Arrays and Pointers](/windows/desktop/Rpc/arrays-and-pointers). The parameter declarator in the function declarator, such as the parameter name, is optional.

</dd> </dl>

## Remarks

The **\[annotate\]** attribute allows overriding MIDL-generated SAL annotations or adding them in places where MIDL does not explicitly generate an annotation. If [**/sal**](-sal.md) is not specified on the command line, this attribute is ignored.

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/sal**](-sal.md)
</dt> <dt>

[**/sal\_local**](-sal-local.md)
</dt> </dl>

 

 