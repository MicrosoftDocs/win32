---
description: The WPD\_COMMAND\_DEVICE\_HINTS\_GET\_CONTENT\_LOCATION command retrieves the object IDs of folders that can hold an object of a specified type.
ms.assetid: 85de64cc-44ee-4536-b658-49d5936351e4
title: WPD_COMMAND_DEVICE_HINTS_GET_CONTENT_LOCATION Command (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WPD_COMMAND_DEVICE_HINTS_GET_CONTENT_LOCATION
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# WPD\_COMMAND\_DEVICE\_HINTS\_GET\_CONTENT\_LOCATION Command

The **WPD\_COMMAND\_DEVICE\_HINTS\_GET\_CONTENT\_LOCATION** command retrieves the object IDs of folders that can hold an object of a specified type. This command is provided as a faster way for a client to discover where a device stores specific objects than by brute object enumeration.

## Command category

**WPD\_CATEGORY\_DEVICE\_HINTS**

## Parameters

The driver expects the following parameters.



| Parameter                                   | VarType   | Description                                                                                                                                                                                                                                                                                                                                     |
|---------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WPD\_PROPERTY\_DEVICE\_HINTS\_CONTENT\_TYPE | VT\_CLSID | Required. The object type that the caller wishes to find the container for. For example, to find the top-level folders used to hold images on a digital camera, the caller would submit WPD\_CONTENT\_TYPE\_IMAGE. See [Requirements for Objects](requirements-for-objects.md) for a list of object types defined by Windows Portable Devices. |



 

## Return Value

The driver should return the following results.



| Result                                               | VarType     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------------------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_PROPERTY\_DEVICE\_HINTS\_CONTENT\_LOCATIONS** | VT\_UNKNOWN | Required. An [**IPortableDevicePropVariantCollection**](iportabledevicepropvariantcollection.md) of type VT\_LPWSTR values that specify the object IDs of folders containing objects of the type indicated by the calling parameter. If no folders are found, this should be an empty list.The folders indicated by the result may or may not contain objects of other content types. See the [WPD\_FOLDER\_CONTENT\_TYPES\_ALLOWED](miscellaneous-properties.md) property for information on folder restrictions.<br/> |
| **WPD\_PROPERTY\_COMMON\_HRESULT**                   | VT\_ERROR   | Required. An **HRESULT** that indicates success or failure of handling the command. If the caller is making an invalid request, the driver should return **HRESULT\_FROM\_WIN32(ERROR\_NOT\_SUPPORTED)** and is not required to return any other result values. Error codes include [Windows Portable Devices error codes](error-constants.md) or any other appropriate error codes.                                                                                                                                                                            |
| **WPD\_PROPERTY\_COMMON\_DRIVER\_ERROR\_CODE**       | VT\_UI4     | Optional. A driver-specific error code. This is typically only used for driver testing, or if the driver, device, and client are all designed together.                                                                                                                                                                                                                                                                                                                                                                                                          |



 

## Calling Methods

Can only be called directly using [**IPortableDevice::SendCommand**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevice-sendcommand).

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



 

 




