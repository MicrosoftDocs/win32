---
title: auto_handle attribute
description: The \ auto\_handle\ ACF attribute directs the stub to automatically establish the binding for a function that does not have an explicit binding-handle parameter.Note  This attribute is obsolete and no longer supported.
ms.assetid: a402b933-f69b-4dfe-b0c5-b034d65d4a84
keywords:
- auto_handle attribute MIDL
topic_type:
- apiref
api_name:
- auto_handle
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# auto\_handle attribute

The **\[auto\_handle\]** ACF attribute directs the stub to automatically establish the binding for a function that does not have an explicit binding-handle parameter.

> [!Note]  
> This attribute is obsolete and no longer supported. Use of the [**/robust**](-robust.md) switch is recommended.

 

``` syntax
[ 
    auto_handle [, interface-attribute-list] 
] 
interface interface-name
{
    interface-definition
}
```

## Parameters

<dl> <dt>

*interface-attribute-list* 
</dt> <dd>

Specifies zero or more attributes that apply to the interface as a whole, such as [**code**](code.md) or [**nocode**](nocode.md). Separate interface attributes with commas.

</dd> <dt>

*interface-name* 
</dt> <dd>

Specifies the name of the interface.

</dd> <dt>

*interface-definition* 
</dt> <dd>

Specifies IDL statements that form the definition of the interface.

</dd> </dl>

## Remarks

The **\[auto\_handle\]** attribute appears in the interface header of the ACF. It also appears in the interface header of the IDL file when you specify the MIDL compiler switch [**/app\_config**](-app-config.md).

When the client calls a function that uses automatic binding and no binding to a server exists, the stub automatically establishes the binding. The binding is reused for subsequent calls to other functions in the interface that use automatic binding. The client application program does not have to declare or perform any processing relating to the binding handle.

When the ACF is not present or does not include the [**\[implicit\_handle\]**](implicit-handle.md) attribute, the MIDL compiler uses **\[auto\_handle\]** and issues an informational message. The MIDL compiler also uses **\[auto\_handle\]**, if needed, to establish the initial binding for a [**\[context\_handle\]**](context-handle.md).

The **\[auto\_handle\]** attribute can occur only if the [**\[implicit\_handle\]**](implicit-handle.md) or [**\[explicit\_handle\]**](explicit-handle.md) attribute does not occur. The **\[auto\_handle\]** attribute can occur in the ACF or IDL interface header at most once.

> [!Note]  
> You cannot use automatic binding (either with the **\[auto\_handle\]** attribute, or by default) if you are processing data through pipes.

 

## Examples

``` syntax
[
    auto_handle
] 
interface MyInterface 
{ 
    /* Interface definition goes here*/
} 
[
    auto_handle, 
    code
] 
interface MyInterface
{ 
    /* Interface definition goes here*/
}
```

## See also

<dl> <dt>

[Application Configuration File (ACF)](application-configuration-file-acf-.md)
</dt> <dt>

[**/app\_config**](-app-config.md)
</dt> <dt>

[**code**](code.md)
</dt> <dt>

[**explicit\_handle**](explicit-handle.md)
</dt> <dt>

[**context\_handle**](context-handle.md)
</dt> <dt>

[**implicit\_handle**](implicit-handle.md)
</dt> <dt>

[**nocode**](nocode.md)
</dt> </dl>

 

 




