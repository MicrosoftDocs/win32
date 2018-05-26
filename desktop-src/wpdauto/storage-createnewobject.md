---
title: Storage.CreateNewObject method
description: The CreateNewObject method creates and initializes a WPDObject to the specified data format.
ms.assetid: 8e5b5b89-f4fd-4fc8-af6a-cbaa69a2586a
keywords:
- CreateNewObject method WPD Automation
- CreateNewObject method WPD Automation , Storage object
- Storage object WPD Automation , CreateNewObject method
topic_type:
- apiref
api_name:
- Storage.CreateNewObject
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Storage.CreateNewObject method

The **CreateNewObject** method creates and initializes a **WPDObject** to the specified data format.

## Syntax


```JScript
retVal = Storage.CreateNewObject(
  Format
)
```



## Parameters

<dl> <dt>

*Format* 
</dt> <dd>

A string that is the data format of the new **WPDObject**.

</dd> </dl>

## Return value

Returns a [**Creation Container**](creation-container-object.md) object that is used to set properties and data. When the [**Creation Container**](creation-container-object.md) is passed to the [**Storage.AddChild**](storage-addchild.md) method, a new **WPDObject** containing the properties and data of the specified data format will be added as the child of a **Storage** object.

## Examples

The following JScript example uses the **CreateNewObject** method to add a newly created storage object (a "VCard2" formatted contact) as a child of another storage object. In this example, *contact* is the [**Creation Container**](creation-container-object.md) that is used to set the properties *ContactDisplayName*, and *ContactMobilePhone*. When *contact* is added as a child of the *storage* object, it becomes a new **WPDObject** object that represents a contact on the device, and the property values are persisted.


```JScript
// Create a new storage object of the "Vcard2" format.
var contact = storage.CreateNewObject("Vcard2");
contact.ContactDisplayName = "Bob";
contact.ContactMobilePhone = "(206)555-1234";

// Add the new contact as a child of the storage object.
// Note that the new object will not be persisted until
// it is added by using this method.
storage.AddChild(contact);
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

 

 





