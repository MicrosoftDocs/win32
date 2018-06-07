---
title: IOCTL\_SCSI\_MINIPORT\_HYBRID control code
description: The IOCTL\_SCSI\_MINIPORT\_HYBRID control code sends a hybrid disk control request to an HBA-specific miniport driver.
ms.assetid: 57DA022A-FAC6-4727-94E1-BCF6FEF1E945
keywords:
- IOCTL_SCSI_MINIPORT_HYBRID control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_SCSI_MINIPORT_HYBRID
api_location:
- Ntddscsi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_SCSI\_MINIPORT\_HYBRID control code

The **IOCTL\_SCSI\_MINIPORT\_HYBRID** control code sends a hybrid disk control request to an HBA-specific miniport driver. The **IOCTL\_SCSI\_MINIPORT\_HYBRID** request is a sub-IOCTL of [**IOCTL\_SCSI\_MINIPORT**](ioctl-scsi-miniport.md). This IOCTL is received and reformatted by StorPort, then sent to the miniport as a [**STORAGE\_REQUEST\_BLOCK**](storage-request-block.md) (SRB) with a function type of SRB\_FUNCTION\_IO\_CONTROL. The input and output data is contained in the SRB data block.

**IOCTL\_SCSI\_MINIPORT\_HYBRID** is intended for use by third-party applications or filter drives which manage security features such as encryption or write-through behavior.

> \[!Warning\]  
> Use of **IOCTL\_SCSI\_MINIPORT\_HYBRID** to modify hybrid cache behavior will conflict with the operation of Windows system components and is not supported.

 

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Input Buffer

The buffer specified in the **DataBuffer** member of the SRB must contain an [**SRB\_IO\_CONTROL**](srb-io-control.md) structure and a **HYBRID\_REQUEST\_BLOCK** structure. Depending on the **Function** member of **HYBRID\_REQUEST\_BLOCK**, additional data can be supplied.

## Input Buffer Length

**DataTransferLength** indicates the size, in bytes, of the buffer, which must be at least **sizeof** (SRB\_IO\_CONTROL) + **sizeof**(HYBRID\_REQUEST\_BLOCK), with additional storage for function data if the **DataBufferLength** member of the **HYBRID\_REQUEST\_BLOCK** is nonzero.

## Output Buffer

An updated [**SRB\_IO\_CONTROL**](srb-io-control.md) structure is returned to the data buffer in the SRB.

## Output Buffer Length

The **DataBufferOffset** and **DataBufferLength** members of **HYBRID\_REQUEST\_BLOCK** are nonzero when data is returned for the specified **Function**. The **DataTransferLength** member of the SRB is updated when data is returned for the request function.

## Status block

The resulting status of the function request is set in the **ReturnCode** member of [**SRB\_IO\_CONTROL**](srb-io-control.md). The following are the hybrid disk IOCTL status codes.



| Return Code                                | Description                                                                               |
|--------------------------------------------|-------------------------------------------------------------------------------------------|
| HYBRID\_STATUS\_SUCCESS                    | The function completed successfully.                                                      |
| HYBRID\_STATUS\_ILLEGAL\_REQUEST           | The request contains an invalid function code.                                            |
| HYBRID\_STATUS\_INVALID\_PARAMETER         | Either the input or output parameters are formatted incorrectly.                          |
| HYBRID\_STATUS\_OUTPUT\_BUFFER\_TOO\_SMALL | The data length given in **DataBufferLength** is too small to contain the request output. |



 

## Remarks

A **HYBRID\_REQUEST\_BLOCK** structure immediately follows the [**SRB\_IO\_CONTROL**](srb-io-control.md) structure in the data buffer. **HYBRID\_REQUEST\_BLOCK** is defined in ntddscsi.h as the following.


```
typedef struct _HYBRID_REQUEST_BLOCK {
    ULONG   Version;
    ULONG   Size;
    ULONG   Function;
    ULONG   Flags;
    ULONG   DataBufferOffset;
    ULONG   DataBufferLength;
} HYBRID_REQUEST_BLOCK, *PHYBRID_REQUEST_BLOCK;
```



<dl> <dt>

<span id="Version"></span><span id="version"></span><span id="VERSION"></span>Version
</dt> <dd>

The version of the structure. Set to HYBRID\_REQUEST\_BLOCK\_STRUCTURE\_VERSION.

</dd> <dt>

<span id="Size"></span><span id="size"></span><span id="SIZE"></span>Size
</dt> <dd>

The size of the structure. Set to **sizeof**(HYBRID\_REQUEST\_BLOCK).

</dd> <dt>

<span id="Function"></span><span id="function"></span><span id="FUNCTION"></span>Function
</dt> <dd>

The hybrid disk request function. The function code is one of the following.

<dl> <dt>

