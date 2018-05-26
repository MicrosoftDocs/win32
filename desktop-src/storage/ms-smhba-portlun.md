---
title: MS\_SMHBA\_PORTLUN structure
description: The MS\_SMHBA\_PORTLUN structure reports target LUN information that is associated with a port.
ms.assetid: cf62685f-7b4d-4671-a755-d59a593bf5d6
keywords:
- MS_SMHBA_PORTLUN structure Storage Devices
- PMS_SMHBA_PORTLUN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MS_SMHBA_PORTLUN
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MS\_SMHBA\_PORTLUN structure

The MS\_SMHBA\_PORTLUN structure reports target LUN information that is associated with a port.

## Syntax


```C++
typedef struct _MS_SMHBA_PORTLUN {
  UCHAR     PortWWN[8];
  UCHAR     domainPortWWN[8];
  ULONGLONG TargetLun;
} MS_SMHBA_PORTLUN, *PMS_SMHBA_PORTLUN;
```



## Members

<dl> <dt>

**PortWWN**
</dt> <dd>

The worldwide name of the local port whose events the WMI client will receive.

</dd> <dt>

**domainPortWWN**
</dt> <dd>

A worldwide name that specifies the SAS domain worldwide name of the local port.

</dd> <dt>

**TargetLun**
</dt> <dd>

The target LUN number.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MS_SMHBA_PORTLUN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





