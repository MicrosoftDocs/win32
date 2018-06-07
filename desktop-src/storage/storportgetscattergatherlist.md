---
title: StorPortGetScatterGatherList routine
description: The StorPortGetScatterGatherList routine retrieves the associated scatter/gather list for the specified SCSI request block (SRB).
ms.assetid: ddb7052d-b9f3-40f6-b00a-6bf52f010cdc
keywords:
- StorPortGetScatterGatherList routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortGetScatterGatherList
api_location:
- Storport.lib
- Storport.dll
api_type:
- LibDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StorPortGetScatterGatherList routine

The **StorPortGetScatterGatherList** routine retrieves the associated scatter/gather list for the specified SCSI request block (SRB).

## Syntax


```C++
STORPORT_API PSTOR_SCATTER_GATHER_LIST StorPortGetScatterGatherList(
  _In_ PVOID               HwDeviceExtension,
  _In_ PSCSI_REQUEST_BLOCK Srb
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport immediately after the miniport driver calls [**StorPortInitialize**](storportinitialize.md). The port driver frees this memory when it removes the device.

</dd> <dt>

*Srb* \[in\]
</dt> <dd>

Pointer to the SRB for which the scatter gather list is to be constructed.

</dd> </dl>

## Return value

**StorPortGetScatterGatherList** returns a pointer to the scatter/gather list.

## Remarks

This routine is provided with the Storport driver library. There is no parallel routine provided in the SCSI port library.

The pointer to the scatter/gather list that is returned is valid only until the SRB is completed.

The miniport driver does not have to free the memory for the scatter/gather list that **StorPortGetScatterGatherList** returns.

The miniport driver must not modify the scatter/gather list.

Starting in Windows 8, the *Srb* parameter may point to either [**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md) or [**STORAGE\_REQUEST\_BLOCK**](storage-request-block.md). If the function identifier in the **Function** field of *Srb* is **SRB\_FUNCTION\_STORAGE\_REQUEST\_BLOCK**, the SRB is a **STORAGE\_REQUEST\_BLOCK** request structure.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>         | <dl> <dt>Storport.lib</dt> </dl>                                                 |



## See also

<dl> <dt>

[**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md)
</dt> <dt>

[**STORAGE\_REQUEST\_BLOCK**](storage-request-block.md)
</dt> <dt>

[**STOR\_SCATTER\_GATHER\_ELEMENT**](stor-scatter-gather-element.md)
</dt> <dt>

[**STOR\_SCATTER\_GATHER\_LIST**](stor-scatter-gather-list.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortGetScatterGatherList%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






