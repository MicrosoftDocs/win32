---
description: This topic describes what you must do to start to create programs that use the Sensor API.
ms.assetid: a8d3228a-5f8b-4850-9e47-5dfb2335e655
title: General Requirements for Application Development (Sensor API)
ms.topic: article
ms.date: 05/31/2018
---

# General Requirements for Application Development (Sensor API)

This topic describes what you must do to start to create programs that use the Sensor API.

To create a Sensor API application, you must install Windows 7 and the Windows 7 Software Development Kit (SDK) on your computer. The following table describes the specific files that you will need.



| File name               | Description                                                                                                 |
|-------------------------|-------------------------------------------------------------------------------------------------------------|
| Sensorsapi.h            | The main header file for the Sensor API. This header file contains the interface definitions.               |
| Sensors.h               | The header file that contains definitions of platform-defined constants.                                    |
| Initguid.h              | The header file that contains definitions for controlling **GUID** initialization.                          |
| FunctionDiscoveryKeys.h | The header file that defines device ID property keys that are required when you connect to logical sensors. |
| Sensorsapi.lib          | A static library that contains **GUID** definitions for the Sensor API.                                     |
| PortableDeviceGuids.lib | A static library that contains **GUID** definitions for Windows Portable Devices objects.                   |



 

Your program may require additional files.

## Supported Operating Systems

Sensor API applications will run on all editions of Windows 7, except for Windows 7 Starter edition.

## Windows Portable Devices Interfaces

The Sensor API uses certain Windows Portable Devices (WPD) objects to encapsulate property keys and values. The following table describes the interfaces for these objects.



| Interface                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [IPortableDeviceValues](/previous-versions//ms740012(v=vs.85))        | This interface provides a convenient way to create a property bag of name/value pairs. Names are represented by **PROPERTYKEY**s and values are represented by **PROPVARIANT**s. <br/> The API uses this interface for setting and retrieving both single values and sets of values. This interface can be retrieved from a method or, if a new object is required, by calling **CoCreateInstance** with CLSID\_PortableDeviceValues.<br/> |
| [IPortableDeviceKeyCollection](/previous-versions//ms739549(v=vs.85)) | This interface contains a collection of **PROPERTYKEY**s. These keys represent property names that can be stored by **IPortableDeviceValues**. The API uses this collection object for setting and retrieving both single property names and sets of property names.<br/> This interface can be retrieved from a method or, if a new object is required, by calling **CoCreateInstance** with CLSID\_PortableDeviceKeyCollection. <br/>    |



 

 

