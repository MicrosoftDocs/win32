---
Description: The WPD\_COMMAND\_MTP\_EXT\_EXECUTE\_COMMAND\_WITH\_DATA\_TO\_WRITE command sends an MTP command block, which is followed by a data phase. The data is sent from the host to the device.
ms.assetid: b675fc3c-4d50-429d-9e00-42160d409a2b
title: WPD\_COMMAND\_MTP\_EXT\_EXECUTE\_COMMAND\_WITH\_DATA\_TO\_WRITE Command
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WPD\_COMMAND\_MTP\_EXT\_EXECUTE\_COMMAND\_WITH\_DATA\_TO\_WRITE Command

The **WPD\_COMMAND\_MTP\_EXT\_EXECUTE\_COMMAND\_WITH\_DATA\_TO\_WRITE** command sends an MTP command block, which is followed by a data phase. The data is sent from the host to the device.

## Command category

**WPD\_CATEGORY\_MTP\_EXT\_VENDOR\_OPERATIONS**

## Parameters

The driver expects the following parameters.



| Parameter                                                | VarType | Description                                                                                                                             |
|----------------------------------------------------------|---------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **WPD\_PROPERTY\_MTP\_EXT\_OPERATION\_CODE**             | VT\_UI4 | Required. Identifies a vendor-extended MTP operation code.                                                                              |
| **WPD\_PROPERTY\_MTP\_EXT\_OPERATION\_PARAMS**           | VT\_UI4 | Required. An **IPortableDevicePropVariantCollection** collection that identifies the required parameters for the vendor operation code. |
| **WPD\_PROPERTY\_MTP\_EXT\_TRANSFER\_TOTAL\_DATA\_SIZE** | VT\_UI8 | Required.Specifies the total data size, in bytes, excluding any overhead, to be sent to device.                                         |



 

## Return Value

The driver returns the following results.



| Result                                                       | VarType    | Description                                                                        |
|--------------------------------------------------------------|------------|------------------------------------------------------------------------------------|
| **WPD\_PROPERTY\_MTP\_EXT\_OPTIMAL\_TRANSFER\_BUFFER\_SIZE** | VT\_UI4    | Required. Specifies the optimal size of the transfer buffer.                       |
| **WPD\_PROPERTY\_MTP\_EXT\_TRANSFER\_CONTEXT**               | VT\_LPWSTR | Optional. A context identifier that the driver uses for subsequent data transfers. |



 

## Calling Methods

Can only be called directly by using [**IPortableDevice::SendCommand**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevice-sendcommand).

## Requirements



|                   |                                                                                               |
|-------------------|-----------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>WpdMtpExtensions.h</dt> </dl> |



## See also

<dl> <dt>

[Supporting MTP Extensions](supporting-mtp-extensions.md)
</dt> </dl>

 

 




