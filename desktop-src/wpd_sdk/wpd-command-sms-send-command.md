---
description: The WPD\_COMMAND\_SMS\_SEND command initiates the sending of a short message service (SMS) message by an SMS functional object.
ms.assetid: 507d3237-f2dd-499c-85e4-3c6857a15f6f
title: WPD_COMMAND_SMS_SEND Command (PortableDevice.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WPD_COMMAND_SMS_SEND
api_type: 
- HeaderDef
api_location: 
- PortableDevice.h
---

# WPD\_COMMAND\_SMS\_SEND Command

The **WPD\_COMMAND\_SMS\_SEND** command initiates the sending of a short message service (SMS) message by an SMS functional object.

## Command category

**WPD\_CATEGORY\_SMS**

## Parameters

The driver expects the following parameters.



| Parameter                              | VarType             | Description                                                                                                                                                                                                                          |
|----------------------------------------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WPD\_PROPERTY\_COMMON\_COMMAND\_TARGET | VT\_LPWSTR          | Required. The object ID of the SMS functional object that should send the message. Different SMS functional objects can have different settings.                                                                                     |
| WPD\_PROPERTY\_SMS\_RECIPIENT          | VT\_LPWSTR          | Required. The URI of the recipient.                                                                                                                                                                                                  |
| WPD\_PROPERTY\_SMS\_MESSAGE\_TYPE      | VT\_UI4             | Required. An [**SMS\_MESSAGE\_TYPES**](sms-message-types.md) enumerator that indicates the type of message (text or binary).                                                                                                        |
| WPD\_PROPERTY\_SMS\_TEXT\_MESSAGE      | VT\_LPWSTR          | Optional. If **WPD\_PROPERTY\_SMS\_MESSAGE\_TYPE** indicates a text message, this is the message string; otherwise, this parameter is not included.                                                                                  |
| WPD\_PROPERTY\_SMS\_BINARY\_MESSAGE    | VT\_VECTOR\|VT\_UI1 | Optional. If **WPD\_PROPERTY\_SMS\_MESSAGE\_TYPE** indicates a binary message, this is a pointer to an array of bytes; otherwise, this parameter is not included. The first DWORD of the value is the length of the array, in bytes. |



 

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

 

 




