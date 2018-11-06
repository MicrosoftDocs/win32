---
title: What is the Control Point Object Model
description: The following illustration shows the basic Control Point object model.
ms.assetid: 6c5a32a1-932e-4868-b4c6-8701e90a7c26
ms.topic: article
ms.date: 05/31/2018
---

# What is the Control Point Object Model?

The following illustration shows the basic Control Point object model.

![control point object model](images/upnp-object-model.png)

Searching for devices with the Device Finder interface creates a Devices collection. A Devices collection contains zero or more Device objects. Applications can use the various Devices collection methods to access individual Device objects.

Device objects always contain a Services collection that contains one or more Service objects. These service objects are used by applications to communicate with and control devices.

 

 




