---
description: Representing Functionality
ms.assetid: 34a4a015-614d-4fac-98d8-29ae43165798
title: Representing Functionality
ms.topic: article
ms.date: 05/31/2018
---

# Representing Functionality

Functional objects exist to identify or logically group feature capabilities of a device. For example, an application can see that a device supports SMS by looking for the SMS functional object. Similarly, the application can see that a device has camera capabilities by looking for the Still Image Capture functional object.

This flexible object representation helps enable easy support for devices with multi-function capabilities. Drivers can simply expose whatever functional objects represent their device, which is more granular than using traditional device classes. The object representation also helps isolate overlapping functional pieces; for example, some phones may have two cameras or four storages.

In the Windows 7 operating system, services extend functional objects by providing rich queries of capabilities and an abstract grouping of content. Applications can use services to discover device capabilities and to interact with content more efficiently. For example, an application can see that a device supports the contacts-synchronization capabilities by looking for a Contacts service object, and can find all contacts as child objects of the service object, without having to recursively search the storage hierarchy.

Services also allow applications to discover and invoke custom behavior on a device.

## Related topics

<dl> <dt>

[**Application Overview**](application-overview.md)
</dt> </dl>

 

 



