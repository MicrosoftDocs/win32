---
title: SCSI\_PASS\_THROUGH structure
description: The SCSI\_PASS\_THROUGH structure is used in conjunction with an IOCTL\_SCSI\_PASS\_THROUGH request to instruct the port driver to send an embedded SCSI command to the target device.
ms.assetid: c7c4a98a-51c3-46c8-856e-053291b412b3
keywords:
- SCSI_PASS_THROUGH structure Storage Devices
- PSCSI_PASS_THROUGH structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SCSI_PASS_THROUGH
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

# SCSI\_PASS\_THROUGH structure

The SCSI\_PASS\_THROUGH structure is used in conjunction with an [**IOCTL\_SCSI\_PASS\_THROUGH**](ioctl-scsi-pass-through.md) request to instruct the port driver to send an embedded SCSI command to the target device.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _SCSI_PASS_THROUGH {
  USHORT    Length;
  UCHAR     ScsiStatus;
  UCHAR     PathId;
  UCHAR     TargetId;
  UCHAR     Lun;
  UCHAR     CdbLength;
  UCHAR     SenseInfoLength;
  UCHAR     DataIn;
  ULONG     DataTransferLength;
  ULONG     TimeOutValue;
  ULONG_PTR DataBufferOffset;
  ULONG     SenseInfoOffset;
  UCHAR     Cdb[16];
} SCSI_PASS_THROUGH, *PSCSI_PASS_THROUGH;
```



## Members

<dl> <dt>

**Length**
</dt> <dd>

Contains the value of **sizeof**(SCSI\_PASS\_THROUGH).

</dd> <dt>

**ScsiStatus**
</dt> <dd>

Reports the SCSI status that was returned by the HBA or the target device.

</dd> <dt>

**PathId**
</dt> <dd>

Indicates the SCSI port or bus for the request.

</dd> <dt>

**TargetId**
</dt> <dd>

Indicates the target controller or device on the bus.

</dd> <dt>

**Lun**
</dt> <dd>

Indicates the logical unit number of the device.

</dd> <dt>

**CdbLength**
</dt> <dd>

Indicates the size in bytes of the SCSI command descriptor block.

</dd> <dt>

**SenseInfoLength**
</dt> <dd>

Indicates the size in bytes of the request-sense buffer.

</dd> <dt>

**DataIn**
</dt> <dd> <dl> <dt>

Indicates whether the SCSI command will read or write data. This field must have one of three values:
</dt> <dt>





| Data Transfer Type                        | Meaning                               |
|-------------------------------------------|---------------------------------------|
| SCSI\_IOCTL\_DATA\_IN<br/>          | Read data from the device.<br/> |
| SCSI\_IOCTL\_DATA\_OUT<br/>         | Write data to the device.<br/>  |
| SCSI\_IOCTL\_DATA\_UNSPECIFIED<br/> | No data is transferred. <br/>   |



 


</dt> </dl> </dd> <dt>

**DataTransferLength**
</dt> <dd>

Indicates the size in bytes of the data buffer. Many devices transfer chunks of data of predefined length. The value in **DataTransferLength** must be an integral multiple of this predefined, minimum length that is specified by the device. If an underrun occurs, the miniport driver must update this member to the number of bytes actually transferred.

</dd> <dt>

**TimeOutValue**
</dt> <dd>

Indicates the interval in seconds that the request can execute before the port driver considers it timed out.

</dd> <dt>

**DataBufferOffset**
</dt> <dd>

Contains an offset from the beginning of this structure to the data buffer. The offset must respect the data alignment requirements of the device.

</dd> <dt>

**SenseInfoOffset**
</dt> <dd>

Offset from the beginning of this structure to the request-sense buffer.

</dd> <dt>

**Cdb**
</dt> <dd>

Specifies the SCSI command descriptor block to be sent to the target device.

</dd> </dl>

## Remarks

The SCSI\_PASS\_THROUGH structure is used with [**IOCTL\_SCSI\_PASS\_THROUGH**](ioctl-scsi-pass-through.md), which is a buffered device control request. To bypass buffering in system memory, callers should use [**IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT**](ioctl-scsi-pass-through-direct.md). When handling an IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT request, the system locks down the buffer in user memory and the device accesses this memory directly.

The members of SCSI\_PASS\_THROUGH correspond roughly to the members of a [**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md) structure. The values of the **DataIn** member correspond to the SCSI\_IOCTL\_DATA\_IN, SCSI\_IOCTL\_DATA\_OUT, and SCSI\_IOCTL\_DATA\_UNSPECIFIED flags assigned to **SrbFlags** member of SCSI\_REQUEST\_BLOCK.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_SCSI\_PASS\_THROUGH**](ioctl-scsi-pass-through.md)
</dt> <dt>

[**IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT**](ioctl-scsi-pass-through-direct.md)
</dt> <dt>

[**SCSI\_PASS\_THROUGH\_DIRECT**](scsi-pass-through-direct.md)
</dt> <dt>

[**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SCSI_PASS_THROUGH%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






