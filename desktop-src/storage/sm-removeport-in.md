---
title: SM\_RemovePort\_IN structure
description: The SM\_RemovePort\_IN structure is used to provide input parameters to the SM\_RemovePort WMI method.
ms.assetid: b8eb6321-928f-4366-9553-c75900fa1ac6
keywords:
- SM_RemovePort_IN structure Storage Devices
- PSM_RemovePort_IN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SM_RemovePort_IN
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

# SM\_RemovePort\_IN structure

The SM\_RemovePort\_IN structure is used to provide input parameters to the SM\_RemovePort WMI method.

## Syntax


```C++
typedef struct _SM_RemovePort_IN {
  UCHAR PortWWN[8];
  ULONG EventType;
} SM_RemovePort_IN, *PSM_RemovePort_IN;
```



## Members

<dl> <dt>

**PortWWN**
</dt> <dd>

A worldwide name (WWN) that indicates the port that should be removed from the list of ports whose events are reported to the WMI client.

</dd> <dt>

**EventType**
</dt> <dd>

An event type value.

</dd> </dl>

## Remarks

The WMI tool suite generates a declaration of the SM\_RemovePort\_IN structure in *Hbapiwmi.h* when it compiles the MS\_SM\_EventControl WMI class.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SM_RemovePort_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





