---
title: ScsiPortWmiPostProcess routine
description: The ScsiPortWmiPostProcess routine updates a request context for a WMI SRB.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
ms.assetid: da1770bc-2233-47ef-afab-cfcb34edb4b9
keywords:
- ScsiPortWmiPostProcess routine Storage Devices
topic_type:
- apiref
api_name:
- ScsiPortWmiPostProcess
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

# ScsiPortWmiPostProcess routine

The **ScsiPortWmiPostProcess** routine updates a request context for a WMI SRB.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
VOID ScsiPortWmiPostProcess(
  _In_ PSCSIWMI_REQUEST_CONTEXT RequestContext,
  _In_ UCHAR                    SrbStatus,
  _In_ ULONG                    BufferUsed
);
```



## Parameters

<dl> <dt>

*RequestContext* \[in\]
</dt> <dd>

A pointer to the request context for this SRB.

</dd> <dt>

*SrbStatus* \[in\]
</dt> <dd>

Specifies any valid SRB status. If the output buffer passed to the miniport driver was too small to contain all of the data from a request, the miniport driver sets *SrbStatus* to SRB\_STATUS\_DATA\_OVERRUN.

</dd> <dt>

*BufferUsed* \[in\]
</dt> <dd>

If *SrbStatus* indicates success, the miniport driver sets *BufferUsed* to the number of bytes of data written to the buffer. If *SrbStatus* is SRB\_STATUS\_DATA\_OVERRUN, the miniport driver sets *BufferUsed* to the number of bytes required to complete the SRB successfully.

</dd> </dl>

## Return value

None

## Remarks

A miniport driver must call **ScsiPortWmiPostProcess** after the WMI SRB request has been processed and is ready to be completed.

For synchronous SRBs, **ScsiPortWmiPostProcess** is called in the callback routine.

For pending SRBs, **ScsiPortWmiPostProcess** is called after the SRB has been processed, and before it is completed.

If a miniport driver sets *SrbStatus* to SRB\_STATUS\_DATA\_OVERRUN and sets *BufferUsed*, successive identical WMI SRBs with an allocated buffer equal to or greater than *BufferUsed* bytes should succeed. This should be achieved if the driver sets the exact value for *BufferUsed* that is needed to complete the request when calling **ScsiPortWmiPostProcess** with *SrbStatus* equal to SRB\_STATUS\_DATA\_OVERRUN. For a variable-sized output structure, the input data buffer of the SRB should have enough information to determine the exact *BufferUsed* value. If the input data buffer does not contain enough information, the driver should never fail the same SRB two times with SRB\_STATUS\_DATA\_OVERRUN. Instead, the driver should set SRB\_STATUS\_DATA\_OVERRUN and request the minimum size necessary for the output buffer first, and then set SRB\_STATUS\_SUCCESS and indicate the failure in the contents of the output buffer.

## Requirements



|                            |                                                                                                                     |
|----------------------------|---------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                  |
| Header<br/>          | <dl> <dt>Scsiwmi.h (include Miniport.h or Scsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md)
</dt> <dt>

[**ScsiPortWmiGetReturnSize**](scsiportwmigetreturnsize.md)
</dt> <dt>

[**ScsiPortWmiGetReturnStatus**](scsiportwmigetreturnstatus.md)
</dt> <dt>

[**SCSIWMI\_REQUEST\_CONTEXT**](scsiwmi-request-context.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ScsiPortWmiPostProcess%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






