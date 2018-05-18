---
title: ATA\_PASS\_THROUGH\_DIRECT structure
description: The ATA\_PASS\_THROUGH\_DIRECT structure is used in conjunction with an IOCTL\_ATA\_PASS\_THROUGH\_DIRECT request to instruct the port driver to send an embedded ATA command to the target device.
ms.assetid: '0f7a424e-5d83-4ab0-b5a2-7e9093bbd34b'
keywords: ["ATA_PASS_THROUGH_DIRECT structure Storage Devices", "PATA_PASS_THROUGH_DIRECT structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- ATA_PASS_THROUGH_DIRECT
api_location:
- ntddscsi.h
api_type:
- HeaderDef
---

# ATA\_PASS\_THROUGH\_DIRECT structure

The ATA\_PASS\_THROUGH\_DIRECT structure is used in conjunction with an [**IOCTL\_ATA\_PASS\_THROUGH\_DIRECT**](ioctl-ata-pass-through-direct.md) request to instruct the port driver to send an embedded ATA command to the target device.

## Syntax


```C++
typedef struct _ATA_PASS_THROUGH_DIRECT {
  USHORT Length;
  USHORT AtaFlags;
  UCHAR  PathId;
  UCHAR  TargetId;
  UCHAR  Lun;
  UCHAR  ReservedAsUchar;
  ULONG  DataTransferLength;
  ULONG  TimeOutValue;
  ULONG  ReservedAsUlong;
  PVOID  DataBuffer;
  UCHAR  PreviousTaskFile[8];
  UCHAR  CurrentTaskFile[8];
} ATA_PASS_THROUGH_DIRECT, *PATA_PASS_THROUGH_DIRECT;
```



## Members

<dl> <dt>

**Length**
</dt> <dd>

Specifies the length in bytes of the ATA\_PASS\_THROUGH\_DIRECT structure.

</dd> <dt>

**AtaFlags**
</dt> <dd>

Indicates the direction of data transfer and specifies the kind of operation to be performed. The value of this member must be some combination of the flags in the following table.



| ATA flags                             | Meaning                                                                                                                                                                                                                            |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ATA\_FLAGS\_DRDY\_REQUIRED<br/> | Wait for DRDY status from the device before sending the command to the device.<br/>                                                                                                                                          |
| ATA\_FLAGS\_DATA\_IN<br/>       | Read data from the device.<br/>                                                                                                                                                                                              |
| ATA\_FLAGS\_DATA\_OUT<br/>      | Write data to the device.<br/>                                                                                                                                                                                               |
| ATA\_FLAGS\_48BIT\_COMMAND<br/> | The ATA command to be sent uses the 48-bit logical block address (LBA) feature set. When this flag is set, the contents of the **PreviousTaskFile** member in the ATA\_PASS\_THROUGH\_DIRECT structure should be valid.<br/> |
| ATA\_FLAGS\_USE\_DMA<br/>       | Set the transfer mode to DMA.<br/>                                                                                                                                                                                           |
| ATA\_FLAGS\_NO\_MULTIPLE<br/>   | Read single sector only.<br/>                                                                                                                                                                                                |



 

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

Indicates the size, in bytes, of the data buffer. If an underrun occurs, the miniport driver must update this member to the number of bytes actually transferred.

</dd> <dt>

**TimeOutValue**
</dt> <dd>

Indicates the number of seconds that are allowed for the request to execute before the OS-specific port driver determines that the request has timed out.

</dd> <dt>

**ReservedAsUlong**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**DataBuffer**
</dt> <dd>

Pointer to the data buffer.

</dd> <dt>

**PreviousTaskFile**
</dt> <dd>

Specifies the contents of the input task file register prior to the current pass-through command. This member is not used when the ATA\_FLAGS\_48BIT\_COMMAND flag is not set.

</dd> <dt>

**CurrentTaskFile**
</dt> <dd>

Specifies the content of the task file register on both input and output. On input, the array values in **CurrentTaskFile** map to the input registers in the following manner.



| Byte         | Input Register                    |
|--------------|-----------------------------------|
| 0<br/> | Features Register<br/>      |
| 1<br/> | Sector Count Register<br/>  |
| 2<br/> | Sector Number Register<br/> |
| 3<br/> | Cylinder Low Register<br/>  |
| 4<br/> | Cylinder High Register<br/> |
| 5<br/> | Device/Head Register<br/>   |
| 6<br/> | Command Register<br/>       |
| 7<br/> | Reserved<br/>               |



 

When [**IOCTL\_ATA\_PASS\_THROUGH\_DIRECT**](ioctl-ata-pass-through-direct.md) completes, the port driver updates **CurrentTaskFile** with the values that are present in the device's output registers at the completion of the embedded command. The array values in **CurrentTaskFile** correspond to the following task file output registers.



| Byte         | Output Register                   |
|--------------|-----------------------------------|
| 0<br/> | Error Register<br/>         |
| 1<br/> | Sector Count Register<br/>  |
| 2<br/> | Sector Number Register<br/> |
| 3<br/> | Cylinder Low Register<br/>  |
| 4<br/> | Cylinder High Register<br/> |
| 5<br/> | Device/Head Register<br/>   |
| 6<br/> | Status Register<br/>        |
| 7<br/> | Reserved<br/>               |



 

</dd> </dl>

## Remarks

The ATA\_PASS\_THROUGH\_DIRECT structure is used with [**IOCTL\_ATA\_PASS\_THROUGH\_DIRECT**](ioctl-ata-pass-through-direct.md). With this request, the system locks down the buffer in user memory and the device accesses this memory directly. For a double-buffered equivalent of this device control request, see [**IOCTL\_ATA\_PASS\_THROUGH**](ioctl-ata-pass-through.md) and [**ATA\_PASS\_THROUGH\_EX**](ata-pass-through-ex.md).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_ATA\_PASS\_THROUGH\_DIRECT**](ioctl-ata-pass-through-direct.md)
</dt> <dt>

[**IOCTL\_ATA\_PASS\_THROUGH**](ioctl-ata-pass-through.md)
</dt> <dt>

[**ATA\_PASS\_THROUGH\_EX**](ata-pass-through-ex.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ATA_PASS_THROUGH_DIRECT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






