---
title: TAPE\_PROCESS\_COMMAND\_ROUTINE routine
description: TAPE\_PROCESS\_COMMAND\_ROUTINE handles the device-specific aspects of an IOCTL request.
ms.assetid: 6675d840-8b13-44ef-bbdb-84d683240175
keywords:
- ( TAPE_PROCESS_COMMAND_ROUTINE) routine Storage Devices
- TAPE_PROCESS_COMMAND_ROUTINE
topic_type:
- apiref
api_name:
- ( TAPE_PROCESS_COMMAND_ROUTINE)
api_location:
- minitape.h
api_type:
- UserDefined
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TAPE\_PROCESS\_COMMAND\_ROUTINE routine

*TAPE\_PROCESS\_COMMAND\_ROUTINE* handles the device-specific aspects of an IOCTL request.

## Syntax


```C++
TAPE_PROCESS_COMMAND_ROUTINE (*TAPE_PROCESS_COMMAND_ROUTINE);

TAPE_STATUS (*TAPE_PROCESS_COMMAND_ROUTINE)(
  _Inout_  PVOID               MinitapeExtension,
  _Inout_  PVOID               CommandExtension,
  _Inout_  PVOID               CommandParameters,
  _Inout_  PSCSI_REQUEST_BLOCK Srb,
  _In_     ULONG               CallNumber,
  _In_opt_ TAPE_STATUS         StatusOfLastCommand,
  _Inout_  PULONG              RetryFlags
)
{ ... }
```



## Parameters

<dl> <dt>

*MinitapeExtension* \[in, out\]
</dt> <dd>

Pointer to the driver-specific minitape extension. This is **NULL** if the miniclass driver did not request a minitape extension when it initialized.

</dd> <dt>

*CommandExtension* \[in, out\]
</dt> <dd>

Pointer to the command extension. This is **NULL** if the miniclass driver did not request a command extension when it initialized.

</dd> <dt>

*CommandParameters* \[in, out\]
</dt> <dd>

Pointer to a buffer allocated by the caller that contains a [**TAPE\_CREATE\_PARTITION**](tape-create-partition.md) structure.

</dd> <dt>

*Srb* \[in, out\]
</dt> <dd>

Pointer to an SRB allocated and partially filled in by the tape class driver. *TAPE\_PROCESS\_COMMAND\_ROUTINE* must fill in the CDB in the SRB.

-   **Cdb** - Pointer to the SCSI CDB for the command. Clear the CDB with **TapeClassZeroMemory** before filling it in.

-   **CdbLength** - Specifies the number of bytes in the CDB.

*TAPE\_PROCESS\_COMMAND\_ROUTINE* might also fill in the following members in the SRB:

-   **DataBuffer** - Pointer to the data buffer to be transferred. Use [**TapeClassAllocateSrbBuffer**](tapeclassallocatesrbbuffer.md) to allocate a **DataBuffer** of length greater than or equal to **DataTransferLength**.

-   **DataTransferLength** - Specifies the number of bytes to be transferred in the SRB. This member is set by **TapeClassAllocateSrbBuffer**.

-   **TimeOutValue** - Specifies a time-out value for this command, overriding the default time-out value from the tape class driver's device extension.

-   **SrbFlags** - Specifies a flag for this command. The tape miniclass driver must set SRB\_FLAGS\_DATA\_OUT if the SRB is sending data to the tape drive. This member can be zero if the SRB is requesting data from the tape drive or if no data is being transferred by the command.

</dd> <dt>

*CallNumber* \[in\]
</dt> <dd>

Specifies the number of times *TAPE\_PROCESS\_COMMAND\_ROUTINE* has been called to process a given tape command. *CallNumber* is zero the first time this routine is called and is incremented for each subsequent call until the miniclass driver returns a [**TAPE\_STATUS**](tape-status.md) value that indicates the command is complete.

</dd> <dt>

*StatusOfLastCommand* \[in, optional\]
</dt> <dd>

Specifies the status of the last command. In the first call to *TAPE\_PROCESS\_COMMAND\_ROUTINE* to process a given request, *StatusOfLastCommand* is TAPE\_STATUS\_SUCCESS. In subsequent calls, *StatusOfLastCommand* is either TAPE\_STATUS\_SUCCESS or an error status if an error occurred and the tape miniclass driver set RETURN\_ERRORS in *RetryFlags* in the previous call.

