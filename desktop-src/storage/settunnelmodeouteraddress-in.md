---
title: SetTunnelModeOuterAddress\_IN structure
description: The SetTunnelModeOuterAddress\_IN structure holds the input data for the SetTunnelModeOuterAddress method.
ms.assetid: '3f698252-213f-482c-8c8f-624f0c370705'
keywords: ["SetTunnelModeOuterAddress_IN structure Storage Devices", "PSetTunnelModeOuterAddress_IN structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- SetTunnelModeOuterAddress_IN
api_location:
- iscsiop.h
api_type:
- HeaderDef
---

# SetTunnelModeOuterAddress\_IN structure

The SetTunnelModeOuterAddress\_IN structure holds the input data for the [SetTunnelModeOuterAddress](https://msdn.microsoft.com/library/windows/hardware/ff566186) method.

## Syntax


```C++
typedef struct _SetTunnelModeOuterAddress_IN {
  ULONG            PortNumber;
  ISCSI_IP_Address DestinationAddress;
  ISCSI_IP_Address TunnelModeOuterAddress;
} SetTunnelModeOuterAddress_IN, *PSetTunnelModeOuterAddress_IN;
```



## Members

<dl> <dt>

**PortNumber**
</dt> <dd>

The number of the port to associate with the tunnel-mode address. A value of 0xffffffff associates the tunnel-mode address with all ports.

</dd> <dt>

**DestinationAddress**
</dt> <dd>

An [**ISCSI\_IP\_Address**](iscsi-ip-address.md) structure that indicates the destination IP address in a way that is independent of the version of IP protocol in use.

</dd> <dt>

**TunnelModeOuterAddress**
</dt> <dd>

An ISCSI\_IP\_Address structure that indicates the IP address of the security gateway (tunnel-mode outer address) in a way that is independent of the version of IP protocol in use.

</dd> </dl>

## Remarks

You must implement this method.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_IP\_Address**](iscsi-ip-address.md)
</dt> <dt>

[SetTunnelModeOuterAddress](https://msdn.microsoft.com/library/windows/hardware/ff566186)
</dt> <dt>

[**SetTunnelModeOuterAddress\_OUT**](settunnelmodeouteraddress-out.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SetTunnelModeOuterAddress_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






