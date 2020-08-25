---
title: retval attribute
description: The \ retval\ attribute designates the parameter that receives the return value of the member.
ms.assetid: 3a5f1469-7828-4c38-b58f-195a47b2a66f
keywords:
- retval attribute MIDL
topic_type:
- apiref
api_name:
- retval
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# retval attribute

The **\[retval\]** attribute designates the parameter that receives the return value of the member.

``` syntax
return-type function-name(
    [out, retval [, optional-attributes]] data-type * param-name,
    ...);
```

## Parameters

<dl> <dt>

*return-type* 
</dt> <dd>

The data type of the return value of the remote procedure.

</dd> <dt>

*function-name* 
</dt> <dd>

The name used to invoke the remote procedure.

</dd> <dt>

*optional-attributes* 
</dt> <dd>

Zero or more MIDL attributes.

</dd> <dt>

*data-type* 
</dt> <dd>

The type of the data passed through the parameter.

</dd> <dt>

*param-name* 
</dt> <dd>

The identifier name of the parameter.

</dd> </dl>

## Remarks

You can use the **\[retval\]** attribute on parameters of interface members that describe methods or get properties. (The attribute is required on the last parameter of a method that has the **\[**[**propget**](propget.md)**\]** attribute.) The parameter must have the **\[**[**out**](out-idl.md)**\]** attribute and must be a pointer type.

You cannot apply the **\[**[**optional**](optional.md)**\]** attribute to a **\[retval\]** parameter.

The MIDL compiler accepts the following parameter ordering (from left-to-right):

1.  Required parameters (parameters that do not have the **\[**[**defaultvalue**](defaultvalue.md)**\]** or **\[**[**optional**](optional.md)**\]** attributes).
2.  Optional parameters with or without the **\[**[**defaultvalue**](defaultvalue.md)**\]** attribute.
3.  Parameters with the **\[**[**optional**](optional.md)**\]** attribute and without the **\[**[**defaultvalue**](defaultvalue.md)**\]** attribute.
4.  **\[**[**lcid**](lcid.md)**\]** parameter, if any.
5.  **\[retval\]** parameter.

Parameters with the **\[retval\]** attribute are not displayed in user-oriented browsers.

### Flags

IDLFLAG\_FRETVAL

## Examples

``` syntax
HRESULT MyMethod([out, retval] InMyFace** ReturnVal);
HRESULT MyOtherMethod([out, retval] VARIANT_BOOL* ReturnVal);
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

[**optional**](optional.md)
</dt> <dt>

[**out**](out-idl.md)
</dt> <dt>

[**propget**](propget.md)
</dt> <dt>

[**TYPEFLAGS**](/windows/win32/api/oaidl/ne-oaidl-typeflags)
</dt> </dl>

 

 