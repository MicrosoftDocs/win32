---
title: SCSI\_PASS\_THROUGH\_DIRECT\_EX structure
description: The SCSI\_PASS\_THROUGH\_DIRECT\_EX structure is used in conjunction with an IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT\_EX request to instruct the port driver to send an embedded SCSI command to the target device.
ms.assetid: 'FB210147-9CF3-4D32-884E-256BEAFAE6C4'
keywords: ["SCSI_PASS_THROUGH_DIRECT_EX structure Storage Devices", "PSCSI_PASS_THROUGH_DIRECT_EX structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- SCSI_PASS_THROUGH_DIRECT_EX
api_location:
- ntddscsi.h
api_type:
- HeaderDef
---

# SCSI\_PASS\_THROUGH\_DIRECT\_EX structure

The **SCSI\_PASS\_THROUGH\_DIRECT\_EX** structure is used in conjunction with an [**IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT\_EX**](ioctl-scsi-pass-through-direct-ex.md) request to instruct the port driver to send an embedded SCSI command to the target device. **SCSI\_PASS\_THROUGH\_DIRECT\_EX** can contain a bi-directional data transfers and a variable length command data block.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _SCSI_PASS_THROUGH_DIRECT_EX {
  USHORT Version;
  USHORT Length;
  ULONG  CdbLength;
  UCHAR  StorAddressLength;
  UCHAR  ScsiStatus;
  UCHAR  SenseInfoLength;
  UCHAR  DataDirection;
  UCHAR  Reserved;
  ULONG  TimeOutValue;
  ULONG  StorAddressOffset;
  ULONG  SenseInfoOffset;
  ULONG  DataOutTransferLength;
  ULONG  DataInTransferLength;
  VOID   DataOutBuffer;
  VOID   DataInBuffer;
  UCHAR  Cdb[ANYSIZE_ARRAY];
} SCSI_PASS_THROUGH_DIRECT_EX, *PSCSI_PASS_THROUGH_DIRECT_EX;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of this structure. Set to 0.

</dd> <dt>

**Length**
</dt> <dd>

The size of the this structure. Set to **sizeof**(SCSI\_PASS\_THROUGH\_DIRECT\_EX).

</dd> <dt>

**CdbLength**
</dt> <dd>

Indicates the size in bytes of the SCSI command descriptor block in **Cdb**.

</dd> <dt>

**StorAddressLength**
</dt> <dd>

The length of the storage device address structure at the offset of **StorAddressOffset** after this structure. This is set to **sizeof**(STOR\_ADDR\_BTL8).

</dd> <dt>

**ScsiStatus**
</dt> <dd>

Reports the SCSI status that was returned by the HBA or the target device.

</dd> <dt>

**SenseInfoLength**
</dt> <dd>

Indicates the size in bytes of the request-sense buffer. This member is optional and can be set to 0.

</dd> <dt>

**DataDirection**
</dt> <dd> <dl> <dt>

Indicates whether the SCSI command will read data, write data, or both. This field must have one of these values:
</dt> <dt>





| Data Transfer Type                          | Meaning                                             |
|---------------------------------------------|-----------------------------------------------------|
| SCSI\_IOCTL\_DATA\_IN<br/>            | Read data from the device.<br/>               |
| SCSI\_IOCTL\_DATA\_OUT<br/>           | Write data to the device.<br/>                |
| SCSI\_IOCTL\_DATA\_UNSPECIFIED<br/>   | No data is transferred.<br/>                  |
| SCSI\_IOCTL\_DATA\_BIDIRECTIONAL<br/> | Data is valid for both input and output.<br/> |



 


</dt> </dl> </dd> <dt>

**Reserved**
</dt> <dd>

Reserved. Set to 0.

</dd> <dt>

**TimeOutValue**
</dt> <dd>

Indicates the interval in seconds that the request can execute before the port driver considers it timed out.

</dd> <dt>

**StorAddressOffset**
</dt> <dd>

The location of the target device's [**STOR\_ADDR\_BTL8**](stor-addr-btl8.md) address structure, in bytes, from the beginning of this structure.

</dd> <dt>

**SenseInfoOffset**
</dt> <dd>

Offset from the beginning of this structure to the request-sense buffer. Set to 0 if no request-sense buffer is present.

</dd> <dt>

**DataOutTransferLength**
</dt> <dd>

Indicates the size in bytes of the output data buffer. Many devices transfer chunks of data of predefined length. The value in **DataOutTransferLength** must be an integral multiple of this predefined, minimum length that is specified by the device. If an underrun occurs, the miniport driver must update this member to the number of bytes actually transferred. If no output data buffer is present, this member is set to 0.

</dd> <dt>

**DataInTransferLength**
</dt> <dd>

Indicates the size in bytes of the input data buffer. Many devices transfer chunks of data of predefined length. The value in **DataInTransferLength** must be an integral multiple of this predefined, minimum length that is specified by the device. If an underrun occurs, the miniport driver must update this member to the number of bytes actually transferred. If no input data buffer is present, this member is set to 0.

</dd> <dt>

**DataOutBuffer**
</dt> <dd>

A pointer to a output data buffer.

</dd> <dt>

**DataInBuffer**
</dt> <dd>

A pointer to a input data buffer.

</dd> <dt>

**Cdb**
</dt> <dd>

Specifies the SCSI command descriptor block to be sent to the target device.

</dd> </dl>

## Remarks

The **SCSI\_PASS\_THROUGH\_DIRECT\_EX** structure is used with [**IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT\_EX**](ioctl-scsi-pass-through-direct-ex.md). With this request, the system locks down the buffer in user memory and the device accesses this memory directly. For a double-buffered equivalent of this device control request see **IOCTL\_SCSI\_PASS\_THROUGH\_EX** and [**SCSI\_PASS\_THROUGH\_EX**](scsi-pass-through-ex.md).

> [!Note]  
> Drivers executing on a 64 bit version of Windows must use the **SCSI\_PASS\_THROUGH\_DIRECT32\_EX** structure as the request data type when handling an [**IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT\_EX**](ioctl-scsi-pass-through-direct-ex.md) request from a 32 bit process.

 

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                              |
| Header<br/>  | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT**](ioctl-scsi-pass-through-direct.md)
</dt> <dt>

[**IOCTL\_SCSI\_PASS\_THROUGH\_DIRECT\_EX**](ioctl-scsi-pass-through-direct-ex.md)
</dt> <dt>

[**SCSI\_PASS\_THROUGH\_DIRECT**](scsi-pass-through-direct.md)
</dt> <dt>

[**STOR\_ADDR\_BTL8**](stor-addr-btl8.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SCSI_PASS_THROUGH_DIRECT_EX%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






