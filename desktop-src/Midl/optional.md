---
title: optional attribute
description: The \ optional\ attribute specifies an optional parameter for a member function.
ms.assetid: 683e5c9e-5b25-4beb-99ce-cfae4fee4ea6
keywords:
- optional attribute MIDL
topic_type:
- apiref
api_name:
- optional
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# optional attribute

The **\[optional\]** attribute specifies an optional parameter for a member function.

``` syntax
return-type function-name([optional [, other-attributes]] parameter-type parameter-name)
```

## Parameters

<dl> <dt>

*return-type* 
</dt> <dd>

Specifies the return type of the function.

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the function as defined in the IDL file.

</dd> <dt>

*other-attributes* 
</dt> <dd>

Zero or more optional MIDL attributes.

</dd> <dt>

*parameter-type* 
</dt> <dd>

The data type of the optional parameter.

</dd> <dt>

*parameter-name* 
</dt> <dd>

Specifies the name of the optional parameter.

</dd> </dl>

## Remarks

The **\[optional\]** attribute is valid only if the parameter is of type **VARIANT** or **VARIANT**Â \*.

The MIDL compiler accepts the following parameter ordering (from left-to-right):

1.  Required parameters (parameters that do not have the **\[**[**defaultvalue**](defaultvalue.md)**\]** or **\[optional\]** attributes),
2.  Optional parameters with or without the **\[**[**defaultvalue**](defaultvalue.md)**\]** attribute,
3.  Parameters with the **\[optional\]** attribute and without the **\[**[**defaultvalue**](defaultvalue.md)**\]** attribute,
4.  **\[**[**lcid**](lcid.md)**\]** parameter, if any,
5.  **\[**[**retval**](retval.md)**\]** parameter

You cannot apply the **\[optional\]** attribute to a parameter that also has the **\[**[**lcid**](lcid.md)**\]** or **\[**[**retval**](retval.md)**\]** attributes.

## Examples

``` syntax
HRESULT MyFunc([in, optional] VARIANT Param1, 
               [out, optional] VARIANT Param2)
```

## See also

<dl> <dt>

[**defaultvalue**](defaultvalue.md)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[**lcid**](lcid.md)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[**retval**](retval.md)
</dt> </dl>

 

 