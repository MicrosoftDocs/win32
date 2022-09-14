---
description: The WPD\_COMMAND\_MTP\_EXT\_READ\_DATA command retrieves data from the device after the WPD\_COMMAND\_MTP\_EXT\_EXECUTE\_COMMAND\_WITH\_DATA\_TO\_READ command is run.
ms.assetid: d7acb2cc-28b0-4314-99fd-4e7eded22122
title: WPD_COMMAND_MTP_EXT_READ_DATA Command (WpdMtpExtensions.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WPD\_COMMAND\_MTP\_EXT\_READ\_DATA Command

The **WPD\_COMMAND\_MTP\_EXT\_READ\_DATA** command retrieves data from the device after the **WPD\_COMMAND\_MTP\_EXT\_EXECUTE\_COMMAND\_WITH\_DATA\_TO\_READ** command is run.

## Command category

**WPD\_CATEGORY\_MTP\_EXT\_VENDOR\_OPERATIONS**

## Parameters

The driver expects the following parameters.



| Parameter                                                   | VarType             | Description                                                                            |
|-------------------------------------------------------------|---------------------|----------------------------------------------------------------------------------------|
| **WPD\_PROPERTY\_MTP\_EXT\_TRANSFER\_CONTEXT**              | VT\_LPWSTR          | Required. Identifies the context that was returned by the previous call to the device. |
| **WPD\_PROPERTY\_MTP\_EXT\_TRANSFER\_NUM\_BYTES\_TO\_READ** | VT\_UI4             | Required. Specifies the number of bytes to read.                                       |
| **WPD\_PROPERTY\_MTP\_EXT\_TRANSFER\_DATA**                 | VT\_VECTOR\|VT\_UI1 | Required. Identifies the buffer into which the device data is copied.                  |



 

## Return Value

The driver returns the following results.



| Result                                                  | VarType             | Description                                                       |
|---------------------------------------------------------|---------------------|-------------------------------------------------------------------|
| **WPD\_PROPERTY\_MTP\_EXT\_TRANSFER\_NUM\_BYTES\_READ** | VT\_UI4             | Required. Specifies the number of bytes received from the device. |
| **WPD\_PROPERTY\_MTP\_EXT\_TRANSFER\_DATA**             | VT\_VECTOR\|VT\_UI1 | Required. The buffer that contains the device data.               |



 

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

 

 




