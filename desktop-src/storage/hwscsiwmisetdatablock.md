---
title: PSCSIWMI\_SET\_DATABLOCK callback function
description: A miniport drivers HwScsiWmiSetDataBlock routine is called to change all data items in a single instance of a data block.
ms.assetid: 5523d4d6-8eb5-48eb-a652-6612101b8422
keywords:
- HwScsiWmiSetDataBlock callback function Storage Devices
- PSCSIWMI_SET_DATABLOCK
topic_type:
- apiref
api_name:
- HwScsiWmiSetDataBlock
api_location:
- scsiwmi.h
api_type:
- UserDefined
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PSCSIWMI\_SET\_DATABLOCK callback function

A miniport driver's **HwScsiWmiSetDataBlock** routine is called to change all data items in a single instance of a data block. This routine is optional.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
BOOLEAN HwScsiWmiSetDataBlock(
  _In_ PVOID                    DeviceContext,
  _In_ PSCSIWMI_REQUEST_CONTEXT RequestContext,
  _In_ ULONG                    GuidIndex,
  _In_ ULONG                    InstanceIndex,
  _In_ ULONG                    BufferSize,
  _In_ PUCHAR                   Buffer
);
```



## Parameters

<dl> <dt>

*DeviceContext* \[in\]
</dt> <dd>

Points to the miniport driver-defined context value passed to [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md).

</dd> <dt>

*RequestContext* \[in\]
</dt> <dd>

Points to the SCSIWMI\_REQUEST\_CONTEXT structure that the miniport driver passed to [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md).

</dd> <dt>

*GuidIndex* \[in\]
</dt> <dd>

Specifies the data block by its index into the list of GUIDs in the SCSI\_WMILIB\_CONTEXT structure that the miniport driver passed to [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md).

</dd> <dt>

*InstanceIndex* \[in\]
</dt> <dd>

If the block specified by *GuidIndex* has multiple instances, *InstanceIndex* specifies the instance.

</dd> <dt>

*BufferSize* \[in\]
</dt> <dd>

Specifies the size in bytes of the buffer at *Buffer*.

</dd> <dt>

*Buffer* \[in\]
</dt> <dd>

Points to a buffer that contains new values for the instance.

</dd> </dl>

## Return value

**HwScsiWmiSetDataBlock** returns SRB\_STATUS\_PENDING if the request is pending, or a nonzero SRB status value if the request was completed. The SRB status value returned by this routine is the same as what was passed in to [**ScsiPortWmiPostProcess**](scsiportwmipostprocess.md).

## Remarks

When a miniport driver receives an SRB in which the **Function** member is set to SRB\_FUNCTION\_WMI, it calls [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md) with a pointer to an initialized SCSI\_WMILIB\_CONTEXT structure and *MinorFunction* set to **Srb-&gt;WmiSubFunction**. The SCSI port driver calls the miniport driver's **HwScsiWmiSetDataBlock** routine if *MinorFunction* indicates a request to change an instance of a data block.

If a miniport driver does not implement a **HwScsiWmiSetDataBlock** routine, it must set **SetWmiDataBlock** to **NULL** in the SCSI\_WMILIB\_CONTEXT the miniport driver passes to [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md). In this case, the port driver returns SRB\_STATUS\_ERROR to the caller.

If the miniport driver implements **HwScsiWmiSetDataBlock** it should change the instance of the data block to the new values from the buffer.

If all of the items in the data block are read-only, the miniport driver should return SRB\_STATUS\_ERROR. Otherwise, the miniport driver changes the items it can and returns SRB\_STATUS\_SUCCESS.

The miniport driver should call [**ScsiPortWmiPostProcess**](scsiportwmipostprocess.md) with an appropriate *SrbStatus* value when the request is completed. If the request does not pend, **ScsiPortWmiPostProcess** should be called in the **HwScsiWmiSetDataBlock** callback. Otherwise, **ScsiPortWmiPostProcess** should be called when the request is actually completed.

## Requirements



|                            |                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                       |
| Header<br/>          | <dl> <dt>Scsiwmi.h (include Scsiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**SCSI\_WMILIB\_CONTEXT**](scsi-wmilib-context.md)
</dt> <dt>

[**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md)
</dt> <dt>

[**ScsiPortWmiPostProcess**](scsiportwmipostprocess.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PSCSIWMI_SET_DATABLOCK%20callback%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






