---
title: IOCTL\_CDROM\_ENABLE\_STREAMING control code
description: Enables or disables CDROM streaming mode on a per-handle basis for raw read and write requests.
ms.assetid: DC31EABA-CE58-4B6F-ADCD-0BF72A92C6AB
keywords:
- IOCTL_CDROM_ENABLE_STREAMING control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_CDROM_ENABLE_STREAMING
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_CDROM\_ENABLE\_STREAMING control code

Enables or disables CDROM streaming mode on a per-handle basis for raw read and write requests.

To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function and specify the **IOCTL\_CDROM\_ENABLE\_STREAMING** I/O control request as the *dwIoControlCode* parameter.

## Input Buffer

[**CDROM\_STREAMING\_CONTROL**](cdrom-streaming-control.md)

## Input Buffer Length

Length of a [**CDROM\_STREAMING\_CONTROL**](cdrom-streaming-control.md).

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

The **Information** field is set to the number of bytes returned.

Because of status code propagation from other APIs, the **Status** field can be set to (but not limited to) the following:

<dl> <dt>

<span id="STATUS_SUCCESS"></span><span id="status_success"></span>STATUS\_SUCCESS
</dt> <dd>

The request completed successfully.

</dd> <dt>

<span id="STATUS_INFO_LENGTH_MISMATCH"></span><span id="status_info_length_mismatch"></span>STATUS\_INFO\_LENGTH\_MISMATCH
</dt> <dd>

The input buffer length is smaller than required.

</dd> <dt>

<span id="STATUS_INVALID_PARAMETER"></span><span id="status_invalid_parameter"></span>STATUS\_INVALID\_PARAMETER
</dt> <dd>

The request type is not one of the four in types defined in the **STREAMING\_CONTROL\_REQUEST\_TYPE** enumeration.

</dd> <dt>

<span id="STATUS_INVALID_HANDLE"></span><span id="status_invalid_handle"></span>STATUS\_INVALID\_HANDLE
</dt> <dd>

Cannot find the file object context in the request.

</dd> <dt>

<span id="STATUS_INVALID_DEVICE_REQUEST"></span><span id="status_invalid_device_request"></span>STATUS\_INVALID\_DEVICE\_REQUEST
</dt> <dd>

The requested streaming mode is not supported.

</dd> </dl>

## Remarks

By default, streaming is disabled for all newly opened raw CDROM handles. A playback application that does not want to use the file system and prefers to work with raw data should open two file handles for the same device: a regular one for file system metadata and a streaming one for real-time files.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Winioctl.h)</dt> </dl> |



## See also

<dl> <dt>

[**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216)
</dt> <dt>

[**CDROM\_STREAMING\_CONTROL**](cdrom-streaming-control.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_CDROM_ENABLE_STREAMING%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






