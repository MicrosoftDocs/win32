---
title: defaultvalue attribute
description: The \ defaultvalue\ attribute allows you to specify a default value for a typed optional parameter.
ms.assetid: a974a0f7-7b08-4f17-bb28-0e23e6aa97db
keywords:
- defaultvalue attribute MIDL
topic_type:
- apiref
api_name:
- defaultvalue
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# defaultvalue attribute

The **\[defaultvalue\]** attribute allows you to specify a default value for a typed optional parameter.

``` syntax
interface interface-name
{
  return-type function-name(
        mandatory-param-list, 
        [[attribute-list,] defaultvalue(value)] param-type param-name
        [ , optional-param-list]);
}
```

## Parameters

<dl> <dt>

*interface-name* 
</dt> <dd>

Specifies the name of the interface.

</dd> <dt>

*return-type* 
</dt> <dd>

Specifies the return type of the function.

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the function to which the **\[defaultvalue\]** attribute will be applied.

</dd> <dt>

*mandatory-param-list* 
</dt> <dd>

Specifies on or more required parameters.

</dd> <dt>

*attribute-list* 
</dt> <dd>

Specifies a list of one or more attributes, separated by commas, that apply to the parameter.

</dd> <dt>

*param-type* 
</dt> <dd>

Indicates the type of the optional parameter.

</dd> <dt>

*param-name* 
</dt> <dd>

Specifies the name of the optional parameter.

</dd> <dt>

*optional-param-list* 
</dt> <dd>

Specifies zero or more additional parameters, each of which must have a default value.

</dd> </dl>

## Remarks

The default value you specify for the parameter can be any constant, or an expression that resolves to a constant, that can be represented by a **VARIANT**. Specifically, you cannot apply the **\[defaultvalue\]** attribute to a parameter that is a structure, an array, or a **SAFEARRAY** type.

The MIDL compiler accepts the following parameter ordering (from left-to-right):

1.  Required parameters (parameters that do not have the **\[defaultvalue\]** or **\[**[**optional**](optional.md)**\]** attributes),
2.  optional parameters with or without the **\[defaultvalue\]** attribute,
3.  parameters with the **\[optional\]** attribute and without the **\[defaultvalue\]** attribute,
4.  **\[**[**lcid**](lcid.md)**\]** parameter, if any,
5.  **\[**[**retval**](retval.md)**\]** parameter

## Examples

``` syntax
interface IFace : IUnknown
{
    HRESULT Ex1([defaultvalue(44)] LONG i);
    HRESULT Ex2([defaultvalue(44)] SHORT i);
...
};

interface QueryDef : IUnknown
{
    HRESULT OpenRecordset( [in, defaultvalue(DBOPENTABLE)]
    LONG Type,
    [out,retval] Recordset **pprst);
}
//  Type is now known to be a LONG type (good for browser in VBA and
//  good for a C/C++ programmer) and has a default value of
//  DBOPENTABLE
```

## See also

<dl> <dt>

[**dispinterface**](dispinterface.md)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[**interface**](interface.md)
</dt> <dt>

[**lcid**](lcid.md)
</dt> <dt>

[**optional**](optional.md)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[**retval**](retval.md)
</dt> <dt>

[TYPEFLAGS](/windows/win32/api/oaidl/ne-oaidl-typeflags)
</dt> </dl>

 

 