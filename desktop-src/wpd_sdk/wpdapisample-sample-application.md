---
title: WpdApiSample sample app
description: WpdApiSample sample app
ms.assetid: 854a6304-5d62-4f00-9366-8c2244568250
ms.topic: sample
ms.date: 09/04/2024
---

# WpdApiSample sample app

The [WPD API sample](/samples/microsoft/windows-classic-samples/wpd-sample/) sample application is a command-line desktop application that enables you to enumerate connected devices, explore devices, query objects for properties and attributes, send and retrieve objects, and so on. On startup, the application opens a command window that lists the tasks you can perform.

The **WPD API sample** sample application includes the following files:

| **File** | **Description** |
|-|-|
| ContentEnumeration.cpp | Contains functions that enumerate all the objects on a device. |
| ContentProperties.cpp | Contains functions that read and write object properties and make bulk property set/get requests. |
| ContentTransfer.cpp | Contains functions that transfer content to or from the device, read object type requirements, and create a folder on the device. |
| DeviceCapabilities.cpp | Contains functions to list the functional object types on the device, list the content types supported by each functional object type, and display rendering object profiles. |
| DeviceEnumeration.cpp | Lists the friendly names, manufacturers, and descriptions of all connected devices. |
| DeviceEvents.cpp | Contains functions that log device events and their parameters whenever events are fired. |
| Stdafx.cpp | Includes the standard files. |
| WpdApiSample.cpp | Hosts the **\_tmain** startup function, which calls the local **DoMenu** function, which displays a list of available devices and tasks and calls the function appropriate for the user's menu selection. |

## Related topics

* [WPD sample apps](./sample.md)
