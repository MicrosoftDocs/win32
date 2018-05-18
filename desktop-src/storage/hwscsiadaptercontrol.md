---
title: PHW\_ADAPTER\_CONTROL routine
description: A miniport driver's HwScsiAdapterControl routine is called to perform synchronous operations to control the state or behavior of an HBA, such as stopping or restarting the HBA for power management.Note The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models.
ms.assetid: '54b806a6-2b4b-4495-a89e-a6ea9b01a7ac'
keywords: ["HwScsiAdapterControl routine Storage Devices", "PHW_ADAPTER_CONTROL"]
topic_type:
- apiref
api_name:
- HwScsiAdapterControl
api_location:
- miniport.h
api_type:
- HeaderDef
---

# PHW\_ADAPTER\_CONTROL routine

A miniport driver's **HwScsiAdapterControl** routine is called to perform synchronous operations to control the state or behavior of an HBA, such as stopping or restarting the HBA for power management.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
SCSI_ADAPTER_CONTROL_STATUS HwScsiAdapterControl(
  _In_ PVOID                     HwDeviceExtension,
  _In_ SCSI_ADAPTER_CONTROL_TYPE ControlType,
  _In_ PVOID                     Parameters
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

Points to the miniport driver's per-HBA storage area.

</dd> <dt>

*ControlType* \[in\]
</dt> <dd>

Specifies one of the following adapter-control operations.

<dl> <dt>

<span id="ScsiQuerySupportedControlTypes"></span><span id="scsiquerysupportedcontroltypes"></span><span id="SCSIQUERYSUPPORTEDCONTROLTYPES"></span>**ScsiQuerySupportedControlTypes**
</dt> <dd>

Reports the adapter-control operations implemented by the miniport driver. The port driver calls **HwScsiAdapterControl** with this control type after the HBA has been initialized but before the first I/O. The miniport driver fills in the SCSI\_SUPPORTED\_CONTROL\_TYPE\_LIST structure at *Parameters* with the operations it supports. After **HwScsiAdapterControl** returns from this call, the port driver calls the miniport driver's **HwScsiAdapterControl** only for supported operations.

</dd> <dt>

<span id="ScsiStopAdapter"></span><span id="scsistopadapter"></span><span id="SCSISTOPADAPTER"></span>**ScsiStopAdapter**
</dt> <dd>

Shuts down the HBA. The port driver calls **HwScsiAdapterControl** with this control type when the HBA has been removed from the system, stopped for resource reconfiguration, shut down for power management, or otherwise reconfigured or disabled. The port driver ensures that there are no uncompleted requests and issues an SRB\_FUNCTION\_FLUSH request to the miniport driver before calling this routine.

The miniport driver disables interrupts on its HBA, halts all processing, (including background processing not subject to interrupts or processing of which the port driver is unaware, such as reconstructing fault-tolerant volumes), flushes any remaining cached data to persistent storage, and puts the HBA into a state from which it can be reinitialized or restarted.

The miniport driver should not free its resources when stopping its HBA. If the HBA was removed or stopped for PnP resource reconfiguration, the port driver releases resources on behalf of the miniport driver. If the HBA is shut down for power management, the miniport driver's resources are preserved so the HBA can be restarted.

After **HwScsiAdapterControl** returns from stopping the HBA, any data structures allocated on behalf of the miniport driver for the HBA should be considered invalid until the miniport driver is asked to restart.

Note that the port driver might call **HwScsiAdapterControl** to stop the adapter after the HBA has already been physically removed from the system, so the miniport driver's **HwScsiAdapterControl** routine must not perform any operations that require the HBA to be physically present while it is stopping the HBA.

The miniport driver is not called again for the HBA until either the PnP manager requests that the HBA be started, in which case the port driver (re)initializes by calling its **HwScsiAdapterControl** and [**HwScsiInitialize**](hwscsiinitialize.md) routines, or an HBA that was stopped for power management is powered up, in which case the port driver calls the miniport driver's **HwScsiAdapterControl** routine with **ScsiRestartAdapter** or, if the miniport driver does not implement that control type, repeats the initialization sequence for the HBA.

</dd> <dt>

<span id="ScsiRestartAdapter"></span><span id="scsirestartadapter"></span><span id="SCSIRESTARTADAPTER"></span>**ScsiRestartAdapter**
</dt> <dd>

Reinitializes an HBA. The port driver calls **HwScsiAdapterControl** with this control type to power up an HBA that was shut down for power management. All resources previously assigned to the miniport driver are still available, and its device extension and logical unit extensions, if any, are intact.

The miniport driver performs the same operations as in its [**HwScsiInitialize**](hwscsiinitialize.md) routine, such as setting up the HBA's registers and its initial state, if any.

The miniport driver must not call routines that can only be called from [**HwScsiFindAdapter**](hwscsifindadapter.md) or from **HwScsiAdapterControl** when the control type is ScsiSetRunningConfig, such as [**ScsiPortGetBusData**](scsiportgetbusdata.md) and [**ScsiPortSetBusDataByOffset**](scsiportsetbusdatabyoffset.md). If the miniport driver must call such routines to restart its HBA, it must also implement **ScsiSetRunningConfig**.

If the miniport driver does not implement **ScsiRestartAdapter**, the port driver calls the miniport driver's [**HwScsiFindAdapter**](hwscsifindadapter.md) and [**HwScsiInitialize**](hwscsiinitialize.md) routines. However, because such routines might do detection work unnecessary for restarting the HBA, such a miniport driver will not power up its HBA as quickly as a miniport driver that implements **ScsiRestartAdapter**.

</dd> <dt>

<span id="ScsiSetBootConfig"></span><span id="scsisetbootconfig"></span><span id="SCSISETBOOTCONFIG"></span>**ScsiSetBootConfig**
</dt> <dd>

Restores any settings on an HBA that the BIOS might need to reboot. The port driver calls **HwScsiAdapterControl** with this control type after calling this routine with **ScsiStopAdapter**.

A miniport driver must implement **ScsiSetBootConfig** if it must call [**ScsiPortGetBusData**](scsiportgetbusdata.md) or [**ScsiPortSetBusDataByOffset**](scsiportsetbusdatabyoffset.md) before the system will be able to reboot.

</dd> <dt>

<span id="ScsiSetRunningConfig"></span><span id="scsisetrunningconfig"></span><span id="SCSISETRUNNINGCONFIG"></span>**ScsiSetRunningConfig**
</dt> <dd>

Restores any settings on an HBA that the miniport driver might need to control the HBA while the system is running. The port driver calls **HwScsiAdapterControl** with **ScsiSetRunningConfig** before calling this routine with **ScsiRestartAdapter** if the miniport driver implements that control type.

The HBA's interrupt is not yet connected when the port driver makes this call, so the miniport driver must take care not to generate an interrupt.

A miniport driver must implement **ScsiSetRunningConfig**if it must call [**ScsiPortGetBusData**](scsiportgetbusdata.md) and [**ScsiPortSetBusDataByOffset**](scsiportsetbusdatabyoffset.md) to restore the appropriate running configuration to the HBA before it can be restarted.

</dd> </dl> </dd> <dt>

*Parameters* \[in\]
</dt> <dd>

If *ControlType* is **ScsiStopAdapter**, **ScsiSetBootConfig**, **ScsiSetRunningConfig**, or **ScsiRestartAdapter**, *Parameters* is **NULL**.

If *ControlType* is **ScsiQuerySupportedControlTypes**, *Parameters*points to a caller-allocated SCSI\_SUPPORTED\_CONTROL\_TYPE\_LIST structure, which is defined as follows:


```
typedef struct _SCSI_SUPPORTED_CONTROL_TYPE_LIST { 
    IN ULONG MaxControlType;
    OUT BOOLEAN SupportedTypeList[0];
} SCSI_SUPPORTED_CONTROL_TYPE_LIST, *PSCSI_SUPPORTED_CONTROL_TYPE_LIST;
```



<dl> <dt>

<span id="MaxControlType"></span><span id="maxcontroltype"></span><span id="MAXCONTROLTYPE"></span>**MaxControlType**
</dt> <dd>

Specifies the number of entries in the **SupportedTypeList** array.

</dd> <dt>

<span id="SupportedTypeList"></span><span id="supportedtypelist"></span><span id="SUPPORTEDTYPELIST"></span>**SupportedTypeList**
</dt> <dd>

Points to a caller-allocated array of BOOLEAN values that indicate the control types implemented by the miniport driver. The port driver initializes each element to **FALSE**.

The miniport driver sets the corresponding array element to **TRUE** for each operation it supports:

<dl> <dt>

SupportedTypeList\[ScsiQuerySupportedControlTypes\]
</dt> <dt>

SupportedTypeList\[ScsiStopAdapter\]
</dt> <dt>

SupportedTypeList\[ScsiRestartAdapter\]
</dt> <dt>

SupportedTypeList\[ScsiSetBootConfig\] 
</dt> <dt>

SupportedTypeList\[ScsiSetRunningConfig\]
</dt> </dl>

The miniport driver must not set any element beyond **SupportedTypeList**\[**MaxControlType** - 1\].

</dd> </dl> </dd> </dl>

## Return value

Depending on the control type, **HwScsiAdapterControl** might return one of the following SCSI\_ADAPTER\_CONTROL\_STATUS values:



| Return code                                                                                                    | Description                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt> **ScsiAdapterControlSuccess**</dt> </dl>      | The miniport driver completed the requested operation successfully. Currently, **HwScsiAdapterControl** must return this value for all control types.<br/> |
| <dl> <dt> **ScsiAdapterControlUnsuccessful**</dt> </dl> | Reserved for future use.<br/>                                                                                                                              |



 

## Remarks

A PnP miniport driver must implement **HwScsiAdapterControl** for PnP and power management operations. At a minimum, a miniport driver's **HwScsiAdapterControl** routine must support **ScsiQuerySupportedControlTypes** and **ScsiStopAdapter.**

A non-PnP miniport driver should set the **HwScsiAdapterControl** entry point to **NULL** in its HW\_INITIALIZATION\_DATA structure. PnP and power management are effectively disabled for an HBA controlled by a legacy miniport driver.

The name **HwScsiAdapterControl** is just a placeholder. The actual prototype of this routine is defined in srb.h as follows:


```
typedef
SCSI_ADAPTER_CONTROL_STATUS
(*PHW_ADAPTER_CONTROL) (
  IN PVOID  DeviceExtension,
  IN SCSI_ADAPTER_CONTROL_TYPE  ControlType,
  IN PVOID  Parameters
  );
```



For more information about the [**HwScsiFindAdapter**](hwscsifindadapter.md) routine, see [SCSI Miniport Driver's HwScsiFindAdapter Routine](https://msdn.microsoft.com/library/windows/hardware/ff565326).

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Miniport.h (include Scsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HW\_INITIALIZATION\_DATA**](hw-initialization-data--scsi-.md)
</dt> <dt>

[*HwScsiFindAdapter*](hwscsifindadapter.md)
</dt> <dt>

[*HwScsiInitialize*](hwscsiinitialize.md)
</dt> <dt>

[**ScsiPortGetBusData**](scsiportgetbusdata.md)
</dt> <dt>

[**ScsiPortSetBusDataByOffset**](scsiportsetbusdatabyoffset.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PHW_ADAPTER_CONTROL%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






