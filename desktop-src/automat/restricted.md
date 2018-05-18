---
title: restricted
description: Prevents the item from being used by a macro programmer.
ms.assetid: '97c9e46d-0bc9-4606-9994-acbe07d14040'
---

# restricted

Prevents the item from being used by a macro programmer.

## Allowed on

Type library, type information, coclass member, or member of a module or interface.

## Flags

<dl> IMPLTYPEFLAG\_FRESTRICTED  
FUNCFLAG\_FRESTRICTED  
TYPEFLAG\_FRESTRICTED  
VARFLAG\_FRESTRICTED  
</dl>

## Remarks

This attribute is allowed on a member of a coclass, independent of whether the member is a dispinterface or interface, and independent of whether the member is a sink or source. A member of a coclass cannot have both the restrictedand [default](default.md) attributes.

## Example


```C++
[     odl, 
      dual,
      uuid(1e196b20-1f3c-1069-996b-00dd010ef676),
      helpstring("This is IForm"),
      restricted
   ]
   interface IForm: IDispatch
   {
      [propget]
      HRESULT Backcolor([out, retval] long *Value);

      [propput]
      HRESULT Backcolor([in] long Value);
   }


   [  odl, 
      dual,
      uuid(1e196b20-1f3c-1069-996b-00dd010ef767),
      helpstring("This is IFormEvents"),
      restricted
   ]
   interface IFormEvents: IDispatch
   {
      HRESULT Click();
   }


   [  uuid(1e196b20-1f3c-1069-996b-00dd010fe676),
      helpstring("This is Form")
   ]
   coclass Form
   {
      [default] interface IForm;
      [default, source] interface IFormEvents;
   }
```



## Related topics

<dl> <dt>

[Attribute Descriptions](attribute-descriptions.md)
</dt> </dl>

 

 




