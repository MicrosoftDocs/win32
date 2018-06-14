---
title: propputref attribute
description: The \ propputref\ attribute specifies a property-setting function that uses a reference instead of a value.
ms.assetid: 84f1cd08-3c42-4a6d-bb1d-0bfd3f4c33f2
keywords:
- propputref attribute MIDL
topic_type:
- apiref
api_name:
- propputref
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# propputref attribute

The **\[propputref\]** attribute specifies a property-setting function that uses a reference instead of a value.

``` syntax
[propputref [,optional-property-attributes]] return-type function-name( parameters);
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

A function that has the **\[propputref\]** attribute must also have, as its last parameter, a pointer that has the **\[**[**in**](in.md)**\]** attribute.

The property must have the same name as the function. At most, one of **\[**[**propget**](propget.md)**\]**, **\[**[**propput**](propput.md)**\]** and **\[propputref\]** attributes can be specified for a function.

### Flags

INVOKE\_PROPERTYPUTREF

## Examples

``` syntax
interface InMyFace : IDispatch 
{
    [propget, 
     helpstring("A meaningful comment."), 
     id(1)] HRESULT Method2([out, retval] YourInterface** ReturnVal); 
    [propputref, 
     helpstring("Another meaningful comment."), 
     id(1)] HRESULT Method2([in] YourPoint* Point);
}
```

## See also

<dl> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[**in**](in.md)
</dt> <dt>

[ODL File Example](https://msdn.microsoft.com/en-us/library/ms221308(v=VS.71).aspx)
</dt> <dt>

[ODL File Syntax](https://msdn.microsoft.com/en-us/library/ms221683(v=VS.71).aspx)
</dt> <dt>

[**propget**](propget.md)
</dt> <dt>

[**propput**](propput.md)
</dt> <dt>

[**TYPEFLAGS**](https://msdn.microsoft.com/en-us/library/ms221509(v=VS.71).aspx)
</dt> </dl>

 

 




