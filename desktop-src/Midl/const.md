---
title: const attribute
description: The const keyword modifies the type of a type declaration or the type of a function parameter, preventing the value from varying.
ms.assetid: 398fab76-93f3-4d5a-9223-1c57c612b2d7
keywords:
- const attribute MIDL
topic_type:
- apiref
api_name:
- const
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# const attribute

The **const** keyword modifies the type of a type declaration or the type of a function parameter, preventing the value from varying.

``` syntax
const const-type identifier = const-expression ;

[ typedef [ , type-attribute-list ] ] const const-type declarator-list;

[ typedef [ , type-attribute-list ] ] pointer-type const declarator-list;

[ [ function-attr-list ] ] type-specifier [ ptr-decl ] function-name(
    [ [ parameter-attribute-list ] ] ) const; 

const-type [declarator], [ [ parameter-attribute-list ] ] pointer-type const [declarator], ...);
```

## Parameters

<dl> <dt>

*const-type* 
</dt> <dd>

Specifies a valid MIDL integer, character, string, or Boolean type. Valid MIDL types include [**small**](small.md), [**short**](short.md), [**long**](long.md), [**char**](char-idl.md), **charÂ \***, [**wchar\_t**](wchar-t.md), **wchar\_tÂ \***, [**byte**](byte.md), **byteÂ \***, and [**voidÂ \***](void.md). The integer and character types can be [**signed**](signed.md) or [**unsigned**](unsigned.md).

</dd> <dt>

*identifier* 
</dt> <dd>

Specifies a valid MIDL identifier. Valid MIDL identifiers consist of up to 31 alphanumeric and/or underscore characters and must start with an alphabetic or underscore character.

</dd> <dt>

*const-expression* 
</dt> <dd>

Specifies an expression, identifier, or numeric or character constant appropriate for the specified type: constant integer literals or constant integer expressions for integer constants; Boolean expressions that can be computed at compilation for [**Boolean**](boolean.md) types; single-character constants for [**char**](char-idl.md) types; and string constants for **\[**[**string**](string.md)**\]** types. The [**voidÂ \***](void.md) type can be initialized only to **NULL**.

</dd> <dt>

*type-attribute-list* 
</dt> <dd>

Specifies one or more attributes that apply to the type.

</dd> <dt>

*pointer-type* 
</dt> <dd>

Specifies a valid MIDL pointer type.

</dd> <dt>

*declarator and declarator-list* 
</dt> <dd>

Specifies standard C declarators, such as identifiers, pointer declarators, and array declarators. For more information, see [Array and Sized-Pointer Attributes](array-and-sized-pointer-attributes.md), [**arrays**](arrays-1.md), and [Arrays and Pointers](/windows/desktop/Rpc/arrays-and-pointers). The *declarator-list* consists of one or more declarators, separated by commas. The parameter-name identifier in the function declarator is optional.

</dd> <dt>

*function-attr-list* 
</dt> <dd>

Specifies zero or more attributes that apply to the function. Valid function attributes are **\[**[**callback**](callback.md)**\]**, **\[**[**local**](local.md)**\]**; the pointer attribute **\[**[**ref**](ref.md)**\]**, **\[**[**unique**](unique.md)**\]**, or **\[**[**ptr**](ptr.md)**\]**; and the usage attributes **\[**[**string**](string.md)**\]**, **\[**[**ignore**](ignore.md)**\]**, and **\[**[**context\_handle**](context-handle.md)**\]**.

</dd> <dt>

*type-specifier* 
</dt> <dd>

Specifies a [base\_type](midl-base-types.md), [**struct**](struct.md), [**union**](union.md), [**enum**](enum.md) type, or type identifier. An optional storage specification can precede *type-specifier*.

</dd> <dt>

*ptr-decl* 
</dt> <dd>

Specifies zero or more pointer declarators. A pointer declarator is the same as the pointer declarator used in C. It is constructed from the **\*** designator, modifiers such as **far**, and the qualifier **const**.

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the remote procedure.

</dd> <dt>

*parameter-attribute-list* 
</dt> <dd>

Specifies zero or more directional attributes, field attributes, usage attributes, and pointer attributes appropriate for the specified parameter type. Separate multiple attributes with commas.

</dd> </dl>

## Remarks

MIDL allows you to declare constant integer, character, string, and Boolean types in the interface body of the IDL file. **Const** type declarations are reproduced in the generated header file as **\#define** directives.

DCE IDL compilers do not support constant expressions. Therefore, this feature is not available when you use the MIDL compiler [**/osf**](-osf.md) switch.

A previously defined constant can be used as the assigned value of a subsequent constant. The value of a constant integral expression is automatically converted to the respective integer type in accordance with C conversion rules.

The value of a character constant must be a single-quoted ASCII character. When the character constant is the single-quote character itself ('), the backslash character (\\) must precede the single-quote character, as in \\'.

The value of a character-string constant must be a double-quoted string. Within a string, the backslash (**\\**) character must precede a literal double-quote character ( **"** ), as in **\\"**. Within a string, the backslash character (**\\**) represents an escape character. String constants can consist of up to 255 characters.

The value **NULL** is the only valid value for constants of type [**voidÂ \***](void.md). Any attributes associated with the **const** declaration are ignored.

The MIDL compiler does not check for range errors in **const** initialization. For example, when you specify "const short x = 0xFFFFFFFF;" the MIDL compiler does not report an error and the initializer is reproduced in the generated header file.

## Examples

``` syntax
const void *  p1        = NULL; 
const char    my_char1  = 'a'; 
const char    my_char2  = my_char1; 
const wchar_t my_wchar3 = L'a'; 
const wchar_t * pszNote = L"Note"; 
const unsigned short int x = 123; 
 
typedef [string] const char *LPCSTR; 
 
HRESULT GetName([out] wchar_t * const pszName );
```

## See also

<dl> <dt>

[**arrays**](arrays-1.md)
</dt> <dt>

[MIDL Base Types](midl-base-types.md)
</dt> <dt>

[**Boolean**](boolean.md)
</dt> <dt>

[**byte**](byte.md)
</dt> <dt>

[**callback**](callback.md)
</dt> <dt>

[**char**](char-idl.md)
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

[**long**](long.md)
</dt> <dt>

[**/osf**](-osf.md)
</dt> <dt>

[**ptr**](ptr.md)
</dt> <dt>

[**ref**](ref.md)
</dt> <dt>

[**short**](short.md)
</dt> <dt>

[**signed**](signed.md)
</dt> <dt>

[**small**](small.md)
</dt> <dt>

[**string**](string.md)
</dt> <dt>

[**struct**](struct.md)
</dt> <dt>

[**union**](union.md)
</dt> <dt>

[**unique**](unique.md)
</dt> <dt>

[**unsigned**](unsigned.md)
</dt> <dt>

[**void**](void.md)
</dt> <dt>

[**wchar\_t**](wchar-t.md)
</dt> </dl>

 

 