---
title: helpcontext attribute
description: The \ helpcontext\ attribute specifies a context identifier that lets the user view information about this element in the Help file.
ms.assetid: 44a60c75-be69-4cd9-afb0-5eb988830e6c
keywords:
- helpcontext attribute MIDL
topic_type:
- apiref
api_name:
- helpcontext
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# helpcontext attribute

The \[**helpcontext**\] attribute specifies a context identifier that lets the user view information about this element in the Help file.

``` syntax
[
    uuid(uuid-number), 
    helpcontext(helpcontext-value)
    [, attribute-list]
] 
element element-name
{
    definitions
}
```

## Parameters

<dl> <dt>

*uuid-number* 
</dt> <dd>

Specifies a universally unique identification number for the [**library**](library.md), \[[**importlib**](importlib.md)\], [**interface**](interface.md), [**dispinterface**](dispinterface.md), [**module**](module.md), [**typedef**](typedef.md), **methods**, **\[property\]**, or [**coclass**](coclass.md).

</dd> <dt>

*helpcontext-value* 
</dt> <dd>

A unique integer that identifies the help text associated with the current MIDL element.

</dd> <dt>

*attribute-list* 
</dt> <dd>

Specifies a list of one or more attributes that apply to the MIDL element as a whole.

</dd> <dt>

*element* 
</dt> <dd>

One of the following directives: [**library**](library.md), \[[**importlib**](importlib.md)\], [**interface**](interface.md), [**dispinterface**](dispinterface.md), [**module**](module.md), [**typedef**](typedef.md), **method**, **property**, or [**coclass**](coclass.md).

</dd> <dt>

*element-name* 
</dt> <dd>

The name that other software components can use to delineate the current element.

</dd> <dt>

*definitions* 
</dt> <dd>

Specifies statements that make up the element definition.

</dd> </dl>

## Remarks

The \[**helpcontext**\] attribute can be applied to the following elements: [**library**](library.md), \[[**importlib**](importlib.md)\], [**interface**](interface.md), [**dispinterface**](dispinterface.md), [**module**](module.md), [**typedef**](typedef.md), **method**, **property**, or [**coclass**](coclass.md).

The *helpcontext-value* is a 32-bit context identifier within the Help file that can be retrieved with the [**GetDocumentation**](https://msdn.microsoft.com/en-us/library/ms221396(v=VS.71).aspx) functions in the [**ITypeLib**](https://msdn.microsoft.com/en-us/library/ms221549(v=VS.71).aspx) and [**ITypeInfo**](https://msdn.microsoft.com/en-us/library/ms221696(v=VS.71).aspx) interfaces.

## Examples

``` syntax
[
    uuid(1e196b20-1f3c-1069-996b-00dd010fe676),
    helpcontext(7035943),
    helpstring("Hello Class"),
    appobject
] 
coclass Hello
{
    [default, helpcontext(3914972)] interface IHello : IUnknown;
    interface IDispatch;
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

[**importlib**](importlib.md)
</dt> <dt>

[**interface**](interface.md)
</dt> <dt>

[**library**](library.md)
</dt> <dt>

[**module**](module.md)
</dt> <dt>

[ODL File Syntax](https://msdn.microsoft.com/en-us/library/ms221683(v=VS.71).aspx)
</dt> <dt>

[ODL File Example](https://msdn.microsoft.com/en-us/library/ms221308(v=VS.71).aspx)
</dt> <dt>

[**typedef**](typedef.md)
</dt> </dl>

 

 




