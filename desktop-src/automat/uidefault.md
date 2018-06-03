---
title: uidefault
description: Indicates that the type information member is the default member for display in the user interface.
ms.assetid: e9c71374-7976-4fc7-b2fd-0a0ec46f7463
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# uidefault

Indicates that the type information member is the default member for display in the user interface.

## Allowed on

A member of an interface or dispinterface.

## Flags

<dl> FUNCFLAG\_FUIDEFAULT  
VARFLAG\_FUIDEFAULT  
</dl>

## Remarks

This attribute is used to mark an event as the default (the first one created) or a property as the default (the one to select first in the properties browser).

For example, Visual Basic uses this attribute in the following ways:

-   When an object is double-clicked at design time, Visual Basic jumps to the event in the default source interface that is marked as \[uidefault\]. If there is no such member, then Visual Basic displays the first one listed in the default source interface.

-   When an object is selected at design time, by default, the Properties window in Visual Basic displays the property in the default interface that is marked as \[uidefault\]. If there is no such member, then Visual Basic displays the first one listed in the default interface.

## Example


```C++
 [   odl, 
   dual,
   uuid(1e196b20-1f3c-1069-996b-00dd010ef676),
   restricted
]
interface IForm: IDispatch
{
   [propget]
   HRESULT Backcolor([out, retval] long *Value);

   [propput]
   HRESULT Backcolor([in] long Value);


   [propget, uidefault]
   HRESULT Name([out, retval] BSTR *Value);

   [propput, uidefault]
   HRESULT Name([in] BSTR Value);
}

[   odl, 
   dual,
   uuid(1e196b20-1f3c-1069-996b-00dd010ef767),
   restricted
]
interface IFormEvents: IDispatch
{
   [uidefault]
   HRESULT Click();

   HRESULT Resize();
}

[uuid(1e196b20-1f3c-1069-996b-00dd010fe676)]
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

 

 




