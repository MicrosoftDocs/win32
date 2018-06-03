---
title: About the WPD Automation Object Model
description: The WPD Automation object model is made up of objects that represent a physical device and the services, storages, properties, methods, and events that are present on that device.
ms.assetid: 0d8cc8ec-197b-4439-814a-0a39c0eb5f94
keywords:
- WPD Automation,object model
- WPD Automation,hierarchy of objects
- Windows Portable Devices (WPD),WPD Automation object model
- WPD (Windows Portable Devices),WPD Automation object model
- Windows Portable Devices (WPD),WPD Automation
- WPD (Windows Portable Devices),WPD Automation
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About the WPD Automation Object Model

The WPD Automation object model is made up of objects that represent a physical device and the services, storages, properties, methods, and events that are present on that device.

The following diagram shows the hierarchy of objects in WPD Automation.

![diagram showing objects arranged in a hierarchy](images/wpdautomation-object-hierarchy.png)

In WPD Automation, a device is represented by a hierarchy of objects. The preceding example illustrates a device (in this case, a mobile phone) represented by a Device object that contains one Storage object, a Contacts Service, and a Ringtones Service. Storage objects store data and typically represent the actual storage on the device. Services can also store data and can support additional functionality depending on the type of service implemented. Some services store only specific types of data. In this example, the Ringtones Service stores only ringtones, and can support a method to associate a contact with a ringtone. Both storages and services can store a collection of child objects. Each child object represents data on the device. In this example, the data can represent music, images, contacts, or ringtones.

The following topics provide overview information about the WPD Automation Object Model.

-   [Using WPD Automation](using-wpd-automation.md)
-   [About the Device Object](about-the-device-object.md)
-   [About the servicesCollection and storagesCollection Objects](about-the-servicescollection-and-storagescollection-objects.md)
-   [About the WPDobject](about-the-wpdobject-.md)
-   [About the Service Object](about-the-service-object.md)
-   [About the Storage Object](about-the-storage-object.md)
-   [About the childrenCollection Object](about-the-childrencollection-object.md)
-   [About the Creation Container Object](about-the-creation-container-object.md)
-   [About the Resource Object](about-the-resource-object.md)

## Related topics

<dl> <dt>

[WPD Automation Object Model](wpd-automation-object-model.md)
</dt> </dl>

 

 




