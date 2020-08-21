---
title: usesgetlasterror attribute
description: The \ usesgetlasterror\ attribute signals the caller that it can call GetLastError to retrieve the error code.
ms.assetid: 8e9ab8b5-f446-4aab-bb40-b6f78799e18e
keywords:
- usesgetlasterror attribute MIDL
topic_type:
- apiref
api_name:
- usesgetlasterror
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# usesgetlasterror attribute

The **\[usesgetlasterror\]** attribute signals the caller that it can call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) to retrieve the error code.

``` syntax
[
    module-attributes
]
module module-name
{
    [entry(entry-id), usesgetlasterror [, other-attributes]] return-type function-name(param-list);
};
```

## Parameters

<dl> <dt>

*module-attributes* 
</dt> <dd>

Zero or more MIDL attributes that will be applied to the [**module**](module.md).

</dd> <dt>

*module-name* 
</dt> <dd>

The identifier name of the [**module**](module.md).

</dd> <dt>

*entry-id* 
</dt> <dd>

Specifies the module entry point–function name or integer-identification number.

</dd> <dt>

*other-attributes* 
</dt> <dd>

Zero or more MIDL attributes that will be applied to the remote procedure.

</dd> <dt>

*return-type* 
</dt> <dd>

The type of the data that the remote procedure will return upon completion.

</dd> <dt>

*function-name* 
</dt> <dd>

The name of the remote procedure as defined in the IDL file.

</dd> <dt>

*param-list* 
</dt> <dd>

Zero or more parameters to the remote procedure.

</dd> </dl>

## Remarks

The **\[usesgetlasterror\]** attribute can be set on a module entry point, if that entry point uses the Windows function [**SetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-setlasterror) to return error codes. The attribute tells the caller that, if there is an error when calling that function, the caller can then call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) to retrieve the error code.

## Examples

``` syntax
[
    dllname("MyOwn.dll")
] 
module MyModule
{
    [entry("One"), usesgetlasterror, bindable, requestedit,
     propputref, defaultbind] HRESULT Func1(
         [in]IUnknown * iParam1, 
         [out] long * Param2) ;
    [entry("TwentyOne"), usesgetlasterror, 
     hidden, vararg] SAFEARRAY (int) Func2(
         [in, out] SAFEARRAY (variant) *varP) ;

    // Other module definition statements.
};
```

## See also

<dl> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> </dl>

 

 