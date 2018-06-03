---
title: SendRPS\_IN structure
description: The SendRPS\_IN structure is used to deliver input parameter data to the SendRPS WMI method.
ms.assetid: 7ab8986d-1e28-4d25-888f-cd10e310d623
keywords:
- SendRPS_IN structure Storage Devices
- PSendRPS_IN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SendRPS_IN
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

# SendRPS\_IN structure

The SendRPS\_IN structure is used to deliver input parameter data to the [**SendRPS**](https://msdn.microsoft.com/library/windows/hardware/ff565505) WMI method.

## Syntax


```C++
typedef struct _SendRPS_IN {
  UCHAR PortWWN[8];
  UCHAR AgentWWN[8];
  UCHAR ObjectWWN[8];
  ULONG AgentDomain;
  ULONG ObjectPortNumber;
} SendRPS_IN, *PSendRPS_IN;
```



## Members

<dl> <dt>

**PortWWN**
</dt> <dd>

Contains a worldwide name for the local port through which the RPS command is sent.

</dd> <dt>

**AgentWWN**
</dt> <dd>

Contains a worldwide name for the port that is to be queried for the status of the port indicated by **ObjectWWN**.

</dd> <dt>

**ObjectWWN**
</dt> <dd>

Contains the worldwide name of the port for which port status is to be returned.

</dd> <dt>

**AgentDomain**
</dt> <dd>

Contains the domain number of the domain controller to be queried for the status of the port indicated by **ObjectWWN**.

</dd> <dt>

**ObjectPortNumber**
</dt> <dd>

Contains the worldwide name of the port for which port status is to be returned.

</dd> </dl>

## Remarks

The WMI tool suite generates a declaration of the SendRPS\_IN structure in *Hbapiwmi.h* when it compiles the [MSFC\_HBAAdapterMethods WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562506).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**SendRPS**](https://msdn.microsoft.com/library/windows/hardware/ff565505)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SendRPS_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






