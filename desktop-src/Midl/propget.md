---
title: propget attribute
description: The \ propget\ attribute specifies a property accessor function. The property must have the same name as the function.
ms.assetid: 0b76ece3-e19b-4c80-883c-ff414bc2e435
keywords:
- propget attribute MIDL
topic_type:
- apiref
api_name:
- propget
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# propget attribute

The **\[propget\]** attribute specifies a property accessor function. The property must have the same name as the function.

``` syntax
[propget [,optional-property-attributes]] return-type function-name( parameters);
```

## Parameters

<dl> <dt>

*optional-property-attributes* 
</dt> <dd>

Zero or more property attributes.

</dd> <dt>

*return-type* 
</dt> <dd>

The type of the data returned by the remote procedure.

</dd> <dt>

*function-name* 
</dt> <dd>

The name of the remote procedure.

</dd> <dt>

*parameters* 
</dt> <dd>

Zero or more parameters to the remote procedure.

</dd> </dl>

## Remarks

A function that has the propget attribute should also have, as its last parameter, a pointer type with the **\[**[**out**](out-idl.md)**\]** and **\[**[**retval**](retval.md)**\]** attributes. If the last parameter does not have the \[out, retval\] attributes, the return value of the function is treated as an \[out, retval\] parameter. For example, a function with the prototype

``` syntax
[propget] short MyFunction([in] long aLongValue);
```

is treated as

``` syntax
[propget] HRESULT MyFunction([in] long aLongValue, [out,retval] short *outValue);
```

At most, one of **\[propget\]**, **\[**[**propput**](propput.md)**\]**, and **\[**[**propputref**](propputref.md)**\]** can be specified for a function.

If the **\[**[**lcid**](lcid.md)**\]** attribute is used in the parameter list of a function that contains a parameter with the **\[**[**propput**](propput.md)**\]** attribute, the **\[lcid\]** parameter must be second to the last.

### Flags

INVOKE\_PROPERTYGET

## Examples

``` syntax
interface MyInterface : IDispatch                         
{                
    [propget, 
     helpstring("A meaningful comment.")] HRESULT Method1(
         [out, retval] int* ReturnVal); 

    [propput, 
     helpstring("Another meaningful comment.")] HRESULT Method1(
         [in] int Value);
        
    [propget, 
     helpstring("A meaningful comment."), id(1)] HRESULT Method2(
         [out, retval] YourInterface** ReturnVal); 

    [propputref, 
     helpstring("Another meaningful comment."), 
     id(1)] HRESULT Method2([in] YourPoint* Point);
}                 
```

## See also

<dl> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[ODL File Example](86d64a4f-08eb-422a-bb1d-dfa868094645)
</dt> <dt>

[ODL File Syntax](df7aa86f-1453-4409-939e-788d469d611e)
</dt> <dt>

[**out**](out-idl.md)
</dt> <dt>

[**retval**](retval.md)
</dt> <dt>

[**propput**](propput.md)
</dt> <dt>

[**propputref**](propputref.md)
</dt> <dt>

[**TYPEFLAGS**](bf34cc90-f772-4562-9d18-7cf35aeed41e)
</dt> </dl>

 

 




