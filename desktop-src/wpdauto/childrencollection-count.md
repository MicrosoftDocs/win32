---
title: childrenCollection.Count property
description: The Count property gets the number of child objects in the collection.
ms.assetid: 0d52fe4b-2c5d-4032-b7d3-24f274d6b3d1
keywords:
- Count property WPD Automation
- Count property WPD Automation , childrenCollection object
- childrenCollection object WPD Automation , Count property
topic_type:
- apiref
api_name:
- childrenCollection.Count
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# childrenCollection.Count property

The **Count** property gets the number of child objects in the collection.

This property is read-only.

## Syntax


```JScript
Count = childrenCollection.Count
```



## Property value

The read-only number of child objects in the collection.

## Examples

The following JScript example uses **childrenCollection.Count** to enumerate a collection of child objects and access them by index.


```JScript
// Retrieve a collection of all the children in a WPDObject.

var childrenCollection = wpdObject.Children;

// Enumerate the children in the collection.

for (i=0; i < childrenCollection.Count; i++)
{
    // Access a child object by numeric index.
    var aChild = childrenCollection[i]; 
}
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**childrenCollection Object**](childrencollection-object.md)
</dt> </dl>

 

 





