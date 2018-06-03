---
title: About the Device Object
description: The Device object is the entry point into the WPD Automation object model, because it programmatically represents a physical device.
ms.assetid: a8e64b13-db88-4abb-a0b0-abe340d0632a
keywords:
- WPD Automation,object model
- WPD Automation,Device object
- WPD Automation,Services properties
- WPD Automation,Storages properties
- WPD Automation,GetServicesByType method
- Windows Portable Devices (WPD),WPD Automation object model
- WPD (Windows Portable Devices),WPD Automation object model
- Device object
- Services properties
- Storages properties
- GetServicesByType
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About the Device Object

The [**Device**](device-object.md) object is the entry point into the WPD Automation object model, because it programmatically represents a physical device.

Through its [**Services**](device-services.md) and [**Storages**](device-storages.md) properties, the **Device** object provides access and enumeration of all the services and storages that are contained in the device. The [**GetServicesByType**](device-getservicesbytype.md) method provides an easy way to access a collection of services that belong to a particular service type.

In addition to these inherent properties, the **Device** object provides access to any properties and events that are defined by the device it represents. A **Device** object is functional only while the physical device that it represents is connected.

For details on how to create a **Device** object, see [Using WPD Automation](using-wpd-automation.md).

## Related topics

<dl> <dt>

[About the WPD Automation Object Model](about-the-wpd-automation-object-model.md)
</dt> <dt>

[**Device Object**](device-object.md)
</dt> <dt>

[Using WPD Automation](using-wpd-automation.md)
</dt> </dl>

 

 