</dd> <dt>

*RetryFlags* \[in, out\]
</dt> <dd>

Pointer to a variable that specifies what action the tape class driver should take when a tape device reports an error.

The low-order word specifies the number of retries to perform in the event of a SCSI command failure. The default is zero (no retries).

The high-order word contains flags that specify how the tape class driver should return control if an error occurs:

-   If RETURN\_ERRORS and IGNORE\_ERRORS are clear (the default) the tape class driver returns a failure status to the original requester.

-   If the miniclass driver sets RETURN\_ERRORS, the tape class driver calls *TAPE\_PROCESS\_COMMAND\_ROUTINE* with *StatusOfLastCommand* set to a failure status.

-   If the miniclass driver sets IGNORE\_ERRORS, the tape class driver converts a failure status to success and calls *TAPE\_PROCESS\_COMMAND\_ROUTINE* with *StatusOfLastCommand* set to success.

</dd> </dl>

## Return value



<table>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><dl> <dt><strong>TAPE_STATUS_SEND_SRB_AND_CALLBACK</strong></dt> </dl></td>
<td>Indicates to the tape class driver that the SRB has been filled in and is ready to be sent to the target device. By default, the tape class driver calls <em>TAPE_PROCESS_COMMAND_ROUTINE</em> again only if the SRB succeeds. A miniclass driver can modify the default behavior by setting <em>RetryFlags</em> before returning from <em>TAPE_PROCESS_COMMAND_ROUTINE</em>.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>TAPE_STATUS_CALLBACK</strong></dt> </dl></td>
<td>Directs the tape class driver to increment <em>CallNumber</em> and call <em>TAPE_PROCESS_COMMAND_ROUTINE</em> again without sending an SRB to the tape device. <br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>TAPE_STATUS_CHECK_TEST_UNIT_READY</strong></dt> </dl></td>
<td>Directs the tape class driver to fill in an SRB for the TEST UNIT READY command and send the SRB to the device.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>TAPE_STATUS_<em>XXX</em></strong></dt> </dl></td>
<td>Any other return code indicates to the tape class driver that the command is complete and indicates success, failure, or warning. Possible completion return values for this routine include, but are not limited to:<br/> <dl> TAPE_STATUS_SUCCESS<br/><br />
TAPE_STATUS_INSUFFICIENT_RESOURCES<br/><br />
TAPE_STATUS_INVALID_DEVICE_REQUEST<br/><br />
TAPE_STATUS_INVALID_PARAMETER<br/><br />
TAPE_STATUS_IO_DEVICE_ERROR<br/><br />
TAPE_STATUS_MEDIA_WRITE_PROTECTED<br/><br />
TAPE_STATUS_NOT_IMPLEMENTED<br/><br />
</dl></td>
</tr>
</tbody>
</table>



 

## Remarks

The following functions can be assigned to this callback placeholder:

### CreatePartition

*CreatePartition* handles the device-specific aspects of an [**IOCTL\_TAPE\_CREATE\_PARTITION**](ioctl-tape-create-partition.md) request. This routine is required. *CreatePartition* creates a partition on a tape by filling in the CDB in an SRB passed by the tape class driver. Creating a partition typically requires a series of SRBs to complete the operation. After *CreatePartition* fills in a given SRB and returns, the tape class driver sends the SRB to the target device and, depending on the result of the SRB and the value of *RetryFlags*, calls *TapeMiniCreatePartition* again.

*CreatePartition* must fill in the following members in the SRB before returning to the tape class driver:

If the tape miniclass driver stores partition information in the minitape extension, *CreatePartition* updates the extension before returning to the tape class driver with TAPE\_STATUS\_SUCCESS.

### Erase

*Erase* handles the device-specific aspects of an [**IOCTL\_TAPE\_ERASE**](ioctl-tape-erase.md) request. This routine is required. *Erase* erases a tape by filling in the CDB in an SRB passed by the tape class driver. Erasing a tape typically requires one SRB to complete the operation. After *Erase* fills in the SRB and returns, the tape class driver sends the SRB to the device and, depending on the result of the SRB and the value of *RetryFlags*, calls *Erase* again. *Erase* then returns TAPE\_STATUS\_SUCCESS.

