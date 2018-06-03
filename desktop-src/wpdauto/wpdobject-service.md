---
title: WPDObject.Service property
description: The Service property gets the Service object that contains this WPDObject.
ms.assetid: 0efacca7-8471-47de-95c5-85fc8c7b5bd2
keywords:
- Service property WPD Automation
- Service property WPD Automation , WPDObject object
- WPDObject object WPD Automation , Service property
topic_type:
- apiref
api_name:
- WPDObject.Service
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WPDObject.Service property

The **Service** property gets the **Service** object that contains this **WPDObject**.

This property is read-only.

## Syntax


```JScript
Service = WPDObject.Service
```



## Property value

A **Service** object. If the current **WPDObject** is not contained within a **Service** object, then this property will return "undefined".

## Remarks

This method is useful for determining which service a given object belongs to.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





