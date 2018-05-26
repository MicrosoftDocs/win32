---
title: IOCTL\_SCSI\_MINIPORT\_NVCACHE control code
description: The NV Cache Management operations that are defined here can be invoked by user-mode application code running with administrator privileges, using DeviceIoControl and the IOCTL\_SCSI\_MINIPORT control code.
ms.assetid: 6331e850-34a7-4d03-a87b-527f3e38f735
keywords:
- IOCTL_SCSI_MINIPORT_NVCACHE control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_SCSI_MINIPORT_NVCACHE
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

# IOCTL\_SCSI\_MINIPORT\_NVCACHE control code

The NV Cache Management operations that are defined here can be invoked by user-mode application code running with administrator privileges, using DeviceIoControl and the [**IOCTL\_SCSI\_MINIPORT**](ioctl-scsi-miniport.md) control code. Or, the caller can be kernel-mode driver code using [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318) and the IOCTL\_SCSI\_MINIPORT control code.

The NV Cache Management function request is specified in a field in the [**NVCACHE\_REQUEST\_BLOCK**](nvcache-request-block.md) structure. The input to [**IOCTL\_SCSI\_MINIPORT**](ioctl-scsi-miniport.md) is a user-defined data structure that contains an [**SRB\_IO\_CONTROL**](srb-io-control.md) structure followed by an **NVCACHE\_REQUEST\_BLOCK** structure. Additional function-specific data might optionally follow the **NVCACHE\_REQUEST\_BLOCK** structure.

The interface that is used for the NV Cache Management functionality consists of two layers. The first layer is the interface between a caller and the port driver, which is defined by [**IOCTL\_SCSI\_MINIPORT**](ioctl-scsi-miniport.md). The second layer is the interface between the caller and the device, which is defined by the [ATA8-ACS specification](http://go.microsoft.com/fwlink/p/?linkid=74996) and IOCTL\_SCSI\_MINIPORT\_NVCACHE. The API for user-mode application code is the DeviceIoControl interface. The API for kernel-mode driver code is the [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318) interface, which uses **IOCTL\_SCSI\_MINIPORT**.

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains an [**SRB\_IO\_CONTROL**](srb-io-control.md) structure with the Signature field set to "HYBRDISK", and the ControlCode field set to IOCTL\_SCSI\_MINIPORT\_NVCACHE. The [**NVCACHE\_REQUEST\_BLOCK**](nvcache-request-block.md) structure immediately follows the **SRB\_IO\_CONTROL** structure. Any optional function-specific data buffer immediately follows the **NVCACHE\_REQUEST\_BLOCK** structure.

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** indicates the size, in bytes, of all the input data: [**SRB\_IO\_CONTROL**](srb-io-control.md), [**NVCACHE\_REQUEST\_BLOCK**](nvcache-request-block.md), and function-specific data buffer combined. The presence or absence of a data buffer is indicated by the **NVCACHE\_REQUEST\_BLOCKDataBufSize** field.

## Output Buffer

Updated [**SRB\_IO\_CONTROL**](srb-io-control.md) and [**NVCACHE\_REQUEST\_BLOCK**](nvcache-request-block.md) structures, as well as the optional function-specific data buffer, are returned to the buffer at **Irp-&gt;AssociatedIrp.SystemBuffer**.

## Output Buffer Length

The length of the buffer.

## Status block

The **Information** field contains the number of bytes returned in the output buffer. The **Status** field indicates the results of the operation.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318)
</dt> <dt>

[**IOCTL\_SCSI\_MINIPORT**](ioctl-scsi-miniport.md)
</dt> <dt>

[**SRB\_IO\_CONTROL**](srb-io-control.md)
</dt> <dt>

[**NVCACHE\_REQUEST\_BLOCK**](nvcache-request-block.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_SCSI_MINIPORT_NVCACHE%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






