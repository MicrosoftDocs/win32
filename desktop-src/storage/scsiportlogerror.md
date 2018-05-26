---
title: ScsiPortLogError routine
description: The ScsiPortLogError routine logs errors to the system event log when a miniport driver or its HBA detects a SCSI error condition.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
ms.assetid: 278f4fff-6e71-4544-8838-90f659c5029e
keywords:
- ScsiPortLogError routine Storage Devices
topic_type:
- apiref
api_name:
- ScsiPortLogError
api_location:
- Scsiport.lib
- Scsiport.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ScsiPortLogError routine

The **ScsiPortLogError** routine logs errors to the system event log when a miniport driver or its HBA detects a SCSI error condition.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
VOID ScsiPortLogError(
  _In_     PVOID               HwDeviceExtension,
  _In_opt_ PSCSI_REQUEST_BLOCK Srb,
  _In_     UCHAR               PathId,
  _In_     UCHAR               TargetId,
  _In_     UCHAR               Lun,
  _In_     ULONG               ErrorCode,
  _In_     ULONG               UniqueId
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

Pointer to the hardware device extension. This is a per-HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the HBA's mapped access ranges. This area is available to the miniport driver in the **DeviceExtension-&gt;HwDeviceExtension** member of the HBA's device object immediately after the miniport driver calls [**ScsiPortInitialize**](scsiportinitialize.md). The port driver frees this memory when it removes the device.

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

Specifies a unique identifier for the error. This value differentiates the current error from other errors with the same *ErrorCode*. For some miniport drivers, this identifies the line of code where the error was detected. For others, it is additional information returned by the HBA.

</dd> </dl>

## Return value

None

## Remarks

A miniport driver should log all real hardware errors. However, it should not log common operational errors, such as selection time-outs or bus resets.

## Requirements



|                            |                                                                                                                 |
|----------------------------|-----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                              |
| Header<br/>          | <dl> <dt>Srb.h (include Miniport.h or Scsi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Scsiport.lib</dt> </dl>                         |



## See also

<dl> <dt>

[**ScsiPortNotification**](scsiportnotification.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortLogError%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






