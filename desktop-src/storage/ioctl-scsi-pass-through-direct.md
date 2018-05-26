---
title: IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT control code
description: Allows an application to send almost any SCSI command to a target device, with the following restrictions Multitarget commands, such as COPY, are not allowed.Bidirectional data transfer operations are not supported.If a class driver for the target type of device exists, the request must be sent to that class driver. Thus, an application can send this request directly to the system port driver for a target logical unit only if there is no class driver for the type of device connected to that LU.This request must be made if the input CDB might require the underlying miniport driver to access memory directly.The calling application creates the SCSI command descriptor block, which can include a request for request-sense data if a CHECK CONDITION occurs. If the CDB requests a data transfer operation, the caller must set up an adapter device aligned buffer from which or into which the miniport driver can transfer data directly. This request is typically used for transferring larger amounts of data ( 16K).Applications can send this request by means of an IRP\_MJ\_DEVICE\_CONTROL request. Storage class drivers set the minor IRP number to IRP\_MN\_SCSI\_CLASS to indicate that the request has been processed by a storage class driver.
ms.assetid: 7706e861-b8d6-41c3-9b64-371de4f58d48
keywords:
- IOCTL_SCSI_PASS_THROUGH_DIRECT control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_SCSI_PASS_THROUGH_DIRECT
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

# IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT control code

Allows an application to send almost any SCSI command to a target device, with the following restrictions:

-   Multitarget commands, such as COPY, are not allowed.

-   Bidirectional data transfer operations are not supported.

-   If a class driver for the target type of device exists, the request must be sent to that class driver. Thus, an application can send this request directly to the system port driver for a target logical unit only if there is no class driver for the type of device connected to that LU.

-   This request *must* be made if the input CDB might require the underlying miniport driver to access memory directly.

The calling application creates the SCSI command descriptor block, which can include a request for request-sense data if a CHECK CONDITION occurs. If the CDB requests a data transfer operation, the caller must set up an adapter device aligned buffer from which or into which the miniport driver can transfer data directly. This request is typically used for transferring larger amounts of data (&gt;16K).

Applications can send this request by means of an [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) request.

Storage class drivers set the minor IRP number to IRP\_MN\_SCSI\_CLASS to indicate that the request has been processed by a storage class driver.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Input Buffer

This structure includes a SCSI CDB, which must be initialized by the caller except for the path, target ID, and LUN, which are filled in by the port driver. For a data-out command, the data to be transferred must be in an adapter device aligned buffer. The **DataBuffer** member of [**SCSI\_PASS\_THROUGH\_DIRECT**](scsi-pass-through-direct.md) is a pointer to this adapter device aligned buffer. The caller must allocate additional storage, following the **SCSI\_PASS\_THROUGH\_DIRECT** structure, if the caller asks for request-sense data.

## Input Buffer Length

*Parameters.DeviceIoControl.InputBufferLength* indicates the size, in bytes, of the buffer at *Irp-&gt;AssociatedIrp.SystemBuffer*, which must be at least (*sense data size* + **sizeof** ([**SCSI\_PASS\_THROUGH\_DIRECT**](scsi-pass-through-direct.md))). The size of the **SCSI\_PASS\_THROUGH\_DIRECT** structure is fixed.

## Output Buffer

The port driver returns any request-sense data and the [**SCSI\_PASS\_THROUGH\_DIRECT**](scsi-pass-through-direct.md) structure to the buffer at *Irp-&gt;AssociatedIrp.SystemBuffer*.

## Output Buffer Length

**SenseInfoLength** and **DataTransferLength** are updated to indicate the amount of data transferred. The port driver returns any data transferred from the device to the supplied cache-aligned buffer at **DataBuffer**.

## Status block

The **Information** field is set to the number of bytes returned in the output buffer at *Irp-&gt;AssociatedIrp.SystemBuffer*. The Status field is set to **STATUS\_SUCCESS**, or possibly to **STATUS\_BUFFER\_TOO\_SMALL** or **STATUS\_INVALID\_PARAMETER** if the input **Length** value in [**SCSI\_PASS\_THROUGH\_DIRECT**](scsi-pass-through-direct.md) is improperly set or the buffer specifed in **DataBuffer** is not properly device aligned.

## Remarks

For data transfer operations, a buffer with alignment matching the adapter device is required. Applications can retrieve the device alignment mask by issuing an [**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md) control code request with a query type of **PropertyStandardQuery** and property id of **StorageAdapterProperty**. The alignment mask is found in the **AlignmentMask** member of the [**STORAGE\_ADAPTER\_DESCRIPTOR**](storage-adapter-descriptor.md) structure that is returned. Drivers may also use the value in the **AlignmentMask** member of the adapter's *DeviceObject*.

In the following example function, a buffer is prepared as a device aligned data transfer buffer.


```C++
PVOID AllocateAlignedBuffer(ULONG size, ULONG AlignmentMask, PVOID *pUnAlignedBuffer)
{
    PVOID AlignedBuffer;
    ULONG_PTR FullWordMask = (ULONG_PTR)AlignmentMask;

    if (AlignmentMask == 0)
    {
        AlignedBuffer = malloc(size);
        // return the original buffer to free later
        *pUnAlignedBuffer = AlignedBuffer;
    }
    else
    {
        // expand the size for the alignment window
        size += AlignmentMask;
        AlignedBuffer = malloc(size);
        // return the original buffer to free later
        *pUnAlignedBuffer = AlignedBuffer;
        // adjust buffer pointer for the desired alignment
        AlignedBuffer = (PVOID)(((ULONG_PTR)AlignedBuffer + FullWordMask) & ~FullWordMask);
    }

    return AlignedBuffer;
}
```



## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_SCSI\_PASS\_THROUGH**](ioctl-scsi-pass-through.md)
</dt> <dt>

[**IOCTL\_STORAGE\_QUERY\_PROPERTY**](ioctl-storage-query-property.md)
</dt> <dt>

[**SCSI\_PASS\_THROUGH\_DIRECT**](scsi-pass-through-direct.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_SCSI_PASS_THROUGH_DIRECT%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






