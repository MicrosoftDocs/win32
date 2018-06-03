---
title: IOCTL\_STORAGE\_FIRMWARE\_ACTIVATE control code
description: A driver can use IOCTL\_STORAGE\_FIRMWARE\_ACTIVATE to activate a firmware image on a storage device.
ms.assetid: 5604A708-D321-423B-826D-94F4295B4307
keywords:
- IOCTL_STORAGE_FIRMWARE_ACTIVATE control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_FIRMWARE_ACTIVATE
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

# IOCTL\_STORAGE\_FIRMWARE\_ACTIVATE control code

A driver can use **IOCTL\_STORAGE\_FIRMWARE\_ACTIVATE** to activate a firmware image on a storage device.

## Input Buffer

**Irp-&gt;AssociatedIrp.SystemBuffer** contains [**STORAGE\_HW\_FIRMWARE\_ACTIVATE**](storage-hw-firmware-activate.md) data that specifies information about the downloaded firmware to activate.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** indicates the size, in bytes, of the parameter buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**, which must be &gt;= **sizeof**([**STORAGE\_HW\_FIRMWARE\_ACTIVATE**](storage-hw-firmware-activate.md)).

## Output Buffer

This IOCTL has no output structure.

## Output Buffer Length

None.

## Status block

The **Information** field is set to the number of bytes returned. The **Status** field is set to **STATUS\_SUCCESS**, or possibly to **STATUS\_INSUFFICIENT\_RESOURCES**.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Client<br/> | Windows 10<br/>                                                                                      |
| Server<br/> | Windows Server 2016<br/>                                                                             |
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**STORAGE\_HW\_FIRMWARE\_ACTIVATE**](storage-hw-firmware-activate.md)
</dt> <dt>

[**IOCTL\_STORAGE\_FIRMWARE\_DOWNLOAD**](ioctl-storage-firmware-download.md)
</dt> <dt>

[**STORAGE\_HW\_FIRMWARE\_DOWNLOAD**](storage-hw-firmware-download.md)
</dt> <dt>

[**IOCTL\_STORAGE\_FIRMWARE\_GET\_INFO**](ioctl-storage-firmware-get-info.md)
</dt> <dt>

[**STORAGE\_HW\_FIRMWARE\_INFO**](storage-hw-firmware-info.md)
</dt> <dt>

[**STORAGE\_HW\_FIRMWARE\_INFO\_QUERY**](storage-hw-firmware-info-query.md)
</dt> <dt>

[**STORAGE\_HW\_FIRMWARE\_SLOT\_INFO**](storage-hw-firmware-slot-info.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_FIRMWARE_ACTIVATE%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






