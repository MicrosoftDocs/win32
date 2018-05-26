---
title: IO\_SCSI\_CAPABILITIES structure
description: The IO\_SCSI\_CAPABILITIES structure is used in conjunction with the IOCTL\_SCSI\_GET\_CAPABILITIES request to retrieve the capabilities and limitations of the underlying SCSI host adapter.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models.
ms.assetid: cc348bc8-137a-4abd-9f0e-4c5fb521428f
keywords:
- IO_SCSI_CAPABILITIES structure Storage Devices
- PIO_SCSI_CAPABILITIES structure pointer Storage Devices
topic_type:
- apiref
api_name:
- IO_SCSI_CAPABILITIES
api_location:
- ntddscsi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IO\_SCSI\_CAPABILITIES structure

The IO\_SCSI\_CAPABILITIES structure is used in conjunction with the [**IOCTL\_SCSI\_GET\_CAPABILITIES**](ioctl-scsi-get-capabilities.md) request to retrieve the capabilities and limitations of the underlying SCSI host adapter.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _IO_SCSI_CAPABILITIES {
  ULONG   Length;
  ULONG   MaximumTransferLength;
  ULONG   MaximumPhysicalPages;
  ULONG   SupportedAsynchronousEvents;
  ULONG   AlignmentMask;
  BOOLEAN TaggedQueuing;
  BOOLEAN AdapterScansDown;
  BOOLEAN AdapterUsesPio;
} IO_SCSI_CAPABILITIES, *PIO_SCSI_CAPABILITIES;
```



## Members

<dl> <dt>

**Length**
</dt> <dd>

Contains the length in bytes of this structure.

</dd> <dt>

**MaximumTransferLength**
</dt> <dd>

Contains the maximum size, in bytes, of a single SCSI request block (SRB).

</dd> <dt>

**MaximumPhysicalPages**
</dt> <dd>

Contains the maximum number of physical pages per data buffer.

</dd> <dt>

**SupportedAsynchronousEvents**
</dt> <dd>

When **TRUE**, indicates that the host adapter supports SCSI asynchronous receive-event operations.

</dd> <dt>

**AlignmentMask**
</dt> <dd>

Contains the alignment mask for data transfers. The host adapter requires that data to be transferred must be aligned on an address that is an integer multiple of the value in this field.

</dd> <dt>

**TaggedQueuing**
</dt> <dd>

When **TRUE**, indicates that the host adapter supports tagged queuing.

</dd> <dt>

**AdapterScansDown**
</dt> <dd>

When **TRUE**, indicates that the host adapter scans down for BIOS devices.

</dd> <dt>

**AdapterUsesPio**
</dt> <dd>

When **TRUE**, indicates that the host adapter uses programmed I/O.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_SCSI\_GET\_CAPABILITIES**](ioctl-scsi-get-capabilities.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IO_SCSI_CAPABILITIES%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






