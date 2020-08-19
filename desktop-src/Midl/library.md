---
title: library attribute
description: The library statement contains all the information that the MIDL compiler uses to generate a type library.
ms.assetid: d73acb17-abe4-4c31-a264-a131d1f9fa51
keywords:
- library attribute MIDL
topic_type:
- apiref
api_name:
- library
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# library attribute

The **library** statement contains all the information that the MIDL compiler uses to generate a type library.

``` syntax
[
    uuid(uuid-number), 
    [, optional-attribute-list]
] 
library library-name
{ 
    library-definition-statements
}
```

## Parameters

<dl> <dt>

*uuid-number* 
</dt> <dd>

Specifies a universally unique identification number for the library.

</dd> <dt>

*optional-attribute-list* 
</dt> <dd>

Specifies additional attributes that apply to the entire **library** statement. Allowable attributes include **\[**[**control**](control.md)**\]**, **\[**[**helpcontext**](helpcontext.md)**\]**, **\[**[**helpfile**](helpfile.md)**\]**, **\[**[**helpstring**](helpstring.md)**\]**, **\[**[**hidden**](hidden.md)**\]**, **\[**[**lcid**](lcid.md)**\]**, **\[**[**restricted**](restricted.md)**\]**, and **\[**[**version**](version.md)**\]**.

</dd> <dt>

*library-name* 
</dt> <dd>

The name by which software components refer to the **library**.

</dd> <dt>

*library-definition-statements* 
</dt> <dd>

One or more MIDL statements which define the contents of the **library**.

</dd> </dl>

## Remarks

Statements inside the library block can use elements that are declared inside or outside of the library block. Library statements can use those elements as base types, inheriting from those elements, or by simply referencing them on a line, as follows:

``` syntax
interface MyFace 
{
    // Interface definition statements
};

[
    // library attributes
] 
library
{
    interface MyFace;

    // Other library definition statements.
};
```

The MIDL compiler will create a type library that includes definitions for every element inside the library block, plus definitions for any elements defined outside and referenced from within the library block.

For information on generating both a type library and proxy stubs and headers from a single IDL file see [Generating a Proxy DLL and a Type Library From a Single IDL File](generating-a-proxy-dll-and-a-type-library-from-a-single-idl-file-2.md).

## Examples

``` syntax
[
    uuid(12345678-1234-1234-1234-123456789ABC), 
    helpstring("Hello 2.0 Type Library"), 
    lcid(0x0409), 
    version(2.0)
] 
library Hello 
{
    /* Library definition statements */
};
```

## See also

<dl> <dt>

[Contents of a Type Library](/previous-versions/windows/desktop/automat/contents-of-a-type-library)
</dt> <dt>

[**control**](control.md)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[**helpcontext**](helpcontext.md)
</dt> <dt>

[**helpfile**](helpfile.md)
</dt> <dt>

[**helpstring**](helpstring.md)
</dt> <dt>

[**hidden**](hidden.md)
</dt> <dt>

[**lcid**](lcid.md)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[**restricted**](restricted.md)
</dt> <dt>

[**version**](version.md)
</dt> </dl>

 

 