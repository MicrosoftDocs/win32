---
title: ISCSI\_NIC\_LINKSTATE enumeration
description: The ISCSI\_NIC\_LINKSTATE enumeration indicates whether a port is connected to the network or not.
ms.assetid: 'e373b1dd-54bd-429c-a5b9-9f8df546c185'
keywords: ["ISCSI_NIC_LINKSTATE enumeration Storage Devices", "PISCSI_NIC_LINKSTATE enumeration pointer Storage Devices"]
topic_type:
- apiref
api_name:
- ISCSI_NIC_LINKSTATE
api_location:
- iscsicfg.h
api_type:
- HeaderDef
---

# ISCSI\_NIC\_LINKSTATE enumeration

The ISCSI\_NIC\_LINKSTATE enumeration indicates whether a port is connected to the network or not.

## Syntax


```C++
typedef enum  { 
  ISCSI_NIC_LINKSTATE_DISCONNECTED  = 0,
  ISCSI_NIC_LINKSTATE_CONNECTED     = 1
} ISCSI_NIC_LINKSTATE, *PISCSI_NIC_LINKSTATE;
```



## Constants

<dl> <dt>

<span id="ISCSI_NIC_LINKSTATE_DISCONNECTED"></span><span id="iscsi_nic_linkstate_disconnected"></span>**ISCSI\_NIC\_LINKSTATE\_DISCONNECTED**
</dt> <dd>

A network port is disconnected from the network.

</dd> <dt>

<span id="ISCSI_NIC_LINKSTATE_CONNECTED"></span><span id="iscsi_nic_linkstate_connected"></span>**ISCSI\_NIC\_LINKSTATE\_CONNECTED**
</dt> <dd>

A network port is connected to the network.

</dd> </dl>

## Remarks

The ISCSI\_NIC\_LINKSTATE enumeration is used with the [MSiSCSI\_NICConfig WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563083).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsicfg.h (include Iscsicfg.h)</dt> </dl> |



## See also

<dl> <dt>

[**MSiSCSI\_NICConfig**](msiscsi-nicconfig.md)
</dt> <dt>

[MSiSCSI\_NICConfig WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563083)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSI_NIC_LINKSTATE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






