---
Description: 'The WPD\_COMMAND\_STORAGE\_FORMAT command formats a storage functional object on the device.'
ms.assetid: '5dc06ed3-791f-4c6b-9fb3-42452e948e0d'
title: 'WPD\_COMMAND\_STORAGE\_FORMAT Command'
---

# WPD\_COMMAND\_STORAGE\_FORMAT Command

The **WPD\_COMMAND\_STORAGE\_FORMAT** command formats a storage functional object on the device.

## Command category

**WPD\_CATEGORY\_STORAGE**

## Parameters

The driver expects the following parameters.



| Parameter                          | VarType    | Description                                              |
|------------------------------------|------------|----------------------------------------------------------|
| WPD\_PROPERTY\_STORAGE\_OBJECT\_ID | VT\_LPWSTR | Required. The object ID of the storage medium to format. |



 

## Return Value

The driver should return the following results.



| Result                                         | VarType   | Description                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_PROPERTY\_COMMON\_HRESULT**             | VT\_ERROR | Required. An **HRESULT** that indicates success or failure to carry out the command. If the caller is making an invalid request, the driver should return **HRESULT\_FROM\_WIN32(ERROR\_NOT\_SUPPORTED)** and is not required to return any other result values. Error codes include [Windows Portable Devices error codes](error-constants.md) or any other appropriate error codes. |
| **WPD\_PROPERTY\_COMMON\_DRIVER\_ERROR\_CODE** | VT\_UI4   | Optional. A driver-specific error code. This is typically only used for driver testing, or if the driver, device, and client are all designed together.                                                                                                                                                                                                                                |



 

## Calling Methods

Can only be called directly using [**IPortableDevice::SendCommand**](iportabledevice-sendcommand.md).

## Requirements



|                   |                                                                                             |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Commands**](commands.md)
</dt> </dl>

 

 




