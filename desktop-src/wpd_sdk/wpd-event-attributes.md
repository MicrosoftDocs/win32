---
description: For Windows 7, Windows Portable Devices supports the following attributes for events of a device service. These attributes are returned by the IPortableDeviceServiceCapabilities::GetEventAttributes method.
ms.assetid: 2c71c3ec-842b-44f7-b127-5750883b33ba
title: Event Attributes (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Event
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# Event Attributes (PortableDevice.h)

For Windows 7, Windows Portable Devices supports the following attributes for events of a device service. These attributes are returned by the [**IPortableDeviceServiceCapabilities::GetEventAttributes**](/windows/desktop/api/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservicecapabilities-geteventattributes) method.




| Attribute                             | VarType         | Description                                                                                                              |
|---------------------------------------|-----------------|--------------------------------------------------------------------------------------------------------------------------|
| **WPD\_EVENT\_ATTRIBUTE\_NAME**       | **VT\_LPWSTR**  | A string that specifies the script-friendly name of the event. Valid characters are alphanumeric \[a-zA-Z0-9\] and '\_'. |
| **WPD\_EVENT\_ATTRIBUTE\_OPTIONS**    | **VT\_UNKNOWN** | An [**IPortableDeviceValues**](iportabledevicevalues.md) that contains the event options.                               |
| **WPD\_EVENT\_ATTRIBUTE\_PARAMETERS** | **VT\_UNKNOWN** | An [**IPortableDeviceKeyCollection**](iportabledevicekeycollection.md) that contains the event parameters.              |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Properties and Attributes**](properties-and-attributes.md)
</dt> </dl>

 

 




