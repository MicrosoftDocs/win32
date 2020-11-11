---
title: defaultcollelem attribute
description: The \ defaultcollelem\ attribute flags a property as an accessor function for an element of the default collection.
ms.assetid: e409f845-3f26-4551-abda-86c4776160aa
keywords:
- defaultcollelem attribute MIDL
topic_type:
- apiref
api_name:
- defaultcollelem
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# defaultcollelem attribute

The **\[defaultcollelem\]** attribute flags a property as an accessor function for an element of the default collection.

``` syntax
[property-attribute-list, defaultcollelem] return-type property-name(prop-param-list)
```

## Parameters

<dl> <dt>

*property-attribute-list* 
</dt> <dd>

Other attributes that apply to the property.

</dd> <dt>

*return-type* 
</dt> <dd>

Specifies the return type of the function.

</dd> <dt>

*property-name* 
</dt> <dd>

The name of the property.

</dd> <dt>

*prop-param-list* 
</dt> <dd>

A list of zero or more parameters associated with the property.

</dd> </dl>

## Remarks

The **\[defaultcollelem\]** attribute is used for Visual BasicÂ® code optimization. If a member of an interface or dispinterface is flagged as an accessor function, then the call will go directly to that member.

Use of **\[defaultcollelem\]** must be consistent for a property. For example, if you use the attribute on a *Get* property, it must also be present on a *Let* property.

### Typeflags Representation

The presence of FUNCFLAG\_FDEFAULTCOLLELEM or VARFLAG\_FDEFAULTCOLLELEM.

## Examples

``` syntax
//A form has a button on it named Button1. 
//To enable use of the property syntax and efficient use of the !
//syntax, the form describes itself in type info this way.
[
    dual,
    uuid(12345678-1234-1234-1234-123456789ABC),
    helpstring("This is IForm"),
    restricted
]
interface IForm1: IForm
{
    [propget, defaultcollelem] HRESULT Button1(
        [out, retval] Button *Value);
}

//User code may access the button using property syntax or ! syntax.

Sub Test()
Dim f as Form1
Dim b1 As Button
Dim b2 As Button

Set f = Form1

Set b1 = f.Button1        ' Property syntax
Set b = f!Button1        ' ! syntax
End Sub
```

## See also

<dl> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> </dl>

 

 