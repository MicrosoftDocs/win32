---
title: ScsiPortWmiGetReturnStatus macro
description: The ScsiPortWmiGetReturnStatus routine returns the status of a WMI SRB.
ms.assetid: 79213f47-ba4c-41b0-b095-1b5c25c79456
keywords:
- ScsiPortWmiGetReturnStatus macro Storage Devices
topic_type:
- apiref
api_name:
- ScsiPortWmiGetReturnStatus
api_location:
- scsiwmi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ScsiPortWmiGetReturnStatus macro

The **ScsiPortWmiGetReturnStatus** routine returns the status of a WMI SRB.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
UCHAR ScsiPortWmiGetReturnStatus(
   PSCSIWMI_REQUEST_CONTEXT RequestContext
);
```



## Parameters

<dl> <dt>

*RequestContext* 
</dt> <dd>

Pointer to the request context for this SRB.

</dd> </dl>

## Return value

The return value represents the return status for the SRB. The miniport driver should set **Srb-&gt;SrbStatus** to the value returned by **ScsiPortWmiGetReturnStatus** before completing the SRB.

## Remarks

A miniport driver must call **ScsiPortWmiGetReturnStatus** to obtain the value to put into **Srb-&gt;SrbStatus**. **ScsiPortWmiGetReturnStatus** should be called sometime after the miniport driver calls **ScsiPortWmiPostProcess.**

## Requirements



|                            |                                                                                                                     |
|----------------------------|---------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                  |
| Header<br/>          | <dl> <dt>Scsiwmi.h (include Miniport.h or Scsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**ScsiPortWmiGetReturnStatus**](scsiportwmigetreturnstatus.md)
</dt> <dt>

[**ScsiPortWmiPostProcess**](scsiportwmipostprocess.md)
</dt> <dt>

[**SCSIWMI\_REQUEST\_CONTEXT**](scsiwmi-request-context.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortWmiGetReturnStatus%20macro%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