<span id="HYBRID_FUNCTION_GET_INFO"></span><span id="hybrid_function_get_info"></span>HYBRID\_FUNCTION\_GET\_INFO
</dt> <dd>

Returns information about the capabilities and attributes of a hybrid devices, such as supported priority levels, command set support, and cache size in a [**HYBRID\_INFORMATION**](hybrid-information.md) structure. On input, the **DataBuffer** specified in the SRB must contain the [**SRB\_IO\_CONTROL**](srb-io-control.md) and **HYBRID\_REQUEST\_BLOCK** structures. The **DataBufferLength** must be large enough to include the **HYBRID\_INFORMATION** structure returned. The **DataBufferOffset** points to the output data containing **HYBRID\_INFORMATION**. If the buffer is too small to return the data, the **ReturnCode** member of **SRB\_IO\_CONTROL** is set to HYBRID\_STATUS\_OUTPUT\_BUFFER\_TOO\_SMALL and **DataBufferLength** of the **HYBRID\_REQUEST\_BLOCK** is set to indicate the required length.

</dd> <dt>

<span id="HYBRID_FUNCTION_DISABLE_CACHING_MEDIUM_______________"></span><span id="hybrid_function_disable_caching_medium_______________"></span>HYBRID\_FUNCTION\_DISABLE\_CACHING\_MEDIUM 
</dt> <dd>

Disables the hybrid cache. Disabling the cache can take several minutes. If queried during this operation, the **NV\_CACHE\_STATUS** member of the [**HYBRID\_INFORMATION**](hybrid-information.md) structure is set to **NvCacheStatusDisabling** until the cache is completely disabled. The caller should check the status of **NV\_CACHE\_STATUS** to verify that the caching medium is disabled. Once the cache is fully disabled, the status is **NvCacheStatusDisabled**. For this function, the **DataBufferOffset** member of **HYBRID\_REQUEST\_BLOCK** is set 0. This function has no output parameters.

</dd> <dt>

<span id="HYBRID_FUNCTION_ENABLE_CACHING_MEDIUM"></span><span id="hybrid_function_enable_caching_medium"></span>HYBRID\_FUNCTION\_ENABLE\_CACHING\_MEDIUM
</dt> <dd>

Sets the caching medium to its default state, which is  enabled . The **DataBufferOffset** member of **HYBRID\_REQUEST\_BLOCK** is set to 0. When this function completes, when queried, the **NV\_CACHE\_STATUS** member of the [**HYBRID\_INFORMATION**](hybrid-information.md) structure is set to **NvCacheStatusEnabled**. For this function, the **DataBufferOffset** member of **HYBRID\_REQUEST\_BLOCK** is set 0. This function has no output parameters.

</dd> <dt>

<span id="HYBRID_FUNCTION_SET_DIRTY_THRESHOLD"></span><span id="hybrid_function_set_dirty_threshold"></span>HYBRID\_FUNCTION\_SET\_DIRTY\_THRESHOLD
</dt> <dd>

Sets the thresholds for dirty data synchronization on the device. In addition to [**SRB\_IO\_CONTROL**](srb-io-control.md) and **HYBRID\_REQUEST\_BLOCK**, this function requires a **HYBRID\_DIRTY\_THRESHOLDS** structure included as input. The **DataBufferOffset** member is set to the beginning of the **HYBRID\_DIRTY\_THRESHOLDS** structure. This function has no output parameters.

</dd> <dt>

<span id="HYBRID_FUNCTION_DEMOTE_BY_SIZE"></span><span id="hybrid_function_demote_by_size"></span>HYBRID\_FUNCTION\_DEMOTE\_BY\_SIZE
</dt> <dd>

This function demotes the priority of a given amount of cache contents to a lower priority. It can be used to achieve a soft reset of the cache by demoting all cache contents to priority 0. In addition to [**SRB\_IO\_CONTROL**](srb-io-control.md) and **HYBRID\_REQUEST\_BLOCK**, this function requires a **HYBRID\_DEMOTE\_BY\_SIZE** structure included as input. The **DataBufferOffset** member is set to the beginning of the **HYBRID\_DEMOTE\_BY\_SIZE** structure. This function has no output parameters.

</dd> </dl> </dd> <dt>

<span id="Flags"></span><span id="flags"></span><span id="FLAGS"></span>Flags
</dt> <dd>

Reserved. Set to 0.

</dd> <dt>

<span id="DataBufferOffset"></span><span id="databufferoffset"></span><span id="DATABUFFEROFFSET"></span>DataBufferOffset
</dt> <dd>

