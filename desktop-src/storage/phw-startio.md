---
title: PHW\_STARTIO callback function
description: The PHW\_INITIALIZE routine prototype declares a routine that initializes the miniport driver after a reboot or power failure occurs.
ms.assetid: 1b177ef5-2b58-425e-9b9a-428bbe15de69
keywords:
- ( PHW_STARTIO) callback function Storage Devices
topic_type:
- apiref
api_name:
- ( PHW_STARTIO)
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

# PHW\_STARTIO callback function

The PHW\_INITIALIZE routine prototype declares a routine that initializes the miniport driver after a reboot or power failure occurs.

## Syntax


```C++
typedef BOOLEAN (*PHW_STARTIO)(
  _In_ PVOID               DeviceExtension ,
  _In_ PSCSI_REQUEST_BLOCK Srb 
);
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Pointer to the miniport driver's per-HBA storage area.

</dd> <dt>

*Srb* \[in\]
</dt> <dd>

Pointer to the SCSI request block to be started.

</dd> </dl>

## Return value

The start I/O routine returns **TRUE** to acknowledge receipt of the SCSI request block (SRB). If the start I/O routine does not receive a well-formed SRB, it returns **FALSE**.

## Remarks

The start routine for both SCSI and StorPort miniport drivers are declared using this prototype.

For more information about the SCSI miniport driver's start I/O routine see [**HwScsiStartIo**](hwscsistartio.md).

For more information about the miniport driver's start I/O routine that is used with the StorPort driver see [**HwStorStartIo**](hwstorstartio.md).

## Requirements



|                            |                                                                                                                             |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                          |
| Header<br/>          | <dl> <dt>Srb.h (include Storport.h, Srb.h, or Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**HwScsiStartIo**](hwscsistartio.md)
</dt> <dt>

[**HwStorStartIo**](hwstorstartio.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PHW_STARTIO%20callback%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






