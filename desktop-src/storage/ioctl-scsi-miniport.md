---
title: IOCTL\_SCSI\_MINIPORT control code
description: Sends a special control function to an HBA-specific miniport driver.
ms.assetid: 5a9facc7-c83e-4dd4-9fb4-e3385c1b94ea
keywords:
- IOCTL_SCSI_MINIPORT control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_SCSI_MINIPORT
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

# IOCTL\_SCSI\_MINIPORT control code

Sends a special control function to an HBA-specific miniport driver. Results vary, depending on the particular miniport driver to which this request is forwarded. If the caller specifies a nonzero **Length**, either the input or output buffer must be at least (**sizeof**(SRB\_IO\_CONTROL) + *DataBufferLength*)).

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** must contain an [**SRB\_IO\_CONTROL**](srb-io-control.md) structure.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** indicates the size, in bytes, of the buffer, which must be at least **sizeof**(SRB\_IO\_CONTROL), with additional storage for data if the **Length** field is nonzero.

## Output Buffer

An updated [**SRB\_IO\_CONTROL**](srb-io-control.md) structure is returned to the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

The length of the [**SRB\_IO\_CONTROL**](srb-io-control.md) structure.

## Status block

The **Information** field contains the number of bytes returned in the output buffer. The **Status** field indicates the results of the operation.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**SRB\_IO\_CONTROL**](srb-io-control.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_SCSI_MINIPORT%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






