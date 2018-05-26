---
title: Resource.IsReadOnly property
description: The IsReadOnly property retrieves a value indicating whether the resource is read-only.
ms.assetid: f0741166-f74b-4b9c-a514-a21217dcc0f0
keywords:
- IsReadOnly property WPD Automation
- IsReadOnly property WPD Automation , Resource object
- Resource object WPD Automation , IsReadOnly property
topic_type:
- apiref
api_name:
- Resource.IsReadOnly
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Resource.IsReadOnly property

The **IsReadOnly** property retrieves a value indicating whether the resource is read-only.

This property is read-only.

## Syntax


```JScript
bIsReadOnly = Resource.IsReadOnly
```



## Property value

True if the resource is read-only and false otherwise.

## Remarks

In Windows 7 all resources are read-only. However, in future versions, resources may be modifiable.

## Examples

The following JScript example uses **IsReadOnly** to determine whether the resource *ringtone.Data* can be written to.


```JScript
// Test the "ringtone" Resource to see if it is read-only.
var readOnly = ringtone.Data.IsReadOnly;

if(!readOnly)
{
   // Perform some action.
}
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

 

 





