---
title: NVCACHE\_REQUEST\_BLOCK structure
description: The NVCACHE\_REQUEST\_BLOCK structure is used in conjunction with the IOCTL\_SCSI\_MINIPORT request to manage hybrid-hard disk drive (H-HDD) devices (for example, Microsoft ReadyDrive technology).
ms.assetid: '25ca2d81-72a5-47ae-bdfd-0ec63e1ca39a'
keywords: ["NVCACHE_REQUEST_BLOCK structure Storage Devices", "PNVCACHE_REQUEST_BLOCK structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- NVCACHE_REQUEST_BLOCK
api_location:
- ntddscsi.h
api_type:
- HeaderDef
---

# NVCACHE\_REQUEST\_BLOCK structure

The **NVCACHE\_REQUEST\_BLOCK** structure is used in conjunction with the [**IOCTL\_SCSI\_MINIPORT**](ioctl-scsi-miniport.md) request to manage hybrid-hard disk drive (H-HDD) devices (for example, Microsoft ReadyDrive technology). This topic defines the general structure for both input data and output data for a call made to the NV Cache Manager. A caller should fill all required fields before calling [**DeviceIoControl**](https://msdn.microsoft.com/library/windows/desktop/aa363216) or [**IoBuildDeviceIoControlRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548318). The miniport driver must do the same after the requested function is completed, and before it returns.

## Syntax


```C++
typedef struct _NVCACHE_REQUEST_BLOCK {
  ULONG     NRBSize;
  USHORT    Function;
  ULONG     NRBFlags;
  ULONG     NRBStatus;
  ULONG     Count;
  ULONGLONG LBA;
  ULONG     DataBufSize;
  ULONG     NVCacheStatus;
  ULONG     NVCacheSubStatus;
} NVCACHE_REQUEST_BLOCK, *PNVCACHE_REQUEST_BLOCK;
```



## Members

<dl> <dt>

**NRBSize**
</dt> <dd>

The **sizeof**(NVCACHE\_REQUEST\_BLOCK).

</dd> <dt>

**Function**
</dt> <dd>

Specifies the operation to be performed, which can be one of the following values:

<dl> <dt>

<span id="NRB_FUNCTION_NVCACHE_INFO"></span><span id="nrb_function_nvcache_info"></span>NRB\_FUNCTION\_NVCACHE\_INFO
</dt> <dd>

Get NV Cache Manager feature support information from the device. Upon the successful completion of this function, the required data fields are returned to the caller. The return data structure is [**NV\_FEATURE\_PARAMETER**](nv-feature-parameter.md).

</dd> <dt>

<span id="NRB_FUNCTION_SPINDLE_STATUS"></span><span id="nrb_function_spindle_status"></span>NRB\_FUNCTION\_SPINDLE\_STATUS
</dt> <dd>

Determine if the device is currently spinning up or spinning down. For an ATA device, a Check Power Mode command is required to obtain the device's spindle status. For a SCSI device, a Mode Sense command can be used to query the device's current power mode.

</dd> <dt>

<span id="NRB_FUNCTION_NVCACHE_POWER_MODE_SET"></span><span id="nrb_function_nvcache_power_mode_set"></span>NRB\_FUNCTION\_NVCACHE\_POWER\_MODE\_SET
</dt> <dd>

Turn on the NV Cache Manager power mode.

</dd> <dt>

<span id="NRB_FUNCTION_NVCACHE_POWER_MODE_RESET"></span><span id="nrb_function_nvcache_power_mode_reset"></span>NRB\_FUNCTION\_NVCACHE\_POWER\_MODE\_RESET
</dt> <dd>

Turn off the NV Cache Manager power mode.

</dd> <dt>

<span id="NRB_FUNCTION_FLUSH_NVCACHE"></span><span id="nrb_function_flush_nvcache"></span>NRB\_FUNCTION\_FLUSH\_NVCACHE
</dt> <dd>

Flush the data that is currently pinned in NV cache memory to make the required NV cache memory space available.

</dd> <dt>

<span id="NRB_FUNCTION_QUERY_PINNED_SET"></span><span id="nrb_function_query_pinned_set"></span>NRB\_FUNCTION\_QUERY\_PINNED\_SET
</dt> <dd>

Get the Logical Block Address (LBA) ranges currently in the NV Cache Manager pinned set.

</dd> <dt>

<span id="NRB_FUNCTION_QUERY_CACHE_MISS"></span><span id="nrb_function_query_cache_miss"></span>NRB\_FUNCTION\_QUERY\_CACHE\_MISS
</dt> <dd>

Request that the device report NV Cache Misses in LBA ranges in a single 512-byte block.

</dd> <dt>

<span id="NRB_FUNCTION_ADD_LBAS_PINNED_SET"></span><span id="nrb_function_add_lbas_pinned_set"></span>NRB\_FUNCTION\_ADD\_LBAS\_PINNED\_SET
</dt> <dd>

Add the LBAs that are specified in the NV Cache Manager Set Data to the NV Cache Manager Pinned Set if they are not already.

</dd> <dt>

<span id="NRB_FUNCTION_REMOVE_LBAS_PINNED_SET"></span><span id="nrb_function_remove_lbas_pinned_set"></span>NRB\_FUNCTION\_REMOVE\_LBAS\_PINNED\_SET
</dt> <dd>

Remove the LBAs that are specified in the NV Cache Set Data from the NV Cache pinned set.

</dd> <dt>

<span id="NRB_FUNCTION_QUERY_HYBRID_DISK_STATUS"></span><span id="nrb_function_query_hybrid_disk_status"></span>NRB\_FUNCTION\_QUERY\_HYBRID\_DISK\_STATUS
</dt> <dd>

Reserved for future use.

</dd> <dt>

<span id="NRB_FUNCTION_PASS_HINT_PAYLOAD"></span><span id="nrb_function_pass_hint_payload"></span>NRB\_FUNCTION\_PASS\_HINT\_PAYLOAD
</dt> <dd>

Pass IO hints to a SATA device.

</dd> </dl> </dd> <dt>

**NRBFlags**
</dt> <dd>

Reserved for future use.

</dd> <dt>

**NRBStatus**
</dt> <dd>

Indicates the NV Cache Manager function request status from the driver. There are seven possible values for this field:

<dl> <dt>

<span id="NRB_SUCCESS"></span><span id="nrb_success"></span>NRB\_SUCCESS
</dt> <dd>

No error.

</dd> <dt>

<span id="NRB_ILLEGAL_REQUEST"></span><span id="nrb_illegal_request"></span>NRB\_ILLEGAL\_REQUEST
</dt> <dd>

Illegal request detected by the port driver.

</dd> <dt>

<span id="NRB_INVALID_PARAMETER"></span><span id="nrb_invalid_parameter"></span>NRB\_INVALID\_PARAMETER
</dt> <dd>

Invalid parameter passed to the port driver.

</dd> <dt>

<span id="NRB_INPUT_DATA_OVERRUN"></span><span id="nrb_input_data_overrun"></span>NRB\_INPUT\_DATA\_OVERRUN
</dt> <dd>

Too much data provided to the port driver.

</dd> <dt>

<span id="NRB_INPUT_DATA_UNDERRUN"></span><span id="nrb_input_data_underrun"></span>NRB\_INPUT\_DATA\_UNDERRUN
</dt> <dd>

Not enough data provided to the port driver.

</dd> <dt>

<span id="NRB_OUTPUT_DATA_OVERRUN"></span><span id="nrb_output_data_overrun"></span>NRB\_OUTPUT\_DATA\_OVERRUN
</dt> <dd>

Too much data returned from the port driver.

</dd> <dt>

<span id="NRB_OUTPUT_DATA_UNDERRUN"></span><span id="nrb_output_data_underrun"></span>NRB\_OUTPUT\_DATA\_UNDERRUN
</dt> <dd>

Not enough data returned from the port driver.

</dd> </dl> </dd> <dt>

**Count**
</dt> <dd>

Number of 512-byte blocks to be transferred with the specified function.

</dd> <dt>

**LBA**
</dt> <dd>

Starting LBA of the device for the specified function.

</dd> <dt>

**DataBufSize**
</dt> <dd>

Size of the data buffer, in bytes.

</dd> <dt>

**NVCacheStatus**
</dt> <dd>

Status returned from the device. For an ATA device, this value is the contents of the Status Register in its Task File. For a SCSI device, this value is the Sense Code returned from the device.

</dd> <dt>

**NVCacheSubStatus**
</dt> <dd>

The error code returned from the device. For an ATA device, this value is the contents of the Error Register in its Task File. For a SCSI device, this value is the Sense key returned from the device.

</dd> </dl>

## Remarks

For more information on function behavior, see section 7.20 of the [ATA8-ACS specification](http://go.microsoft.com/fwlink/p/?linkid=74996).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddscsi.h (include Ntddscsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_SCSI\_MINIPORT**](ioctl-scsi-miniport.md)
</dt> <dt>

[**IOCTL\_SCSI\_MINIPORT\_NVCACHE**](ioctl-scsi-miniport-nvcache.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20NVCACHE_REQUEST_BLOCK%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






