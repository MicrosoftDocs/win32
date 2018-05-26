---
title: IOCTL\_SCSI\_GET\_INQUIRY\_DATA control code
description: Returns the SCSI inquiry data for all devices on a given SCSI host bus adapter (HBA).
ms.assetid: a429061b-ede6-48b1-9fc6-e85e4a7c0dfe
keywords:
- IOCTL_SCSI_GET_INQUIRY_DATA control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_SCSI_GET_INQUIRY_DATA
api_location:
- Ntddscsi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_SCSI\_GET\_INQUIRY\_DATA control code

Returns the SCSI inquiry data for all devices on a given SCSI host bus adapter (HBA). If the IOCTL is employed in user space, the program must have opened a handle to the HBA, which can be enumerated by various means, such as SetupDixxx calls. You can use [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) to find information about a specific device on the HBA. To determine the size of the output buffer that is required, the caller should send this IOCTL request in a loop. Every time that the storage stack rejects the IOCTL with an error message that indicates that the buffer was too small, the caller should double the buffer size.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains the returned inquiry data. For a description of the layout of the inquiry data in the output buffer, see [**SCSI\_ADAPTER\_BUS\_INFO**](scsi-adapter-bus-info.md).

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** indicates the size, in bytes, of the buffer, which must be &gt;= (**sizeof**(SCSI\_ADAPTER\_BUS\_INFO) + (*NumberOfBuses*) \* **sizeof**(SCSI\_BUS\_DATA)) + (*InquiryDataSize* \* *NumberOfLUs*), where the *InquiryDataSize* is (**sizeof**(SCSI\_INQUIRY\_DATA) - 1 + INQUIRYDATABUFFERSIZE) rounded up to an alignment boundary.

## Status block

The **Information** field contains the number of bytes returned in the output buffer. The **Status** field indicates the results of the operation.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_SCSI\_MINIPORT**](ioctl-scsi-miniport.md)
</dt> <dt>

[**IOCTL\_SCSI\_PASS\_THROUGH**](ioctl-scsi-pass-through.md)
</dt> <dt>

[**IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT**](ioctl-scsi-pass-through-direct.md)
</dt> <dt>

[**IOCTL\_SCSI\_RESCAN\_BUS**](ioctl-scsi-rescan-bus.md)
</dt> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> <dt>

[**SCSI\_ADAPTER\_BUS\_INFO**](scsi-adapter-bus-info.md)
</dt> <dt>

[**SCSI\_INQUIRY\_DATA**](scsi-inquiry-data.md)
</dt> <dt>

[**STORAGE\_DEVICE\_DESCRIPTOR**](storage-device-descriptor.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_SCSI_GET_INQUIRY_DATA%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






