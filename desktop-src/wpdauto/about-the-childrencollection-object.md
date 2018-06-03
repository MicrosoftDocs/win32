---
title: About the childrenCollection Object
description: All Service and Storage objects contain a childrenCollection of child objects. Child objects can be retrieved in their entirety, read and enumerated directly, retrieved partially by a list of formats, added to, or removed from a childrenCollection.
ms.assetid: 9339db79-db69-47d8-bcaa-2d40471932de
keywords:
- WPD Automation,WPDObject
- WPD Automation,Service object
- WPD Automation,Storage object
- WPD Automation,CreateNewObject
- WPD Automation,childrenCollection
- WPDObject,WPD Automation
- WPDObject,childrenCollection object
- childrenCollection,about
- childrenCollection,WPD Automation
- childrenCollection,WPDObject
- childrenCollection,CreateNewObject
- CreateNewObject
- GetChildrenByFormat
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About the childrenCollection Object

All [**Service**](service-object.md) and [**Storage**](storage-object.md) objects contain a [**childrenCollection**](childrencollection-object.md) of child objects. Child objects can be retrieved in their entirety, read and enumerated directly, retrieved partially by a list of formats, added to, or removed from a **childrenCollection**.

The **Children** property of a **Service** or **Storage** object returns a **childrenCollection** that contains all of the children contained in the object, as shown in the following example.


```JScript
var aChildrenCollection = storage.Children;
```



The **childrenCollection** can also be enumerated directly through the same property by using the [**childrenCollection.Count**](childrencollection-count.md) property and a zero-based numeric index, as in this example.


```JScript
for (i=0; i < aChildrenCollection.Count; i++)
{
    var aChild = aChildrenCollection[i];

    // Do something with each child in the collection.
}
```



The **GetChildrenByFormat** method of a **Service** or **Storage** object returns a **childrenCollection** that contains only the children that are formatted with one of the data formats specified in a list. This makes it easy, for example, to retrieve a collection of all the WMA and MP3 ringtones contained in a service.


```JScript
var aChildrenCollection = service.GetChildrenByFormat(["Wma", "Mp3"]);
```



> [!Note]  
> For more information and examples of using the **GetChildrenByFormat** method, and of retrieving and enumerating the objects in a **childrenCollection**, see [Enumerating the Content of a Service or a Storage](enumerating-the-content-of-a-service-or-a-storage.md).

 

Child objects that are created through the **CreateNewObject** method of a **Service** or **Storage** object can be added to a **childrenCollection** by using the **WPDObject.AddChild** method. Child objects already in a **childrenCollection** can be removed by using the **WPDObject.RemoveChild** method. For more information, see [Creating and Deleting Objects](creating-and-deleting-objects.md).

## Related topics

<dl> <dt>

[About the WPD Automation Object Model](about-the-wpd-automation-object-model.md)
</dt> <dt>

[**Device Object**](device-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**servicesCollection Object**](servicescollection-object.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[**storagesCollection Object**](servicescollection-object.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 




