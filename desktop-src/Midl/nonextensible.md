---
title: nonextensible attribute
description: The \ nonextensible\ attribute specifies that the IDispatch implementation includes only the properties and methods listed in the interface description and cannot be extended with additional members at run time.
ms.assetid: 5fcffa65-4f0c-4180-a6c2-f68d63ff99ae
keywords:
- nonextensible attribute MIDL
topic_type:
- apiref
api_name:
- nonextensible
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# nonextensible attribute

The **\[nonextensible\]** attribute specifies that the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) implementation includes only the properties and methods listed in the interface description and cannot be extended with additional members at run time. (By default, Automation assumes that interfaces may add members at run time; that is, it assumes they are extensible.)

``` syntax
[
    uuid(uuid-number), 
    nonextensible 
    [, optional-attribute-list]
] 
interface | dispinterface interface-name 
{
    interface-definition
}
```

## Parameters

<dl> <dt>

*uuid-number* 
</dt> <dd>

Specifies a universally unique identification number for the [**interface**](interface.md).

</dd> <dt>

*optional-attribute-list* 
</dt> <dd>

Specifies a list of zero or more MIDL interface attributes.

</dd> <dt>

*interface-name* 
</dt> <dd>

Specifies the name of the [**interface**](interface.md) or [**dispinterface**](dispinterface.md).

</dd> <dt>

*interface-definition* 
</dt> <dd>

Specifies IDL statements that form the definition of the [**interface**](interface.md) or [**dispinterface**](dispinterface.md).

</dd> </dl>

## Remarks

You can apply the **\[nonextensible\]** attribute to either an interface or a dispinterface. However, an interface must also have the **\[**[**dual**](dual.md)**\]** and **\[**[**oleautomation**](oleautomation.md)**\]** attributes.

### Flags

TYPEFLAG\_FNONEXTENSIBLE

## Examples

``` syntax
library Hello
{
    [
        uuid(12345678-1234-1234-1234-123456789ABC), 
        helpstring("A helpful description."),
        oleautomation, 
        dual, 
        nonextensible
    ] 
    interface IHello : IDispatch
    {
        // Interface definition statements.
    }
}
```

## See also

<dl> <dt>

[Contents of a Type Library](/previous-versions/windows/desktop/automat/contents-of-a-type-library)
</dt> <dt>

[**dispinterface**](dispinterface.md)
</dt> <dt>

[**dual**](dual.md)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[**interface**](interface.md)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[**oleautomation**](oleautomation.md)
</dt> <dt>

[**TYPEFLAGS**](/windows/win32/api/oaidl/ne-oaidl-typeflags)
</dt> </dl>

 

 