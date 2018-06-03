---
title: MS\_SMHBA\_PORTATTRIBUTES structure
description: The MS\_SMHBA\_PORTATTRIBUTES structure is used to report the port information.
ms.assetid: ce967b15-723f-4ab7-8a79-8234291d1950
keywords:
- MS_SMHBA_PORTATTRIBUTES structure Storage Devices
- PMS_SMHBA_PORTATTRIBUTES structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MS_SMHBA_PORTATTRIBUTES
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

# MS\_SMHBA\_PORTATTRIBUTES structure

The MS\_SMHBA\_PORTATTRIBUTES structure is used to report the port information.

## Syntax


```C++
typedef struct _MS_SMHBA_PORTATTRIBUTES {
  ULONG     PortType;
  ULONG     PortState;
  ULONG     PortSpecificAttributesSize;
  WCHAR     OSDeviceName[256 + 1];
  ULONGLONG Reserved;
  UCHAR     PortSpecificAttributes[1];
} MS_SMHBA_PORTATTRIBUTES, *PMS_SMHBA_PORTATTRIBUTES;
```



## Members

<dl> <dt>

**PortType**
</dt> <dd>

An integer that indicates the port type of the SMHBA port.

</dd> <dt>

**PortState**
</dt> <dd>

An integer that indicates the current state of the SMHBA port.

</dd> <dt>

**PortSpecificAttributesSize**
</dt> <dd></dd> <dt>

**OSDeviceName**
</dt> <dd>

A nonpersistent operating system target name, for example "\\Device\\HarddiskVolume1".

</dd> <dt>

**Reserved**
</dt> <dd></dd> <dt>

**PortSpecificAttributes**
</dt> <dd></dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MS_SMHBA_PORTATTRIBUTES%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





