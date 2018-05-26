---
title: About the Creation Container Object
description: New WPDObjects are created only when either the Service.CreateNewObject method or the Storage.CreateNewObject method is called.
ms.assetid: 6fe901a2-0702-4622-9350-d5bfd0dcc5cb
keywords:
- WPD Automation,WPDObject
- WPD Automation,Service object
- WPD Automation,Storage object
- WPD Automation,CreateNewObject
- WPD Automation,Creation Container object
- WPDObject,WPD Automation
- WPDObject,childrenCollection object
- Creation Container object
- CreateNewObject
- Service object,Creation Container object
- Storage object,Creation Container object
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About the Creation Container Object

New [**WPDObject**](wpdobject.md)s are created only when either the [**Service.CreateNewObject**](service-createnewobject.md) method or the [**Storage.CreateNewObject**](storage-createnewobject.md) method is called. A [**Creation Container**](creation-container-object.md) object is created to hold properties and data temporarily that must be set during the creation of the new object. The new object remains a **Creation Container** object, and is not persisted as a **WPDObject** until the [**AddChild**](wpdobject-addchild.md) method on the parent object is called.

## Creating a WPD Automation Object

The following flowchart shows how new objects in WPD Automation are created and initialized.

![flowchart showing how new objects are created and initialized in wpd automation](images/wpdautomation-object-creation.jpg)

Use the following steps to create a WPD Automation object.

1.  Identify the storage or service that the object will be stored in.
2.  Instantiate a **Creation Container** object, which is a temporary object that holds the properties and data that are used to initialize the new object. Depending on the location of the new object, use either [**Service.CreateNewObject**](service-createnewobject.md)([**Format**](service-createnewobject.md)), or [**Storage.CreateNewObject**](storage-createnewobject.md)([**Format**](storage-createnewobject.md)). The format is used by WPD Automation to determine what properties can be set. For example, the format can be "mp3" to create a container to hold properties and data for transferring an MP3 object to the device.
3.  Assign the properties for the new object to the **Creation Container** object. Depending on the capabilities of the device, objects of different formats might require different properties.
4.  If the new object will contain only properties, for example, a contact or a folder, skip to step 6.
5.  If the new object will contain binary data in addition to properties, for example, a music or image file, assign the [**Data**](createcontainerobject-data.md) property of the **Creation Container** object to the *responseStream* returned by [IXMLHttpRequest](http://go.microsoft.com/fwlink/p/?linkid=130621). This enables data to be transferred from a Web service and stored with the new object.
6.  Save the new object by calling the **AddChild** method of the parent **WPDObject** object, passing in the **Creation Container** object. The object is not stored until this step is completed.

The following example illustrates how a child contact object is created and added to a storage. The contact object does not contain any data.


```JScript
// Create a container object of the "Vcard2" format.
// This will be used to hold the properties for the new contact
// until it is added to the storage.
var container = storage.CreateNewObject("Vcard2");

// Set the value of two properties on the contact.
container.ContactDisplayName = "Bob";
container.ContactMobilePhone = "(206)555-1234";

// Write the Vcard2 contact to the storage by calling the AddChild()
// method. Here, the new object is created as a direct child of the
// storage.
var newContact = storage.AddChild(container);
```



When a new object contains data, the data is set through the [**Data**](createcontainerobject-data.md) property of the [**Creation Container**](creation-container-object.md) object. This **Data** property is used to hold the IStream retrieved from the XMLHttpRequest response, as in the following example.


```JScript
// Create a container object of the "mp3" format.
// This will be used to hold properties and binary data of the new
// music object until it is added to the storage.
var container = storage.CreateNewObject("mp3");

// Set the value of two properties on the music file.
container.MediaTitle = "Contoso";
container.MediaGenre = "Blues";

// Set the binary data for the mp3 file from a web service.
container.Data = xmlHttpRequest.ResponseStream;

// Write the mp3 object (with data) to the storage by calling the 
// AddChild() method. Here, the new object is created as a direct
// child of the storage.
var newMp3 = storage.AddChild(container);
```



For more examples of using the [**Data**](createcontainerobject-data.md) property of the [**Creation Container**](creation-container-object.md) while writing resource data synchronously and asynchronously, see [Reading and Writing Resource Data](reading-and-writing-resource-data.md).

## Related topics

<dl> <dt>

[About the WPD Automation Object Model](about-the-wpd-automation-object-model.md)
</dt> <dt>

[Creating and Deleting Objects](creating-and-deleting-objects.md)
</dt> <dt>

[**Creation Container Object**](creation-container-object.md)
</dt> <dt>

[**Resource Object**](resource-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 