The offset for additional data that was sent or is returned for the function specified in **Function**. This value varies on the data required for **Function**. This value is the offset from the beginning the **DataBuffer** of the SRB which contains a [**SRB\_IO\_CONTROL**](srb-io-control.md) structure and other required data structures. It should point to the first location after **SRB\_IO\_CONTROL** and **HYBRID\_REQUEST\_BLOCK**. This value is aligned at a multiple of **sizeof**(PVOID). If there is no buffer then **DataBufferOffset** is set to 0.

</dd> <dt>

<span id="DataBufferLength"></span><span id="databufferlength"></span><span id="DATABUFFERLENGTH"></span>DataBufferLength
</dt> <dd>

The size the data block found at **DataBufferOffset**.

</dd> </dl>

The parameter requirements depend on the function code of the hybrid disk request. The following table lists the parameters required for each function.



| Function                                   | Input Parameters                                                                                                                         | Output Parameters                                                                                                                                            |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HYBRID\_FUNCTION\_GET\_INFO                | [**SRB\_IO\_CONTROL**](srb-io-control.md) +<br/> **HYBRID\_REQUEST\_BLOCK**<br/>                                            | [**SRB\_IO\_CONTROL**](srb-io-control.md) +<br/> **HYBRID\_REQUEST\_BLOCK** +<br/> [**HYBRID\_INFORMATION**](hybrid-information.md)<br/> |
| HYBRID\_FUNCTION\_DISABLE\_CACHING\_MEDIUM | [**SRB\_IO\_CONTROL**](srb-io-control.md) +<br/> **HYBRID\_REQUEST\_BLOCK**<br/>                                            | [**SRB\_IO\_CONTROL**](srb-io-control.md)<br/>                                                                                                        |
| HYBRID\_FUNCTION\_ENABLE\_CACHING\_MEDIUM  | [**SRB\_IO\_CONTROL**](srb-io-control.md) +<br/> **HYBRID\_REQUEST\_BLOCK**<br/>                                            | [**SRB\_IO\_CONTROL**](srb-io-control.md)<br/>                                                                                                        |
| HYBRID\_FUNCTION\_SET\_DIRTY\_THRESHOLD    | [**SRB\_IO\_CONTROL**](srb-io-control.md) +<br/> **HYBRID\_REQUEST\_BLOCK** +<br/> **HYBRID\_DIRTY\_THRESHOLDS**<br/> | [**SRB\_IO\_CONTROL**](srb-io-control.md)<br/>                                                                                                        |
| HYBRID\_FUNCTION\_DEMOTE\_BY\_SIZE         | [**SRB\_IO\_CONTROL**](srb-io-control.md) +<br/> **HYBRID\_REQUEST\_BLOCK** +<br/> **HYBRID\_DEMOTE\_BY\_SIZE**<br/>  | [**SRB\_IO\_CONTROL**](srb-io-control.md)<br/>                                                                                                        |



 

The **HYBRID\_REQUEST\_BLOCK** structure is located after the [**SRB\_IO\_CONTROL**](srb-io-control.md) structure in the **DataBuffer** of the SRB. Any function data included with the request is found at the offset in **DataBufferOffset** after the beginning of the **SRB\_IO\_CONTROL** structure.

The following example demonstrates retrieval of the function data for a HYBRID\_FUNCTION\_SET\_DIRTY\_THRESHOLD request.


```
    PSRB_IO_CONTROL srbIoCtl = (PSRB_IO_CONTROL)srb->DataBuffer;
    PHYBRID_REQUEST_BLOCK hybridRequest = (PHYBRID_REQUEST_BLOCK)(srbIoCtl + 1);
    PHYBRID_DIRTY_THRESHOLDS hybridDirtyThresholds = NULL;

    if (hybridRequest->DataBufferOffset >= sizeof(SRB_IO_CONTROL) + sizeof(HYBRID_REQUEST_BLOCK))
    {
        if (hybridRequest->DataBufferLength >= sizeof(HYBRID_FUNCTION_SET_DIRTY_THRESHOLD))
        {
            hybridDirtyThresholds = (PHYBRID_DIRTY_THRESHOLDS)((PUCHAR)srbIoCtl + hybridRequest->DataBufferOffset);
        }
        else
        {
            srbIoCtl->ReturnCode = HYBRID_STATUS_INVALID_PARAMETER;
        }
    }
```



**HYBRID\_DIRTY\_THRESHOLDS**

The HYBRID\_FUNCTION\_SET\_DIRTY\_THRESHOLD function uses the **HYBRID\_DIRTY\_THRESHOLDS** structure for its input parameters. **HYBRID\_DIRTY\_THRESHOLDS** is defined in ntddscsi.h as the following.


```
typedef struct _HYBRID_DIRTY_THRESHOLDS {
    ULONG   Version;
    ULONG   Size;
    ULONG   DirtyLowThreshold;
    ULONG   DirtyHighThreshold;
} HYBRID_DIRTY_THRESHOLDS, *PHYBRID_DIRTY_THRESHOLDS;
```



