---
title: STORAGE\_ZONE\_CONDITION enumeration
description: Note This structure is for internal use only and should not be called from your code. .
ms.assetid: 57FF3890-6B37-45EB-BB02-22B2ADDFAA90
keywords:
- STORAGE_ZONE_CONDITION enumeration Storage Devices
- PSTORAGE_ZONE_CONDITION enumeration pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_ZONE_CONDITION
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# STORAGE\_ZONE\_CONDITION enumeration

> [!Note]  
> This structure is for internal use only and should not be called from your code.

 

## Syntax


```C++
typedef enum _STORAGE_ZONE_CONDITION { 
  ZoneConditionConventional      = 0x00,
  ZoneConditionEmpty             = 0x01,
  ZoneConditionImplicitlyOpened  = 0x02,
  ZoneConditionExplicitlyOpened  = 0x03,
  ZoneConditionClosed            = 0x04,
  ZoneConditionReadOnly          = 0x0D,
  ZoneConditionFull              = 0x0E,
  ZoneConditionOffline           = 0x0F
} STORAGE_ZONE_CONDITION, *PSTORAGE_ZONE_CONDITION;
```



## Constants

<dl> <dt>

<span id="ZoneConditionConventional"></span><span id="zoneconditionconventional"></span><span id="ZONECONDITIONCONVENTIONAL"></span>**ZoneConditionConventional**
</dt> <dd>

N/A

</dd> <dt>

<span id="ZoneConditionEmpty"></span><span id="zoneconditionempty"></span><span id="ZONECONDITIONEMPTY"></span>**ZoneConditionEmpty**
</dt> <dd>

N/A

</dd> <dt>

<span id="ZoneConditionImplicitlyOpened"></span><span id="zoneconditionimplicitlyopened"></span><span id="ZONECONDITIONIMPLICITLYOPENED"></span>**ZoneConditionImplicitlyOpened**
</dt> <dd>

N/A

</dd> <dt>

<span id="ZoneConditionExplicitlyOpened"></span><span id="zoneconditionexplicitlyopened"></span><span id="ZONECONDITIONEXPLICITLYOPENED"></span>**ZoneConditionExplicitlyOpened**
</dt> <dd>

N/A

</dd> <dt>

<span id="ZoneConditionClosed"></span><span id="zoneconditionclosed"></span><span id="ZONECONDITIONCLOSED"></span>**ZoneConditionClosed**
</dt> <dd>

N/A

</dd> <dt>

<span id="ZoneConditionReadOnly"></span><span id="zoneconditionreadonly"></span><span id="ZONECONDITIONREADONLY"></span>**ZoneConditionReadOnly**
</dt> <dd>

N/A

</dd> <dt>

<span id="ZoneConditionFull"></span><span id="zoneconditionfull"></span><span id="ZONECONDITIONFULL"></span>**ZoneConditionFull**
</dt> <dd>

N/A

</dd> <dt>

<span id="ZoneConditionOffline"></span><span id="zoneconditionoffline"></span><span id="ZONECONDITIONOFFLINE"></span>**ZoneConditionOffline**
</dt> <dd>

N/A

</dd> </dl>

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddstor.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_ZONE_CONDITION%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





