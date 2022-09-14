---
title: vararg attribute
description: The \ vararg\ attribute specifies that the function takes a variable number of parameters. To accomplish this, the last parameter must be a safe array of VARIANT type that contains all the remaining parameters.
ms.assetid: df0995d3-5266-4a13-90aa-d78bfa753e0e
keywords:
- vararg attribute MIDL
topic_type:
- apiref
api_name:
- vararg
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# vararg attribute

The **\[vararg\]** attribute specifies that the function takes a variable number of parameters. To accomplish this, the last parameter must be a safe array of **VARIANT** type that contains all the remaining parameters.

``` syntax
[vararg [, optional-attributes]] return-type function-name(
  [optional-param-attributes] param-list, 
  SAFEARRAY(VARIANT) last-param-name);
```

## Parameters

<dl> <dt>

*optional-attributes* 
</dt> <dd>

Specifies zero or more attributes to be applied to the function. Separate multiple attributes with commas.

</dd> <dt>

*return-type* 
</dt> <dd>

The type of the data returned by the remote procedure upon completion.

</dd> <dt>

*function-name* 
</dt> <dd>

The name of the remote procedure.

</dd> <dt>

*optional-param-attributes* 
</dt> <dd>

Specifies zero or more attributes to be applied to the function parameter immediately following the attribute listing.

</dd> <dt>

*param-list* 
</dt> <dd>

Specifies all the parameters, save the final, varying, parameter.

</dd> <dt>

*last-param-name* 
</dt> <dd>

The name of the varying parameter.

</dd> </dl>

## Remarks

You cannot apply the **\[**[**optional**](optional.md)**\]** or **\[**[**defaultvalue**](defaultvalue.md)**\]** attributes to any parameters in a function that has the **\[vararg\]** attribute.

## Examples

``` syntax
[vararg] VARIANT_BOOL Button([in]SAFEARRAY(VARIANT) psa);
```

## See also

<dl> <dt>

[**defaultvalue**](defaultvalue.md)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[**optional**](optional.md)
</dt> </dl>

 

 