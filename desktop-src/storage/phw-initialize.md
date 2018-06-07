---
title: PHW\_INITIALIZE callback function
description: The PHW\_INITIALIZE routine prototype declares a routine that initializes the miniport driver after a reboot or power failure occurs.
ms.assetid: dd678196-62f6-4c27-845f-a9b52c663e2a
keywords:
- ( PHW_INITIALIZE) callback function Storage Devices
topic_type:
- apiref
api_name:
- ( PHW_INITIALIZE)
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

# PHW\_INITIALIZE callback function

The PHW\_INITIALIZE routine prototype declares a routine that initializes the miniport driver after a reboot or power failure occurs.

## Syntax


```C++
typedef BOOLEAN (*PHW_INITIALIZE)(
  _In_ PVOID DeviceExtension 
);
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Pointer to the miniport driver's per-HBA storage area.

</dd> </dl>

## Return value

If the operation succeeds, the initialization routine returns **TRUE**. Otherwise, the initialize routine returns **FALSE**.

## Remarks

The initialization routine for both SCSI and StorPort miniport drivers are declared using this prototype.

For more information about the SCSI miniport driver initialization routine see [*HwScsiInitialize*](hwscsiinitialize.md).

For more information about the miniport driver initialization routine that is used with the StorPort driver see [**HwStorInitialize**](hwstorinitialize.md).

## Requirements



|                            |                                                                                                                             |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                          |
| Header<br/>          | <dl> <dt>Srb.h (include Storport.h, Srb.h, or Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[*HwScsiInitialize*](hwscsiinitialize.md)
</dt> <dt>

[**HwStorInitialize**](hwstorinitialize.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PHW_INITIALIZE%20callback%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






