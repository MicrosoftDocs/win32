---
title: Enumerating the Content of a Service or a Storage
description: There are two ways to enumerate the child objects contained in the childrenCollection of a parent WPDObject retrieving a collection of all children from the Children property, and retrieving a collection of children by calling the GetChildrenByFormat method.
ms.assetid: d6f63c24-ee53-4fe0-9307-526ac044777b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enumerating the Content of a Service or a Storage

The [**Service**](service-object.md) object and the [**Storage**](storage-object.md) object are both specialized types of [**WPDObject**](wpdobject.md). This means that they inherit from **WPDObject** the common functionality of containing a collection of child objects that can be enumerated, added to, or removed from the collection.

This collection of child objects is known generically as a [**childrenCollection**](childrencollection-object.md), and more specifically as a [**servicesCollection**](servicescollection-object.md) or a [**storagesCollection**](storagescollection-object.md), depending on whether it is contained in a **Service** object or a **Storage** object.

There are two ways to enumerate the child objects contained in the [**childrenCollection**](childrencollection-object.md) of a parent [**WPDObject**](wpdobject.md): retrieving a collection of all children from the **Children** property, and retrieving a collection of children by calling the **GetChildrenByFormat** method.

## Enumerating Child Objects in a childrenCollection

Retrieving a collection of all children from the read-only **Children** property is shown in the following example.


```JScript
var children = wpdObject.Children;
```



Retrieving a collection of children by format by calling the **GetChildrenByFormat** method is shown in the following example.


```JScript
var children = wpdObject.GetChildrenByFormat(VARIANT);
```



## Retrieving a Collection of Children by Format

When retrieving a collection of children by format, as in the previous example, VARIANT can be a string containing the name of the format or an array of strings that are format names. In the following example, VARIANT is a string that contains the name of the format.


```JScript
var children = wpdObject.GetChildrenByFormat("AbstractContact");
```



The following example uses VARIANT as an array of strings that are format names.


```JScript
// This is the array type supported by JScript.
var children = wpdObject.GetChildrenByFormat(["AbstractContact", "Vcard2"]); 

// A regular JScript Array can also be used.
var formats = new Array("AbstractContact", "Vcard2"); 
var children = wpdObject.GetChildrenByFormat(formats);
```



## Enumerating the Content of a Service

The content of a [**Service**](service-object.md) object can be enumerated using the same two ways outlined previously for enumerating the content of a [**WPDObject**](wpdobject.md): retrieving a collection of the children from a service, and retrieving a collection of children from a service by format.

The following example shows how to retrieve a collection of the children from a service.


```JScript
// Get a specific service from the device.
var service = deviceObject.Services[1];

// Get the collection of all children for this service.
var children = service.Children;
```



The following example shows how to retrieve a collection of children from a service by format, enumerate the collection, and retrieve property values from items in the collection. This example assumes that the PUID of the contacts service is known. For more information on retrieving the PUID for a specific service, see [Enumerating Services and Storages](enumerating-services-and-storages.md).


```JScript
function GetServiceContent()
{
    // Get the contacts service from the device.
    var service = deviceObject.Services["contactsServicePUID"];

    // Retrieve a collection of contacts from the service by format.
    var contactObjects = service.GetChildrenByFormat(["AbstractContact", "Vcard2"]);

    // Enumerate the contacts in the collection. 
    for (i=0; i < contactObjects.Count; i++)
    {
        // Get a property value from this contact.
        var firstName = contactObjects[i].ContactPhoneticFirstName;
          
        // Get other property values from this contact.
    }    
}
```



### Enumerating the Content of a Storage

The content of a [**Storage**](storage-object.md) object can also be enumerated using the same two ways described for enumerating the content of a [**WPDObject**](wpdobject.md): retrieving a collection of the children from a storage, and retrieving a collection of children from a storage by format.

The following example shows how to retrieve a collection of the children from a storage.


```JScript
// Get a specific storage from the device.
var storage = deviceObject.Storages[1];

// Get the collection of all children for this storage.
var children = storage.Children;
```



The following example shows how to retrieve a collection of children from a storage by format, enumerate the collection, and retrieve property values from items in the collection.


```JScript
function GetStorageContent()
{
    // Get a specific storage from the device.
    var storage = deviceObject.Storages[0];     

    // Retrieve a collection of audio objects from the storage by format.
    var audioObjects = storage.GetChildrenByFormat(["Wma", "Mp3"]);

    // Enumerate the audio objects in the collection.
    for (i=0; i < audioObjects.Count; i++)
    {
        // Get a property value from this audio object.
        var title = audioObjects[i].MediaTitle;

        // Get other property values from this audio object.
    }    
}
```



## Related topics

<dl> <dt>

[**childrenCollection Object**](childrencollection-object.md)
</dt> <dt>

[**Device Object**](device-object.md)
</dt> <dt>

[Enumerating Services and Storages](enumerating-services-and-storages.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**servicesCollection Object**](servicescollection-object.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[**storagesCollection Object**](storagescollection-object.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> <dt>

[WPD Automation Programming Guide](wpd-automation-programming-guide.md)
</dt> </dl>

 

 




