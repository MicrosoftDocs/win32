---
title: Resource.Size property
description: The Size property gets the size of the Resource, in bytes.
ms.assetid: 4b32ddf0-0302-4eda-b42f-5aebc2088de6
keywords:
- Size property WPD Automation
- Size property WPD Automation , Resource object
- Resource object WPD Automation , Size property
topic_type:
- apiref
api_name:
- Resource.Size
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resource.Size property

The **Size** property gets the size of the **Resource**, in bytes.

This property is read-only.

## Syntax


```JScript
Size = Resource.Size
```



## Property value

Read-only number of bytes.

## Examples

The following JScript example uses **Size** to read the total number of bytes in a **Resource**.


```JScript
// Get a Resource object and read its total size in bytes.

var stream = wpdObject.Resource;
var totalSizeInBytes = stream.Size;
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Resource Object**](resource-object.md)
</dt> </dl>

 

 





