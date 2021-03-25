---
description: Retrieves the properties supported by an object.
ms.assetid: 842bd4d6-0824-4597-bb5d-9ef8769055fb
title: WPD_COMMAND_OBJECT_PROPERTIES_GET_SUPPORTED Command (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WPD_COMMAND_OBJECT_PROPERTIES_GET_SUPPORTED
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# WPD\_COMMAND\_OBJECT\_PROPERTIES\_GET\_SUPPORTED Command

The **WPD\_COMMAND\_OBJECT\_PROPERTIES\_GET\_SUPPORTED** command retrieves the properties supported by an object.

## Command Category

**WPD\_CATEGORY\_OBJECT\_PROPERTIES**

## Parameters

The driver expects the following parameter.



| Parameter                                         | VarType        | Description                                                            |
|---------------------------------------------------|----------------|------------------------------------------------------------------------|
| **WPD\_PROPERTY\_OBJECT\_PROPERTIES\_OBJECT\_ID** | **VT\_LPWSTR** | Required. The ID of the object that contains the requested properties. |



 

## Return Value

The driver should return the following results.



| Result                                                | VarType         | Description                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_PROPERTY\_OBJECT\_PROPERTIES\_PROPERTY\_KEYS** | **VT\_UNKNOWN** | Required. An [**IPortableDeviceKeyCollection**](iportabledevicekeycollection.md) interface that specifies all of the supported properties.                                                                                                                                                                                                            |
| **WPD\_PROPERTY\_COMMON\_HRESULT**                    | **VT\_ERROR**   | Required. An **HRESULT** value that indicates overall success or failure. Possible result values include [Windows Portable Devices error codes](error-constants.md). If the caller makes an invalid request, the driver should return **HRESULT\_FROM\_WIN32(ERROR\_NOT\_SUPPORTED)** but is otherwise not required to return any other result value. |
| **WPD\_PROPERTY\_COMMON\_DRIVER\_ERROR\_CODE**        | **VT\_UI4**     | Optional. A driver-specific error code. This is typically used only for driver testing, or if the driver, device, and client are all designed together.                                                                                                                                                                                                |



 

## Requirements



| Requirement | Value |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Commands**](commands.md)
</dt> </dl>

 

 




