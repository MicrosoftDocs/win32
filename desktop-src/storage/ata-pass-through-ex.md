---
title: ATA\_PASS\_THROUGH\_EX structure
description: The ATA\_PASS\_THROUGH\_EX structure is used in conjunction with an IOCTL\_ATA\_PASS\_THROUGH request to instruct the port driver to send an embedded ATA command to the target device.
ms.assetid: 76d8f5be-0011-4a7c-ac21-7115ad7e1155
keywords:
- ATA_PASS_THROUGH_EX structure Storage Devices
- PATA_PASS_THROUGH_EX structure pointer Storage Devices
topic_type:
- apiref
api_name:
- ATA_PASS_THROUGH_EX
api_location:
- ntddscsi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# ATA\_PASS\_THROUGH\_EX structure

The ATA\_PASS\_THROUGH\_EX structure is used in conjunction with an [**IOCTL\_ATA\_PASS\_THROUGH**](ioctl-ata-pass-through.md) request to instruct the port driver to send an embedded ATA command to the target device.

## Syntax


```C++
typedef struct _ATA_PASS_THROUGH_EX {
  USHORT    Length;
  USHORT    AtaFlags;
  UCHAR     PathId;
  UCHAR     TargetId;
  UCHAR     Lun;
  UCHAR     ReservedAsUchar;
  ULONG     DataTransferLength;
  ULONG     TimeOutValue;
  ULONG     ReservedAsUlong;
  ULONG_PTR DataBufferOffset;
  UCHAR     PreviousTaskFile[8];
  UCHAR     CurrentTaskFile[8];
} ATA_PASS_THROUGH_EX, *PATA_PASS_THROUGH_EX;
```



## Members

<dl> <dt>

**Length**
</dt> <dd>

Specifies the length in bytes of the ATA\_PASS\_THROUGH\_EX structure.

</dd> <dt>

**AtaFlags**
</dt> <dd>

Indicates the direction of data transfer and specifies the kind of operation to be performed. The value of this member must be some combination of the following flags:



| ATA flags                             | Meaning                                                                                                                                                                                                                        |
|---------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ATA\_FLAGS\_DRDY\_REQUIRED<br/> | Wait for DRDY status from the device before sending the command to the device.<br/>                                                                                                                                      |
| ATA\_FLAGS\_DATA\_IN<br/>       | Read data from the device.<br/>                                                                                                                                                                                          |
| ATA\_FLAGS\_DATA\_OUT<br/>      | Write data to the device.<br/>                                                                                                                                                                                           |
| ATA\_FLAGS\_48BIT\_COMMAND<br/> | The ATA command to be sent uses the 48-bit logical block address (LBA) feature set. When this flag is set, the contents of the **PreviousTaskFile** member in the ATA\_PASS\_THROUGH\_EX structure should be valid.<br/> |
| ATA\_FLAGS\_USE\_DMA<br/>       | Set the transfer mode to DMA.<br/>                                                                                                                                                                                       |
| ATA\_FLAGS\_NO\_MULTIPLE<br/>   | Read single sector only.<br/>                                                                                                                                                                                            |



 

</dd> <dt>

**PathId**
</dt> <dd>

Contains an integer that indicates the IDE port or bus for the request. This value is set by the port driver.

</dd> <dt>

**TargetId**
</dt> <dd>

Contains an integer that indicates the target device on the bus. This value is set by the port driver.

</dd> <dt>

**Lun**
</dt> <dd>

Indicates the logical unit number of the device. This value is set by the port driver.

</dd> <dt>

**ReservedAsUchar**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**DataTransferLength**
</dt> <dd>

Indicates the size, in bytes, of the data buffer. If an underrun occurs, the miniport driver must update this member to the number of bytes that were actually transferred.

</dd> <dt>

**TimeOutValue**
</dt> <dd>

Indicates the number of seconds that are allowed for the request to execute before the OS-specific port driver determines that the request has timed out.

</dd> <dt>

**ReservedAsUlong**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**DataBufferOffset**
</dt> <dd>

Specifies the offset, in bytes, from the beginning of this structure to the data buffer.

</dd> <dt>

**PreviousTaskFile**
</dt> <dd>

Specifies the contents of the task file input registers prior to the current pass-through command. This member is not used when the ATA\_FLAGS\_48BIT\_COMMAND flag is not set.

</dd> <dt>

**CurrentTaskFile**
</dt> <dd>

Specifies the content of the task file register on both input and output. On input, the array values in **CurrentTaskFile** map to the task file input registers in the following manner.



| Byte         | Input Register                    |
|--------------|-----------------------------------|
| 0<br/> | Features register<br/>      |
| 1<br/> | Sector count register<br/>  |
| 2<br/> | Sector number register<br/> |
| 3<br/> | Cylinder low register<br/>  |
| 4<br/> | Cylinder high register<br/> |
| 5<br/> | Device/head register<br/>   |
| 6<br/> | Command register<br/>       |
| 7<br/> | Reserved<br/>               |



 

When [**IOCTL\_ATA\_PASS\_THROUGH**](ioctl-ata-pass-through.md) completes, the port driver updates **CurrentTaskFile** with the values that are present in the device's output registers at the completion of the embedded command. The array values in **CurrentTaskFile** correspond to the following task file output registers.



| Byte         | Output Register                   |
|--------------|-----------------------------------|
| 0<br/> | Error register<br/>         |
| 1<br/> | Sector count register<br/>  |
| 2<br/> | Sector number register<br/> |
| 3<br/> | Cylinder low register<br/>  |
| 4<br/> | Cylinder high register<br/> |
| 5<br/> | Device/head register<br/>   |
| 6<br/> | Status register<br/>        |
| 7<br/> | Reserved<br/>               |



 

</dd> </dl>

## Remarks

[**IOCTL\_ATA\_PASS\_THROUGH**](ioctl-ata-pass-through.md) is a buffered device control request. To bypass buffering in system memory, callers should use [**IOCTL\_ATA\_PASS\_THROUGH\_DIRECT**](ioctl-ata-pass-through-direct.md) and [**ATA\_PASS\_THROUGH\_DIRECT**](ata-pass-through-direct.md). When handling an IOCTL\_ATA\_PASS\_THROUGH\_DIRECT request, the system locks down the buffer in user memory and the device accesses this memory directly.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**ATA\_PASS\_THROUGH\_DIRECT**](ata-pass-through-direct.md)
</dt> <dt>

[**IOCTL\_ATA\_PASS\_THROUGH**](ioctl-ata-pass-through.md)
</dt> <dt>

[**IOCTL\_ATA\_PASS\_THROUGH\_DIRECT**](ioctl-ata-pass-through-direct.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ATA_PASS_THROUGH_EX%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