<dl> <dt>

<span id="Version"></span><span id="version"></span><span id="VERSION"></span>Version
</dt> <dd>

The version of the structure. Set to HYBRID\_REQUEST\_INFO\_STRUCTURE\_VERSION.

</dd> <dt>

<span id="Size"></span><span id="size"></span><span id="SIZE"></span>Size
</dt> <dd>

The size of the structure. Set to **sizeof**(HYBRID\_DIRTY\_THRESHOLDS).

</dd> <dt>

<span id="DirtyLowThreshold"></span><span id="dirtylowthreshold"></span><span id="DIRTYLOWTHRESHOLD"></span>DirtyLowThreshold
</dt> <dd>

The fractional low threshold value for the hybrid disk cache to synchronize to disk.

</dd> <dt>

<span id="DirtyHighThreshold"></span><span id="dirtyhighthreshold"></span><span id="DIRTYHIGHTHRESHOLD"></span>DirtyHighThreshold
</dt> <dd>

The fractional high threshold value for the hybrid disk cache to synchronize to disk.

</dd> </dl>

The values of **DirtyLowThreshold** and **DirtyHighThreshold** are expressed as the smaller part of a ratio between the threshold value and a fraction base. The fraction base is determined by the **FractionBase** member of the [**HYBRID\_INFORMATION**](hybrid-information.md) structure.

**HYBRID\_DEMOTE\_BY\_SIZE**

The HYBRID\_FUNCTION\_DEMOTE\_BY\_SIZE function uses the **HYBRID\_DEMOTE\_BY\_SIZE** structure for its input parameters. **HYBRID\_DEMOTE\_BY\_SIZE** is defined in ntddscsi.h as the following.


```
typedef struct _HYBRID_DEMOTE_BY_SIZE {
    ULONG       Version;
    ULONG       Size;
    UCHAR       SourcePriority;
    UCHAR       TargetPriority;
    USHORT      Reserved0;
    ULONG       Reserved1;
    ULONGLONG   LbaCount;
} HYBRID_DEMOTE_BY_SIZE, *PHYBRID_DEMOTE_BY_SIZE;
```



<dl> <dt>

<span id="Version"></span><span id="version"></span><span id="VERSION"></span>Version
</dt> <dd>

The version of the structure. Set to HYBRID\_REQUEST\_INFO\_STRUCTURE\_VERSION.

</dd> <dt>

<span id="Size"></span><span id="size"></span><span id="SIZE"></span>Size
</dt> <dd>

The size of the structure. Set to **sizeof**(HYBRID\_DEMOTE\_BY\_SIZE).

</dd> <dt>

<span id="SourcePriority"></span><span id="sourcepriority"></span><span id="SOURCEPRIORITY"></span>SourcePriority
</dt> <dd>

The original priority level of the data to demote. This value must be &lt;= the value in the **MaximumHybridPriorityLevel** member of the **HYBRID\_INFORMATION** structure returned by from a **HYBRID\_FUNCTION\_GET\_INFO** function request. This value must be &gt; 0.

</dd> <dt>

<span id="TargetPriority"></span><span id="targetpriority"></span><span id="TARGETPRIORITY"></span>TargetPriority
</dt> <dd>

The target priority level of the data to demote from the *SourcePriority* level. This value must be &lt; *SourcePriority*.

</dd> <dt>

<span id="Reserved0"></span><span id="reserved0"></span><span id="RESERVED0"></span>Reserved0
</dt> <dd>

Reserved.

</dd> <dt>

<span id="Reserved1"></span><span id="reserved1"></span><span id="RESERVED1"></span>Reserved1
</dt> <dd>

Reserved.

</dd> <dt>

<span id="LbaCount"></span><span id="lbacount"></span><span id="LBACOUNT"></span>LbaCount
</dt> <dd>

The number of LBAs to demote to the new priority level.

</dd> </dl>

The [**SRB\_IO\_CONTROL**](srb-io-control.md) structure for this IOCTL contains IOCTL\_MINIPORT\_SIGNATURE\_HYBRDISK in its **Signature** member and **IOCTL\_SCSI\_MINIPORT\_HYBRID** in the **ControlCode** member.

## Requirements



|                    |                                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.1.<br/>                                                            |
| Header<br/>  | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HYBRID\_INFORMATION**](hybrid-information.md)
</dt> <dt>

[**IOCTL\_SCSI\_MINIPORT**](ioctl-scsi-miniport.md)
</dt> <dt>

[**SRB\_IO\_CONTROL**](srb-io-control.md)
</dt> <dt>

[**STORAGE\_REQUEST\_BLOCK**](storage-request-block.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_SCSI_MINIPORT_HYBRID%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






