---
title: idempotent attribute
description: The \ idempotent\ attribute specifies that an operation does not modify state information and returns the same results each time it is performed. Performing the routine more than once has the same effect as performing it once.
ms.assetid: 876a40b5-8165-4b5c-bd62-9c43a9eb4b2b
keywords:
- idempotent attribute MIDL
topic_type:
- apiref
api_name:
- idempotent
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# idempotent attribute

The **\[idempotent\]** attribute specifies that an operation does not modify state information and returns the same results each time it is performed. Performing the routine more than once has the same effect as performing it once.

``` syntax
[
    interface-attribute-list
] 
interface interface-name 
{
    [idempotent [, attribute-list]] returntype function-name(params)
}
```

## Parameters

<dl> <dt>

*interface-attribute-list* 
</dt> <dd>

Specifies a list of zero or more IDL attributes that apply to the interface as a whole. When two or more interface attributes are present, they must be separated by commas.

</dd> <dt>

*interface-name* 
</dt> <dd>

Specifies the name of the interface.

</dd> <dt>

*attribute-list* 
</dt> <dd>

Specifies additional attributes to be applied to the function. Separate multiple attributes with commas.

</dd> <dt>

*returntype* 
</dt> <dd>

Specifies the return type of the function.

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the function to which the **\[idempotent\]** attribute will be applied.

</dd> <dt>

*params* 
</dt> <dd>

Function parameter list.

</dd> </dl>

## Remarks

RPC supports two types of remote call semantics: calls to operations with the **\[idempotent\]** attribute and calls to operations (*idempotent* operations) without the **\[idempotent\]** attribute (*non-idempotent* operations). An idempotent operation can be carried out more than once with no ill effect. Conversely, a non-idempotent operation cannot be executed more than once because it will either return different results each time or because it modifies some state.

To ensure that a procedure is automatically re-executed if the call does not complete, use the **\[idempotent\]** attribute. If the **\[idempotent\]**, **\[**[**broadcast**](broadcast.md)**\]**, or **\[**[**maybe**](maybe.md)**\]** attributes are not present, the procedure will use non-idempotent semantics by default. In this case, the operation is executed only once.

## See also

<dl> <dt>

[**broadcast**](broadcast.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**maybe**](maybe.md)
</dt> </dl>

 

 




