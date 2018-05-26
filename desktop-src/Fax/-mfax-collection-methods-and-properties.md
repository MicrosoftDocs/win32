---
Description: Objects that are a part of a collection often have a similar set of methods and properties, which are all or a combination of the following.
ms.assetid: b2cac190-a57c-45fe-897f-270806cf5d98
title: Collection Methods and Properties
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Collection Methods and Properties

Objects that are a part of a collection often have a similar set of methods and properties, which are all or a combination of the following.



| Method     | Description                                                                            |
|------------|----------------------------------------------------------------------------------------|
| **Add**    | Adds an object to the collection, and returns a reference to the newly created object. |
| **Remove** | Removes an object from the collection.                                                 |



 



| Property  | Description                                                          |
|-----------|----------------------------------------------------------------------|
| **Count** | Returns a **long** value of the number of objects in the collection. |
| **Item**  | Returns the given object from the collection.                        |



 

While most collections of objects work in the same way, see individual collection reference pages for particular descriptions.

With Microsoft Visual C++, you can browse a collection to find a particular item by using the **\_NewEnum** property or the **Item** property. Fax server collections include the **\_NewEnum** property and the **Item** property. The **Item** property is described in the fax service software development kit (SDK) reference. For more information about **\_NewEnum**, see the fax service SDK Faxcomex.h file. In Microsoft Visual Basic, you do not need to use the **\_NewEnum** property, because it is automatically used in the implementation of **For Each ... Next**.

Both the **Item** property and the **Remove** method use a one-based index parameter to identify a specific object in the collection. In some collections, the index parameter also accepts a string to identify the specific object. For example, the index parameter in the [**FaxOutboundRoutingGroups::get\_Item**](-mfax-faxoutboundroutinggroups-item.md) and [**FaxOutboundRoutingGroups::Remove**](/windows/previous-versions/FaxComex/?branch=master) methods accepts an integer value representing the index of the outbound routing group, or a string representing the unique name of the group.

In Visual Basic, there are four approaches to using the **Item** property. For example, change the [**RingsBeforeAnswer**](/windows/previous-versions/FaxComex/?branch=master) property of the third device from a collection of devices. Use the **Item()** property to access the third device. This can be expressed in Visual Basic in the following four ways.


```
objFaxDevices.Item(2).RingsBeforeAnswer = 5 
objFaxDevices.Item("My Device Name").RingsBeforeAnswer = 5 
objFaxDevices(2).RingsBeforeAnswer = 5 
objFaxDevices("My Device Name").RingsBeforeAnswer = 5
```



You can also create a [**FaxDevice**](-mfax-faxdevice.md) object, set it equal to Item (2) from the [**FaxDevices**](-mfax-faxdevices.md) collection, and then access the [**RingsBeforeAnswer**](/windows/previous-versions/FaxComex/?branch=master) property through the **FaxDevice** object.

Several of these approaches are used in the [Visual Basic Fax Administration Scenarios](-mfax-visual-basic-fax-administration-scenarios.md).

 

 



