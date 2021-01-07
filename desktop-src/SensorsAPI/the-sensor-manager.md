---
description: The sensor manager object provides access to the sensors that are available for your use.
ms.assetid: dd39d533-9983-41b4-a9a3-d94dcadebaac
title: The Sensor Manager Object
ms.topic: article
ms.date: 05/31/2018
---

# The Sensor Manager Object

The sensor manager object provides access to the sensors that are available for your use.

To use the Sensor API, you must first call the COM **CoCreateInstance** method to create an instance of the sensor manager object and retrieve a pointer to its interface, named [**ISensorManager**](/windows/desktop/api/sensorsapi/nn-sensorsapi-isensormanager). The sensor manager maintains the list of available sensors. You can use **ISensorManager** to call methods that retrieve groups of sensors by category or by type, or you can call a method to retrieve a particular sensor by using its unique ID. The sensor manager also enables you to register to receive an event that notifies you when a new sensor has been connected to the platform.

Sometimes, the sensor manager provides a pointer to a sensor, but the user has not enabled the sensor. For example, you can often retrieve values for non-private sensor properties, such as the sensor manufacturer or model, before the user enables the sensor. This information can help you to decide whether to ask the user for permission to use the sensor. You can call [**ISensorManager::RequestPermissions**](/windows/win32/api/sensorsapi/nf-sensorsapi-isensormanager-requestpermissions) to prompt the user to enable a particular sensor or collection of sensors.

## Related topics

<dl> <dt>

[Managing User Permissions](managing-user-permissions.md)
</dt> <dt>

[Requesting User Permissions](requesting-user-permissions.md)
</dt> </dl>

 

 