### GetDriveParameters

*GetDriveParameters* handles the device-specific aspects of an [**IOCTL\_TAPE\_GET\_DRIVE\_PARAMS**](ioctl-tape-get-drive-params.md) request. This routine is required. *GetDriveParameters* gets tape drive parameters by filling in the CDB in an SRB passed by the tape class driver. Getting drive parameters typically requires a series of SRBs to complete the operation. After *GetDriveParameters* fills in a given SRB and returns, the tape class driver sends the SRB to the target device and, depending on the result of the SRB and the value of *RetryFlags*, calls *GetDriveParameters* again.

### GetMediaParameters

*GetMediaParameters* handles the device-specific aspects of an [**IOCTL\_TAPE\_GET\_MEDIA\_PARAMS**](ioctl-tape-get-media-params.md) request. This routine is required. *GetMediaParameters* gets tape media parameters by filling in the CDB in an SRB passed by the tape class driver. Getting media parameters typically requires more than one SRB to complete the operation, starting with a test unit ready which the miniclass driver requests by returning TAPE\_STATUS\_CHECK\_TEST\_UNIT\_READY the first time the tape class driver calls the routine.

After *GetMediaParameters* fills in a given SRB and returns, the tape class driver sends the SRB to the device and, depending on the result of the SRB and the value of *RetryFlags*, calls GetMediaParameters again.

### GetMediaTypes

*GetMediaTypes* handles the device-specific aspects of an [**IOCTL\_STORAGE\_GET\_MEDIA\_TYPES\_EX**](ioctl-storage-get-media-types-ex.md) request. This routine is required. *GetMediaTypes* gets information about the media types supported by a tape device by filling in the CDB in an SRB passed by the tape class driver. Getting media types typically requires more than one SRB to complete the operation, starting with a test unit ready which the miniclass driver requests by returning TAPE\_STATUS\_CHECK\_TEST\_UNIT\_READY the first time the tape class driver calls the routine.

### GetPosition

*GetPosition* handles the device-specific aspects of an [**IOCTL\_TAPE\_GET\_POSITION**](ioctl-tape-get-position.md) request. This routine is required. *GetPosition* reads the position of a tape by filling in the CDB in an SRB passed by the tape class driver. Reading tape position typically requires more than one SRB to complete the operation, often starting with a test unit ready which the miniclass driver requests by returning TAPE\_STATUS\_CHECK\_TEST\_UNIT\_READY the first time the tape class driver calls the routine.

### GetStatus

*GetStatus* handles the device-specific aspects of an [**IOCTL\_TAPE\_GET\_STATUS**](ioctl-tape-get-status.md) request. This routine is required. *GetStatus* reads the status of a tape device, typically by directing the tape class driver to issue a test unit ready command.

If a device indicates whether a drive needs cleaning in sense data (as opposed to reporting the need for cleaning as an error, which a miniclass driver would handle in its [**TapeMiniTapeError**](tapeminitapeerror.md) routine), *GetStatus* fills in the CDB in the SRB passed by the tape class driver to obtain the sense data and, if necessary, returns TAPE\_STATUS\_REQUIRES\_CLEANING.

### Prepare

*Prepare* handles the device-specific aspects of an [**IOCTL\_TAPE\_PREPARE**](ioctl-tape-prepare.md) request. This routine is required. *Prepare* prepares a tape by filling in the CDB in an SRB passed by the tape class driver. If the device supports the requested operation, preparing a tape typically requires one SRB. After *Prepare* fills in the SRB and returns, the tape class driver sends the SRB to the device and, depending on the result of the SRB and the value of *RetryFlags*, calls *Prepare* again.

### SetDriveParameters

*SetDriveParameters* handles the device-specific aspects of an [**IOCTL\_TAPE\_SET\_DRIVE\_PARAMS**](ioctl-tape-set-drive-params.md) request. This routine is required. *SetDriveParameters* sets parameters for a tape device by filling in the CDB in an SRB passed by the tape class driver. Setting parameters typically involves a series of SRBs to complete the operation. After *SetDriveParameters* fills in a given SRB and returns, the tape class driver sends the SRB to the device and, depending on the result of the SRB and the value of *RetryFlags*, calls *SetDriveParameters* again.

