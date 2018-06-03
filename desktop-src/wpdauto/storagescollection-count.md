---
title: storagesCollection.Count property
description: The Count property gets the number of Storage objects in the collection.
ms.assetid: 020c7dea-94c7-4115-844d-90a209c3e527
keywords:
- Count property WPD Automation
- Count property WPD Automation , storagesCollection object
- storagesCollection object WPD Automation , Count property
topic_type:
- apiref
api_name:
- storagesCollection.Count
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# storagesCollection.Count property

The **Count** property gets the number of **Storage** objects in the collection.

This property is read-only.

## Syntax


```JScript
Count = storagesCollection.Count
```



## Property value

The read-only number of **Storage** objects in the collection.

## Examples

The following JScript example uses **storagesCollection.Count** to enumerate a collection of storages and access them by index.


```JScript
// Retrieve a collection of storages from the device.
var storages = deviceObject.Storages;

// Enumerate the storages in the collection and access them by index.
for (i=0; i < storages.Count; i++)
{
    var aStorage = storages[i];
}
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**storagesCollection Object**](storagescollection-object.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> </dl>

 

 





