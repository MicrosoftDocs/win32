---
description: Windows Portable Devices (WPD) supports the following properties of command parameters.
ms.assetid: 03eff101-5c36-48ea-9dcd-2c4ee29a2ac6
title: Command Parameters (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Command
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# Command Parameters

Windows Portable Devices (WPD) supports the following properties of command parameters.




| **Property**                                            | **VarType**     | **Description**                                                                                                                                                              |
|---------------------------------------------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_PROPERTY\_COMMON\_CLIENT\_INFORMATION**          | **VT\_UNKNOWN** | An [**IPortableDeviceValues**](iportabledevicevalues.md) interface that the driver uses to identify the client.                                                             |
| **WPD\_PROPERTY\_COMMON\_CLIENT\_INFORMATION\_CONTEXT** | **VT\_LPWSTR**  | A driver-specified context which identifies a client for all subsequent operations.                                                                                          |
| **WPD\_PROPERTY\_COMMON\_COMMAND\_CATEGORY**            | **VT\_CLSID**   | The **GUID** portion of the **PROPERTYKEY** value of the command.                                                                                                            |
| **WPD\_PROPERTY\_COMMON\_COMMAND\_ID**                  | **VT\_UI4**     | The Persistent Unique ID (PID) portion of the **PROPERTYKEY** value of the command.                                                                                          |
| **WPD\_PROPERTY\_COMMON\_COMMAND\_TARGET**              | **VT\_LPWSTR**  | The target-object identifier.                                                                                                                                                |
| **WPD\_PROPERTY\_COMMON\_DRIVER\_ERROR\_CODE**          | **VT\_UI4**     | A driver-specific error code returned by a WPD driver.                                                                                                                       |
| **WPD\_PROPERTY\_COMMON\_HRESULT**                      | **VT\_ERROR**   | The **HRESULT** value returned by a WPD driver for a particular operation.                                                                                                   |
| **WPD\_PROPERTY\_COMMON\_OBJECT\_IDS**                  | **VT\_UNKNOWN** | An [**IPortableDevicePropVariantCollection**](iportabledevicepropvariantcollection.md) interface of variant type **VT\_LPWSTR** that contains a list of object identifiers. |
| **WPD\_PROPERTY\_COMMON\_PERSISTENT\_UNIQUE\_IDS**      | **VT\_UNKNOWN** | An [**IPortableDevicePropVariantCollection**](iportabledevicepropvariantcollection.md) interface of variant type **VT\_LPWSTR** that contains a list of PIDs.               |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Properties and Attributes**](properties-and-attributes.md)
</dt> </dl>

 

 




