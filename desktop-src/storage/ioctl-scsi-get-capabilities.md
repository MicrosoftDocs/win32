---
title: IOCTL\_SCSI\_GET\_CAPABILITIES control code
description: Returns the capabilities and limitations of the underlying SCSI HBA.
ms.assetid: 1917e0f0-47a3-4f95-97d6-c60d3f511a91
keywords:
- IOCTL_SCSI_GET_CAPABILITIES control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_SCSI_GET_CAPABILITIES
api_location:
- Ntddscsi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_SCSI\_GET\_CAPABILITIES control code

Returns the capabilities and limitations of the underlying SCSI HBA. The most important information is returned in the **MaximumTransferLength** and **AlignmentMask** members. Class drivers and users of [**IOCTL\_SCSI\_PASS\_THROUGH**](ioctl-scsi-pass-through.md) and [**IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT**](ioctl-scsi-pass-through-direct.md) are required to honor these limitations.

Only legacy drivers can issue this request. The request fails if it is sent to a PDO created by the port driver.

To get SCSI capabilities data, a Plug and Play driver must issue an [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) request for [**STORAGE\_ADAPTER\_DESCRIPTOR**](storage-adapter-descriptor.md) data to the PDO for each device to which the driver has been added (that is, each device for which the driver has received an *AddDevice* call). A legacy driver should forward this request to the port driver. This request fails if it is sent to the FDO for an adapter.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Input Buffer

None.

## Input Buffer Length

None.

## Output Buffer

Updated [**IO\_SCSI\_CAPABILITIES**](io-scsi-capabilities.md) information is returned to the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

**Parameters.DeviceIoControl.OutputBufferLength** in the I/O stack location indicates the size, in bytes, of the buffer, which must be &gt;= **sizeof**(IO\_SCSI\_CAPABILITIES).

## Status block

The **Information** field contains the number of bytes returned in the output buffer. The **Status** field indicates the results of the operation.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**IO\_SCSI\_CAPABILITIES**](io-scsi-capabilities.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_SCSI_GET_CAPABILITIES%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






