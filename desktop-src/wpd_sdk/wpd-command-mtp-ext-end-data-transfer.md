---
description: The WPD\_COMMAND\_MTP\_EXT\_END\_DATA\_TRANSFER command completes a data transfer and read response from the device.
ms.assetid: df2da2e6-ed5a-41a1-be30-844c0d6b409b
title: WPD_COMMAND_MTP_EXT_END_DATA_TRANSFER Command (WpdMtpExtensions.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WPD\_COMMAND\_MTP\_EXT\_END\_DATA\_TRANSFER Command

The **WPD\_COMMAND\_MTP\_EXT\_END\_DATA\_TRANSFER** command completes a data transfer and read response from the device. The transfer is initiated by either the [**WPD\_COMMAND\_MTP\_EXT\_EXECUTE\_COMMAND\_WITH\_DATA\_TO\_READ**](/windows/desktop/wpd_sdk/wpd-command-mtp-ext-execute-command-with-data-to-read) command or the [**WPD\_COMMAND\_MTP\_EXT\_EXECUTE\_COMMAND\_WITH\_DATA\_TO\_WRITE**](/windows/desktop/wpd_sdk/wpd-command-mtp-ext-execute-command-with-data-to-write) command.

## Command category

**WPD\_CATEGORY\_MTP\_EXT\_VENDOR\_OPERATIONS**

## Parameters

The driver expects the following parameters.



| Parameter                                      | VarType    | Description                                                                  |
|------------------------------------------------|------------|------------------------------------------------------------------------------|
| **WPD\_PROPERTY\_MTP\_EXT\_TRANSFER\_CONTEXT** | VT\_LPWSTR | Required. Identifies the context that is returned by an earlier method call. |



 

## Return Value

The driver returns the following results.



| Result                                        | VarType | Description                                                                                                                             |
|-----------------------------------------------|---------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_PROPERTY\_MTP\_EXT\_RESPONSE\_CODE**   | VT\_UI4 | Required.The response code to the vendor operation code.                                                                                |
| **WPD\_PROPERTY\_MTP\_EXT\_RESPONSE\_PARAMS** | VT\_UI4 | Optional. An **IPortableDevicePropVariantCollection** collection that identifies any response parameters. This collection can be empty. |



 

## Calling Methods

Can only be called directly by using [**IPortableDevice::SendCommand**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevice-sendcommand).

## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>WpdMtpExtensions.h</dt> </dl> |



## See also

<dl> <dt>

[Supporting MTP Extensions](supporting-mtp-extensions.md)
</dt> </dl>

 

