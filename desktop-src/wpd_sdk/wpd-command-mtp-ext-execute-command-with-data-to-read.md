---
description: The WPD\_COMMAND\_MTP\_EXT\_EXECUTE\_COMMAND\_WITH\_DATA\_TO\_READ command sends an MTP command block, which will be followed by a data phase. (The data is sent from the device to the host.).
ms.assetid: 7a76a601-c051-4c0c-bfeb-24e9dddcb9e0
title: WPD_COMMAND_MTP_EXT_EXECUTE_COMMAND_WITH_DATA_TO_READ Command (WpdMtpExtensions.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WPD\_COMMAND\_MTP\_EXT\_EXECUTE\_COMMAND\_WITH\_DATA\_TO\_READ Command

The **WPD\_COMMAND\_MTP\_EXT\_EXECUTE\_COMMAND\_WITH\_DATA\_TO\_READ** command sends an MTP command block, which will be followed by a data phase. (The data is sent from the device to the host.)

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



| Result                                                       | VarType    | Description                                                                                                                                                                                                                         |
|--------------------------------------------------------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_PROPERTY\_MTP\_EXT\_TRANSFER\_TOTAL\_DATA\_SIZE**     | VT\_UI8    | Required. Returns the total data size, in bytes, excluding any overhead coming from the device. If the device reports unknown datasize (0xFFFFFFFF), the driver should call **ReadData** repeatedly until a short chunk is received |
| **WPD\_PROPERTY\_MTP\_EXT\_OPTIMAL\_TRANSFER\_BUFFER\_SIZE** | VT\_UI4    | Optional. Returns the optimal size of the transfer buffer.                                                                                                                                                                          |
| **WPD\_PROPERTY\_MTP\_EXT\_TRANSFER\_CONTEXT**               | VT\_LPWSTR | Required. Specifies the context identifier for subsequent data transfers.                                                                                                                                                           |



 

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

 

 




