---
title: WPDObject.Storage property
description: The Storage property gets the Storage object that contains this WPDObject.
ms.assetid: d59d8d56-aac4-45e1-958d-1e973edf6df3
keywords:
- Storage property WPD Automation
- Storage property WPD Automation , WPDObject object
- WPDObject object WPD Automation , Storage property
topic_type:
- apiref
api_name:
- WPDObject.Storage
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WPDObject.Storage property

The **Storage** property gets the **Storage** object that contains this **WPDObject**.

This property is read-only.

## Syntax


```JScript
Storage = WPDObject.Storage
```



## Property value

A **Storage** object. If the current **WPDObject** is not contained within a **Storage** object, this property will return "undefined".

## Remarks

This method is useful for determining which storage a given object belongs to.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





