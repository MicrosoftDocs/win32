---
title: Service.Children property
description: The Children property returns a collection of all of the immediate children of this Service object.
ms.assetid: af41c0a2-6b0b-4b7e-9da7-55d43dc25977
keywords:
- Children property WPD Automation
- Children property WPD Automation , Service object
- Service object WPD Automation , Children property
topic_type:
- apiref
api_name:
- Service.Children
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Service.Children property

The **Children** property returns a collection of all of the immediate children of this **Service** object.

This property is read-only.

## Syntax


```JScript
Children = Service.Children
```



## Property value

A read-only **childrenCollection**.

## Remarks

To retrieve a collection of children from a service that is filtered by one or more data formats, such as "WPD" or "MP3", use the [**Service.GetChildrenByFormat**](service-getchildrenbyformat.md) method.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**childrenCollection Object**](childrencollection-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> </dl>

 

 





