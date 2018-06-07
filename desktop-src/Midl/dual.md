---
title: dual attribute
description: The dual attribute identifies an interface that exposes properties and methods through IDispatch and directly through the VTBL.
ms.assetid: 1c214f10-57eb-4a05-99a8-a09770666a74
keywords:
- dual attribute MIDL
topic_type:
- apiref
api_name:
- dual
api_type:
- NA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# dual attribute

The **dual** attribute identifies an interface that exposes properties and methods through [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) and directly through the VTBL.

``` syntax
[
    uuid(uuid-number), 
    oleautomation,
    dual 
  [ , optional-attribute-list]
]
interface interface-name
{
    . . .
};
```

## Parameters

<dl> <dt>

*uuid-number* 
</dt> <dd>

Specifies a universally unique identification number for the interface

</dd> <dt>

*optional-attribute-list* 
</dt> <dd>

Specifies a list of zero or more additional MIDL attributes.

</dd> <dt>

*interface-name* 
</dt> <dd>

The name of the interface to which the **dual** attribute will be applied.

</dd> </dl>

## Remarks

Interfaces identified by the **dual** attribute must be compatible with Automation and be derived from [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5). This attribute is not allowed on dispinterfaces.

The **dual** attribute creates an interface that is both an [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface and a Component Object Model (COM) interface. The first seven entries of the VTBL for a dual interface are the seven members of **IDispatch**, and the remaining entries are for direct access to members of the dual interface. All the parameters and return types specified for members of a dual interface must be Automation-compatible types.

All members of a dual interface must pass an HRESULT as the function return value. Members, such as property accessor functions, that need to return other values, should specify the last parameter as [**out**](out-idl.md), [**retval**](retval.md), indicating an output parameter that returns the value of the function. In addition, members that need to support multiple locales should pass an [**lcid**](lcid.md) parameter.

A dual interface provides for both the speed of direct VTBL binding and the flexibility of [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) binding. For this reason, dual interfaces are recommended whenever possible.

> [!Note]  
> If your application accesses object data by casting the *this* pointer within the interface call, you should check the VTBL pointers in the object against your own VTBL pointers to ensure that you are connected to the appropriate proxy.

 

Specifying **dual** on an interface implies that the interface is compatible with Automation, and therefore causes both the TYPEFLAG\_FDUAL and TYPEFLAG\_FOLEAUTOMATION flags to be set.

### Flags

TYPEFLAG\_FDUAL, TYPEFLAG\_FOLEAUTOMATION

## Examples

``` syntax
[
    uuid(1e196b20-1f3c-1069-996b-00dd010fe676), 
    oleautomation, dual
]
interface IHello : IDispatch
{
    //Diverse properties and methods defined here.
};
```

## See also

<dl> <dt>

[Generating a Type Library With MIDL](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[**interface**](interface.md)
</dt> <dt>

[**lcid**](lcid.md)
</dt> <dt>

[**oleautomation**](oleautomation.md)
</dt> <dt>

[ODL File Syntax](https://msdn.microsoft.com/windows/desktop/df7aa86f-1453-4409-939e-788d469d611e)
</dt> <dt>

[ODL File Example](https://msdn.microsoft.com/windows/desktop/86d64a4f-08eb-422a-bb1d-dfa868094645)
</dt> <dt>

[**out**](out-idl.md)
</dt> <dt>

[**retval**](retval.md)
</dt> </dl>

 

 




