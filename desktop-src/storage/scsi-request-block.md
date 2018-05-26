---
title: SCSI\_REQUEST\_BLOCK structure
description: SCSI\_REQUEST\_BLOCK structure
ms.assetid: ddd5180d-275c-4226-9af8-8e2ae25256e7
keywords:
- SCSI_REQUEST_BLOCK structure Storage Devices
- PSCSI_REQUEST_BLOCK structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SCSI_REQUEST_BLOCK
api_location:
- srb.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SCSI\_REQUEST\_BLOCK structure

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _SCSI_REQUEST_BLOCK {
  USHORT                     Length;
  UCHAR                      Function;
  UCHAR                      SrbStatus;
  UCHAR                      ScsiStatus;
  UCHAR                      PathId;
  UCHAR                      TargetId;
  UCHAR                      Lun;
  UCHAR                      QueueTag;
  UCHAR                      QueueAction;
  UCHAR                      CdbLength;
  UCHAR                      SenseInfoBufferLength;
  ULONG                      SrbFlags;
  ULONG                      DataTransferLength;
  ULONG                      TimeOutValue;
  PVOID                      DataBuffer;
  PVOID                      SenseInfoBuffer;
  struct _SCSI_REQUEST_BLOCK  *NextSrb;
  PVOID                      OriginalRequest;
  PVOID                      SrbExtension;
  union {
    ULONG InternalStatus;
    ULONG QueueSortKey;
    ULONG LinkTimeoutValue;
  };
#ifdef _WIN64
  ULONG                      Reserved;
#endif 
  UCHAR                      Cdb[16];
} SCSI_REQUEST_BLOCK, *PSCSI_REQUEST_BLOCK;
```



## Members

<dl> <dt>

**Length**
</dt> <dd>

Specifies the size in bytes of this structure.

</dd> <dt>

**Function**
</dt> <dd>

Specifies the operation to be performed, which can be one of the following values:

<dt>

<span id="SRB_FUNCTION_EXECUTE_SCSI"></span><span id="srb_function_execute_scsi"></span>

<span id="SRB_FUNCTION_EXECUTE_SCSI"></span><span id="srb_function_execute_scsi"></span>**SRB\_FUNCTION\_EXECUTE\_SCSI** (0x00)


</dt> <dd>

A SCSI device I/O request should be executed on the target logical unit.

</dd> <dt>

<span id="SRB_FUNCTION_ABORT_COMMAND"></span><span id="srb_function_abort_command"></span>

<span id="SRB_FUNCTION_ABORT_COMMAND"></span><span id="srb_function_abort_command"></span>**SRB\_FUNCTION\_ABORT\_COMMAND** (0x10)


</dt> <dd>

A SCSIMESS\_ABORT message should be sent to cancel the request pointed to by the **NextSrb** member. If this is a tagged-queue request, a SCSIMESS\_ABORT\_WITH\_TAG message should be used instead. If the indicated request has been completed, this request should be completed normally. Only the SRB **Function**, **PathId**, **TargetId**, **Lun**, and **NextSrb** members are valid.

</dd> <dt>

<span id="SRB_FUNCTION_RESET_DEVICE"></span><span id="srb_function_reset_device"></span>

<span id="SRB_FUNCTION_RESET_DEVICE"></span><span id="srb_function_reset_device"></span>**SRB\_FUNCTION\_RESET\_DEVICE** (0x13)


</dt> <dd>

The ScsiPort driver no longer sends this SRB to its miniports. Only Storport miniport drivers use this SRB. The SCSI target controller should be reset using the SCSIMESS\_BUS\_DEVICE\_RESET message. The miniport driver should complete any active requests for the target controller. Only the SRB **Function**, **TargetId**, and **PathId** members are valid.

</dd> <dt>

<span id="SRB_FUNCTION_RESET_LOGICAL_UNIT"></span><span id="srb_function_reset_logical_unit"></span>

<span id="SRB_FUNCTION_RESET_LOGICAL_UNIT"></span><span id="srb_function_reset_logical_unit"></span>**SRB\_FUNCTION\_RESET\_LOGICAL\_UNIT** (0x20)


</dt> <dd>

The logical unit should be reset, if possible. The HBA miniport driver should complete any active requests for the logical unit. Only the **Function**, **PathId**, **TargetId**, and **Lun** members of the SRB are valid. Storport supports this type of reset, but SCSI port does not.

</dd> <dt>

<span id="SRB_FUNCTION_RESET_BUS"></span><span id="srb_function_reset_bus"></span>

<span id="SRB_FUNCTION_RESET_BUS"></span><span id="srb_function_reset_bus"></span>**SRB\_FUNCTION\_RESET\_BUS** (0x12)


</dt> <dd>

The SCSI bus should be reset using the SCSIMESS\_BUS\_DEVICE\_RESET message. A miniport driver receives this request only if a given request has timed out and a subsequent request to abort the timed-out request also has timed out. Only the SRB **Function** and **PathId** members are valid.

</dd> <dt>

<span id="SRB_FUNCTION_TERMINATE_IO"></span><span id="srb_function_terminate_io"></span>

<span id="SRB_FUNCTION_TERMINATE_IO"></span><span id="srb_function_terminate_io"></span>**SRB\_FUNCTION\_TERMINATE\_IO** (0x14)


</dt> <dd>

A SCSIMESS\_TERMINATE\_IO\_PROCESS message should be sent to cancel the request pointed to by the **NextSrb** member. If the indicated request has already completed, this request should be completed normally. Only the SRB **Function**, **PathId**, **TargetId**, **Lun**, and **NextSrb** members are valid.

</dd> <dt>

<span id="SRB_FUNCTION_RELEASE_RECOVERY"></span><span id="srb_function_release_recovery"></span>

<span id="SRB_FUNCTION_RELEASE_RECOVERY"></span><span id="srb_function_release_recovery"></span>**SRB\_FUNCTION\_RELEASE\_RECOVERY** (0x11)


</dt> <dd>

A SCSIMESS\_RELEASE\_RECOVERY message should be sent to the target controller. Only the SRB **Function**, **PathId**, **TargetId**, and **Lun** members are valid.

</dd> <dt>

<span id="SRB_FUNCTION_RECEIVE_EVENT"></span><span id="srb_function_receive_event"></span>

<span id="SRB_FUNCTION_RECEIVE_EVENT"></span><span id="srb_function_receive_event"></span>**SRB\_FUNCTION\_RECEIVE\_EVENT** (0x03)


</dt> <dd>

The HBA should be prepared to receive an asynchronous event notification from the addressed target. The SRB **DataBuffer** member indicates where the data should be placed.

</dd> <dt>

<span id="SRB_FUNCTION_SHUTDOWN"></span><span id="srb_function_shutdown"></span>

<span id="SRB_FUNCTION_SHUTDOWN"></span><span id="srb_function_shutdown"></span>**SRB\_FUNCTION\_SHUTDOWN** (0x07)


</dt> <dd>

The system is being shut down. This request is sent to a miniport driver only if it set **CachesData** to **TRUE** in the PORT\_CONFIGURATION\_INFORMATION for the HBA. Such a miniport driver can receive several of these notifications before all system activity actually stops. However, the last shutdown notification will occur after the last start I/O. Only the SRB **Function**, **PathId**, **TargetId** and **Lun** members are valid.

</dd> <dt>

<span id="SRB_FUNCTION_FLUSH"></span><span id="srb_function_flush"></span>

<span id="SRB_FUNCTION_FLUSH"></span><span id="srb_function_flush"></span>**SRB\_FUNCTION\_FLUSH** (0x08)


</dt> <dd>

The miniport driver should flush any cached data for the target device. This request is sent to the miniport driver only if it set **CachesData** to **TRUE** in the PORT\_CONFIGURATION\_INFORMATION for the HBA. Only the SRB **Function**, **PathId**, **TargetId** and **Lun** members are valid.

</dd> <dt>

<span id="SRB_FUNCTION_IO_CONTROL"></span><span id="srb_function_io_control"></span>

<span id="SRB_FUNCTION_IO_CONTROL"></span><span id="srb_function_io_control"></span>**SRB\_FUNCTION\_IO\_CONTROL** (0x02)


</dt> <dd>

The request is an I/O control request, originating in a user-mode application with a dedicated HBA. The SRB **DataBuffer** points to an SRB\_IO\_CONTROL header followed by the data area. The value in **DataBuffer** can be used by the driver, regardless of the value of **MapBuffers**. Only the SRB **Function**, **SrbFlags**, **TimeOutValue**, **DataBuffer**, and **DataTransferLength** members are valid, along with the **SrbExtension** member if the miniport driver requested SRB extensions when it initialized. If a miniport driver controls an application-dedicated HBA so it supports this request, the miniport driver should execute the request and notify the OS-specific port driver when the SRB has completed, using the normal mechanism of calls to [**ScsiPortNotification**](scsiportnotification.md) with **RequestComplete** and **NextRequest**.

</dd> <dt>

<span id="SRB_FUNCTION_LOCK_QUEUE"></span><span id="srb_function_lock_queue"></span>

<span id="SRB_FUNCTION_LOCK_QUEUE"></span><span id="srb_function_lock_queue"></span>**SRB\_FUNCTION\_LOCK\_QUEUE** (0x18)


</dt> <dd>

Holds requests queued by the port driver for a particular logical unit, typically while a power request is being processed. Only the SRB **Length**, **Function**, **SrbFlags**, and **OriginalRequest** members are valid. When the queue is locked, only requests with **SrbFlags** ORed with SRB\_FLAGS\_BYPASS\_LOCKED\_QUEUE will be processed. SCSI miniport drivers do not process SRB\_FUNCTION\_LOCK\_QUEUE requests.

</dd> <dt>

<span id="SRB_FUNCTION_UNLOCK_QUEUE"></span><span id="srb_function_unlock_queue"></span>

<span id="SRB_FUNCTION_UNLOCK_QUEUE"></span><span id="srb_function_unlock_queue"></span>**SRB\_FUNCTION\_UNLOCK\_QUEUE** (0x19)


</dt> <dd>

Releases the port driver's queue for a logical unit that was previously locked with SRB\_FUNCTION\_LOCK\_QUEUE. The **SrbFlags** of the unlock request must be ORed with SRB\_FLAGS\_BYPASS\_LOCKED\_QUEUE. Only the SRB **Length**, **Function**, **SrbFlags**, and **OriginalRequest** members are valid. SCSI miniport drivers do not process SRB\_FUNCTION\_UNLOCK\_QUEUE requests.

</dd> <dt>

<span id="SRB_FUNCTION_DUMP_POINTERS"></span><span id="srb_function_dump_pointers"></span>

<span id="SRB_FUNCTION_DUMP_POINTERS"></span><span id="srb_function_dump_pointers"></span>**SRB\_FUNCTION\_DUMP\_POINTERS** (0x26)


</dt> <dd>

A request with this function is sent to a Storport miniport driver that is used to control the disk that holds the crash dump data. The request collects information needed from the miniport driver to support crash dump and hibernation. See the **MINIPORT\_DUMP\_POINTERS** structure. A physical miniport driver must set the STOR\_FEATURE\_DUMP\_POINTERS flag in the **FeatureSupport** member of its [**HW\_INITIALIZATION\_DATA**](hw-initialization-data--storport-.md) to receive a request with this function.

</dd> <dt>

<span id="SRB_FUNCTION_FREE_DUMP_POINTERS"></span><span id="srb_function_free_dump_pointers"></span>

<span id="SRB_FUNCTION_FREE_DUMP_POINTERS"></span><span id="srb_function_free_dump_pointers"></span>**SRB\_FUNCTION\_FREE\_DUMP\_POINTERS** (0x27)


</dt> <dd>

A request with this function is sent to a Storport miniport driver to release any resources allocated during a previous request for SRB\_FUNCTION\_DUMP\_POINTERS.

</dd> </dl> </dd> <dt>

**SrbStatus**
</dt> <dd>

Returns the status of the completed request. This member should be set by the miniport driver before it notifies the OS-specific driver that the request has completed by calling [**ScsiPortNotification**](scsiportnotification.md) with **RequestComplete**. The value of this member can be one of the following:

<dt>

<span id="SRB_STATUS_PENDING"></span><span id="srb_status_pending"></span>

<span id="SRB_STATUS_PENDING"></span><span id="srb_status_pending"></span>**SRB\_STATUS\_PENDING**


</dt> <dd>

Indicates the request is in progress. The OS-specific port driver initializes **SrbStatus** to this value.

</dd> <dt>

<span id="SRB_STATUS_SUCCESS"></span><span id="srb_status_success"></span>

<span id="SRB_STATUS_SUCCESS"></span><span id="srb_status_success"></span>**SRB\_STATUS\_SUCCESS**


</dt> <dd>

Indicates the request was completed successfully.

</dd> <dt>

<span id="SRB_STATUS_ABORTED"></span><span id="srb_status_aborted"></span>

<span id="SRB_STATUS_ABORTED"></span><span id="srb_status_aborted"></span>**SRB\_STATUS\_ABORTED**


</dt> <dd>

Indicates the request was aborted as directed by the port driver. A miniport driver sets this status in the **NextSrb** for a successful SRB\_FUNCTION\_ABORT\_COMMAND request.

</dd> <dt>

<span id="SRB_STATUS_ABORT_FAILED"></span><span id="srb_status_abort_failed"></span>

<span id="SRB_STATUS_ABORT_FAILED"></span><span id="srb_status_abort_failed"></span>**SRB\_STATUS\_ABORT\_FAILED**


</dt> <dd>

Indicates an attempt to abort the request failed. Return this status for an SRB\_FUNCTION\_ABORT\_COMMAND request when the specified request cannot be located.

</dd> <dt>

<span id="SRB_STATUS_ERROR"></span><span id="srb_status_error"></span>

<span id="SRB_STATUS_ERROR"></span><span id="srb_status_error"></span>**SRB\_STATUS\_ERROR**


</dt> <dd>

Indicates the request was completed with an error in the SCSI bus status.

</dd> <dt>

<span id="SRB_STATUS_BUSY"></span><span id="srb_status_busy"></span>

<span id="SRB_STATUS_BUSY"></span><span id="srb_status_busy"></span>**SRB\_STATUS\_BUSY**


</dt> <dd>

Indicates the miniport driver or target device could not accept the request at this time. The OS-specific port driver will resubmit the request later.

</dd> <dt>

<span id="SRB_STATUS_INTERNAL_ERROR"></span><span id="srb_status_internal_error"></span>

<span id="SRB_STATUS_INTERNAL_ERROR"></span><span id="srb_status_internal_error"></span>**SRB\_STATUS\_INTERNAL\_ERROR**


</dt> <dd>

Indicates that the SCSI Port driver could not deliver the request to the miniport driver or target device. In such cases, status is recorded in **InternalStatus**.

</dd> <dt>

<span id="SRB_STATUS_INVALID_REQUEST"></span><span id="srb_status_invalid_request"></span>

<span id="SRB_STATUS_INVALID_REQUEST"></span><span id="srb_status_invalid_request"></span>**SRB\_STATUS\_INVALID\_REQUEST**


</dt> <dd>

Indicates the miniport driver does not support the given request.

</dd> <dt>

<span id="SRB_STATUS_NO_DEVICE"></span><span id="srb_status_no_device"></span>

<span id="SRB_STATUS_NO_DEVICE"></span><span id="srb_status_no_device"></span>**SRB\_STATUS\_NO\_DEVICE**


</dt> <dd>

Indicates the device did not respond.

</dd> <dt>

<span id="SRB_STATUS_TIMEOUT"></span><span id="srb_status_timeout"></span>

<span id="SRB_STATUS_TIMEOUT"></span><span id="srb_status_timeout"></span>**SRB\_STATUS\_TIMEOUT**


</dt> <dd>

Indicates the request timed out.

</dd> <dt>

<span id="SRB_STATUS_SELECTION_TIMEOUT"></span><span id="srb_status_selection_timeout"></span>

<span id="SRB_STATUS_SELECTION_TIMEOUT"></span><span id="srb_status_selection_timeout"></span>**SRB\_STATUS\_SELECTION\_TIMEOUT**


</dt> <dd>

Indicates the SCSI device selection timed out.

</dd> <dt>

<span id="SRB_STATUS_COMMAND_TIMEOUT"></span><span id="srb_status_command_timeout"></span>

<span id="SRB_STATUS_COMMAND_TIMEOUT"></span><span id="srb_status_command_timeout"></span>**SRB\_STATUS\_COMMAND\_TIMEOUT**


</dt> <dd>

Indicates the target did not complete the command within the time limit.

</dd> <dt>

<span id="SRB_STATUS_MESSAGE_REJECTED"></span><span id="srb_status_message_rejected"></span>

<span id="SRB_STATUS_MESSAGE_REJECTED"></span><span id="srb_status_message_rejected"></span>**SRB\_STATUS\_MESSAGE\_REJECTED**


</dt> <dd>

Indicates the target rejected a message. This is normally returned only for such message-type requests as SRB\_FUNCTION\_TERMINATE\_IO.

</dd> <dt>

<span id="SRB_STATUS_BUS_RESET"></span><span id="srb_status_bus_reset"></span>

<span id="SRB_STATUS_BUS_RESET"></span><span id="srb_status_bus_reset"></span>**SRB\_STATUS\_BUS\_RESET**


</dt> <dd>

Indicates a bus reset occurred while this request was being executed.

</dd> <dt>

<span id="SRB_STATUS_PARITY_ERROR"></span><span id="srb_status_parity_error"></span>

<span id="SRB_STATUS_PARITY_ERROR"></span><span id="srb_status_parity_error"></span>**SRB\_STATUS\_PARITY\_ERROR**


</dt> <dd>

Indicates a parity error occurred on the SCSI bus and that a retry failed.

</dd> <dt>

<span id="SRB_STATUS_REQUEST_SENSE_FAILED"></span><span id="srb_status_request_sense_failed"></span>

<span id="SRB_STATUS_REQUEST_SENSE_FAILED"></span><span id="srb_status_request_sense_failed"></span>**SRB\_STATUS\_REQUEST\_SENSE\_FAILED**


</dt> <dd>

Indicates the request-sense command failed. This is returned only if the HBA performs auto request sense and the miniport driver set **AutoRequestSense** to **TRUE** in the PORT\_CONFIGURATION\_INFORMATION for this HBA.

</dd> <dt>

<span id="SRB_STATUS_NO_HBA"></span><span id="srb_status_no_hba"></span>

<span id="SRB_STATUS_NO_HBA"></span><span id="srb_status_no_hba"></span>**SRB\_STATUS\_NO\_HBA**


</dt> <dd>

Indicates the HBA does not respond.

</dd> <dt>

<span id="SRB_STATUS_DATA_OVERRUN"></span><span id="srb_status_data_overrun"></span>

<span id="SRB_STATUS_DATA_OVERRUN"></span><span id="srb_status_data_overrun"></span>**SRB\_STATUS\_DATA\_OVERRUN**


</dt> <dd>

Indicates that a data overrun or underrun error occurred. The miniport driver also must update the SRB's **DataTransferLength** member to indicate how much data actually was transferred if an underrun occurs.

</dd> <dt>

<span id="SRB_STATUS_UNEXPECTED_BUS_FREE"></span><span id="srb_status_unexpected_bus_free"></span>

<span id="SRB_STATUS_UNEXPECTED_BUS_FREE"></span><span id="srb_status_unexpected_bus_free"></span>**SRB\_STATUS\_UNEXPECTED\_BUS\_FREE**


</dt> <dd>

Indicates the target disconnected unexpectedly.

</dd> <dt>

<span id="SRB_STATUS_PHASE_SEQUENCE_FAILURE"></span><span id="srb_status_phase_sequence_failure"></span>

<span id="SRB_STATUS_PHASE_SEQUENCE_FAILURE"></span><span id="srb_status_phase_sequence_failure"></span>**SRB\_STATUS\_PHASE\_SEQUENCE\_FAILURE**


</dt> <dd>

Indicates the HBA detected an illegal phase sequence failure error.

</dd> <dt>

<span id="SRB_STATUS_REQUEST_FLUSHED"></span><span id="srb_status_request_flushed"></span>

<span id="SRB_STATUS_REQUEST_FLUSHED"></span><span id="srb_status_request_flushed"></span>**SRB\_STATUS\_REQUEST\_FLUSHED**


</dt> <dd>

Indicates the request for status was stopped.

</dd> <dt>

<span id="SRB_STATUS_BAD_FUNCTION"></span><span id="srb_status_bad_function"></span>

<span id="SRB_STATUS_BAD_FUNCTION"></span><span id="srb_status_bad_function"></span>**SRB\_STATUS\_BAD\_FUNCTION**


</dt> <dd>

Indicates the SRB **Function** code is not supported.

</dd> <dt>

<span id="SRB_STATUS_INVALID_PATH_ID"></span><span id="srb_status_invalid_path_id"></span>

<span id="SRB_STATUS_INVALID_PATH_ID"></span><span id="srb_status_invalid_path_id"></span>**SRB\_STATUS\_INVALID\_PATH\_ID**


</dt> <dd>

Indicates the **PathId** specified in the SRB does not exist.

</dd> <dt>

<span id="SRB_STATUS_INVALID_TARGET_ID"></span><span id="srb_status_invalid_target_id"></span>

<span id="SRB_STATUS_INVALID_TARGET_ID"></span><span id="srb_status_invalid_target_id"></span>**SRB\_STATUS\_INVALID\_TARGET\_ID**


</dt> <dd>

Indicates the **TargetID** value in the SRB is invalid.

</dd> <dt>

<span id="SRB_STATUS_INVALID_LUN"></span><span id="srb_status_invalid_lun"></span>

<span id="SRB_STATUS_INVALID_LUN"></span><span id="srb_status_invalid_lun"></span>**SRB\_STATUS\_INVALID\_LUN**


</dt> <dd>

Indicates the **Lun** value in the SRB is invalid.

</dd> <dt>

<span id="SRB_STATUS_ERROR_RECOVERY"></span><span id="srb_status_error_recovery"></span>

<span id="SRB_STATUS_ERROR_RECOVERY"></span><span id="srb_status_error_recovery"></span>**SRB\_STATUS\_ERROR\_RECOVERY**


</dt> <dd>

Indicates the request was completed with an error in the SCSI bus status and that the SCSI INITIATE RECOVERY message was received.

</dd> <dt>

<span id="SRB_STATUS_AUTOSENSE_VALID"></span><span id="srb_status_autosense_valid"></span>

<span id="SRB_STATUS_AUTOSENSE_VALID"></span><span id="srb_status_autosense_valid"></span>**SRB\_STATUS\_AUTOSENSE\_VALID**


</dt> <dd>

Indicates information returned in the **SenseInfoBuffer** is valid.

</dd> <dt>

<span id="SRB_STATUS_QUEUE_FROZEN"></span><span id="srb_status_queue_frozen"></span>

<span id="SRB_STATUS_QUEUE_FROZEN"></span><span id="srb_status_queue_frozen"></span>**SRB\_STATUS\_QUEUE\_FROZEN**


</dt> <dd>

A miniport driver should *never* set the **SrbStatus** member to this value. The Windows port driver can set this value to inform a storage class driver that its queue of requests for a particular peripheral has been frozen.

</dd> </dl> </dd> <dt>

**ScsiStatus**
</dt> <dd>

Returns the SCSI status that was returned by the HBA or target device. If the status is not SUCCESS, the miniport driver should set the **SrbStatus** member to SRB\_STATUS\_ERROR.

</dd> <dt>

**PathId**
</dt> <dd>

Indicates the SCSI port or bus for the request. This value is zero-based.

</dd> <dt>

**TargetId**
</dt> <dd>

Indicates the target controller or device on the bus.

</dd> <dt>

**Lun**
</dt> <dd>

Indicates the logical unit number of the device.

</dd> <dt>

**QueueTag**
</dt> <dd>

Contains the queue-tag value assigned by the OS-specific port driver. If this member is used for tagged queuing, the HBA supports internal queuing of requests to LUs and the miniport driver set **TaggedQueueing** to **TRUE** in the PORT\_CONFIGURATION\_INFORMATION for this HBA.

</dd> <dt>

**QueueAction**
</dt> <dd>

Indicates the tagged-queuing message to be used when the SRB\_FLAGS\_QUEUE\_ACTION\_ENABLE flag is set. The value can be one of the following: SRB\_SIMPLE\_TAG\_REQUEST, SRB\_HEAD\_OF\_QUEUE\_TAG\_REQUEST, or SRB\_ORDERED\_QUEUE\_TAG\_REQUEST, as defined according to the SCSI specification.

</dd> <dt>

**CdbLength**
</dt> <dd>

Indicates the size in bytes of the SCSI-2 or later command descriptor block.

</dd> <dt>

**SenseInfoBufferLength**
</dt> <dd>

Indicates the size in bytes of the request-sense buffer. If an underrun occurs, the miniport driver must update this member to the number of bytes actually transferred.

</dd> <dt>

**SrbFlags**
</dt> <dd>

Indicates various parameters and options about the request. **SrbFlags** is read-only, except when SRB\_FLAGS\_UNSPECIFIED\_DIRECTION is set and miniport drivers of subordinate DMA adapters are required to update SRB\_FLAGS\_DATA\_IN or SRB\_FLAGS\_DATA\_OUT. This member can have one or more of the following flags set:

<dt>

<span id="SRB_FLAGS_QUEUE_ACTION_ENABLE"></span><span id="srb_flags_queue_action_enable"></span>

<span id="SRB_FLAGS_QUEUE_ACTION_ENABLE"></span><span id="srb_flags_queue_action_enable"></span>**SRB\_FLAGS\_QUEUE\_ACTION\_ENABLE**


</dt> <dd>

Indicates tagged-queue actions are to be enabled.

</dd> <dt>

<span id="SRB_FLAGS_DISABLE_AUTOSENSE"></span><span id="srb_flags_disable_autosense"></span>

<span id="SRB_FLAGS_DISABLE_AUTOSENSE"></span><span id="srb_flags_disable_autosense"></span>**SRB\_FLAGS\_DISABLE\_AUTOSENSE**


</dt> <dd>

Indicates that request-sense information should not be returned.

</dd> <dt>

<span id="SRB_FLAGS_DATA_IN"></span><span id="srb_flags_data_in"></span>

<span id="SRB_FLAGS_DATA_IN"></span><span id="srb_flags_data_in"></span>**SRB\_FLAGS\_DATA\_IN**


</dt> <dd>

Indicates data will be transferred from the device to the system.

</dd> <dt>

<span id="SRB_FLAGS_DATA_OUT"></span><span id="srb_flags_data_out"></span>

<span id="SRB_FLAGS_DATA_OUT"></span><span id="srb_flags_data_out"></span>**SRB\_FLAGS\_DATA\_OUT**


</dt> <dd>

Indicates data will be transferred from the system to the device.

</dd> <dt>

<span id="SRB_FLAGS_UNSPECIFIED_DIRECTION"></span><span id="srb_flags_unspecified_direction"></span>

<span id="SRB_FLAGS_UNSPECIFIED_DIRECTION"></span><span id="srb_flags_unspecified_direction"></span>**SRB\_FLAGS\_UNSPECIFIED\_DIRECTION**


</dt> <dd>

Defined for backward compatibility with the ASPI/CAM SCSI interfaces, this flag indicates that the transfer direction could be either of the preceding because both of the preceding flags are set. If this flag is set, a miniport driver should determine the transfer direction by examining the data phase for the target on the SCSI bus. If its HBA is a subordinate DMA device, such a miniport driver must update SRB\_FLAGS\_DATA\_OUT or SRB\_FLAGS\_DATA\_IN to the correct value before it calls [**ScsiPortIoMapTransfer**](scsiportiomaptransfer.md).

</dd> <dt>

<span id="SRB_FLAGS_NO_DATA_TRANSFER"></span><span id="srb_flags_no_data_transfer"></span>

<span id="SRB_FLAGS_NO_DATA_TRANSFER"></span><span id="srb_flags_no_data_transfer"></span>**SRB\_FLAGS\_NO\_DATA\_TRANSFER**


</dt> <dd>

Indicates no data transfer with this request. If this is set, the flags SRB\_FLAGS\_DATA\_OUT, SRB\_FLAGS\_DATA\_IN, and SRB\_FLAGS\_UNSPECIFIED\_DIRECTION are clear.

</dd> <dt>

<span id="SRB_FLAGS_DISABLE_SYNCH_TRANSFER"></span><span id="srb_flags_disable_synch_transfer"></span>

<span id="SRB_FLAGS_DISABLE_SYNCH_TRANSFER"></span><span id="srb_flags_disable_synch_transfer"></span>**SRB\_FLAGS\_DISABLE\_SYNCH\_TRANSFER**


</dt> <dd>

Indicates the HBA, if possible, should perform asynchronous I/O for this transfer request. If synchronous I/O was negotiated previously, the HBA must renegotiate for asynchronous I/O before performing the transfer.

</dd> <dt>

<span id="SRB_FLAGS_DISABLE_DISCONNECT"></span><span id="srb_flags_disable_disconnect"></span>

<span id="SRB_FLAGS_DISABLE_DISCONNECT"></span><span id="srb_flags_disable_disconnect"></span>**SRB\_FLAGS\_DISABLE\_DISCONNECT**


</dt> <dd>

Indicates the HBA should not allow the target to disconnect from the SCSI bus during processing of this request.

</dd> <dt>

<span id="SRB_FLAGS_BYPASS_FROZEN_QUEUE"></span><span id="srb_flags_bypass_frozen_queue"></span>

<span id="SRB_FLAGS_BYPASS_FROZEN_QUEUE"></span><span id="srb_flags_bypass_frozen_queue"></span>**SRB\_FLAGS\_BYPASS\_FROZEN\_QUEUE**


</dt> <dd>

Is irrelevant to miniport drivers.

</dd> <dt>

<span id="SRB_FLAGS_NO_QUEUE_FREEZE"></span><span id="srb_flags_no_queue_freeze"></span>

<span id="SRB_FLAGS_NO_QUEUE_FREEZE"></span><span id="srb_flags_no_queue_freeze"></span>**SRB\_FLAGS\_NO\_QUEUE\_FREEZE**


</dt> <dd>

Is irrelevant to miniport drivers.

</dd> <dt>

<span id="SRB_FLAGS_IS_ACTIVE"></span><span id="srb_flags_is_active"></span>

<span id="SRB_FLAGS_IS_ACTIVE"></span><span id="srb_flags_is_active"></span>**SRB\_FLAGS\_IS\_ACTIVE**


</dt> <dd>

Is irrelevant to miniport drivers.

</dd> <dt>

<span id="SRB_FLAGS_ALLOCATED_FROM_ZONE"></span><span id="srb_flags_allocated_from_zone"></span>

<span id="SRB_FLAGS_ALLOCATED_FROM_ZONE"></span><span id="srb_flags_allocated_from_zone"></span>**SRB\_FLAGS\_ALLOCATED\_FROM\_ZONE**


</dt> <dd>

Is irrelevant to miniport drivers and is obsolete to current Windows class drivers. To a Windows legacy class driver, this indicates whether the SRB was allocated from a zone buffer. If this flag is set, the class driver must call [**ExInterlockedFreeToZone**](https://msdn.microsoft.com/library/windows/hardware/ff545387) to release the SRB; otherwise, it must call [**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590). New class drivers should use lookaside lists rather than zone buffers.

</dd> <dt>

<span id="SRB_FLAGS_SGLIST_FROM_POOL"></span><span id="srb_flags_sglist_from_pool"></span>

<span id="SRB_FLAGS_SGLIST_FROM_POOL"></span><span id="srb_flags_sglist_from_pool"></span>**SRB\_FLAGS\_SGLIST\_FROM\_POOL**


</dt> <dd>

Is irrelevant to miniport drivers. To a Windows class driver, this indicates that memory for a scatter/gather list was allocated from nonpaged pool. If this flag is set, the class driver must call [**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590) to release the memory after the SRB is completed.

</dd> <dt>

<span id="SRB_FLAGS_BYPASS_LOCKED_QUEUE"></span><span id="srb_flags_bypass_locked_queue"></span>

<span id="SRB_FLAGS_BYPASS_LOCKED_QUEUE"></span><span id="srb_flags_bypass_locked_queue"></span>**SRB\_FLAGS\_BYPASS\_LOCKED\_QUEUE**


</dt> <dd>

Is irrelevant to miniport drivers. To the port driver, this flag indicates that the request should be processed whether the logical-unit queue is locked. A higher-level driver must set this flag to send an SRB\_FUNCTION\_UNLOCK\_QUEUE request.

</dd> <dt>

<span id="SRB_FLAGS_NO_KEEP_AWAKE"></span><span id="srb_flags_no_keep_awake"></span>

<span id="SRB_FLAGS_NO_KEEP_AWAKE"></span><span id="srb_flags_no_keep_awake"></span>**SRB\_FLAGS\_NO\_KEEP\_AWAKE**


</dt> <dd>

Is irrelevant to miniport drivers. A Windows class driver uses this flag to indicate to the port driver to report idle rather than powering up the device to handle this request.

</dd> <dt>

<span id="SRB_FLAGS_FREE_SENSE_BUFFER"></span><span id="srb_flags_free_sense_buffer"></span>

<span id="SRB_FLAGS_FREE_SENSE_BUFFER"></span><span id="srb_flags_free_sense_buffer"></span>**SRB\_FLAGS\_FREE\_SENSE\_BUFFER**


</dt> <dd>

Indicates that either the port or the miniport driver has allocated a buffer for sense data. This informs the class driver that it must free the sense data buffer after extracting the data.

</dd> </dl> </dd> <dt>

**DataTransferLength**
</dt> <dd>

Indicates the size in bytes of the data buffer. If an underrun occurs, the miniport driver must update this member to the number of bytes actually transferred.

</dd> <dt>

**TimeOutValue**
</dt> <dd>

Indicates the interval in seconds that the request can execute before the OS-specific port driver might consider it timed out. Miniport drivers are not required to time requests because the port driver already does.

</dd> <dt>

**DataBuffer**
</dt> <dd>

Points to the data buffer. Miniport drivers should not use this value as a data pointer unless the miniport driver set **MapBuffers** to **TRUE** in the PORT\_CONFIGURATION\_INFORMATION for the HBA. In the case of SRB\_FUNCTION\_IO\_CONTROL requests, however, miniport drivers can use this value as a data pointer regardless of the value of **MapBuffers**.

</dd> <dt>

**SenseInfoBuffer**
</dt> <dd>

Points to the request-sense buffer. A miniport driver is not required to provide request-sense data after a CHECK CONDITION.

</dd> <dt>

**NextSrb**
</dt> <dd>

Indicates the SCSI\_REQUEST\_BLOCK to which this request applies. Only a small subset of requests use a second SRB, for example SRB\_FUNCTION\_ABORT\_COMMAND.

</dd> <dt>

**OriginalRequest**
</dt> <dd>

Points to the IRP for this request. This member is irrelevant to miniport drivers

</dd> <dt>

**SrbExtension**
</dt> <dd>

Points to the Srb extension. A miniport driver must not use this member if it set **SrbExtensionSize** to zero in the SCSI\_HW\_INITIALIZATION\_DATA. The memory at **SrbExtension** is not initialized by the OS-specific port driver, and the miniport driver-determined data can be accessed directly by the HBA. The corresponding physical address can be obtained by calling [**ScsiPortGetPhysicalAddress**](scsiportgetphysicaladdress.md) with the **SrbExtension** pointer.

</dd> <dt>

**InternalStatus**
</dt> <dd>

Used by the SCSI Port driver, instead of **SrbStatus**, to report the status of the completed request whenever the request cannot be delivered to the miniport driver. In such cases, **SrbStatus** is set to SRB\_STATUS\_INTERNAL\_ERROR. This member is used exclusively for communication between the SCSI Port and the class driver and should not be used by miniport drivers.

</dd> <dt>

**QueueSortKey**
</dt> <dd>

Specifies the offset from the start of the media or zero, depending on the type of the target device.

</dd> <dt>

**LinkTimeoutValue**
</dt> <dd> <dl> <dt>

offset 2c 
</dt> <dt>


</dt> </dl> </dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**Cdb**
</dt> <dd>

Specifies the SCSI-2 or later command descriptor block to be sent to the target device.

</dd> </dl>

## Remarks

Windows storage class and filter drivers can send SRBs with the following **Function** values to the system port driver:

-   SRB\_FUNCTION\_CLAIM\_DEVICE to indicate that the class driver supports a peripheral identified in the SRB by the **PathId**, **TargetId**, and **Lun** members.

-   SRB\_ATTACH\_DEVICE to indicate that a filter driver, layered above a class driver, wants requests for a particular peripheral to be routed first to the filter driver.

-   SRB\_FUNCTION\_RELEASE\_DEVICE to indicate that a class driver is releasing its claim on a particular peripheral.

-   SRB\_FUNCTION\_FLUSH\_QUEUE to request cancellation of any requests currently queued in the port driver to a particular peripheral.

-   SRB\_FUNCTION\_RELEASE\_QUEUE to request that the port driver release a frozen queue of requests to a particular peripheral.

The preceding SRB\_FUNCTION\_*XXX* are never set in SRBs sent to SCSI miniport drivers. SRB\_FUNCTION\_REMOVE\_DEVICE is defined for use in future versions of the system. It, too, is never set in SRBs sent to SCSI miniport drivers. SRB\_FUNCTION\_WMI\_REQUEST is valid only in SCSI\_WMI\_REQUEST\_BLOCK. A storage class or filter driver uses this to send WMI requests to the port driver.

## Requirements



|                   |                                                                                                                             |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Srb.h (include Srb.h, Minitape.h, or Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**ExFreePool**](https://msdn.microsoft.com/library/windows/hardware/ff544590)
</dt> <dt>

[**ExInterlockedFreeToZone**](https://msdn.microsoft.com/library/windows/hardware/ff545387)
</dt> <dt>

[**HW\_INITIALIZATION\_DATA (SCSI)**](hw-initialization-data--scsi-.md)
</dt> <dt>

[**PORT\_CONFIGURATION\_INFORMATION (SCSI)**](port-configuration-information--scsi-.md)
</dt> <dt>

[**SCSI\_WMI\_REQUEST\_BLOCK**](scsi-wmi-request-block.md)
</dt> <dt>

[**ScsiPortGetPhysicalAddress**](scsiportgetphysicaladdress.md)
</dt> <dt>

[**ScsiPortGetSrb**](scsiportgetsrb.md)
</dt> <dt>

[**ScsiPortIoMapTransfer**](scsiportiomaptransfer.md)
</dt> <dt>

[**ScsiPortNotification**](scsiportnotification.md)
</dt> <dt>

[**SRB\_IO\_CONTROL**](srb-io-control.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SCSI_REQUEST_BLOCK%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






