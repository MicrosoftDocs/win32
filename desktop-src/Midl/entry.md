---
title: entry attribute
description: The \ entry\ attribute specifies an exported function or constant in a module by identifying the entry point in the DLL.
ms.assetid: 1d2d6429-d828-44ec-8b0a-cefb64c6e706
keywords:
- entry attribute MIDL
topic_type:
- apiref
api_name:
- entry
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# entry attribute

The **\[entry\]** attribute specifies an exported function or constant in a module by identifying the entry point in the DLL.

``` syntax
[
    uuid(uuid-number), 
    entry(entry-id)
  [, optional-attribute-list]
]
module modulename 
{
    elementlist
};
```

## Parameters

<dl> <dt>

*uuid-number* 
</dt> <dd>

Specifies a universally unique identification number for the [**module**](module.md).

</dd> <dt>

*entry-id* 
</dt> <dd>

Specifies the module entry point function name or integer identification number.

</dd> <dt>

*optional-attribute-list* 
</dt> <dd>

Specifies zero or more attributes for the MIDL compiler to apply to the [**module**](module.md).

</dd> <dt>

*modulename* 
</dt> <dd>

Specifies the name other software components use to denote the [**module**](module.md).

</dd> <dt>

*elementlist* 
</dt> <dd>

Specifies one or more module element definition statements.

</dd> </dl>

## Remarks

If the *entryid* variable of the **\[entry\]** attribute is a string, this is a named entry point. If *entryid* is a number, the entry point is defined by an ordinal. This attribute provides a way to obtain the address of a function in a module.

## Examples

``` syntax
[
    dllname("MyAppsFirst.dll")
] 
module MyModule
{
    [entry(20), bindable, requestedit, 
     propputref, defaultbind ] HRESULT Func1(
         [in]IUnknown * Param1, 
         [out] MyType * Param2);
    [entry("TwentyOne"), hidden, vararg] SAFEARRAY (int) Func2(
        [in, out] SAFEARRAY (variant) *varP) ;
    [entry(22)] Float Func3(
        [in] lpstr pName, [in] double dLevel,
        [out] short * sByte) ;
    } ;
```

## See also

<dl> <dt>

[**dllname**](dllname-str-.md)
</dt> <dt>

[**module**](module.md)
</dt> <dt>

[ODL File Syntax](/previous-versions/windows/desktop/automat/odl-file-syntax)
</dt> <dt>

[ODL File Example](/previous-versions/windows/desktop/automat/odl-file-example)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> </dl>

 

 