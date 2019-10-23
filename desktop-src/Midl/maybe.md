---
title: maybe attribute
description: The keyword \ maybe\ indicates that the remote procedure call does not need to execute every time it is called and the client does not expect a response. Note that the \ maybe\ protocol ensures neither delivery nor completion of the call.
ms.assetid: 163b9fd5-7dce-493e-95bc-63807f42a498
keywords:
- maybe attribute MIDL
topic_type:
- apiref
api_name:
- maybe
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# maybe attribute

The keyword **\[maybe\]** indicates that the remote procedure call does not need to execute every time it is called and the client does not expect a response. Note that the **\[maybe\]** protocol ensures neither delivery nor completion of the call.

``` syntax
[
    interface-attribute-list
] 
interface interface-name 
{
    [maybe [, attribute-list]] returntype function-name(params)
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

Specifies the name of the function to which the **\[maybe\]** attribute will be applied.

</dd> <dt>

*params* 
</dt> <dd>

Function parameter list.

</dd> </dl>

## Remarks

A call with the **\[maybe\]** attribute cannot contain output parameters and is implicitly an **\[**[**idempotent**](idempotent.md)**\]** call.

## See also

<dl> <dt>

[**broadcast**](broadcast.md)
</dt> <dt>

[**idempotent**](idempotent.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> </dl>

 

 




