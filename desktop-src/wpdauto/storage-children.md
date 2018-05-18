---
title: Storage.Children property
description: The Children property returns a collection of all of the immediate children of this Storage object.
ms.assetid: '60edf773-181a-4923-beea-8fd42aed7b70'
keywords: ["Children property WPD Automation", "Children property WPD Automation , Storage object", "Storage object WPD Automation , Children property"]
topic_type:
- apiref
api_name:
- Storage.Children
api_type:
- COM
---

# Storage.Children property

The **Children** property returns a collection of all of the immediate children of this **Storage** object.

This property is read-only.

## Syntax


```JScript
Children = Storage.Children
```



## Property value

A read-only **childrenCollection**.

## Remarks

To retrieve a collection of children from a **Storage** object that is filtered by one or more data formats, use the [**Storage.GetChildrenByFormat**](storage-getchildrenbyformat.md) method.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**childrenCollection Object**](childrencollection-object.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> </dl>

 

 





