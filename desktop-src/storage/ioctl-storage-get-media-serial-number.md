---
title: IOCTL\_STORAGE\_GET\_MEDIA\_SERIAL\_NUMBER control code
description: Queries the USB generic parent driver for the serial number of a USB device.
ms.assetid: 'aa903b7e-e844-466e-85b1-33fe6ba40689'
keywords: ["IOCTL_STORAGE_GET_MEDIA_SERIAL_NUMBER control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_GET_MEDIA_SERIAL_NUMBER
api_location:
- Ntddstor.h
api_type:
- HeaderDef
---

# IOCTL\_STORAGE\_GET\_MEDIA\_SERIAL\_NUMBER control code

Queries the USB generic parent driver for the serial number of a USB device. If a USB device has a CSM-1 content security interface, a USB client driver can query for its serial number using this request. USB client drivers that help implement a digital rights management (DRM) system can use this information to ensure that only legitimate customers have access to digitized intellectual property.

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The driver returns the serial number of the indicated device in a structure of type [**MEDIA\_SERIAL\_NUMBER\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff562213) in the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location of the IRP indicates the size, in bytes, of the buffer, which must be at least **sizeof**(MEDIA\_SERIAL\_NUMBER\_DATA).

## Status block

The **Information** field is set to the size, in bytes, of the returned data. The **Status** field can be set to STATUS\_SUCCESS, or possibly to STATUS\_INVALID\_BUFFER\_SIZE or STATUS\_INSUFFICIENT\_RESOURCES.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**MEDIA\_SERIAL\_NUMBER\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff562213)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_GET_MEDIA_SERIAL_NUMBER%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






