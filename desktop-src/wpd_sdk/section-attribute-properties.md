---
description: Windows Portable Devices supports the following section data properties.
ms.assetid: 8760d963-fc07-4b54-aa24-5725f4b95ed2
title: Section Attribute Properties (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Section
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# Section Attribute Properties

Windows Portable Devices supports the following section data properties.



| Property                                             | VarType         | Description                                                                                                                                                                                                                                                                                                                                 |
|------------------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_SECTION\_DATA\_LENGTH**                       | **VT\_UI8**     | Specifies the length of the referenced object.                                                                                                                                                                                                                                                                                              |
| **WPD\_SECTION\_DATA\_OFFSET**                       | **VT\_UI8**     | Specifies the zero-based offset of the data for the referenced object.                                                                                                                                                                                                                                                                      |
| **WPD\_SECTION\_DATA\_REFERENCED\_OBJECT\_RESOURCE** | **VT\_UNKNOWN** | An [**IPortableDeviceKeyCollection**](iportabledevicekeycollection.md) containing a single value that specifies the key for a given resource.This resource is the object referenced by WPD\_SECTION\_DATA\_OFFSET and WPD\_SECTION\_DATA\_LENGTH.<br/> If this property doesn't exist, WPD\_RESOURCE\_DEFAULT is assumed.<br/> |
| **WPD\_SECTION\_DATA\_UNITS**                        | **VT\_UI4**     | Specifies the units used for this offset, for example, bytes, milliseconds, and so on.The possible values for this property are defined in the **WPD\_SECTION\_DATA\_UNITS\_VALUES** enumeration in the file PortableDevice.h.<br/> If no units are specified, bytes are assumed.<br/>                                          |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**WPD Properties and Attributes**](properties-and-attributes.md)
</dt> </dl>

 

 




