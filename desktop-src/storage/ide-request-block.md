---
title: IDE\_REQUEST\_BLOCK structure
description: The IDE\_REQUEST\_BLOCK structure defines an IDE request block.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: '9e112984-0a7e-4bb9-a10f-b50ab67ce4f3'
keywords: ["IDE_REQUEST_BLOCK structure Storage Devices", "PIDE_REQUEST_BLOCK structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- IDE_REQUEST_BLOCK
api_location:
- irb.h
api_type:
- HeaderDef
---

# IDE\_REQUEST\_BLOCK structure

The IDE\_REQUEST\_BLOCK structure defines an IDE request block.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _IDE_REQUEST_BLOCK {
  USHORT Function;
  UCHAR  IrbStatus;
  UCHAR  AtaStatus;
  UCHAR  AtaError;
  UCHAR  Channel;
  UCHAR  TargetId;
  UCHAR  Lun;
  UCHAR  CdbLength;
  UCHAR  SenseInfoBufferLength;
  UCHAR  SenseInfoBufferType;
  UCHAR  QueueTag;
  ULONG  ReservedAsUlong;
  ULONG  IrbFlags;
  ULONG  TimeOutValue;
  ULONG  DataTransferLength;
  PVOID  IrbExtension;
  PVOID  DataBuffer;
  PVOID  SenseInfoBuffer;
  PVOID  NextIrb;
  PVOID  Reserved;
  union {
    IDE_TASK_FILE  IdeTaskFile;
    UCHAR          Cdb[16];
    IDE_POWER_INFO PowerChange;
    UCHAR          AsUChar[16];
  };
} IDE_REQUEST_BLOCK, *PIDE_REQUEST_BLOCK;
```



## Members

<dl> <dt>

**Function**
</dt> <dd>

Specifies the category that the request belongs to. The table below describes the classification of the I/O requests.



|                                             |                                                                                                                                                                                                                                            |                                                                                                                                                                  |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Function**<br/>                     | **Sub-commands**<br/>                                                                                                                                                                                                                | **Description**<br/>                                                                                                                                       |
| IRB\_FUNCTION\_ATA\_COMMAND<br/>      | IRB\_FUNCTION\_ATA\_IDENTIFY<br/> IRB\_FUNCTION\_ATA\_READ<br/> IRB\_FUNCTION\_ATA\_WRITE<br/> IRB\_FUNCTION\_ATA\_FLUSH<br/> IRB\_FUNCTION\_ATA\_SMART<br/>                                                 | Indicates that the IRB contains an IdeTaskFile that describes the ATA command. The sub-commands indicate finer grouping of request for faster lookup.<br/> |
| IRB\_FUNCTION\_ATAPI\_COMMAND<br/>    | IRB\_FUNCTION\_REQUEST\_SENSE<br/>                                                                                                                                                                                                   | Indicates that the IRB contains a CDB that describes the ATAPI command.<br/>                                                                               |
| IRB\_FUNCTION\_MINIPORT\_COMMAND<br/> | IRB\_FUNCTION\_ADAPTER\_FLUSH<br/> IRB\_FUNCTION\_SHUTDOWN<br/> IRB\_FUNCTION\_POWER\_CHANGE<br/> IRB\_FUNCTION\_POWER\_REBOOT<br/> IRB\_FUNCTION\_LUN\_RESET<br/> IRB\_FUNCTION\_MINIPORT\_IOCTL<br/> | Indicates that the IRB is for the miniport. It is the responsibility of the miniport to interpret the command appropriately.<br/>                          |



 

</dd> <dt>

**IrbStatus**
</dt> <dd>

The miniport must set this member to indicates the status of the specified operation. The table below describes the various **IrbStatus** values and their meaning.



|                                                 |                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Value**<br/>                            | **Meaning**<br/>                                                                                                                                                                                                                                                                                                                            |
| IRB\_STATUS\_PENDING<br/>                 | Indicates that the request is in progress. The port driver initializes **IrbStatus** to this value. A miniport driver should never set the **IrbStatus** member to this value.<br/>                                                                                                                                                         |
| IRB\_STATUS\_SUCCESS<br/>                 | Indicates that the request was completed successfully.<br/>                                                                                                                                                                                                                                                                                 |
| IRB\_STATUS\_DATALENGTH\_MISMATCH<br/>    | Indicates that a data underrun or overrun error occurred. The miniport must update the DataTransferLength field in the IRB to indicate the actual amount of data that was transferred in the case of an underrun.<br/>                                                                                                                      |
| IRB\_STATUS\_DEVICE\_ERROR<br/>           | Indicates that the device returned an error. The miniport driver must update the *AtaStatus* and *AtaError* fields in the Irb to the contents of the device ATA status and error register at the completion of the command.<br/>                                                                                                            |
| IRB\_STATUS\_INVALID\_REQUEST<br/>        | Indicates that the miniport does not support the given request.<br/>                                                                                                                                                                                                                                                                        |
| IRB\_STATUS\_BUS\_RESET<br/>              | Indicates that a bus reset occurred while processing the given request.<br/>                                                                                                                                                                                                                                                                |
| IRB\_STATUS\_SELECTION\_TIMEOUT<br/>      | Indicates that the destination device could not be selected.<br/>                                                                                                                                                                                                                                                                           |
| IRB\_STATUS\_BUSY<br/>                    | Indicates that the device is busy. The port driver retries any request completed with this status. A request completed with busy status is retried only once. It is the responsibility of the miniport driver to pause the request queue using **AtaPortDeviceBusy** if the device cannot handle request for a certain period of time.<br/> |
| IRB\_STATUS\_AUTOSENSE\_VALID<br/>        | IRB\_STATUS\_AUTOSENSE\_VALID is a bitmask that indicates valid sense data in the *SenseInfoBuffer* member of the IRB. <br/>                                                                                                                                                                                                                |
| IRB\_STATUS\_RETURN\_TASKFILE\_VALID<br/> | IRB\_STATUS\_RETURN\_TASKFILE\_VALID is a bitmask that indicates a valid return task file in the *SenseInfoBuffer* member of the IRB.<br/>                                                                                                                                                                                                  |



 

</dd> <dt>

**AtaStatus**
</dt> <dd>

Indicates the status returned by the device in its status register. The miniport driver should update this field when completing an IRB with *IRB\_STATUS\_DEVICE\_ERROR*.

</dd> <dt>

**AtaError**
</dt> <dd>

Indicates the error value returned by the device in its error register. The miniport driver should update this field when completing an IRB with *IRB\_STATUS\_DEVICE\_ERROR*.

</dd> <dt>

**Channel**
</dt> <dd>

Specifies the channel number.

</dd> <dt>

**TargetId**
</dt> <dd>

Specifies the target ID of the device.

</dd> <dt>

**Lun**
</dt> <dd>

Specifies the logical unit number of the device.

</dd> <dt>

**CdbLength**
</dt> <dd>

Specifies the length in bytes of the buffer pointed to by **Cdb**.

</dd> <dt>

**SenseInfoBufferLength**
</dt> <dd>

Specifies the length in bytes of the buffer pointed to by **SenseInfoBuffer**.

</dd> <dt>

**SenseInfoBufferType**
</dt> <dd>

Specifies the type of data structure returned in **SenseInfoBuffer**. Because ATA commands don't have a need for the request sense command, ATA\_PASS\_THROUGH commands use **SenseInfoBuffer** to return task file information. For ATA\_PASS\_THROUGH commands, as identified in the **IrbFlags** member, the appropriate return **TaskFile** size should be reported as either SENSE\_INFO\_BUFFER\_RETURN\_TYPE\_28BIT\_TASKFILE or

SENSE\_INFO\_BUFFER\_RETURN\_TYPE\_48BIT\_TASKFILE.

</dd> <dt>

**QueueTag**
</dt> <dd>

The queue tag for this IRB. The port driver sets this field to 0.

</dd> <dt>

**ReservedAsUlong**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**IrbFlags**
</dt> <dd>

Qualifies the request with ceratin actions that need to be performed. The table below describes them in detail.



|                                        |                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Flag**<br/>                    | **Description**<br/>                                                                                                                                                                                                                                                                                                                                         |
| IRB\_FLAGS\_DRDY\_REQUIRED<br/>  | Indicates that the miniport driver must wait for the device to set the DRDY bit in the ATA status register before issuing this command.<br/>                                                                                                                                                                                                                 |
| IRB\_FLAGS\_USE\_DMA<br/>        | Indicates that the request has an associated scatter/gather list and the miniport driver could use DMA to transfer data for this request. <br/>                                                                                                                                                                                                              |
| IRB\_FLAGS\_MAP\_BUFFERS<br/>    | Indicates that the **DataBuffer** field in the IRB is mapped. The miniport can safely access **DataBuffer** when this flag is set. The miniport driver must not access **DataBuffer** if the flag is not set. The miniport driver could request the port driver to map the data buffer by setting this flag in the IRB in its **IdeHwBuildIo** routine.<br/> |
| IRB\_FLAGS\_48BIT<br/>           | Indicates that the ATA command in the IRB belongs to the 48 bit LBA feature set. The **Previous** field in the *\_IDE\_TASK\_FILE* structure is valid when this flag is set.<br/>                                                                                                                                                                            |
| IRB\_FLAGS\_PIO\_MULTIPLE<br/>   | Indicates that the ATA command is to be transferred using the ATA PIO Multiple method.<br/>                                                                                                                                                                                                                                                                  |
| IRB\_FLAGS\_RETURN\_RESULTS<br/> | Indicates that the ATA return task file is to be copied to **SenseInfoBuffer**. <br/>                                                                                                                                                                                                                                                                        |
| IRB\_FLAGS\_DATA\_IN<br/>        | Indicates that the data is to be transferred from the device to the host system (a read operation).<br/>                                                                                                                                                                                                                                                     |
| IRB\_FLAGS\_DATA\_OUT<br/>       | Indicates that the data is to be transferred to the device from the host system ( a write operation).<br/>                                                                                                                                                                                                                                                   |
| IRB\_FLAGS\_DISCARDABLE <br/>    | Indicates that the command shall be done in a best effort manner. (note: this is not currently employed by ATAport).<br/>                                                                                                                                                                                                                                    |
| IRB\_FLAGS\_HIGH\_PRIORITY<br/>  | Indicates that this IRB is to be processed as soon as possible, before non-high-priority IRBs currently in the ATA miniport.<br/>                                                                                                                                                                                                                            |



 

</dd> <dt>

**TimeOutValue**
</dt> <dd>

Indicates the time in seconds after which the request will time out.

</dd> <dt>

**DataTransferLength**
</dt> <dd>

Contains the length in bytes of the data buffer that contains data to be transferred.

</dd> <dt>

**IrbExtension**
</dt> <dd>

Pointer to the per-request extension allocated by the port driver.

</dd> <dt>

**DataBuffer**
</dt> <dd>

Pointer to the buffer where the data resides.

</dd> <dt>

**SenseInfoBuffer**
</dt> <dd>

Pointer to the buffer which holds the sense data.

</dd> <dt>

**NextIrb**
</dt> <dd>

Pointer to the next IRB to be processed. The port driver sets this to **NULL**. The miniport driver can use this field to link IRBs together.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**IdeTaskFile**
</dt> <dd>

Contains a structure of type [**IDE\_TASK\_FILE**](ide-task-file.md) that holds the IDE task file for the indicated controller. This member is defined whenever the result of a bitwise AND between the **Function** member and IRB\_FUNCTION\_ATA\_COMMAND is nonzero.

</dd> <dt>

**Cdb**
</dt> <dd>

Contains a command descriptor block (CDB). This member is defined whenever the result of a bitwise AND between the **Function** member and IRB\_FUNCTION\_ATAPI\_COMMAND is nonzero.

</dd> <dt>

**PowerChange**
</dt> <dd>

Indicates an enumeration value of type [**POWER\_CHANGE\_INFO**](power-change-info.md) that defines a power state transition. This member is defined whenever **Function** is equal to IRB\_FUNCTION\_POWER\_CHANGE.

</dd> <dt>

**AsUChar**
</dt> <dd>

Provides a means of accessing members **IdeTaskFile**, **PowerChange**, and **Cdb** as unsigned character data.

</dd> </dl>

## Remarks

The IDE\_REQUEST\_BLOCK structure provides a functionality similar to the [**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md) but with characteristics more suitable for managing devices on an IDE bus.

## Requirements



|                   |                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



## See also

<dl> <dt>

[**AtaportDeviceBusy**](ataportdevicebusy.md)
</dt> <dt>

[**IDE\_TASK\_FILE**](ide-task-file.md)
</dt> <dt>

[**POWER\_CHANGE\_INFO**](power-change-info.md)
</dt> <dt>

[**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IDE_REQUEST_BLOCK%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






