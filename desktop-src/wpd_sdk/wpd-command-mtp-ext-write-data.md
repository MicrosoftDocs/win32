---
description: The WPD\_COMMAND\_MTP\_EXT\_WRITE\_DATA command sends data to the device after the WPD\_COMMAND\_MTP\_EXT\_EXECUTE\_COMMAND\_WITH\_DATA\_TO\_WRITE command is run.
ms.assetid: 96e7164c-17e7-427b-a0fd-4bfbb8215295
title: WPD_COMMAND_MTP_EXT_WRITE_DATA Command (WpdMtpExtensions.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WPD\_COMMAND\_MTP\_EXT\_WRITE\_DATA Command

The **WPD\_COMMAND\_MTP\_EXT\_WRITE\_DATA** command sends data to the device after the **WPD\_COMMAND\_MTP\_EXT\_EXECUTE\_COMMAND\_WITH\_DATA\_TO\_WRITE** command is run.

## Command category

**WPD\_CATEGORY\_MTP\_EXT\_VENDOR\_OPERATIONS**

## Parameters

The driver expects the following parameters.



| Parameter                                                    | VarType             | Description                                                                            |
|--------------------------------------------------------------|---------------------|----------------------------------------------------------------------------------------|
| **WPD\_PROPERTY\_MTP\_EXT\_TRANSFER\_CONTEXT**               | VT\_LPWSTR          | Required. Identifies the context that was returned by the previous call to the device. |
| **WPD\_PROPERTY\_MTP\_EXT\_TRANSFER\_NUM\_BYTES\_TO\_WRITE** | VT\_UI4             | Required. Specifies the number of bytes to write.                                      |
| **WPD\_PROPERTY\_MTP\_EXT\_TRANSFER\_DATA**                  | VT\_VECTOR\|VT\_UI1 | Required. Identifies the buffer into which the device data is copied.                  |



 

## Return Value

The driver returns the following results.



| Result                                                     | VarType | Description                                                  |
|------------------------------------------------------------|---------|--------------------------------------------------------------|
| **WPD\_PROPERTY\_MTP\_EXT\_TRANSFER\_NUM\_BYTES\_WRITTEN** | VT\_UI4 | Required. Specifies the number of bytes sent to the device.. |



 

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

 

 




