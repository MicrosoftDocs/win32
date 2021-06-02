---
description: Windows Portable Devices supports the following miscellaneous properties.
ms.assetid: 0f2a5684-a94f-4a51-8f72-527204e4ebfa
title: Miscellaneous Properties (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Miscellaneous
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# Miscellaneous Properties

Windows Portable Devices supports the following miscellaneous properties.



| Property                                       | VarType         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|------------------------------------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_API\_OPTION\_USE\_CLEAR\_DATA\_STREAM** | **VT\_BOOL**    | A Boolean value that specifies whether the data stream created for data transfer will be clear, that is, DRM is not involved.Clients can set this option by adding it to the object properties passed to [**IPortableDeviceContent::CreateObjectWithPropertiesAndData**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevicecontent-createobjectwithpropertiesanddata).<br/>                                                                                                                                                   |
| **WPD\_SERVICE\_VERSION**                      | **VT\_LPWSTR**  | A string that specifies the implementation version of a given device service.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **WPD\_FOLDER\_CONTENT\_TYPES\_ALLOWED**       | **VT\_UNKNOWN** | A value that specifies the object types that can be direct children of this folder. Child folders can have different capabilities.This property is an [**IPortableDevicePropVariantCollection**](iportabledevicepropvariantcollection.md) holding VT\_CLSID values that specify permitted object types.<br/> For a list of object types defined by Windows Portable Devices, see [Requirements for Objects](requirements-for-objects.md).<br/>                                         |
| **WPD\_FUNCTIONAL\_OBJECT\_CATEGORY**          | **VT\_CLSID**   | A value that specifies the object's functional category.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **WPD\_RENDERING\_INFORMATION\_PROFILES**      | **VT\_UNKNOWN** | An [**IPortableDeviceValuesCollection**](iportabledevicevaluescollection.md) that holds multiple [**IPortableDeviceValues**](iportabledevicevalues.md) interfaces, each of which contains the property settings for a profile that the object supports.                                                                                                                                                                                                                                            |
| **WPD\_OBJECT\_HINT\_LOCATION\_DISPLAY\_NAME** | **VT\_LPWSTR**  | If an object is a hint location, this property indicates the hint-specific name to display to the user instead of the object name.Drivers can specify location hints for various object types. These are preferred storage locations for folders that hold a particular object type. An equivalent would be the My Pictures folder for image files in Windows. If this property does not exist, typically the [WPD\_OBJECT\_NAME](object-properties.md) is used instead.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**WPD Properties and Attributes**](properties-and-attributes.md)
</dt> </dl>

 

 




