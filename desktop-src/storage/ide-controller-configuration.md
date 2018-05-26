---
title: IDE\_CONTROLLER\_CONFIGURATION structure
description: The IDE\_CONTROLLER\_CONFIGURATION structure is used to pass controller configuration information between the port driver and the miniport driver.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: 89b7f66e-3a3a-4723-a409-3b3030c1a45b
keywords:
- IDE_CONTROLLER_CONFIGURATION structure Storage Devices
- PIDE_CONTROLLER_CONFIGURATION structure pointer Storage Devices
topic_type:
- apiref
api_name:
- IDE_CONTROLLER_CONFIGURATION
api_location:
- irb.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IDE\_CONTROLLER\_CONFIGURATION structure

The IDE\_CONTROLLER\_CONFIGURATION structure is used to pass controller configuration information between the port driver and the miniport driver.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
typedef struct _IDE_CONTROLLER_CONFIGURATION {
  USHORT                  Version;
  UCHAR                   NumberOfChannels;
  IDE_OPERATION_MODE      ControllerMode;
  UCHAR                   NumberOfPhysicalBreaks;
  ULONG                   MaximumTransferLength;
  BOOLEAN                 Reserved;
  BOOLEAN                 NativeModeEnabled;
  BOOLEAN                 Dma64BitAddress;
  BOOLEAN                 BusMaster;
  IDE_BUS_TYPE            AtaBusType;
  PIDE_MINIPORT_RESOURCES ControllerResources;
} IDE_CONTROLLER_CONFIGURATION, *PIDE_CONTROLLER_CONFIGURATION;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The port driver sets this field to indicate the version of the port driver. The port driver sets the version to sizeof(IDE\_CONTROLLER\_CONFIGURATION). The miniport driver should verify that the version is greater than or equal to the one it is using.

</dd> <dt>

**NumberOfChannels**
</dt> <dd>

Specifies the number of channels supported by the HBA. Note that this indicates the total number of channels including the ones that are disabled.

</dd> <dt>

**ControllerMode**
</dt> <dd>

The port driver sets this field to inform the ATA miniport which mode it is running at. There are two possible modes:



| Mode                      | Description                                                                                                                                                                                     |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IdeModeNormal <br/> | This is the standard full capabilities mode where the ATA miniport may operate normally.<br/>                                                                                             |
| IdeModeDump<br/>    | This is the limited no memory mode that an ATA miniport operates in during hibernate or crashdump. Call Back Routines and Registry Access Routines cannot be used when in this mode.<br/> |



 

</dd> <dt>

**NumberOfPhysicalBreaks**
</dt> <dd>

Specifies the maximum number of breaks between address ranges that a data buffer can have if the HBA supports scatter/gather. In other words, the number of scatter/gather lists minus one. By default, the value of this member is IDE\_UNINITIALIZED\_VALUE, which indicates the HBA can support an unlimited number of physical discontiguities. If the port driver sets a value for this member, the miniport driver can adjust the value lower but no higher. If this member is IDE\_UNINITIALIZED\_VALUE, the miniport driver must reset this member according to the HBA's scatter/gather capacity.

</dd> <dt>

**MaximumTransferLength**
</dt> <dd>

Specifies the maximum number of bytes the HBA can transfer in a single transfer operation. By default, the value of this member is IDE\_UNINITIALIZED\_VALUE, which indicates an unlimited maximum transfer size.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for future use. The miniport driver must not use this field.

</dd> <dt>

**NativeModeEnabled**
</dt> <dd>

The miniport driver could set this member to **TRUE** to indicate that the controller is to be operated in Native mode.

</dd> <dt>

**Dma64BitAddress**
</dt> <dd>

The miniport driver could set this member to **TRUE** to indicate support for 64 bit DMA operation.

</dd> <dt>

**BusMaster**
</dt> <dd>

The miniport driver could set this member to **TRUE** to indicate bus mastering support.

</dd> <dt>

**AtaBusType**
</dt> <dd>

Indicates whether it is a SATA or a PATA controller.

</dd> <dt>

**ControllerResources**
</dt> <dd>

Provides the hardware resources for the ATA controller.

</dd> </dl>

## Remarks

## Requirements



|                   |                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Irb.h (include Irb.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IDE_CONTROLLER_CONFIGURATION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





