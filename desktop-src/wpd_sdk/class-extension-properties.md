---
description: Windows Portable Devices supports the following class extension properties.
ms.assetid: 9b8983ba-5824-495d-868f-fd22b98e1954
title: Class Extension Properties (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Class
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# Class Extension Properties

Windows Portable Devices supports the following class extension properties.



| Property                                                                      | VarType         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------------------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_CLASS\_EXTENSION\_OPTIONS\_SUPPORTED\_CONTENT\_TYPES**                 | **VT\_UNKNOWN** | A value that specifies the (superset) list of content types supported by the driver (similar to calling WPD\_COMMAND\_CAPABILITIES\_GET\_SUPPORTED\_CONTENT\_TYPES on **WPD\_FUNCTIONAL\_CATEGORY\_ALL**).                                                                                                                                                                                                                                                                                                                                             |
| **WPD\_CLASS\_EXTENSION\_OPTIONS\_DONT\_REGISTER\_WPD\_DEVICE\_INTERFACE**    | **VT\_BOOL**    | A value that specifies whether the caller wants the WPD class extension library to register the WPD Device Class interface. If this value is true, the caller takes responsibility for registration.<br/> If this value is false, it indicates that the caller expects the class extension library to perform the registration.<br/>Most drivers should allow the class extension library to perform the registration, except where registering the WPD Device Class interface by the class extension library might cause adverse effects. |
| **WPD\_CLASS\_EXTENSION\_OPTIONS\_REGISTER\_WPD\_PRIVATE\_DEVICE\_INTERFACE** | **VT\_BOOL**    | Indicates that the caller wants the WPD class extension library to register the private WPD Device Class interface. This is not recommended for most drivers. It should only be used in cases where the registering of the WPD Device Class interface by the class extension library will cause adverse effects. This option is typically used in conjunction with **WPD\_CLASS\_EXTENSION\_OPTIONS\_DONT\_REGISTER\_WPD\_DEVICE\_INTERFACE** set to **TRUE**                                                                                          |
| **WPD\_CLASS\_EXTENSION\_OPTIONS\_DEVICE\_IDENTIFICATION\_VALUES**            | **VT\_UNKNOWN** | This is an [IPortableDeviceValues](iportabledevicevalues.md) which contains the device identification values (**WPD\_DEVICE\_MANUFACTURER**, **WPD\_DEVICE\_MODEL**, **WPD\_DEVICE\_FIRMWARE\_VERSION** and **WPD\_DEVICE\_FUNCTIONAL\_UNIQUE\_ID**). Include this with other Class Extension options when initializing                                                                                                                                                                                                                               |
| **WPD\_CLASS\_EXTENSION\_OPTIONS\_TRANSPORT\_BANDWIDTH**                      | **VT\_UI4**     | Indicates the theoretical maximum bandwidth of the transport in kilobits per second                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **WPD\_CLASS\_EXTENSION\_OPTIONS\_DEVICE\_IDENTIFICATION\_VALUES**            | **VT\_UNKNOWN** | This is an [IPortableDeviceValues](iportabledevicevalues.md) which contains the device identification values (**WPD\_DEVICE\_MANUFACTURER**, **WPD\_DEVICE\_MODEL**, **WPD\_DEVICE\_FIRMWARE\_VERSION** and **WPD\_DEVICE\_FUNCTIONAL\_UNIQUE\_ID**). Include this with other Class Extension options when initializing.                                                                                                                                                                                                                              |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**WPD Properties and Attributes**](properties-and-attributes.md)
</dt> </dl>

 

 




