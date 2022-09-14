---
title: Sensor Platform
description: Windows 7 has changed how developers use sensors.
ms.assetid: ed323658-dfd6-4c1b-ada2-5d68ebb56482
ms.topic: article
ms.date: 05/31/2018
---

# Sensor Platform

Windows 7 has changed how developers use sensors. It includes native support for sensors, expanded by a new development platform for working with sensors, including location sensors, such as Global Positioning Systems (GPS) devices.

Built on the Sensor Platform, the *Windows Location*APIs are a new Windows 7 feature that enables application developers to access the user's physical location information. The *Windows Location*APIs can abstract hardware, simultaneously support multiple applications, and seamlessly switch between different technologies, relieving the application developer of the burden of managing these constraints. The *Location*APIs can be used by programmers through the C++ programming language (by programmers familiar with Component Object Model (COM)), or by using COM objects in scripting languages, such as Microsoft JScript. Scripting support gives easy access to location data for projects such as gadgets.

Windows 7 provides a solid, easy-to-use platform for using sensor devices, such as an ambient light sensor or a temperature gauge, to create environmental awareness in Windows applications. PCs can use sensors that are built into the computer, connected through wired or wireless connections, or connected through a network or the *Internet*.

The *Sensor* and *Location*APIs provide a standard way to discover sensors, and to programmatically access data that sensors provide.

The *Sensor* control panel lets users enable or disable sensors, control access to sensors that might expose sensitive data, view sensor properties, and change the descriptions of sensors.

The [Sensor Class Extension](/windows-hardware/drivers/sensors/about-the-sensor-class-extension) is a core part of the driver development model for the Sensor Platform. It provides the following mechanisms, which are used when writing a [User-Mode Driver Framework (UMDF)](https://developer.microsoft.com/windows/hardware) sensor driver:

-   Integration with the Sensor Platform
-   Security enforcement

## Related topics

<dl> <dt>

[Sensor API](../sensorsapi/portal.md)
</dt> <dt>