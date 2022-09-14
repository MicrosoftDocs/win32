---
title: helpstringcontext attribute
description: The \ helpstringcontext\ attribute specifies a 32-bit Help context identifier in the Help file. You can apply the \ helpstringcontext\ attribute to library, interface, dispinterface, module, coclass, typedef statements, properties, parameters and methods.
ms.assetid: 0ac41bd9-ccc6-4b5c-b925-63bff9254eed
keywords:
- helpstringcontext attribute MIDL
topic_type:
- apiref
api_name:
- helpstringcontext
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# helpstringcontext attribute

The **\[helpstringcontext\]** attribute specifies a 32-bit Help context identifier in the Help file. You can apply the **\[helpstringcontext\]** attribute to [**library**](library.md), [**interface**](interface.md), [**dispinterface**](dispinterface.md), [**module**](module.md), [**coclass**](coclass.md), [**typedef**](typedef.md) statements, properties, parameters and methods.

``` syntax
[  helpstringcontext(contextid)[, optional-attribute-list]] idl-statement
```

## Parameters

<dl> <dt>

*contextid* 
</dt> <dd>

A unique integer that identifies the help text associated with the current MIDL statement.

</dd> <dt>

*optional-attribute-list* 
</dt> <dd>

Zero or more MIDL attributes.

</dd> <dt>

*idl-statement* 
</dt> <dd>

The MIDL statement to which the **\[helpstringcontext\]** attribute will be applied.

</dd> </dl>

## Remarks

Use the **GetDocumentation2** functions in the **ITypeLib2** and **ITypeInfo2** interfaces to retrieve the help string.

## Examples

``` syntax
[
    uuid(. . .),
    helpstringcontext(103),
    version(1.0)
]
library Lines
{
    [
        uuid(. . .), 
        helpstringcontext(102),
        oleautomation,
        dual
    ]
    interface ILine : IDispatch
    {
        [propget, helpstringcontext(100)] HRESULT Color([out, retval] long* ReturnVal); 
        [propput, helpstringcontext(101)] HRESULT Color([in] long rgb);
    }
};
```

 

 




