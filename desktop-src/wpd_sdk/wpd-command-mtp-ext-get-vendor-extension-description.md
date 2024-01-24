---
description: The WPD\_COMMAND\_MTP\_EXT\_GET\_VENDOR\_EXTENSION\_DESCRIPTION command retrieves the vendor-extension description string. This string is defined by a DeviceInfo dataset.
ms.assetid: 3741fc97-bbe6-41f0-9c0f-fb2f22225fa3
title: WPD_COMMAND_MTP_EXT_GET_VENDOR_EXTENSION_DESCRIPTION Command (WpdMtpExtensions.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WPD\_COMMAND\_MTP\_EXT\_GET\_VENDOR\_EXTENSION\_DESCRIPTION Command

The **WPD\_COMMAND\_MTP\_EXT\_GET\_VENDOR\_EXTENSION\_DESCRIPTION** command retrieves the vendor-extension description string. This string is defined by a **DeviceInfo** dataset.

## Command category

**WPD\_CATEGORY\_MTP\_EXT\_VENDOR\_OPERATIONS**

## Parameters

This command has no parameters.

## Return Value

The driver returns the following results.



| Result                                                      | VarType    | Description                                                  |
|-------------------------------------------------------------|------------|--------------------------------------------------------------|
| **WPD\_PROPERTY\_MTP\_EXT\_VENDOR\_EXTENSION\_DESCRIPTION** | VT\_LPWSTR | Required. Specifies the vendor-extension description string. |



 

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

 

 




