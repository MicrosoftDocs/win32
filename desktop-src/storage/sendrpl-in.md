---
title: SendRPL\_IN structure
description: The SendRPL\_IN structure is used to deliver input parameter data to the SendRPL WMI method.
ms.assetid: '0c084258-2bd6-47a8-a060-d4ba2734ebed'
keywords: ["SendRPL_IN structure Storage Devices", "PSendRPL_IN structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- SendRPL_IN
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
---

# SendRPL\_IN structure

The SendRPL\_IN structure is used to deliver input parameter data to the [**SendRPL**](https://msdn.microsoft.com/library/windows/hardware/ff565488) WMI method.

## Syntax


```C++
typedef struct _SendRPL_IN {
  UCHAR PortWWN[8];
  UCHAR AgentWWN[8];
  ULONG agent_domain;
  ULONG portIndex;
} SendRPL_IN, *PSendRPL_IN;
```



## Members

<dl> <dt>

**PortWWN**
</dt> <dd>

Contains a worldwide name for the local port through which the read port list (RPL) command is sent.

</dd> <dt>

**AgentWWN**
</dt> <dd>

Contains a worldwide name for the port that is to be queried for a list of ports of type FC\_Port. For a definition of FC\_Port, see the T11 committee's specification for *Fibre Channel HBA API*.

</dd> <dt>

**agent\_domain**
</dt> <dd>

Contains the domain number for the domain controller that is to be queried for a list of ports of type FC\_Port. For a definition of FC\_Port, see the T11 committee's specification for *Fibre Channel HBA API*.

</dd> <dt>

**portIndex**
</dt> <dd>

Contains the port index of the first port in the list of ports of type FC\_Port to be returned.

</dd> </dl>

## Remarks

The WMI tool suite generates a declaration of the SendRPL\_IN structure in *Hbapiwmi.h* when it compiles the [MSFC\_HBAAdapterMethods WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562506).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**SendRPL**](https://msdn.microsoft.com/library/windows/hardware/ff565488)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SendRPL_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






