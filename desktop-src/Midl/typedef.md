---
title: typedef attribute
description: The IDL typedef keyword allows typedef declarations that are very similar to C-language typedef declarations.
ms.assetid: 995a233e-0d07-4051-9f00-d1dc0b563f8f
keywords:
- typedef attribute MIDL
topic_type:
- apiref
api_name:
- typedef
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# typedef attribute

The IDL **typedef** keyword allows **typedef** declarations that are very similar to C-language **typedef** declarations.

``` syntax
/* IDL file typedef syntax */
typedef [[ [ idl-type-attribute-list ] ]] type-specifier declarator-list;

/* ACF typedef syntax */
typedef [ acf-type-attribute-list ] typename;
```

## Parameters

<dl> <dt>

*idl-type-attribute-list* 
</dt> <dd>

Specifies one or more attributes that apply to the type. Valid type attributes in an IDL file include **\[**[**handle**](handle.md)**\]**, **\[**[**switch\_type**](switch-type.md)**\]**, **\[**[**transmit\_as**](transmit-as.md)**\]**; the pointer attribute **\[**[**ref**](ref.md)**\]**, **\[**[**unique**](unique.md)**\]**, or **\[**[**ptr**](ptr.md)**\]**; and the usage attributes **\[**[**context\_handle**](context-handle.md)**\]**, **\[**[**string**](string.md)**\]**, and **\[**[**ignore**](ignore.md)**\]**. Separate multiple attributes with commas.

</dd> <dt>

*type-specifier* 
</dt> <dd>

Specifies a [base type](midl-base-types.md), [**struct**](struct.md), [**union**](union.md), [**enum**](enum.md) type, or type identifier. An optional storage specification can precede *type-specifier*. The [**const**](const.md) keyword can precede *type-specifier*.

</dd> <dt>

*declarator-list* 
</dt> <dd>

Specifies standard MIDL declarators, such as identifiers, pointer declarators, and array declarators. For more information, see [Array and Sized-Pointer Attributes](array-and-sized-pointer-attributes.md), [**arrays**](arrays-1.md), and [Arrays and Pointers](/windows/desktop/Rpc/arrays-and-pointers). The *declarator-list* consists of one or more declarators, separated by commas.

</dd> <dt>

*acf-type-attribute-list* 
</dt> <dd>

Specifies one or more attributes that apply to the type. Valid type attributes in an ACF include **\[**[**allocate**](allocate.md)**\]**, **\[**[**encode**](encode.md)**\]**, and **\[**[**decode**](decode.md)**\]**.

</dd> <dt>

*typename* 
</dt> <dd>

Specifies a type defined in the IDL file.

</dd> </dl>

## Remarks

The IDL **typedef** declaration is augmented to allow you to associate type attributes with the defined types. Valid type attributes include **\[**[**handle**](handle.md)**\]**, **\[**[**switch\_type**](switch-type.md)**\]**, **\[**[**transmit\_as**](transmit-as.md)**\]**; the pointer attribute **\[**[**ref**](ref.md)**\]**, **\[**[**unique**](unique.md)**\]**, or **\[**[**ptr**](ptr.md)**\]**; and the usage attributes **\[**[**context\_handle**](context-handle.md)**\]**, **\[**[**string**](string.md)**\]**, and **\[**[**ignore**](ignore.md)**\]**.

The **typedef** keyword in an ACF applies attributes to types that are defined in the corresponding IDL file. For example, the [**allocate**](allocate.md) type attribute allows you to customize memory allocation and deallocation by both the application and the stubs.

The ACF **typedef** statement appears as part of the ACF body. Note that the ACF **typedef** syntax is different from the IDL **typedef** syntax and the C-language **typedef** syntax. No new types can be introduced in the ACF.

## See also

<dl> <dt>

[Application Configuration File (ACF)](application-configuration-file-acf-.md)
</dt> <dt>

[**allocate**](allocate.md)
</dt> <dt>

[**arrays**](arrays-1.md)
</dt> <dt>

[**const**](const.md)
</dt> <dt>

[**context\_handle**](context-handle.md)
</dt> <dt>

[**decode**](decode.md)
</dt> <dt>

[**encode**](encode.md)
</dt> <dt>

[**enum**](enum.md)
</dt> <dt>

[**handle**](handle.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**ignore**](ignore.md)
</dt> <dt>

[**ptr**](ptr.md)
</dt> <dt>

[**ref**](ref.md)
</dt> <dt>

[**string**](string.md)
</dt> <dt>

[**struct**](struct.md)
</dt> <dt>

[**switch\_type**](switch-type.md)
</dt> <dt>

[**transmit\_as**](transmit-as.md)
</dt> <dt>

[**union**](union.md)
</dt> <dt>

[**unique**](unique.md)
</dt> </dl>

 

 