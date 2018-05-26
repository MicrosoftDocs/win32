---
title: PHW\_RESET\_BUS callback function
description: The PHW\_RESET\_BUS prototype declares a routine that resets the indicated SCSI bus.
ms.assetid: 8c41ca6d-4b55-4858-b8bb-d7b2e682a8f7
keywords:
- ( PHW_RESET_BUS) callback function Storage Devices
topic_type:
- apiref
api_name:
- ( PHW_RESET_BUS)
api_location:
- srb.h
api_type:
- UserDefined
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PHW\_RESET\_BUS callback function

The PHW\_RESET\_BUS prototype declares a routine that resets the indicated SCSI bus.

## Syntax


```C++
typedef BOOLEAN (*PHW_RESET_BUS)(
  _In_ PVOID DeviceExtension ,
  _In_ ULONG PathId
);
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Pointer to the miniport driver's per-HBA storage area.

</dd> <dt>

*PathId* \[in\]
</dt> <dd>

Contains a number that identifies the SCSI bus to be reset.

</dd> </dl>

## Return value

The routine that this prototype declares returns **TRUE** if the bus is successfully reset. The routine returns **FALSE** if the bus is not successfully reset.

## Remarks

The initialization routine for both SCSI and StorPort miniport drivers are declared using this prototype.

For more information about the SCSI miniport driver's bus reset routine see [*HwScsiResetBus*](hwscsiresetbus.md).

For more information about the bus reset routine that is used with the StorPort driver's miniport driver routine, see [**HwStorResetBus**](hwstorresetbus.md).

## Requirements



|                            |                                                                                                                             |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                          |
| Header<br/>          | <dl> <dt>Srb.h (include Storport.h, Srb.h, or Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[*HwScsiResetBus*](hwscsiresetbus.md)
</dt> <dt>

[**HwStorResetBus**](hwstorresetbus.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PHW_RESET_BUS%20callback%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






