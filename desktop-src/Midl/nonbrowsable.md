---
title: nonbrowsable attribute
description: Use the \ nonbrowsable\ attribute to tag an interface or dispinterface member that should not be displayed in a properties browser.
ms.assetid: 94e868cc-8d9c-4b8a-ac18-1ea513a103da
keywords:
- nonbrowsable attribute MIDL
topic_type:
- apiref
api_name:
- nonbrowsable
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# nonbrowsable attribute

Use the **\[nonbrowsable\]** attribute to tag an interface or dispinterface member that should not be displayed in a properties browser.

``` syntax
[property-attribute-list, nonbrowsable]return-type property-name(prop-param-list)
```

## Parameters

<dl> <dt>

*property-attribute-list* 
</dt> <dd>

Other attributes that apply to the property.

</dd> <dt>

*return-type* 
</dt> <dd>

The type of the data returned by the method.

</dd> <dt>

*property-name* 
</dt> <dd>

The name of the property or method.

</dd> <dt>

*prop-param-list* 
</dt> <dd>

Zero or more parameters to be passed to the method.

</dd> </dl>

## Remarks

Certain properties should not be displayed in a properties browser. This may be because retrieving the value would take a very long time. The example prevents the user from attempting to retrieve the *Count* property, which returns the number of rows in the dynaset.This number may represent the results of a very large query.

Other properties may have unexpected effects on the browser. For example, consider a control with the property "IsSelected" to tell whether the control is selected. If "IsSelected" is set to false, a selection-based properties browser will browse a different object.

Note that a property tagged as **\[nonbrowsable\]** will still appear in an object browser, which does not show property values.

### Typeflag Representation

The presence of FUNCFLAG\_FNONBROWSABLE or VARFLAG\_FNONBROWSABLE.

## Examples

``` syntax
[
    dual,
    uuid(12345678-1234-1234-1234-123456789ABC),
    restricted
]
interface IDynaset:IDispatch
{
    [propget, nonbrowsable]HRESULT Count([out, retval] long *Value);
}
```

## See also

<dl> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> </dl>

 

 