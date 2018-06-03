---
title: Storage.AddChild method
description: The AddChild method adds a WPDObject obtained from the Storage.CreateNewObject method, as a child of this Storage object.
ms.assetid: 5f744a97-5564-4f8d-8c7c-992bc7340ffe
keywords:
- AddChild method WPD Automation
- AddChild method WPD Automation , Storage object
- Storage object WPD Automation , AddChild method
topic_type:
- apiref
api_name:
- Storage.AddChild
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Storage.AddChild method

The **AddChild** method adds a **WPDObject** obtained from the [**Storage.CreateNewObject**](storage-createnewobject.md) method, as a child of this **Storage** object.

## Syntax


```JScript
Storage.AddChild(
  creationContainerObject
)
```



## Parameters

<dl> <dt>

*creationContainerObject* 
</dt> <dd>

A **creationContainer** that is used to set data in a [**WPDObject**](wpdobject.md) so that it can be added as a child of this **Storage** object.

</dd> </dl>

## Return value

If called in synchronous mode, this method returns the newly created child object. If called in asynchronous mode, this method does not return a value. The newly created child object is provided as a parameter to the handler-function assigned to the [**onAddChildComplete**](storage-onaddchildcomplete.md) event.

## Remarks

To enable asynchronous behavior, set the handler for the [**onAddChildComplete**](storage-onaddchildcomplete.md) event before calling this method.

## Examples

The following JScript example uses the **AddChild** method to add a newly created storage object (a contact) as a child of another storage object.


```JScript
// Create a new storage object that is a contact and set
// its data properties.
var contact = storage.CreateNewObject("Vcard2");
contact.ContactDisplayName = "Bob";
contact.ContactMobilePhone = "(206)555-1234";

// Add the new contact storage object as a child of the 
// main storage object.
storage.AddChild(contact); 

// Also add the contact as a child of another storage object within
// the main storage. Doing both will result in two separate new
// contact storage objects.
folder.AddChild(contact);
```



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Creation Container Object**](creation-container-object.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





