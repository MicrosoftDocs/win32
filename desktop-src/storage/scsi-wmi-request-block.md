---
title: SCSI\_WMI\_REQUEST\_BLOCK structure
description: This structure is a special version of a SCSI\_REQUEST\_BLOCK for use with WMI commands.
ms.assetid: 6dc10c3a-b47e-42c3-a209-34977fb219f1
keywords:
- SCSI_WMI_REQUEST_BLOCK structure Storage Devices
- PSCSI_WMI_REQUEST_BLOCK structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SCSI_WMI_REQUEST_BLOCK
api_location:
- srb.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# SCSI\_WMI\_REQUEST\_BLOCK structure

This structure is a special version of a [**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md) for use with WMI commands.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _SCSI_WMI_REQUEST_BLOCK {
  USHORT Length;
  UCHAR  Function;
  UCHAR  SrbStatus;
  UCHAR  WMISubFunction;
  UCHAR  PathId;
  UCHAR  TargetId;
  UCHAR  Lun;
  UCHAR  Reserved1;
  UCHAR  WMIFlags;
  UCHAR  Reserved2[2];
  ULONG  SrbFlags;
  ULONG  DataTransferLength;
  ULONG  TimeOutValue;
  PVOID  DataBuffer;
  PVOID  DataPath;
  PVOID  Reserved3;
  PVOID  OriginalRequest;
  PVOID  SrbExtension;
  ULONG  Reserved4;
#ifdef _WIN64
  ULONG  Reserved6;
#endif 
  UCHAR  Reserved5[16];
} SCSI_WMI_REQUEST_BLOCK, *PSCSI_WMI_REQUEST_BLOCK;
```



## Members

<dl> <dt>

**Length**
</dt> <dd>

Specifies the size in bytes of this structure.

</dd> <dt>

**Function**
</dt> <dd>

SRB\_FUNCTION\_WMI, which specifies that the request is a WMI request. If this member is not set to SRB\_FUNCTION\_WMI, the miniport driver should fail the request.

</dd> <dt>

**SrbStatus**
</dt> <dd>

Returns the status of the completed request. This member should be set by the miniport driver before it notifies the OS-specific driver that the request has completed by calling [**ScsiPortNotification**](scsiportnotification.md) with **RequestComplete**. The value of this member can be any value listed for **SrbStatus** in SCSI\_REQUEST\_BLOCK.

</dd> <dt>

**WMISubFunction**
</dt> <dd>

Indicates the WMI action to be performed. A miniport driver calls [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md) with *MinorFunction* set to this value. The subfunction value corresponds to the WMI minor IRP number that identifies the WMI operation.

</dd> <dt>

**PathId**
</dt> <dd>

Indicates the SCSI port or bus for the request. This value is zero-based. If SRB\_WMI\_FLAGS\_ADAPTER\_REQUEST is set in **WMIFlags**, this member is reserved.

</dd> <dt>

**TargetId**
</dt> <dd>

Indicates the target controller or device on the bus. If SRB\_WMI\_FLAGS\_ADAPTER\_REQUEST is set in **WMIFlags**, this member is reserved.

</dd> <dt>

**Lun**
</dt> <dd>

Indicates the logical unit number of the device. If SRB\_WMI\_FLAGS\_ADAPTER\_REQUEST is set in **WMIFlags**, this member is reserved.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved for system use and not available for use by miniport drivers.

</dd> <dt>

**WMIFlags**
</dt> <dd>

Indicates that the WMI request is for the adapter if SRB\_WMI\_FLAGS\_ADAPTER\_REQUEST is set and that **PathId**, **TargetId**, and **Lun** are reserved. Otherwise, **WMIFlags** will be **NULL**, indicating that the request is for the device specified by **PathId**, **TargetId**, and **Lun**.

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved for system use and not available for use by miniport drivers.

</dd> <dt>

**SrbFlags**
</dt> <dd>

Indicates various parameters and options about the request. **SrbFlags** is read-only. This member will be set to one or more of the following flags ORed together:

<dl> <dt>

<span id="SRB_FLAGS_DATA_IN"></span><span id="srb_flags_data_in"></span>SRB\_FLAGS\_DATA\_IN
</dt> <dd>

Indicates data will be transferred from the device to the system.

</dd> </dl>

<dl> <dt>

<span id="SRB_FLAGS_DATA_OUT"></span><span id="srb_flags_data_out"></span>SRB\_FLAGS\_DATA\_OUT
</dt> <dd>

Indicates data will be transferred from the system to the device.

</dd> </dl>

<dl> <dt>

<span id="SRB_FLAGS_NO_DATA_TRANSFER"></span><span id="srb_flags_no_data_transfer"></span>SRB\_FLAGS\_NO\_DATA\_TRANSFER
</dt> <dd>

Indicates no data transfer with this request. If this is set, the flags SRB\_FLAGS\_DATA\_OUT, SRB\_FLAGS\_DATA\_IN, and SRB\_FLAGS\_UNSPECIFIED\_DIRECTION are clear.

</dd> </dl>

<dl> <dt>

<span id="SRB_FLAGS_DISABLE_SYNCH_TRANSFER"></span><span id="srb_flags_disable_synch_transfer"></span>SRB\_FLAGS\_DISABLE\_SYNCH\_TRANSFER
</dt> <dd>

Indicates the HBA, if possible, should perform asynchronous I/O for this transfer request. If synchronous I/O was negotiated previously, the HBA must renegotiate for asynchronous I/O before performing the transfer.

</dd> </dl>

<dl> <dt>

<span id="SRB_FLAGS_DISABLE_DISCONNECT"></span><span id="srb_flags_disable_disconnect"></span>SRB\_FLAGS\_DISABLE\_DISCONNECT
</dt> <dd>

Indicates the HBA should not allow the target to disconnect from the SCSI bus during processing of this request.

</dd> </dl> </dd> <dt>

**DataTransferLength**
</dt> <dd>

Indicates the size in bytes of the data buffer. A miniport driver calls [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md) with *BufferSize* set to this value. If an underrun occurs, the miniport driver must update this member to the number of bytes actually transferred.

</dd> <dt>

**TimeOutValue**
</dt> <dd>

Indicates the interval in seconds that the request can execute before the OS-specific port driver might consider it timed out. Miniport drivers are not required to time requests because the port driver already does.

</dd> <dt>

**DataBuffer**
</dt> <dd>

Points to the data buffer. A miniport driver calls [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md) with *Buffer* set to this value. Miniport drivers can use this value as a data pointer regardless of the value of **MapBuffers** in the PORT\_CONFIGURATION\_INFORMATION for the HBA. A miniport driver cannot transfer data directly into the buffer using DMA.

</dd> <dt>

**DataPath**
</dt> <dd>

Specifies the WMI data path for this request. A miniport driver calls [**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md) with *DataPath* set to this value.

</dd> <dt>

**Reserved3**
</dt> <dd>

Reserved for system use and not available for use by miniport drivers.

</dd> <dt>

**OriginalRequest**
</dt> <dd>

Points to the IRP for this request. This member is irrelevant to miniport drivers.

</dd> <dt>

**SrbExtension**
</dt> <dd>

Points to the Srb extension. A miniport driver must not use this member if it set **SrbExtensionSize** to zero in the HW\_INITIALIZATION\_DATA. The memory at **SrbExtension** is not initialized by the OS-specific port driver, and the miniport driver-determined data can be accessed directly by the HBA. The corresponding physical address can be obtained by calling [**ScsiPortGetPhysicalAddress**](scsiportgetphysicaladdress.md) with the **SrbExtension** pointer.

</dd> <dt>

**Reserved4**
</dt> <dd>

Reserved for system use and not available for use by miniport drivers.

</dd> <dt>

**Reserved6**
</dt> <dd>

Reserved for system use and not available for use by miniport drivers. This member is valid starting with Windows Server 2003 with SP1.

</dd> <dt>

**Reserved5**
</dt> <dd>

Reserved for system use and not available for use by miniport drivers.

</dd> </dl>

## Remarks

Windows NT storage class and filter drivers can send WMI SRBs to the system port driver. The system port driver will handle certain WMI requests on behalf of miniport drivers. If the port driver cannot handle a WMI request, it forwards the request to the miniport driver.

A miniport driver receives WMI requests from the port driver only if the miniport driver set **WmiDataProvider** in the PORT\_CONFIGURATION\_INFORMATION structure. If the miniport driver supports a request, it should process it and complete the request by calling **ScsiPortNotification** twice, first with **RequestComplete** and then with **NextRequest** (or **NextLuRequest**).

For information about supporting WMI in miniport drivers, see the [Windows Management Instrumentation](https://msdn.microsoft.com/library/windows/hardware/ff547139).

## Requirements



|                   |                                                                                                                                         |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Srb.h (include Storport.h, Srb.h, Storport.h, or Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**HW\_INITIALIZATION\_DATA (SCSI)**](hw-initialization-data--scsi-.md)
</dt> <dt>

[**PORT\_CONFIGURATION\_INFORMATION (SCSI)**](port-configuration-information--scsi-.md)
</dt> <dt>

[**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md)
</dt> <dt>

[**ScsiPortNotification**](scsiportnotification.md)
</dt> <dt>

[**ScsiPortWmiDispatchFunction**](scsiportwmidispatchfunction.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SCSI_WMI_REQUEST_BLOCK%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






