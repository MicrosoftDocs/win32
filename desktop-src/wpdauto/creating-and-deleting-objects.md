---
title: Creating and Deleting Objects
description: Both types of WPDObject objects, Service objects and Storage objects, support the creation and deletion of child objects.
ms.assetid: fb4b669b-fba6-4e5f-adfb-9de8da0f2b08
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating and Deleting Objects

Both types of [**WPDObject**](wpdobject.md) objects, [**Service**](service-object.md) objects and [**Storage**](storage-object.md) objects, support the creation and deletion of child objects.

An example of this is creating a ringtone object and adding it as a child of a ringtones service object. Another example is deleting a child object of a storage (a JPEG) from a storage object that represents the device's legacy storage.

The following code examples demonstrate adding and deleting objects. For more examples of adding and deleting objects, see the reference pages for the [**Service.AddChild**](service-addchild.md), [**Service.RemoveChild**](service-removechild.md), [**Storage.AddChild**](storage-addchild.md), and [**Storage.RemoveChild**](service-removechild.md) methods.

## Creating and Adding a Storage Object

The following JScript example creates a new storage object (a contact) and adds it as a child of another storage object.


```JScript
function CreateAndAddStorageStuff()
{
    // Create a new storage object (a contact).

    var contact = storage.CreateNewObject("Vcard2");
    contact.ContactDisplayName = "Bob";
    contact.ContactMobilePhone = "(206)555-1234";

    // Add the new object as a child of another storage object.
    // Note that the new object is not persisted until it is added
    // by using the AddChild method.

    storage.AddChild(contact); 

    // The new object can also be added as a child of another object
    // within the storage. This will result in two separate new storage
    // objects.

    folder.AddChild(contact);   
}
```



## Creating and Adding a Service Object

The following JScript example creates a new service object (a ringtone), adds data to it, and then adds it as a child of another service object.


```JScript
function AddRingtoneToService()
{
    // Get a WMA ringtone from a vendor.

    var request = new ActiveXObject("MSXML2.XMLHTTP.3.0");
    request.open("GET", "https://vendor/site/ringtone.wma", false);
    request.send();

    // Create a new service object. Set its title, and set its data
    // to the WMA ringtone.

    var ringtone = ringtonesService.CreateNewObject("Wma");
    ringtone.MediaTitle = "blues";
    ringtone.Data = request.responseStream;

    // Add the new service object as a child of a service.

    ringtoneService.AddChild(ringtone); 

    // Add this object as a child of another object within the service.
    // This will result in two unique ringtone objects.

    ringtoneFolder.AddChild(ringtone); 
}
```



## Deleting a Storage Object

The following JScript example deletes a child storage object (a folder) from another storage object.


```JScript
function DeleteStorages()
{
    // Removes someFolder nonrecursively.

    storage.RemoveChild(someFolder, false);

    // Also removes someFolder nonrecursively, but if someFolder has
    // children, this method will fail.
 
    storage.RemoveChild(someFolder);
    
    // Removes someFolder and all of the children in it. 

    storage.RemoveChild(someFolder, true);  
}
```



## Deleting a Service Object

The following JScript example deletes a child service object (a contact) from another service object.


```JScript
function DeleteServices()
{
    // Removes someContact nonrecursively.

    contactsService.RemoveChild(someContact, false);

    // Also removes someContact nonrecursively, but if someContact has
    // children, this method will fail.

    contactsService.RemoveChild(someContact);
    
    // Removes someContact and all of the children in it. 

    contactsService.RemoveChild(someContact, true);
}
```



## Related topics

<dl> <dt>

[**Device Object**](device-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> <dt>

[WPD Automation Programming Guide](wpd-automation-programming-guide.md)
</dt> </dl>

 

 




