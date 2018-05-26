---
Description: The WPD\_COMMAND\_COMMON\_RESET\_DEVICE command resets the device. This does not mean reformatting; it is equivalent to turning the device off and on again.
ms.assetid: 7a630cc9-02ea-46be-9645-8a0306606139
title: WPD\_COMMAND\_COMMON\_RESET\_DEVICE Command
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WPD\_COMMAND\_COMMON\_RESET\_DEVICE Command

The **WPD\_COMMAND\_COMMON\_RESET\_DEVICE** command resets the device. This does not mean reformatting; it is equivalent to turning the device off and on again.

## Command category

**WPD\_CATEGORY\_COMMON**

## Parameters

This command has no parameters.

## Return Value

The driver should return the following results.



| Result                                         | VarType   | Description                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_PROPERTY\_COMMON\_HRESULT**             | VT\_ERROR | Required. An **HRESULT** that indicates success or failure to carry out the command. If the caller is making an invalid request, the driver should return **HRESULT\_FROM\_WIN32(ERROR\_NOT\_SUPPORTED)** and is not required to return any other result values. Error codes include [Windows Portable Devices error codes](error-constants.md) or any other appropriate error codes. |
| **WPD\_PROPERTY\_COMMON\_DRIVER\_ERROR\_CODE** | VT\_UI4   | Optional. A driver-specific error code. This is typically only used for driver testing, or if the driver, device, and client are all designed together.                                                                                                                                                                                                                                |



 

## Calling Methods

Can only be called directly using [**IPortableDevice::SendCommand**](/windows/win32/PortableDeviceApi/nf-portabledeviceapi-iportabledevice-sendcommand?branch=master).

## Requirements



|                   |                                                                                             |
|-------------------|---------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>PortableDevice.h</dt> </dl> |



## See also

<dl> <dt>

[**Commands**](commands.md)
</dt> </dl>

 

 




