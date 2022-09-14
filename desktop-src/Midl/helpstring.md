---
title: helpstring attribute
description: The \ helpstring\ attribute specifies a character string that is used to describe the element to which it applies.
ms.assetid: f05d3fdd-d975-4f0e-8181-07e16288ff48
keywords:
- helpstring attribute MIDL
topic_type:
- apiref
api_name:
- helpstring
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# helpstring attribute

The **\[helpstring\]** attribute specifies a character string that is used to describe the element to which it applies. You can apply the **\[helpstring\]** attribute to library, importlib, interface, dispinterface, module, or coclass statements, typedefs, properties, and methods.

``` syntax
[
    helpstring(help-text-string)
    [, optional-attribute-list]
] 
element element-name
{
    definition
}

[idl-statement, helpstring(help-text-string)]
```

## Parameters

<dl> <dt>

*help-text-string* 
</dt> <dd>

A zero-terminated string of characters containing help text.

</dd> <dt>

*optional-attribute-list* 
</dt> <dd>

Zero or more MIDL attribute statements.

</dd> <dt>

*element* 
</dt> <dd>

One of the following directives: [**library**](library.md), **\[**[**importlib**](importlib.md)**\]**, [**interface**](interface.md), [**dispinterface**](dispinterface.md), [**module**](module.md), [**typedef**](typedef.md), **method**, **property**, or [**coclass**](coclass.md).

</dd> <dt>

*element-name* 
</dt> <dd>

The name that other software components can use to delineate the current element

</dd> <dt>

*definition* 
</dt> <dd>

Specifies statements that make up the element definition.

</dd> <dt>

*idl-statement* 
</dt> <dd>

A MIDL interface definition statement such as [**propget**](propget.md) or [**propput**](propput.md).

</dd> </dl>

## Remarks

Use the [**GetDocumentation**](/windows/win32/api/oaidl/nf-oaidl-itypelib-getdocumentation) functions in the [**ITypeLib**](/windows/win32/api/oaidl/nn-oaidl-itypelib) and [**ITypeInfo**](/windows/win32/api/oaidl/nn-oaidl-itypeinfo) interfaces to retrieve the help string.

## Examples

``` syntax
[
    uuid(1e196b20-1f3c-1069-996b-00dd010fe676),
    helpstring("Lines 1.0 Type Library"),
    version(1.0)
]
library Lines
{
     [
         uuid(1e123456-1f3c-1069-996b-00dd010fe676), 
         helpstring("Line object."),
         oleautomation,
         dual
     ]
     interface ILine : IDispatch                         
     {
         [propget, helpstring("Returns and sets RGB color.")]
         HRESULT Color([out, retval] long* ReturnVal); 
         [propput, helpstring("Returns and sets RGB color.")]
         HRESULT Color([in] long rgb);
     }
};
```

## See also

<dl> <dt>

[**library**](library.md)
</dt> <dt>

[**importlib**](importlib.md)
</dt> <dt>

[**interface**](interface.md)
</dt> <dt>

[**dispinterface**](dispinterface.md)
</dt> <dt>

[**module**](module.md)
</dt> <dt>

[**coclass**](coclass.md)
</dt> <dt>

[**typedef**](typedef.md)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> </dl>

 

 