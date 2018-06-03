---
title: IOCTL\_CDROM\_GET\_PERFORMANCE control code
description: Retrieves the supported speeds from the device. The IOCTL\_CDROM\_GET\_PERFORMANCE I/O control request is a wrapper over the MMC command, GET PERFORMANCE.
ms.assetid: 3BA2D85A-052B-4851-B31C-072F2872F3FE
keywords:
- IOCTL_CDROM_GET_PERFORMANCE control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_CDROM_GET_PERFORMANCE
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_CDROM\_GET\_PERFORMANCE control code

Retrieves the supported speeds from the device. The **IOCTL\_CDROM\_GET\_PERFORMANCE** I/O control request is a wrapper over the MMC command, GET PERFORMANCE.

To perform this operation, call the [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) function with **IOCTL\_CDROM\_GET\_PERFORMANCE** as the *dwIoControlCode* parameter.

## Input Buffer

[**CDROM\_PERFORMANCE\_REQUEST**](cdrom-performance-request.md) requests performance data. [**CDROM\_WRITE\_SPEED\_REQUEST**](cdrom-write-speed-request.md) requests write speed descriptor.

## Input Buffer Length

Length of a [**CDROM\_PERFORMANCE\_REQUEST**](cdrom-performance-request.md).

## Output Buffer

For request type CdromWriteSpeedRequest, this IOCTL returns the [**CDROM\_PERFORMANCE\_HEADER**](cdrom-performance-header.md) structure followed by a number of CDROM\_WRITE\_SPEED\_DESCRIPTOR descriptors.

For request type CdromPerformanceRequest, this IOCTL returns the [**CDROM\_PERFORMANCE\_HEADER**](cdrom-performance-header.md) structure followed by an optional descriptor. The descriptor following this header depends on the value in the **Except** field of the **CDROM\_PERFORMANCE\_HEADER** structure. If **Except** is false, CDROM\_NOMINAL\_PERFORMANCE\_DESCRIPTOR is used; otherwise, CDROM\_EXCEPTION\_PERFORMANCE\_DESCRIPTOR is used.

## Output Buffer Length

Length of a [**CDROM\_PERFORMANCE\_HEADER**](cdrom-performance-header.md).

## Status block

The **Information** field is set to the number of bytes returned.

Because of status code propagation from other APIs, the **Status** field can be set to (but is not limited to) the following:

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

The CDROM\_PERFORMANCE\_REQUEST header does not contain a valid combination of parameters specified by enumerations.

</dd> <dt>

<span id="STATUS_BUFFER_TOO_SMALL"></span><span id="status_buffer_too_small"></span>STATUS\_BUFFER\_TOO\_SMALL
</dt> <dd>

The output buffer length is smaller than required.

</dd> <dt>

<span id="STATUS_INVALID_DEVICE_REQUEST"></span><span id="status_invalid_device_request"></span>STATUS\_INVALID\_DEVICE\_REQUEST
</dt> <dd>

The device does not support this request.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Winioctl.h)</dt> </dl> |



## See also

<dl> <dt>

[**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216)
</dt> <dt>

[**CDROM\_PERFORMANCE\_REQUEST**](cdrom-performance-request.md)
</dt> <dt>

[**CDROM\_WRITE\_SPEED\_REQUEST**](cdrom-write-speed-request.md)
</dt> <dt>

[**CDROM\_PERFORMANCE\_HEADER**](cdrom-performance-header.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_CDROM_GET_PERFORMANCE%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






