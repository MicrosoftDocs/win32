---
title: id attribute
description: The \ id\ attribute specifies a DISPID for a member function (either a property or a method, in an interface or dispinterface).
ms.assetid: 6f1be049-81b4-4aa2-a893-5dd79bb4d63c
keywords: ["id attribute MIDL"]
topic_type:
- apiref
api_name:
- id
api_type:
- NA
---

# id attribute

The **\[id\]** attribute specifies a DISPID for a member function (either a property or a method, in an interface or dispinterface).

``` syntax
[id(id-num) [,optional-attribute-list]] return-type function-name(optional-parameter-list)
```

## Parameters

<dl> <dt>

*id-num* 
</dt> <dd>

DISPID for the function.

</dd> <dt>

*optional-attribute-list* 
</dt> <dd>

Specifies a list of zero or more MIDL interface attributes.

</dd> <dt>

*return-type* 
</dt> <dd>

Specifies the return type of the function.

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the function in the IDL file.

</dd> <dt>

*optional-parameter-list* 
</dt> <dd>

Zero or more function parameters.

</dd> </dl>

## Remarks

Use the **\[id\]** attribute when you want to assign a standard DISPID (like DISPID\_VALUE, DISPID\_NEWENUM etc.) to a method or property, or when you implement your own **IDispatch::Invoke** instead of delegating to **DispInvoke**/**ITypeInfo::Invoke**.

If you do not use the **\[id\]** attribute on an interface, the MIDL compiler will assign a DISPID for you. However, when you specify a dispinterface by using properties and methods, you must specify a DISPID for every property and method.

The *id-num* is a 32-bit positive integral value. Negative IDs are reserved for use by Automation.

## Examples

``` syntax
interface IKnown : IUnknown
{
    properties:
        [id(90), propget, 
         helpstring("A meaningful comment."] long Func1(void);

    /* Other interface statements */
}
```

## See also

<dl> <dt>

[**interface**](interface.md)
</dt> <dt>

[**dispinterface**](dispinterface.md)
</dt> <dt>

[ODL File Syntax](df7aa86f-1453-4409-939e-788d469d611e)
</dt> <dt>

[ODL File Example](86d64a4f-08eb-422a-bb1d-dfa868094645)
</dt> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> </dl>

 

 




