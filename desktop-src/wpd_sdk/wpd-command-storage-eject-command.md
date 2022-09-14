---
description: The WPD\_COMMAND\_STORAGE\_EJECT command ejects a storage medium that can be ejected remotely by the computer.
ms.assetid: 38d4dd56-e898-4890-8328-eb2b03cdbd12
title: WPD_COMMAND_STORAGE_EJECT Command (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WPD_COMMAND_STORAGE_EJECT
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# WPD\_COMMAND\_STORAGE\_EJECT Command

The **WPD\_COMMAND\_STORAGE\_EJECT** command ejects a storage medium that can be ejected remotely by the computer.

## Command category

**WPD\_CATEGORY\_STORAGE**

## Parameters

The driver expects the following parameters.



| Parameter                          | VarType    | Description                                             |
|------------------------------------|------------|---------------------------------------------------------|
| WPD\_PROPERTY\_STORAGE\_OBJECT\_ID | VT\_LPWSTR | Required. The object ID of the storage object to eject. |



 

## Return Value

The driver should return the following results.



| Result                                         | VarType   | Description                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_PROPERTY\_COMMON\_HRESULT**             | VT\_ERROR | Required. An **HRESULT** that indicates success or failure to carry out the command. If the caller is making an invalid request, the driver should return **HRESULT\_FROM\_WIN32(ERROR\_NOT\_SUPPORTED)** and is not required to return any other result values. Error codes include [Windows Portable Devices error codes](error-constants.md) or any other appropriate error codes. |
| **WPD\_PROPERTY\_COMMON\_DRIVER\_ERROR\_CODE** | VT\_UI4   | Optional. A driver-specific error code. This is typically only used for driver testing, or if the driver, device, and client are all designed together.                                                                                                                                                                                                                                |



 

## Calling Methods

Can only be called directly using [**IPortableDevice::SendCommand**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevice-sendcommand).

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Commands**](commands.md)
</dt> </dl>

 

 




