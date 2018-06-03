---
title: PSCSIWMI\_QUERY\_DATABLOCK callback function
description: A miniport driver's HwScsiWmiQueryDataBlock routine is called to obtain either a single instance or all instances of a data block.
ms.assetid: a2e588b8-50d6-4bed-b50c-c42be24955f1
keywords:
- HwScsiWmiQueryDataBlock callback function Storage Devices
- PSCSIWMI_QUERY_DATABLOCK
topic_type:
- apiref
api_name:
- HwScsiWmiQueryDataBlock
api_location:
- scsiwmi.h
api_type:
- UserDefined
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PSCSIWMI\_QUERY\_DATABLOCK callback function

A miniport driver's **HwScsiWmiQueryDataBlock** routine is called to obtain either a single instance or all instances of a data block. This routine is required.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
BOOLEAN HwScsiWmiQueryDataBlock(
  _In_    PVOID                    Context,
  _In_    PSCSIWMI_REQUEST_CONTEXT DispatchContext,
  _In_    ULONG                    GuidIndex,
  _In_    ULONG                    InstanceIndex,
  _In_    ULONG                    InstanceCount,
  _Inout_ PULONG                   InstanceLengthArray,
  _In_    ULONG                    BufferAvail,
  _Out_   PUCHAR                   Buffer
);
```



## Parameters

<dl> <dt>

*Context* \[in\]
</dt> <dd>

Points to the miniport driver-defined context value passed to [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md).

</dd> <dt>

*DispatchContext* \[in\]
</dt> <dd>

Points to the SCSIWMI\_REQUEST\_CONTEXT structure that the miniport driver passed to [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md).

</dd> <dt>

*GuidIndex* \[in\]
</dt> <dd>

Specifies the data block by its index into the list of GUIDs in the SCSI\_WMILIB\_CONTEXT structure that the miniport driver passed to [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md).

</dd> <dt>

*InstanceIndex* \[in\]
</dt> <dd>

If **HwScsiWmiQueryDataBlock** is called in response to an IRP\_MN\_QUERY\_SINGLE\_INSTANCE request, *InstanceIndex* specifies the instance to be queried. If **HwScsiWmiQueryDataBlock** is called in response to an IRP\_MN\_QUERY\_ALL\_DATA REQUEST, *InstanceIndex* is zero.

</dd> <dt>

*InstanceCount* \[in\]
</dt> <dd>

If **HwScsiWmiQueryDataBlock** is called in response to an IRP\_MN\_QUERY\_SINGLE\_INSTANCE request, *InstanceCount* is 1. If **HwScsiWmiQueryDataBlock** is called in response to an IRP\_MN\_QUERY\_ALL\_DATA REQUEST, *InstanceCount* is the number of instances to be returned.

</dd> <dt>

*InstanceLengthArray* \[in, out\]
</dt> <dd>

Points to an array of ULONGs that indicate the length of each instance of the data block to be returned. This array has *InstanceCount* elements. This value may be **NULL** when there is not enough space in the output buffer to fulfill the request.

</dd> <dt>

*BufferAvail* \[in\]
</dt> <dd>

Specifies the maximum number of bytes available to receive data in the buffer at *Buffer*.

</dd> <dt>

*Buffer* \[out\]
</dt> <dd>

Points to the buffer to receive instance data. If the buffer is large enough to receive all of the data, the miniport driver writes instance data to the buffer with each instance aligned on an 8-byte boundary. If the buffer is too small to receive all of the data, the miniport driver calls [**ScsiPortWmiPostProcess**](scsiportwmipostprocess.md) with a status of SRB\_STATUS\_DATA\_OVERRUN and sets *BufferUsed* to the size of the output buffer needed to fulfill the request.

</dd> </dl>

## Return value

**HwScsiWmiQueryDataBlock** returns SRB\_STATUS\_PENDING if the request is pending or a nonzero SRB status value if the request was completed. The SRB status value returned by this routine is the same as what was passed in to [**ScsiPortWmiPostProcess**](scsiportwmipostprocess.md). Although the return value data type is BOOLEAN, the **HwScsiWmiQueryDataBlock** routine actually returns an SRB status value.

## Remarks

When a miniport driver receives an SRB in which the **Function** member is set to SRB\_FUNCTION\_WMI, it calls [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md) with a pointer to an initialized SCSI\_WMILIB\_CONTEXT structure and *MinorFunction* set to **Srb-&gt;WmiSubFunction**. The SCSI port driver calls the miniport driver's **HwScsiWmiQueryDataBlock** routine if *MinorFunction* indicates a request to obtain a single instance or all instances of a data block.

The miniport driver writes instance data to the buffer. For requests that do not pend, the miniport driver calls [**ScsiPortWmiPostProcess**](scsiportwmipostprocess.md) with an appropriate *SrbStatus* value before returning from **HwScsiWmiQueryDataBlock**. If the request pends, the miniport driver calls **ScsiPortWmiPostProcess** when the request is complete.

## Requirements



|                            |                                                                                                          |
|----------------------------|----------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                       |
| Header<br/>          | <dl> <dt>Scsiwmi.h (include Scsiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**SCSI\_WMILIB\_CONTEXT**](scsi-wmilib-context.md)
</dt> <dt>

[**ScsiPortWmiPostProcess**](scsiportwmipostprocess.md)
</dt> <dt>

[**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PSCSIWMI_QUERY_DATABLOCK%20callback%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






