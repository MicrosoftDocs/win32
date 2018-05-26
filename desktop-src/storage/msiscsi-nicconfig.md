---
title: MSiSCSI\_NICConfig structure
description: The MSiSCSI\_NICConfig structure describes the configuration of a network interface card (NIC) port.
ms.assetid: ee40ea1f-fe9b-4126-b5b1-83f60cf51909
keywords:
- MSiSCSI_NICConfig structure Storage Devices
- PMSiSCSI_NICConfig structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSiSCSI_NICConfig
api_location:
- iscsicfg.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSiSCSI\_NICConfig structure

The MSiSCSI\_NICConfig structure describes the configuration of a network interface card (NIC) port.

## Syntax


```C++
typedef struct _MSiSCSI_NICConfig {
  ULONG LinkSpeed;
  ULONG MaxLinkSpeed;
  ULONG LinkState;
  ULONG MaxFrameSize;
  UCHAR MacAddress[6];
} MSiSCSI_NICConfig, *PMSiSCSI_NICConfig;
```



## Members

<dl> <dt>

**LinkSpeed**
</dt> <dd>

The speed of the network link, in megabits per second.

</dd> <dt>

**MaxLinkSpeed**
</dt> <dd>

The maximum speed of the network link, in megabits per second (Mbps).

</dd> <dt>

**LinkState**
</dt> <dd>

A [**ISCSI\_NIC\_LINKSTATE**](iscsi-nic-linkstate.md) enumeration value that indicates whether the port is connected to the network or not.

</dd> <dt>

**MaxFrameSize**
</dt> <dd>

The maximum frame size, in bytes.

</dd> <dt>

**MacAddress**
</dt> <dd>

The Ethernet MAC address of the port.

</dd> </dl>

## Remarks

The WMI tool suite automatically generates a declaration of the MSiSCSI\_NICConfig structure when it compiles the [MSiSCSI\_NICConfig WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563083) in *Config.mof*.

Initiators are *not* required to implement the MSiSCSI\_NICConfig class.

Initiators that implement the MSiSCSI\_NICConfig class should create one instance of the class for each network port on the adapter.

Initiators should register each instance of the MSiSCSI\_NICConfig class by using the name of the physical device object (PDO) for the corresponding network port. It is optional that you implement this class.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsicfg.h (include Iscsicfg.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_NIC\_LINKSTATE**](iscsi-nic-linkstate.md)
</dt> <dt>

[MSiSCSI\_NICConfig WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563083)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_NICConfig%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






