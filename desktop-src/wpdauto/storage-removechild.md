---
title: Storage.RemoveChild method
description: The RemoveChild method removes a child object from this Storage object.
ms.assetid: ee63d337-a46d-4b97-9492-5f36e0dcf1fe
keywords:
- RemoveChild method WPD Automation
- RemoveChild method WPD Automation , Storage object
- Storage object WPD Automation , RemoveChild method
topic_type:
- apiref
api_name:
- Storage.RemoveChild
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Storage.RemoveChild method

The **RemoveChild** method removes a child object from this **Storage** object.

## Syntax


```JScript
Storage.RemoveChild(
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

A **Boolean** value that indicates whether the delete operation is recursive. If the object to be removed contains children, this parameter must be set or the method will fail. If the *boolRecursive* parameter is not specified, and the object does not contain children, the default value of "false" is assumed and a nonrecursive delete is performed.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

To enable asynchronous behavior, set the handler for the [**onRemoveChildComplete**](storage-onremovechildcomplete.md) event before calling this method.

## Examples

The following JScript example demonstrates the different ways in which the **RemoveChild** method can be used.


```JScript
// Removes someFolder nonrecursively.
storage.RemoveChild(someFolder, false);

// Also removes someFolder nonrecursively, but if someFolder has
// children, this method will fail. 
storage.RemoveChild(someFolder);
    
// Removes someFolder and all of the children in it.
storage.RemoveChild(someFolder, true);
```



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

 

 





