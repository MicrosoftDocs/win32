---
title: iid_is attribute
description: The \ iid\_is\ pointer attribute specifies the IID of the COM interface pointed to by an interface pointer.
ms.assetid: 7fb5eb87-15d8-4717-b79a-e8a81f2f7293
keywords:
- iid_is attribute MIDL
topic_type:
- apiref
api_name:
- iid_is
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# iid\_is attribute

The **\[iid\_is\]** pointer attribute specifies the IID of the COM interface pointed to by an interface pointer.

``` syntax
[ iid_is(limited-expression) ]
```

## Parameters

<dl> <dt>

*limited-expression* 
</dt> <dd>

Specifies a C-language expression. The MIDL compiler supports conditional expressions, logical expressions, relational expressions, and arithmetic expressions. MIDL does not allow function invocations in expressions and does not allow increment and decrement operators.

</dd> </dl>

## Remarks

You can use **\[iid\_is\]** in attribute lists for function parameters and for structure or union members. The stubs use the IID to determine how to marshal the interface pointer. This is useful for an interface pointer that is typed as a base class parameter.

Files that use the **\[iid\_is\]** attribute must be compiled with the MIDL compiler in default mode, that is not using the [**/osf**](-osf.md) switch.

## Examples

``` syntax
HRESULT    CreateInstance( 
    [in] REFIID riid, 
    [out, iid_is(riid)] IUnknown ** ppvObject);
```

## See also

<dl> <dt>

[**object**](object.md)
</dt> <dt>

[**uuid**](uuid.md)
</dt> </dl>

 

 




