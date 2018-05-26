---
title: defaultbind
description: Indicates the single, bindable property that best represents the object.
ms.assetid: 393be90a-b815-4a57-a42f-efbe074d2d04
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# defaultbind

Indicates the single, bindable property that best represents the object.

## Allowed on

Property.

## Flags

<dl> FUNCFLAG\_FDEFAULTBIND  
VARFLAG\_FDEFAULTBIND  
</dl>

## Remarks

Properties that have the defaultbindattribute must also have the [bindable](bindable.md) attribute. The defaultbind attribute cannot be specified on more than one property in a dispinterface.

This attribute is used by containers that have a user model that involves binding to an object rather than binding to a property of an object. An object can support data binding and not have this attribute.

## Related topics

<dl> <dt>

[Attribute Descriptions](attribute-descriptions.md)
</dt> </dl>

 

 




