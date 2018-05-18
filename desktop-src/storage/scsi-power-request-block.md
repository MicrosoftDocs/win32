---
title: SCSI\_POWER\_REQUEST\_BLOCK structure
description: The SCSI\_POWER\_REQUEST\_BLOCK structure is a special version of a SCSI\_REQUEST\_BLOCK that is used for power management requests.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future.
ms.assetid: '04981b68-db32-461b-b24b-8b2bf2e53f78'
keywords: ["SCSI_POWER_REQUEST_BLOCK structure Storage Devices", "PSCSI_POWER_REQUEST_BLOCK structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- SCSI_POWER_REQUEST_BLOCK
api_location:
- storport.h
api_type:
- HeaderDef
---

# SCSI\_POWER\_REQUEST\_BLOCK structure

The **SCSI\_POWER\_REQUEST\_BLOCK** structure is a special version of a [**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md) that is used for power management requests.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _SCSI_POWER_REQUEST_BLOCK {
  USHORT                     Length;
  UCHAR                      Function;
  UCHAR                      SrbStatus;
  UCHAR                      SrbPowerFlags;
  UCHAR                      PathId;
  UCHAR                      TargetId;
  UCHAR                      Lun;
  STOR_DEVICE_POWER_STATE    DevicePowerState;
  ULONG                      SrbFlags;
  ULONG                      DataTransferLength;
  ULONG                      TimeOutValue;
  PVOID                      DataBuffer;
  PVOID                      SenseInfoBuffer;
  struct _SCSI_REQUEST_BLOCK  *NextSrb;
  PVOID                      OriginalRequest;
  PVOID                      SrbExtension;
  STOR_POWER_ACTION          PowerAction;
#ifdef _WIN64
  ULONG                      Reserved;
#endif 
  UCHAR                      Reserved5[16];
} SCSI_POWER_REQUEST_BLOCK, *PSCSI_POWER_REQUEST_BLOCK;
```



## Members

<dl> <dt>

**Length**
</dt> <dd>

The size, in bytes, of the **SCSI\_POWER\_REQUEST\_BLOCK** structure.

</dd> <dt>

**Function**
</dt> <dd>

The operation to perform. For the **SCSI\_POWER\_REQUEST\_BLOCK** structure, this member is always set to SRB\_FUNCTION\_POWER.

</dd> <dt>

**SrbStatus**
</dt> <dd>

The status of the completed request. This member should be set by the miniport driver before it notifies the Storport driver that the request has completed. A miniport driver notifies the Storport driver that the request has completed by calling the [**StorPortNotification**](storportnotification.md) function with the [**RequestComplete**](https://msdn.microsoft.com/library/windows/hardware/ff567446) notification type.

See [**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md) in the WDK documentation for a list of possible values for this member.

</dd> <dt>

**SrbPowerFlags**
</dt> <dd>

The power management flags. Currently, the only flag allowed is SRB\_POWER\_FLAGS\_ADAPTER\_REQUEST, which indicates that the power management request is for the adapter. If this flag is set, the miniport driver should ignore the values in the **PathId**, **TargetId**, and **Lun**.

</dd> <dt>

**PathId**
</dt> <dd>

The SCSI port or bus identifier for the request. This value is zero based.

</dd> <dt>

**TargetId**
</dt> <dd>

The target controller or device identifier on the bus.

</dd> <dt>

**Lun**
</dt> <dd>

The logical unit number (LUN) of the device.

</dd> <dt>

**DevicePowerState**
</dt> <dd>

An enumerator value of type [**STOR\_DEVICE\_POWER\_STATE**](stor-device-power-state.md) that specifies the requested power state of the device.

</dd> <dt>

**SrbFlags**
</dt> <dd>

Miniport driver should ignore this member.

</dd> <dt>

**DataTransferLength**
</dt> <dd>

Miniport driver should ignore this member.

</dd> <dt>

**TimeOutValue**
</dt> <dd>

The interval, in seconds, that the request can execute before the Storport driver determines that the request has timed out.

</dd> <dt>

**DataBuffer**
</dt> <dd>

Miniport driver should ignore this member.

</dd> <dt>

**SenseInfoBuffer**
</dt> <dd>

Miniport driver should ignore this member.

</dd> <dt>

**NextSrb**
</dt> <dd>

Miniport driver should ignore this member.

</dd> <dt>

**OriginalRequest**
</dt> <dd>

Miniport driver should ignore this member.

</dd> <dt>

**SrbExtension**
</dt> <dd>

A pointer to the SRB extension. A miniport driver must not use this member if it set **SrbExtensionSize** to zero in the [**HW\_INITIALIZATION\_DATA**](hw-initialization-data--storport-.md) structure. The Storport driver does not initialize the memory that this member points to. The HBA can directly access the data that the miniport driver writes into the SRB extension. A miniport driver can obtain the physical address of the SRB extension by calling the [**StorPortGetPhysicalAddress**](storportgetphysicaladdress.md) routine.

</dd> <dt>

**PowerAction**
</dt> <dd>

An enumerator value of type [**STOR\_POWER\_ACTION**](stor-power-action.md) that specifies the type of system shutdown that is about to occur. This value is meaningful only if the device is moving into the D1, D2, or D3 power state as indicated by the **DevicePowerState** member.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for system use.

</dd> <dt>

**Reserved5**
</dt> <dd>

Reserved for system use.

</dd> </dl>

## Remarks

The Storport driver calls [**HwStorBuildIo**](hwstorbuildio.md) to pass SRBs to the miniport driver. **HwStorBuildIo** should check the **Function** member of the SRB to determine the type of the SRB. If the **Function** member is set to SRB\_FUNCTION\_POWER, the SRB is a structure of type **SCSI\_POWER\_REQUEST\_BLOCK**.

The Storport driver sends **SCSI\_POWER\_REQUEST\_BLOCK** requests to a miniport driver to notify the miniport driver of Windows power events that affect storage devices that are connected to the adapter. In the case of a power up event, this request gives the miniport driver an opportunity to initialize itself. In the case of a hibernation or shutdown event, this request gives the miniport driver an opportunity to complete I/O requests and prepare for a power down. The miniport driver can use the value in the **PowerAction** member of the **SCSI\_POWER\_REQUEST\_BLOCK** to determine what actions are required. After the miniport driver completes the **SCSI\_POWER\_REQUEST\_BLOCK** request, the Storport driver calls [**HwScsiAdapterControl**](hwscsiadaptercontrol.md) with a control request of **ScsiStopAdapter** to power down the adapter. The miniport driver reinitialize while processing the SRB\_FUNCTION\_POWER request, or it can wait and reinitialize when the Storport driver calls [**HwStorAdapterControl**](hwstoradaptercontrol.md) to perform a an **ScsiRestartAdapter** control request.

When transitioning from the D0 power state to a lower-powered state (D1, D2, or D3) the Storport driver sends a **SCSI\_POWER\_REQUEST\_BLOCK** request to the miniport driver before the underlying bus driver powers down the adapter.

The following conditions must exist before the Storport driver will send a **SCSI\_POWER\_REQUEST\_BLOCK** request to the miniport driver:

-   The adapter is not stopped.

-   The I/O queue for the adapter is paused.

-   The adapter hardware is powered up.

-   The miniport can access the adapter's hardware resources.

## Requirements



|                   |                                                                                                                                  |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storport.h (include Storport.h, Minitape.h, or Srb.h)</dt> </dl> |



## See also

<dl> <dt>

[**HwStorBuildIo**](hwstorbuildio.md)
</dt> <dt>

[**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md)
</dt> <dt>

[**StorPortNotification**](storportnotification.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SCSI_POWER_REQUEST_BLOCK%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






