---
title: PHW\_ADAPTER\_STATE callback function
description: The PHW\_INITIALIZE routine prototype declares a routine that saves or restores the state of the miniport driver's HBA.
ms.assetid: 68483404-5ea7-47f6-a6ae-6909e5b6759e
keywords:
- ( PHW_ADAPTER_STATE) callback function Storage Devices
topic_type:
- apiref
api_name:
- ( PHW_ADAPTER_STATE)
api_location:
- srb.h
api_type:
- UserDefined
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PHW\_ADAPTER\_STATE callback function

The PHW\_INITIALIZE routine prototype declares a routine that saves or restores the state of the miniport driver's HBA.

## Syntax


```C++
typedef BOOLEAN (*PHW_ADAPTER_STATE)(
  _In_ PVOID   DeviceExtension ,
  _In_ PVOID   Context,
  _In_ BOOLEAN SaveState
);
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Pointer to the miniport driver's per-HBA storage area.

</dd> <dt>

*Context* \[in\]
</dt> <dd>

Reserved for system use.

</dd> <dt>

*SaveState* \[in\]
</dt> <dd>

Indicates, when **TRUE**, that the miniport driver should save the current state of the HBA until the [**HwScsiAdapterState**](hwscsiadapterstate.md) routine is called again with *SaveState* set to **FALSE** to restore the saved state.

</dd> </dl>

## Return value

The routine declared by this prototype returns **TRUE** if it successfully saved or restored the HBA state, **FALSE** otherwise.

## Remarks

Only SCSI miniport drivers use this prototype. Miniport drivers that work with the StorPort driver do not use the routine that is declared by this prototype.

For more information about the routine declared by this prototype, see [**HwScsiAdapterState**](hwscsiadapterstate.md).

## Requirements



|                            |                                                                                                                             |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                          |
| Header<br/>          | <dl> <dt>Srb.h (include Storport.h, Srb.h, or Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**HwScsiAdapterState**](hwscsiadapterstate.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PHW_ADAPTER_STATE%20callback%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






