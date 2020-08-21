---
title: hidden attribute
description: The \ hidden\ attribute indicates that the item exists but should not be displayed in a user-oriented browser.
ms.assetid: bf1f9270-fb93-4421-804e-d56e2c863bbd
keywords:
- hidden attribute MIDL
topic_type:
- apiref
api_name:
- hidden
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# hidden attribute

The **\[hidden\]** attribute indicates that the item exists but should not be displayed in a user-oriented browser.

``` syntax
[
    other-attributes, 
    hidden
] 
element element-name
{
    definitions
}

[other-attributes, hidden] function-type function-name(optional-parameter-list);
```

## Parameters

<dl> <dt>

*other-attributes* 
</dt> <dd>

Zero or more optional MIDL attributes.

</dd> <dt>

*element* 
</dt> <dd>

One of the following directives: [**coclass**](coclass.md), [**dispinterface**](dispinterface.md), [**interface**](interface.md), or [**library**](library.md).

</dd> <dt>

*element-name* 
</dt> <dd>

The name that other software components can use to delineate the current element.

</dd> <dt>

*definitions* 
</dt> <dd>

Specifies statements that make up the element definition.

</dd> <dt>

*function-type* 
</dt> <dd>

Return type of the function.

</dd> <dt>

*function-name* 
</dt> <dd>

Name used for invoking the function.

</dd> <dt>

*optional-parameter-list* 
</dt> <dd>

Zero or more function parameters.

</dd> </dl>

## Remarks

The **\[hidden\]** attribute allows you to remove members from your interface (by shielding them from further use) while maintaining compatibility with existing code. You can use the **\[hidden\]** attribute on properties, methods, and the [**coclass**](coclass.md), [**dispinterface**](dispinterface.md), [**interface**](interface.md), and [**library**](library.md) statements.

When specified for a library, the **\[hidden\]** attribute prevents the entire library from being displayed. This usage is intended for use with controls. Hosts need to create a new type library that wraps the control with extended properties.

### Flags

VARFLAG\_FHIDDEN, FUNCFLAG\_FHIDDEN, TYPEFLAG\_FHIDDEN

## Examples

``` syntax
[hidden, vararg] SAFEARRAY (int) SecretFunc(
    [in, out] SAFEARRAY (variant) *varP) ;

[
    uuid(1e196b20-1f3c-1069-996b-00dd010fe676), 
    hidden, 
    version (3.0)
] 
library HiddenLib 
{
    /* Library definition statements here. */
};
```

## See also

<dl> <dt>

[TYPEFLAGS](/windows/win32/api/oaidl/ne-oaidl-typeflags)
</dt> <dt>

[**dispinterface**](dispinterface.md)
</dt> <dt>

[**coclass**](coclass.md)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[**interface**](interface.md)
</dt> <dt>

[**library**](library.md)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> </dl>

 

 