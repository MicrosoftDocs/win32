---
title: ScsiPortCompleteRequest routine
description: The ScsiPortCompleteRequest routine completes all of the active requests for the given SCSI bus, controller, or LU, including a request being processed by the calling miniport driver routine.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models.
ms.assetid: 9cd17a86-6652-414d-a80d-2e61c0ac99b6
keywords:
- ScsiPortCompleteRequest routine Storage Devices
topic_type:
- apiref
api_name:
- ScsiPortCompleteRequest
api_location:
- Scsiport.lib
- Scsiport.dll
api_type:
- LibDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ScsiPortCompleteRequest routine

The **ScsiPortCompleteRequest** routine completes all of the active requests for the given SCSI bus, controller, or LU, including a request being processed by the calling miniport driver routine.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
VOID ScsiPortCompleteRequest(
  _In_ PVOID HwDeviceExtension,
  _In_ UCHAR PathId,
  _In_ UCHAR TargetId,
  _In_ UCHAR Lun,
  _In_ UCHAR SrbStatus
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

Pointer to the hardware device extension. This is a per-HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the HBA's mapped access ranges. This area is available to the miniport driver in the **DeviceExtension-&gt;HwDeviceExtension** member of the HBA's device object immediately after the miniport driver calls [**ScsiPortInitialize**](scsiportinitialize.md). The port driver frees this memory when it removes the device.

</dd> <dt>

*PathId* \[in\]
</dt> <dd>

Identifies the SCSI bus; SP\_UNTAGGED indicates all buses controlled by the HBA.

</dd> <dt>

*TargetId* \[in\]
</dt> <dd>

Identifies the target controller or device on the given buses; SP\_UNTAGGED indicates all targets on the bus.

</dd> <dt>

*Lun* \[in\]
</dt> <dd>

Identifies the logical unit for the given target controller or device; SP\_UNTAGGED indicates all logical units for the given target controllers on the given buses.

</dd> <dt>

*SrbStatus* \[in\]
</dt> <dd>

Specifies the completion status to be set in the **SrbStatus** member of each SRB.

</dd> </dl>

## Return value

None

## Remarks

**ScsiPortCompleteRequest** can be called to complete outstanding requests after a bus reset, a device reset, or an abort, rather than calling [**ScsiPortNotification**](scsiportnotification.md) for each outstanding request individually. After calling **ScsiPortCompleteRequest**, do not also call **ScsiPortNotification**.

## Requirements



|                            |                                                                                                                 |
|----------------------------|-----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                              |
| Header<br/>          | <dl> <dt>Srb.h (include Miniport.h or Scsi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Scsiport.lib</dt> </dl>                         |



## See also

<dl> <dt>

[**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md)
</dt> <dt>

[**ScsiPortNotification**](scsiportnotification.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortCompleteRequest%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






