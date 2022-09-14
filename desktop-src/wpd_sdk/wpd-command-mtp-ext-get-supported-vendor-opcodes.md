---
description: The WPD\_COMMAND\_MTP\_EXT\_GET\_SUPPORTED\_VENDOR\_OPCODES command sends an MTP command block. There is no subsequent data phase associated with this command.
ms.assetid: 397ae29c-f81c-410e-9670-db69c099a321
title: WPD_COMMAND_MTP_EXT_GET_SUPPORTED_VENDOR_OPCODES Command (WpdMtpExtensions.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WPD\_COMMAND\_MTP\_EXT\_GET\_SUPPORTED\_VENDOR\_OPCODES Command

The **WPD\_COMMAND\_MTP\_EXT\_GET\_SUPPORTED\_VENDOR\_OPCODES** command sends an MTP command block. There is no subsequent data phase associated with this command.

## Command category

**WPD\_CATEGORY\_MTP\_EXT\_VENDOR\_OPERATIONS**

## Parameters

This command has no parameters.

## Return Value

The driver returns the following results.



| Result                                                | VarType | Description                                                                                              |
|-------------------------------------------------------|---------|----------------------------------------------------------------------------------------------------------|
| **WPD\_PROPERTY\_MTP\_EXT\_VENDOR\_OPERATION\_CODES** | VT\_UI4 | Required. An **IPortableDevicePropVariantCollection** that contains all vendor-extended operation codes. |



 

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

 

 




