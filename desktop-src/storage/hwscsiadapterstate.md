---
title: PHW\_ADAPTER\_STATE routine
description: The HwScsiAdapterState routine saves or restores the state of the miniport driver's HBA.
ms.assetid: 'bb9b3f5e-6dce-4cd8-80ef-16c1ea7fb70a'
keywords: ["HwScsiAdapterState routine Storage Devices", "PHW_ADAPTER_STATE"]
topic_type:
- apiref
api_name:
- HwScsiAdapterState
api_location:
- miniport.h
api_type:
- HeaderDef
---

# PHW\_ADAPTER\_STATE routine

The *HwScsiAdapterState* routine saves or restores the state of the miniport driver's HBA.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
BOOLEAN HwScsiAdapterState(
  _In_ PVOID   HwDeviceExtension,
  _In_ PVOID   Context,
  _In_ BOOLEAN SaveState
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

Points to the miniport driver's storage for per-HBA data.

</dd> <dt>

*Context* \[in\]
</dt> <dd>

Is reserved for system use.

</dd> <dt>

*SaveState* \[in\]
</dt> <dd>

**TRUE** indicates the miniport driver should save the current state of the HBA until the *HwScsiAdapterState* routine is called again with *SaveState* set to **FALSE** to restore the saved state.

</dd> </dl>

## Return value

*HwScsiAdapterState* returns **TRUE** if it successfully saved or restored the HBA state, **FALSE** otherwise.

## Remarks

A miniport driver must implement this routine if both of the following are true:

-   The miniport driver's HBA has a BIOS and, therefore, can be initialized in x86 real mode.

-   The miniport driver's HBA is sensitive to x86-specific processor mode transitions.

A miniport driver can optionally implement this routine if either of the following is true:

-   The miniport driver's HBA is in x86 protected mode.

-   It is irrelevant whether the miniport driver's HBA is initialized on a CISC-or RISC-based platform.

*HwScsiAdapterState* is called by the x86-only, operating system-dependent port driver when the system transitions from x86 real to protected processor mode.

*HwScsiAdapterState* is usually called after the miniport driver's *HwScsiFindAdapter* routine.

The name *HwScsiAdapterState* is just a placeholder. The actual prototype of this routine is defined in *srb.h* as follows:


```
typedef
BOOLEAN
(*PHW_ADAPTER_STATE) (
  IN PVOID  DeviceExtension,
  IN PVOID  Context,
  IN BOOLEAN  SaveState
  );
```



For more information about the *HwScsiAdapterState* routine, see [SCSI Miniport Driver's HwScsiAdapterState Routine](https://msdn.microsoft.com/library/windows/hardware/ff565318).

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Miniport.h (include Scsi.h)</dt> </dl> |



## See also

<dl> <dt>

[*HwScsiFindAdapter*](hwscsifindadapter.md)
</dt> <dt>

[**ScsiPortInitialize**](scsiportinitialize.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PHW_ADAPTER_STATE%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






