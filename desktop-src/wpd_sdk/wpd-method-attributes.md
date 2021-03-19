---
description: For Windows 7, Windows Portable Devices supports the following attributes for methods of a device service. These attributes are returned by the IPortableDeviceServiceCapabilities::GetMethodAttributes method.
ms.assetid: b920e037-7737-4a18-b4f1-5c59e0a857dd
title: Method Attributes (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Method
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# Method Attributes

For Windows 7, Windows Portable Devices supports the following attributes for methods of a device service. These attributes are returned by the [**IPortableDeviceServiceCapabilities::GetMethodAttributes**](/windows/desktop/api/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservicecapabilities-getmethodattributes) method.




| Attribute                                      | VarType         | Description                                                                                                               |
|------------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------|
| **WPD\_METHOD\_ATTRIBUTE\_ACCESS**             | **VT\_CLSID**   | The required method access.                                                                                               |
| **WPD\_METHOD\_ATTRIBUTE\_ASSOCIATED\_FORMAT** | **VT\_CLSID**   | The format associated with the method, or **GUID\_NULL** if there is no associated format.                                |
| **WPD\_METHOD\_ATTRIBUTE\_NAME**               | **VT\_LPWSTR**  | A string that specifies the script-friendly name of the method. Valid characters are alphanumeric \[a-zA-Z0-9\] and '\_'. |
| **WPD\_METHOD\_ATTRIBUTE\_PARAMETERS**         | **VT\_UNKNOWN** | An [**IPortableDeviceKeyCollection**](iportabledevicekeycollection.md) interface that contains the method parameters.    |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Properties and Attributes**](properties-and-attributes.md)
</dt> </dl>

 

 




