---
title: ScsiPortGetSrb routine
description: The ScsiPortGetSrb routine returns a pointer to an active SCSI request for a particular logical unit.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
ms.assetid: c8f0e47c-4d06-445f-a6dd-9bd80fc490bc
keywords:
- ScsiPortGetSrb routine Storage Devices
topic_type:
- apiref
api_name:
- ScsiPortGetSrb
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

# ScsiPortGetSrb routine

The **ScsiPortGetSrb** routine returns a pointer to an active SCSI request for a particular logical unit.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
PSCSI_REQUEST_BLOCK ScsiPortGetSrb(
  _In_ PVOID DeviceExtension,
  _In_ UCHAR PathId,
  _In_ UCHAR TargetId,
  _In_ UCHAR Lun,
  _In_ LONG  QueueTag
);
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Pointer to the miniport driver's per-HBA storage area.

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

*QueueTag* \[in\]
</dt> <dd>

Specifies the queue tag if the miniport driver handles tagged requests; SP\_UNTAGGED indicates that the request is not tagged.

</dd> </dl>

## Return value

**ScsiPortGetSrb** returns a pointer to a request for the specified logical unit. If there is no outstanding request for the given peripheral or if the *QueueTag* value is invalid, it returns **NULL**.

## Requirements



|                            |                                                                                                                 |
|----------------------------|-----------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                              |
| Header<br/>          | <dl> <dt>Srb.h (include Miniport.h or Scsi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Scsiport.lib</dt> </dl>                         |



## See also

<dl> <dt>

[**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortGetSrb%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






