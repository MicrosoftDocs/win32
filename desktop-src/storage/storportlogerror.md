---
title: StorPortLogError routine
description: The StorPortLogError routine notifies the port driver that an error occurred.
ms.assetid: 'f653e6bf-e99b-4aa2-aa54-d7482d326720'
keywords: ["StorPortLogError routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortLogError
api_location:
- Storport.lib
- Storport.dll
api_type:
- LibDef
---

# StorPortLogError routine

The **StorPortLogError** routine notifies the port driver that an error occurred.

## Syntax


```C++
STORPORT_API VOID StorPortLogError(
  _In_     PVOID               HwDeviceExtension,
  _In_opt_ PSCSI_REQUEST_BLOCK Srb,
  _In_     UCHAR               PathId,
  _In_     UCHAR               TargetId,
  _In_     UCHAR               Lun,
  _In_     ULONG               ErrorCode,
  _In_     ULONG               UniqueId
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport immediately after the miniport driver calls [**StorPortInitialize**](storportinitialize.md). The port driver frees this memory when it removes the device.

</dd> <dt>

*Srb* \[in, optional\]
</dt> <dd>

Pointer to a SCSI request block if one is associated with the error. Otherwise, this parameter is **NULL**.

</dd> <dt>

*PathId* \[in\]
</dt> <dd>

Identifies the SCSI bus.

</dd> <dt>

*TargetId* \[in\]
</dt> <dd>

Identifies the target controller or device on the bus.

</dd> <dt>

*Lun* \[in\]
</dt> <dd>

Identifies the logical unit number of the target device.

</dd> <dt>

*ErrorCode* \[in\]
</dt> <dd>

Specifies an error code indicating one of the following values as the type of error.



| Value                                   | Meaning                                                                                                                                 |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| SP\_BAD\_FW\_ERROR<br/>           | Indicates the driver has detected bad or old firmware. The device will not be used.<br/>                                          |
| SP\_BAD\_FW\_WARNING<br/>         | Indicates the driver has detected a card with old or bad firmware, which can result in reduced performance or functionality.<br/> |
| SP\_BUS\_PARITY\_ERROR<br/>       | Indicates a SCSI bus parity error was detected.<br/>                                                                              |
| SP\_BUS\_TIME\_OUT<br/>           | Indicates a SCSI bus connection to a logical unit timed out.<br/>                                                                 |
| SP\_INTERNAL\_ADAPTER\_ERROR<br/> | Indicates an internal HBA error was detected.<br/>                                                                                |
| SP\_INVALID\_RESELECTION<br/>     | Indicates a logical unit reselected unexpectedly or with an invalid queue tag.<br/>                                               |
| SP\_IRQ\_NOT\_RESPONDING<br/>     | Indicates the HBA is not interrupting when expected.<br/>                                                                         |
| SP\_PROTOCOL\_ERROR<br/>          | Indicates the miniport driver detected a SCSI bus protocol error.<br/>                                                            |
| SP\_REQUEST\_TIMEOUT<br/>         | Indicates an operation to the controller has timed out.<br/>                                                                      |
| SP\_UNEXPECTED\_DISCONNECT<br/>   | Indicates that a target disconnected unexpectedly.<br/>                                                                           |



 

</dd> <dt>

*UniqueId* \[in\]
</dt> <dd>

Specifies a unique identifier for the error. This value differentiates the current error from other errors with the same *ErrorCode* value. For some miniport drivers, this identifies the line of code where the error was detected. For others, it is additional information returned by the HBA.

</dd> </dl>

## Return value

None

## Remarks

The port driver will log an error to the system event log.

Starting in Windows 8, the *Srb* parameter may point to either [**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md) or [**STORAGE\_REQUEST\_BLOCK**](storage-request-block.md). If the function identifier in the **Function** field of *Srb* is **SRB\_FUNCTION\_STORAGE\_REQUEST\_BLOCK**, the SRB is a **STORAGE\_REQUEST\_BLOCK** request structure.

## Requirements



|                                 |                                                                                                                                         |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/>      | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>               | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>              | <dl> <dt>Storport.lib</dt> </dl>                                                 |
| DDI compliance rules<br/> | [**StorPortDeprecated**](https://msdn.microsoft.com/library/windows/hardware/hh454263)                                                                           |



## See also

<dl> <dt>

[**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md)
</dt> <dt>

[**ScsiPortLogError**](scsiportlogerror.md)
</dt> <dt>

[**STORAGE\_REQUEST\_BLOCK**](storage-request-block.md)
</dt> <dt>

[**StorPortLogSystemEvent**](storportlogsystemevent.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortLogError%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






