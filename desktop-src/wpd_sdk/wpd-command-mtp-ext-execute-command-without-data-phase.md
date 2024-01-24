---
description: The WPD\_COMMAND\_MTP\_EXT\_EXECUTE\_COMMAND\_WITHOUT\_DATA\_PHASE command sends an MTP command block. There is no subsequent data phase associated with this command.
ms.assetid: 308550d0-1399-4b64-8f8e-dc16d5044086
title: WPD_COMMAND_MTP_EXT_EXECUTE_COMMAND_WITHOUT_DATA_PHASE Command (WpdMtpExtensions.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WPD\_COMMAND\_MTP\_EXT\_EXECUTE\_COMMAND\_WITHOUT\_DATA\_PHASE Command

The **WPD\_COMMAND\_MTP\_EXT\_EXECUTE\_COMMAND\_WITHOUT\_DATA\_PHASE** command sends an MTP command block. There is no subsequent data phase associated with this command.

## Command category

**WPD\_CATEGORY\_MTP\_EXT\_VENDOR\_OPERATIONS**

## Parameters

The driver expects the following parameters.



| Parameter                                      | VarType | Description                                                                                                                   |
|------------------------------------------------|---------|-------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_PROPERTY\_MTP\_EXT\_OPERATION\_CODE**   | VT\_UI4 | Required. Identifies a vendor-extended MTP operation code.                                                                    |
| **WPD\_PROPERTY\_MTP\_EXT\_OPERATION\_PARAMS** | VT\_UI4 | Required. An **IPortableDevicePropVariantCollection**,which identifies the required parameters for the vendor operation code. |



 

## Return Value

The driver returns the following results.



| Result                                        | VarType | Description                                                                                                                    |
|-----------------------------------------------|---------|--------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_PROPERTY\_MTP\_EXT\_RESPONSE\_CODE**   | VT\_UI4 | Required. The response code to the vendor operation code.                                                                      |
| **WPD\_PROPERTY\_MTP\_EXT\_RESPONSE\_PARAMS** | VT\_UI4 | Optional. An **IPortableDevicePropVariantCollection** that identifies any response parameters. This collection might be empty. |



 

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

 

 




