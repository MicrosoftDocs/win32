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
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# nonextensible attribute

The **\[nonextensible\]** attribute specifies that the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) implementation includes only the properties and methods listed in the interface description and cannot be extended with additional members at run time. (By default, Automation assumes that interfaces may add members at run time; that is, it assumes they are extensible.)

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

[Contents of a Type Library](https://msdn.microsoft.com/windows/desktop/76b062d4-1a08-47f5-b4d4-064237cb1372)
</dt> <dt>

[**dispinterface**](dispinterface.md)
</dt> <dt>

[**dual**](dual.md)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[**interface**](interface.md)
</dt> <dt>

[ODL File Syntax](https://msdn.microsoft.com/windows/desktop/df7aa86f-1453-4409-939e-788d469d611e)
</dt> <dt>

[**oleautomation**](oleautomation.md)
</dt> <dt>

[**TYPEFLAGS**](https://msdn.microsoft.com/windows/desktop/bf34cc90-f772-4562-9d18-7cf35aeed41e)
</dt> </dl>

 

 




