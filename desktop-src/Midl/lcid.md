---
title: lcid attribute
description: The \ lcid\ attribute specifies a locale identifier and enables locale-specific MIDL compiler support.
ms.assetid: 40457a1a-251c-41cd-bfa6-9d506601ff5e
keywords:
- lcid attribute MIDL
topic_type:
- apiref
api_name:
- lcid
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# lcid attribute

The **\[lcid\]** attribute specifies a locale identifier and enables locale-specific MIDL compiler support.

``` syntax
[
    uuid(uuid-number), 
    lcid(localeID)
    [, optional-attribute-list]
] 
library library-name
{ 
    library-definition-statements
}

function-name([parameter-attribute-list, lcid] long  parameter-name,. . .);
```

## Parameters

<dl> <dt>

*uuid-number* 
</dt> <dd>

Specifies a universally unique identification number for the [**library**](library.md).

</dd> <dt>

*localeID* 
</dt> <dd>

Specifies the 32-bit locale identifier used in Windows National Language Support. Typically the locale identifier is given in hexadecimal.

</dd> <dt>

*optional-attribute-list* 
</dt> <dd>

Zero or more attributes to apply to the [**library**](library.md).

</dd> <dt>

*library-name* 
</dt> <dd>

The name by which software components refer to the [**library**](library.md).

</dd> <dt>

*library-definition-statements* 
</dt> <dd>

One or more MIDL statements which define the contents of the [**library**](library.md).

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the function in the IDL file.

</dd> <dt>

*parameter-attribute-list* 
</dt> <dd>

Zero or more MIDL attributes that will be applied to the function parameter.

</dd> <dt>

*parameter-name* 
</dt> <dd>

Specifies the name of the parameter in the IDL file.

</dd> </dl>

## Remarks

The **\[lcid\]** syntax has two different forms; the effect of the attribute depends on which syntax you use — either the [**library**](library.md) statement syntax or the parameter syntax.

When applied to the [**library**](library.md) statement, along with a localeID argument, as shown in the first example, the **\[lcid\]** attribute identifies the locale for a type library or for a function argument and lets you use international characters inside the library block.

Effective with version 3.01.75 of the MIDL compiler, the locale identifier supplied by this attribute not only decorates the resulting type library, but actually changes the behavior of the compiler. Within a [**library**](library.md) statement, from the point where the **\[lcid\]** attribute is used, MIDL will accept input localized according to the specified locale. In particular, full support for Asian languages such as Japanese, Chinese and Korean (full DBCS support) is available. Features supported by the localization are: comments, strings, helpstrings and identifiers.

Use the [**/lcid**](-lcid.md) compiler switch to have this localization support available to the entire input file, including file name and directory path, rather than just inside the library block.

When applied to a parameter, the **\[lcid\]** attribute lets you pass a locale identifier to a function, as shown in the second example. The following restrictions apply to **\[lcid\]** parameters:

-   A function can have at most one **\[lcid\]** parameter.
-   The data type of the parameter must be [**long**](long.md).
-   The direction of the parameter must be **\[**[**in**](in.md)**\]** only.
-   The **\[lcid\]** parameter must follow any other parameters, except a **\[**[**retval**](retval.md)**\]** parameter.
-   You cannot apply the **\[lcid\]** attribute to a [**dispinterface**](dispinterface.md) or [**coclass**](coclass.md) parameter.

## Examples

``` syntax
[  
    uuid(12345678-1234-1234-1234-123456789ABC),
    lcid(0x09),
    version(1.0)
] 
library MyLibrary
{
    /* Library definition statements */
};

interface IMyFace : IDispatch
{
    [propget] HRESULT MyFunc([in, lcid] long LocaleID,
                          [out, retval] BSTR * ReturnVal);
    // Other interface definition statements
}
```

## See also

<dl> <dt>

[**coclass**](coclass.md)
</dt> <dt>

[**dispinterface**](dispinterface.md)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[**/lcid**](-lcid.md)
</dt> <dt>

[**library**](library.md)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[**retval**](retval.md)
</dt> </dl>

 

 