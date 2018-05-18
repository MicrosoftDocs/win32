---
title: IOCTL\_STORAGE\_FIRMWARE\_GET\_INFO control code
description: A driver can use IOCTL\_STORAGE\_FIRMWARE\_GET\_INFO to query a storage device for detailed firmware information.
ms.assetid: 'AB5FA3A5-1187-4925-9EC0-62870851AED1'
keywords: ["IOCTL_STORAGE_FIRMWARE_GET_INFO control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_STORAGE_FIRMWARE_GET_INFO
api_location:
- Ntddstor.h
api_type:
- HeaderDef
---

# IOCTL\_STORAGE\_FIRMWARE\_GET\_INFO control code

A driver can use **IOCTL\_STORAGE\_FIRMWARE\_GET\_INFO** to query a storage device for detailed firmware information. A successful call will return information about firmware revisions, activity status, as well as read/write attributes for each slot. The amount of data returned will vary based on storage protocol.

## Input Buffer

**Parameters.DeviceIoControl.InputBufferLength** indicates the size, in bytes, of the parameter buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**, which must be &gt;= **sizeof**([**STORAGE\_HW\_FIRMWARE\_INFO\_QUERY**](storage-hw-firmware-info-query.md)).

**Irp-&gt;AssociatedIrp.SystemBuffer** contains [**STORAGE\_HW\_FIRMWARE\_INFO\_QUERY**](storage-hw-firmware-info-query.md) data that specifies the target of the request.

**Parameters.DeviceIoControl.OutputBufferLength** indicates the number of bytes that can be written to **Irp-&gt;AssociatedIrp.SystemBuffer**. **OutputBufferLength** must be **sizeof**([**STORAGE\_HW\_FIRMWARE\_INFO**](storage-hw-firmware-info.md)) + **sizeof**([**STORAGE\_HW\_FIRMWARE\_SLOT\_INFO**](storage-hw-firmware-slot-info.md)) \* (**STORAGE\_HW\_FIRMWARE\_INFO.SlotCount** -1).

## Input Buffer Length

The length of .

## Output Buffer

The driver returns query data to the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**. The output buffer should contain a [**STORAGE\_HW\_FIRMWARE\_INFO**](storage-hw-firmware-info.md) and [**STORAGE\_HW\_FIRMWARE\_SLOT\_INFO**](storage-hw-firmware-slot-info.md) structure for each slot on the device.

## Output Buffer Length

The length of .

## Status block

The **Information** field is set to the number of bytes returned. The **Status** field is set to STATUS\_SUCCESS, or possibly to STATUS\_INVALID\_DEVICE\_REQUEST, STATUS\_INVALID\_PARAMETER, or STATUS\_NOT\_SUPPORTED.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Client<br/> | Windows 10<br/>                                                                                      |
| Server<br/> | Windows Server 2016<br/>                                                                             |
| Header<br/> | <dl> <dt>Ntddstor.h (include Ntddstor.h)</dt> </dl> |



## See also

<dl> <dt>

[**STORAGE\_HW\_FIRMWARE\_INFO**](storage-hw-firmware-info.md)
</dt> <dt>

[**STORAGE\_HW\_FIRMWARE\_INFO\_QUERY**](storage-hw-firmware-info-query.md)
</dt> <dt>

[**STORAGE\_HW\_FIRMWARE\_SLOT\_INFO**](storage-hw-firmware-slot-info.md)
</dt> <dt>

[**IOCTL\_STORAGE\_FIRMWARE\_ACTIVATE**](ioctl-storage-firmware-activate.md)
</dt> <dt>

[**STORAGE\_HW\_FIRMWARE\_ACTIVATE**](storage-hw-firmware-activate.md)
</dt> <dt>

[**IOCTL\_STORAGE\_FIRMWARE\_DOWNLOAD**](ioctl-storage-firmware-download.md)
</dt> <dt>

[**STORAGE\_HW\_FIRMWARE\_DOWNLOAD**](storage-hw-firmware-download.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_STORAGE_FIRMWARE_GET_INFO%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