### SetMediaParameters

*SetMediaParameters* handles the device-specific aspects of an [**IOCTL\_TAPE\_SET\_MEDIA\_PARAMS**](ioctl-tape-set-media-params.md) request. This routine is required. *SetMediaParameters* sets the block size of a tape by filling in the CDB in an SRB passed by the tape class driver. Setting the block size typically requires more than one SRB to complete the operation, starting with a test unit ready which the miniclass driver requests by returning TAPE\_STATUS\_CHECK\_TEST\_UNIT\_READY the first time the tape class driver calls the routine.

After *SetMediaParameters* fills in a given SRB and returns, the tape class driver sends the SRB to the device and, depending on the result of the SRB and the value of *RetryFlags*, calls *SetMediaParameters* again.

### SetPosition

*SetPosition* handles the device-specific aspects of an [**IOCTL\_TAPE\_SET\_POSITION**](ioctl-tape-set-position.md) request. This routine is required. *SetPosition* sets the position of a tape by filling in the CDB in an SRB passed by the tape class driver. Setting the position typically requires one SRB. After *SetPosition* fills in the SRB and returns, the tape class driver sends the SRB to the device and, depending on the result of the SRB and the value of *RetryFlags*, calls *SetPosition* again. *SetPosition* then returns TAPE\_STATUS\_SUCCESS.

### WriteMarks

*WriteMarks* handles the device-specific aspects of an [**IOCTL\_TAPE\_WRITE\_MARKS**](ioctl-tape-write-marks.md) request. This routine is required. *WriteMarks* writes marks to a tape by filling in the CDB in an SRB passed by the tape class driver. Writing marks typically takes one SRB to complete the operation. After *WriteMarks* fills in the SRB and returns, the tape class driver sends the SRB to the device and, depending on the result of the SRB and the value of *RetryFlags*, calls *WriteMarks* again. *WriteMarks* then returns TAPE\_STATUS\_SUCCESS.

### PreProcessReadWrite

*PreProcessReadWrite* is an optional, special-purpose routine that performs any device-specific operations required before read and write operations. Most tape miniclass drivers do not need this routine. The activities of the *PreProcessReadWrite* routine are device specific. The routine can use the information passed to it by the class driver to implement special preprocessing for reads and writes. If a drive has limited capabilities, the driver may need this routine to maintain coherent state, for example.

If a tape miniclass driver sets a non-**NULL** entry point for this routine in the TAPE\_INIT\_DATA\_EX structure it passes to [**TapeClassInitialize**](tapeclassinitialize.md) from its **DriverEntry** routine, the tape class driver calls it before each read and write operation on the tape device. The class driver does not expect any information back from this routine.

### WMIOperations

*WMIOperations* is the common entry point for all WMI calls from the tape class driver. A minidriver that supports WMI should set the function pointer member, **WMIOperations**, in the structure TAPE\_INIT\_DATA\_EX to point to the minidriver's *TAPE\_PROCESS\_COMMAND\_ROUTINE* routine. The minidriver should do this in its DriverEntry routine before calling [**TapeClassInitialize**](tapeclassinitialize.md). If a minidriver does not support WMI operations, it should set TapeWMIOperations field to **NULL**.

The tape class driver assigns values to the members of TAPE\_WMI\_OPERATIONS structure, and passes this structure to minidriver's *WMIOperations* routine in the *CommandParameters* parameter. As with other minidriver routines, *WMIOperations* fills, creates, and initializes the SCSI request blocks (SRB) and the command descriptor blocks (CDB) required to implement the indicated WMI method, and returns control to tape class driver. The tape class driver then calls the port driver to execute the request.

The minidriver returns the WMI data in the buffer pointed to by the **DataBuffer** member of the TAPE\_WMI\_OPERATIONS structure.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Minitape.h (include Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md)
</dt> <dt>

[**TapeClassAllocateSrbBuffer**](tapeclassallocatesrbbuffer.md)
</dt> <dt>

[**TapeClassZeroMemory**](tapeclasszeromemory.md)
</dt> <dt>

[**TAPE\_STATUS**](tape-status.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TAPE_PROCESS_COMMAND_ROUTINE%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






