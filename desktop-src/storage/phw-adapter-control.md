---
title: PHW\_ADAPTER\_CONTROL callback function
description: The PHW\_INITIALIZE routine prototype declares a routine that initializes the miniport driver after a reboot or power failure occurs.
ms.assetid: 'ef58c005-e5e5-409d-9010-59635fd4da02'
keywords: ["( PHW_ADAPTER_CONTROL) callback function Storage Devices"]
topic_type:
- apiref
api_name:
- ( PHW_ADAPTER_CONTROL)
api_location:
- srb.h
api_type:
- UserDefined
---

# PHW\_ADAPTER\_CONTROL callback function

The PHW\_INITIALIZE routine prototype declares a routine that initializes the miniport driver after a reboot or power failure occurs.

## Syntax


```C++
typedef SCSI_ADAPTER_CONTROL_STATUS (*PHW_ADAPTER_CONTROL)(
  _In_ PVOID                     DeviceExtension ,
  _In_ SCSI_ADAPTER_CONTROL_TYPE ControlType ,
  _In_ PVOID                     Parameters
);
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Pointer to the miniport driver's per-HBA storage area.

</dd> <dt>

*ControlType* \[in\]
</dt> <dd>

Specifies an adapter-control operation. For a list of the allowed operations, see [**HwScsiAdapterControl**](hwscsiadaptercontrol.md).

</dd> <dt>

*Parameters* \[in\]
</dt> <dd>

Contains information related to the *ControlType*. For an explanation of the meaning of these values, see the discussion accompanying the *Parameters* parameter of the [**HwScsiAdapterControl**](hwscsiadaptercontrol.md).

</dd> </dl>

## Return value

The routine declared by this prototype returns different sets of values depending on the control type. For a complete description of the return values, see [**HwScsiAdapterControl**](hwscsiadaptercontrol.md).

## Remarks

The adapter control routine for both SCSI and StorPort miniport drivers are declared using this prototype.

For more information about the SCSI miniport driver's adapter control routine, see [**HwScsiAdapterControl**](hwscsiadaptercontrol.md).

For more information about the adapter control routine that is used with the StorPort driver's miniport driver, see [**HwStorAdapterControl**](hwstoradaptercontrol.md).

## Requirements



|                            |                                                                                                                             |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                          |
| Header<br/>          | <dl> <dt>Srb.h (include Storport.h, Srb.h, or Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**HwScsiAdapterControl**](hwscsiadaptercontrol.md)
</dt> <dt>

[**HwStorAdapterControl**](hwstoradaptercontrol.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PHW_ADAPTER_CONTROL%20callback%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






