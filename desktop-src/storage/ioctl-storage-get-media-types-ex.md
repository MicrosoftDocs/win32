---
title: IOCTL\_STORAGE\_GET\_MEDIA\_TYPES\_EX control code
description: Returns information about the types of media supported by a device.
ms.assetid: 706269d8-123b-48c6-83cb-8ae47fb92efc
keywords:
- IOCTL_STORAGE_GET_MEDIA_TYPES_EX control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_GET_MEDIA_TYPES_EX
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_STORAGE\_GET\_MEDIA\_TYPES\_EX control code

Returns information about the types of media supported by a device. A storage class driver must handle this IOCTL to control devices to be accessed by the removable storage manager (RSM) either as stand-alone devices or as data transfer elements (drives) in a media library or changer device.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The driver returns an array of [**DEVICE\_MEDIA\_INFO**](device-media-info.md) structures, one for each media type supported by the device, embedded in a [**GET\_MEDIA\_TYPES**](get-media-types.md) structure in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location indicates the size, in bytes, of the parameter buffer, which must be &gt;= **sizeof(**GET\_MEDIA\_TYPES**)** plus additional device-type-specific data, if any.

## Status block

The **Information** field is set to the number of bytes returned. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_INFO\_LENGTH\_MISMATCH or STATUS\_INSUFFICIENT\_RESOURCES.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**DEVICE\_MEDIA\_INFO**](device-media-info.md)
</dt> <dt>

[**GET\_MEDIA\_TYPES**](get-media-types.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_GET_MEDIA_TYPES_EX%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






