---
title: MS\_SMHBA\_SAS\_PHY structure
description: The MS\_SMHBA\_SAS\_PHY structure is used to report the SAS physical port information.
ms.assetid: 9bbf2f63-4479-47ee-a014-78b13deccb4c
keywords:
- MS_SMHBA_SAS_PHY structure Storage Devices
- PMS_SMHBA_SAS_PHY structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MS_SMHBA_SAS_PHY
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# MS\_SMHBA\_SAS\_PHY structure

The MS\_SMHBA\_SAS\_PHY structure is used to report the SAS physical port information.

## Syntax


```C++
typedef struct _MS_SMHBA_SAS_PHY {
  UCHAR PhyIdentifier;
  ULONG NegotiatedLinkRate;
  ULONG ProgrammedMinLinkRate;
  ULONG HardwareMinLinkRate;
  ULONG ProgrammedMaxLinkRate;
  ULONG HardwareMaxLinkRate;
  UCHAR domainPortWWN[8];
} MS_SMHBA_SAS_PHY, *PMS_SMHBA_SAS_PHY;
```



## Members

<dl> <dt>

**PhyIdentifier**
</dt> <dd>

The port whose physical configuration and link information is being returned. It is unique within the context of the SAS device that contains the physical port.

</dd> <dt>

**NegotiatedLinkRate**
</dt> <dd>

The state or the transmission speed that is negotiated by the physical port for the physical link.

</dd> <dt>

**ProgrammedMinLinkRate**
</dt> <dd>

The minimum physical link rate that is set by the physical port control mechanism.

</dd> <dt>

**HardwareMinLinkRate**
</dt> <dd>

The minimum physical link rate that is supported by the physical port.

</dd> <dt>

**ProgrammedMaxLinkRate**
</dt> <dd>

The maximum physical link rate that is set by the physical port control mechanism.

</dd> <dt>

**HardwareMaxLinkRate**
</dt> <dd>

The maximum physical link rate that is supported by the physical port.

</dd> <dt>

**domainPortWWN**
</dt> <dd>

The Port\_Identifier that has the smallest value of any Port\_Identifier of an expander SMP.

</dd> </dl>

## Remarks

Link rates are defined in hpaapi.h as HBA\_SASSPEED\_1\_5GBIT and HBA\_SASSPEED\_3GBIT.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MS_SMHBA_SAS_PHY%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





