---
title: IOCTL\_CDROM\_GET\_CONFIGURATION control code
description: Requests feature and profile information from a CD-ROM device.
ms.assetid: '2eb4b5c3-db06-4d21-8937-847734d7ac2f'
keywords: ["IOCTL_CDROM_GET_CONFIGURATION control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_CDROM_GET_CONFIGURATION
api_location:
- ntddcdrm.h
api_type:
- HeaderDef
---

# IOCTL\_CDROM\_GET\_CONFIGURATION control code

Requests feature and profile information from a CD-ROM device.

Multimedia devices have different characteristics depending on the type of media that is in the device. To provide drivers with a means of querying multimedia devices about these varying characteristics, the *SCSI Multimedia - 3* (*MMC-3*) specification defines a command called "GET CONFIGURATION." This command permits drivers to query a device for both permanent information about the device and information that varies whenever the media changes. In Microsoft Windows 2000 and later operating systems, drivers can send this query to a device using the IOCTL\_CDROM\_GET\_CONFIGURATION request.

The IOCTL\_CDROM\_GET\_CONFIGURATION request returns a list of descriptors that describe the capabilities of the device for the current medium. These descriptors are divided into two groups called "feature descriptors" and "profile list descriptors." A feature specifies the capabilities of a device and its associated medium. A profile is a collection of features. If the device supports a profile, it supports all the features in the profile.

See the *MMC-3* specification for further discussion concerning features and profiles.

## Input Buffer

Input buffer.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the IO\_STACK\_LOCATION structure indicates the size, in bytes, of the input buffer, which must be = **sizeof**(GET\_CONFIGURATION\_IOCTL\_INPUT).

## Output Buffer

The driver returns the feature and profile data in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. The data begins with a header of type [**GET\_CONFIGURATION\_HEADER**](get-configuration-header.md). Feature data is reported in the space immediately following this header. Its size and formatting depend on which features are reported.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location indicates the size, in bytes, of the buffer, which must be &gt;= **sizeof**(GET\_CONFIGURATION\_HEADER).

## Status block

The **Information** field is set to the number of bytes that are returned. The **Status** field is set to STATUS\_SUCCESS if the request succeeds. If the **Parameters.DeviceIoControl.InputBufferLength** does not have the correct value, the request fails with a STATUS\_INFO\_LENGTH\_MISMATCH error. If **Parameters.DeviceIoControl.OutputBufferLength** is not large enough, the request fails with a STATUS\_BUFFER\_TOO\_SMALL error. If the value for the output buffer is too large, the request fails a STATUS\_INVALID\_BUFFER\_SIZE message.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdrm.h (include Ntddcdrm.h)</dt> </dl> |



## See also

<dl> <dt>

[**GET\_CONFIGURATION\_IOCTL\_INPUT**](get-configuration-ioctl-input.md)
</dt> <dt>

[**GET\_CONFIGURATION\_HEADER**](get-configuration-header.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_CDROM_GET_CONFIGURATION%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






