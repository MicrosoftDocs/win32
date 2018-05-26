---
title: WPDObject.AddChild method
description: The AddChild method adds a WPDObject obtained from either the Service.CreateNewObject() method or the Storage.CreateNewObject() method, as a child of this WPDObject.
ms.assetid: b2371cad-eb89-4fd2-8a08-a98880a9d4a2
keywords:
- AddChild method WPD Automation
- AddChild method WPD Automation , WPDObject object
- WPDObject object WPD Automation , AddChild method
topic_type:
- apiref
api_name:
- WPDObject.AddChild
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WPDObject.AddChild method

The **AddChild** method adds a **WPDObject** obtained from either the [**Service.CreateNewObject()**](service-createnewobject.md) method or the [**Storage.CreateNewObject()**](storage-createnewobject.md) method, as a child of this **WPDObject**.

## Syntax


```JScript
WPDObject.AddChild(
  creationContainerObject
)
```



## Parameters

<dl> <dt>

*creationContainerObject* 
</dt> <dd>

A **creationContainer** that is used to set data in a **WPDObject** so that it can be added as a child of this object.

</dd> </dl>

## Return value

If called in synchronous mode, this method returns the newly created child object. If called in asynchronous mode, this method does not return a value. The newly created child object is provided as a parameter to the handler-function assigned to the [**onAddChildComplete**](onaddchildcomplete.md) event.

## Remarks

To enable asynchronous behavior, set the handler for the [**onAddChildComplete**](onaddchildcomplete.md) event before calling this method.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Creation Container Object**](creation-container-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





