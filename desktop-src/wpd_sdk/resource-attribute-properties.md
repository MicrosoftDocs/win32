---
Description: Windows Portable Devices supports the following resource attribute properties.
ms.assetid: 9b90db8a-e833-48cf-b484-70ac5ac32a76
title: Resource Attribute Properties
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Resource Attribute Properties

Windows Portable Devices supports the following resource attribute properties.



| Property                                    | VarType         | Description                                                                                                                                                               |
|---------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_RESOURCE\_ATTRIBUTE\_RESOURCE\_KEY** | **VT\_UNKNOWN** | This is an [**IPortableDeviceKeyCollection**](iportabledevicekeycollection.md) containing a single value, which is the key identifying the resource.                     |
| **WPD\_RESOURCE\_ATTRIBUTE\_FORMAT**        | **VT\_CLSID**   | A GUID value that specifies the format of the resource. See [Object Formats](object-format-guids.md) for a list of formats that are defined by Windows Portable Devices. |
| **WPD\_RESOURCE\_ATTRIBUTE\_TOTAL\_SIZE**   | **VT\_UI8**     | The total size of the resource data, in bytes.                                                                                                                            |



 

## Remarks

These attributes are returned by the [**IPortableDeviceResources::GetResourceAttributes**](/windows/win32/PortableDeviceApi/nf-portabledeviceapi-iportabledeviceresources-getresourceattributes?branch=master) method.

## Requirements



|                   |                                                                                             |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDeviceResources::GetResourceAttributes**](/windows/win32/PortableDeviceApi/nf-portabledeviceapi-iportabledeviceresources-getresourceattributes?branch=master)
</dt> <dt>

[**WPD Properties and Attributes**](properties-and-attributes.md)
</dt> </dl>

 

 




