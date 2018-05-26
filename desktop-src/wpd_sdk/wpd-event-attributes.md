---
Description: For Windows 7, Windows Portable Devices supports the following attributes for events of a device service. These attributes are returned by the IPortableDeviceServiceCapabilitiesGetEventAttributes method.
ms.assetid: 2c71c3ec-842b-44f7-b127-5750883b33ba
title: Event Attributes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Event Attributes

For Windows 7, Windows Portable Devices supports the following attributes for events of a device service. These attributes are returned by the [**IPortableDeviceServiceCapabilities::GetEventAttributes**](/windows/win32/PortableDeviceAPI/nf-portabledeviceapi-iportabledeviceservicecapabilities-geteventattributes?branch=master) method.

## 



| Attribute                             | VarType         | Description                                                                                                              |
|---------------------------------------|-----------------|--------------------------------------------------------------------------------------------------------------------------|
| **WPD\_EVENT\_ATTRIBUTE\_NAME**       | **VT\_LPWSTR**  | A string that specifies the script-friendly name of the event. Valid characters are alphanumeric \[a-zA-Z0-9\] and '\_'. |
| **WPD\_EVENT\_ATTRIBUTE\_OPTIONS**    | **VT\_UNKNOWN** | An [**IPortableDeviceValues**](iportabledevicevalues.md) that contains the event options.                               |
| **WPD\_EVENT\_ATTRIBUTE\_PARAMETERS** | **VT\_UNKNOWN** | An [**IPortableDeviceKeyCollection**](iportabledevicekeycollection.md) that contains the event parameters.              |



 

## Requirements



|                   |                                                                                             |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Properties and Attributes**](properties-and-attributes.md)
</dt> </dl>

 

 




