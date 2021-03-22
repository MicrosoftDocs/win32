---
description: Windows Portable Devices supports the following resource attribute properties.
ms.assetid: 9b90db8a-e833-48cf-b484-70ac5ac32a76
title: Resource Attribute Properties (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Resource
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# Resource Attribute Properties

Windows Portable Devices supports the following resource attribute properties.



| Property                                    | VarType         | Description                                                                                                                                                               |
|---------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_RESOURCE\_ATTRIBUTE\_RESOURCE\_KEY** | **VT\_UNKNOWN** | This is an [**IPortableDeviceKeyCollection**](iportabledevicekeycollection.md) containing a single value, which is the key identifying the resource.                     |
| **WPD\_RESOURCE\_ATTRIBUTE\_FORMAT**        | **VT\_CLSID**   | A GUID value that specifies the format of the resource. See [Object Formats](object-format-guids.md) for a list of formats that are defined by Windows Portable Devices. |
| **WPD\_RESOURCE\_ATTRIBUTE\_TOTAL\_SIZE**   | **VT\_UI8**     | The total size of the resource data, in bytes.                                                                                                                            |



 

## Remarks

These attributes are returned by the [**IPortableDeviceResources::GetResourceAttributes**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledeviceresources-getresourceattributes) method.

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDeviceResources::GetResourceAttributes**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledeviceresources-getresourceattributes)
</dt> <dt>

[**WPD Properties and Attributes**](properties-and-attributes.md)
</dt> </dl>

 

 




