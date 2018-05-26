---
title: WPDObject.RemoveChild method
description: The RemoveChild method deletes a child object from this WPDObject.
ms.assetid: 3b4dd16f-1dff-448e-9f8e-4a589c0b07cf
keywords:
- RemoveChild method WPD Automation
- RemoveChild method WPD Automation , WPDObject object
- WPDObject object WPD Automation , RemoveChild method
topic_type:
- apiref
api_name:
- WPDObject.RemoveChild
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WPDObject.RemoveChild method

The **RemoveChild** method deletes a child object from this **WPDObject**.

## Syntax


```JScript
WPDObject.RemoveChild(
  wpdObject,
  [ boolRecursive ]
)
```



## Parameters

<dl> <dt>

*wpdObject* 
</dt> <dd>

A **WPDObject** that is the child object to be deleted. If the child object does not exist, this method returns an error.

</dd> <dt>

*boolRecursive* \[optional\]
</dt> <dd>

A **Boolean** value that indicates whether the delete operation is recursive. If the child object to be removed contains children, this parameter must be set or the method will fail. If the *boolRecursive* parameter is not specified, and the child object does not contain children, the default value of "false" is assumed, and a nonrecursive delete is performed.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

To enable asynchronous behavior, set the handler for the [**onRemoveChildComplete**](onremovechildcomplete.md) event before calling this method.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





