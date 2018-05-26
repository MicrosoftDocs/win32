---
title: SCSIWMI\_ENABLE\_DISABLE\_CONTROL enumeration
description: The SCSIWMI\_ENABLE\_DISABLE\_CONTROL enumerator is used to specify what to enable or disable.
ms.assetid: 0327bdc0-e4a4-4c2f-a9b9-5854e3330068
keywords:
- SCSIWMI_ENABLE_DISABLE_CONTROL enumeration Storage Devices
topic_type:
- apiref
api_name:
- SCSIWMI_ENABLE_DISABLE_CONTROL
api_location:
- scsiwmi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SCSIWMI\_ENABLE\_DISABLE\_CONTROL enumeration

The SCSIWMI\_ENABLE\_DISABLE\_CONTROL enumerator is used to specify what to enable or disable.

> [!Note]  
> The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef enum  { 
  ScsiWmiEventControl      = 0,
  ScsiWmiDataBlockControl  = 1
} SCSIWMI_ENABLE_DISABLE_CONTROL;
```



## Constants

<dl> <dt>

<span id="ScsiWmiEventControl"></span><span id="scsiwmieventcontrol"></span><span id="SCSIWMIEVENTCONTROL"></span>**ScsiWmiEventControl**
</dt> <dd>

Indicates that a WMI event is to be enabled or disabled.

</dd> <dt>

<span id="ScsiWmiDataBlockControl"></span><span id="scsiwmidatablockcontrol"></span><span id="SCSIWMIDATABLOCKCONTROL"></span>**ScsiWmiDataBlockControl**
</dt> <dd>

Indicates that a data collection for a block is to be enabled or disabled.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Scsiwmi.h (include Scsiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HwScsiWmiFunctionControl**](hwscsiwmifunctioncontrol.md)
</dt> <dt>

[**DpWmiFunctionControl**](https://msdn.microsoft.com/library/windows/hardware/ff544094)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SCSIWMI_ENABLE_DISABLE_CONTROL%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






