---
title: PHW\_STARTIO routine
description: All miniport drivers must have a HwScsiStartIo routine.
ms.assetid: 95e6beb7-ed01-4386-9ee4-33ac30478e1a
keywords:
- HwScsiStartIo routine Storage Devices
- PHW_STARTIO
topic_type:
- apiref
api_name:
- HwScsiStartIo
api_location:
- miniport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PHW\_STARTIO routine

All miniport drivers must have a *HwScsiStartIo* routine. The operating system-specific port driver calls *HwScsiStartIo* first with each incoming I/O request for a target on a SCSI bus.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
BOOLEAN HwScsiStartIo(
  _In_ PVOID               DeviceExtension,
  _In_ PSCSI_REQUEST_BLOCK Srb
);
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Points to the miniport driver's per-HBA storage area.

</dd> <dt>

*Srb* \[in\]
</dt> <dd>

Points to the SCSI request block to be started.

</dd> </dl>

## Return value

*HwScsiStartIo* returns **TRUE** to acknowledge receipt of the SRB.

## Remarks

As soon as it receives the initial request for a target peripheral, the operating system-specific port driver calls the *HwScsiStartIo* routine with an input SRB. After this call, the HBA miniport driver owns the request and is expected to complete it.

Subsequently, the operating system-specific port driver calls the *HwScsiStartIo* routine after the port driver receives each **NextRequest**, **NextLuRequest,** or notification as the miniport driver makes calls to **ScsiPortNotification** and/or **ScsiPortCompleteRequest**.

When the *HwScsiStartIo* routine is called but the driver needs to defer processing of the given SRB, *HwScsiStartIo* should do the following:

1.  Set the **SrbStatus** member to SRB\_STATUS\_BUSY.

2.  Call **ScsiPortNotification** with the request to be deferred and a notification type of **RequestComplete**.

3.  Return **TRUE**.

The port driver requeues such a request and resubmits it later.

The name *HwScsiStartIo* is just a placeholder. The actual prototype of this routine is defined in *srb.h* as follows:


```
typedef
BOOLEAN
(*PHW_STARTIO) (
  IN PVOID  DeviceExtension,
  IN PSCSI_REQUEST_BLOCK  Srb
  );
```



For more information about the *HwScsiStartIo* routine, see [SCSI Miniport Driver's HwScsiStartIo Routine](https://msdn.microsoft.com/library/windows/hardware/ff565336).

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Miniport.h (include Scsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**ScsiPortCompleteRequest**](scsiportcompleterequest.md)
</dt> <dt>

[**ScsiPortNotification**](scsiportnotification.md)
</dt> <dt>

[**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PHW_STARTIO%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






