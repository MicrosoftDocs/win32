---
title: Service.RemoveChild method
description: The RemoveChild method deletes a child object from this Service object.
ms.assetid: 273bdca8-e493-4e67-a838-2f0d657f63fb
keywords:
- RemoveChild method WPD Automation
- RemoveChild method WPD Automation , Service object
- Service object WPD Automation , RemoveChild method
topic_type:
- apiref
api_name:
- Service.RemoveChild
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Service.RemoveChild method

The **RemoveChild** method deletes a child object from this **Service** object.

## Syntax


```JScript
Service.RemoveChild(
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

A **Boolean** value that indicates whether the delete operation is recursive. If the child object to be removed contains children, this parameter must be set or the method will fail. If the *boolRecursive* parameter is not specified, and the child object does not contain children, the default value of "false" is assumed, and a non-recursive delete is performed.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

To enable asynchronous behavior, set the handler for the [**onRemoveChildComplete**](service-onremovechildcomplete.md) event before calling this method.

## Examples

The following JScript example demonstrates the different ways in which the **RemoveChild** method can be used.


```JScript
// Removes someContact nonrecursively.
contactsService.RemoveChild(someContact, false);

// Also removes someContact nonrecursively, but if someContact has
// children, this method will fail. 
contactsService.RemoveChild(someContact);
    
// Removes someContact and all of the children in it. 
contactsService.RemoveChild(someContact, true);
```



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

 

 





