---
title: propput attribute
description: The \ propput\ attribute specifies a property-setting function. The property must have the same name as the function.
ms.assetid: ffd8af15-42a4-4852-a29b-1fc66f673978
keywords:
- propput attribute MIDL
topic_type:
- apiref
api_name:
- propput
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# propput attribute

The **\[propput\]** attribute specifies a property-setting function. The property must have the same name as the function*.*

``` syntax
[propput [,optional-property-attributes]] return-type function-name( parameters);
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

A function that has the **\[propput\]** attribute must also have, as its last parameter, a parameter that has the **\[**[**in**](in.md)**\]** attribute.

At most, one of **\[**[**propget**](propget.md)**\]**, **\[propput\]** and **\[**[**propputref**](propputref.md)**\]** can be specified for a function.

If the **\[**[**lcid**](lcid.md)**\]** attribute is used in the parameter list of a function that contains a parameter with the **\[propput\]** attribute, the **\[lcid\]** parameter must be second to the last.

### Flags

INVOKE\_PROPERTYPUT

## Examples

``` syntax
interface InMyFace : IDispatch                         
{
    [propget, 
     helpstring("A meaningful comment.")] HRESULT Method1(
         [out, retval] int* ReturnVal); 

    [propput, 
     helpstring("Another meaningful comment.")] HRESULT Method1(
         [in] int Value);
}
```

## See also

<dl> <dt>

[Differences Between MIDL and MKTYPLIB](differences-between-midl-and-mktyplib.md)
</dt> <dt>

[ODL File Example](86d64a4f-08eb-422a-bb1d-dfa868094645)
</dt> <dt>

[ODL File Syntax](df7aa86f-1453-4409-939e-788d469d611e)
</dt> <dt>

[**propget**](propget.md)
</dt> <dt>

[**propputref**](propputref.md)
</dt> <dt>

[**TYPEFLAGS**](bf34cc90-f772-4562-9d18-7cf35aeed41e)
</dt> </dl>

 

 




