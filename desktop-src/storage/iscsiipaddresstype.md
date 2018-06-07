---
title: ISCSIIPADDRESSTYPE enumeration
description: The ISCSIIPADDRESSTYPE enumeration indicates formats for an IP address.
ms.assetid: a92f7048-ca8a-450c-93ab-6ea040412198
keywords:
- ISCSIIPADDRESSTYPE enumeration Storage Devices
- PISCSIIPADDRESSTYPE enumeration pointer Storage Devices
topic_type:
- apiref
api_name:
- ISCSIIPADDRESSTYPE
api_location:
- iscsidef.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# ISCSIIPADDRESSTYPE enumeration

The ISCSIIPADDRESSTYPE enumeration indicates formats for an IP address.

## Syntax


```C++
typedef enum  { 
  ISCSI_IP_ADDRESS_TEXT   = 0,
  ISCSI_IP_ADDRESS_IPV4   = 1,
  ISCSI_IP_ADDRESS_IPV6   = 2,
  ISCSI_IP_ADDRESS_EMPTY  = 3
} ISCSIIPADDRESSTYPE, *PISCSIIPADDRESSTYPE;
```



## Constants

<dl> <dt>

<span id="ISCSI_IP_ADDRESS_TEXT"></span><span id="iscsi_ip_address_text"></span>**ISCSI\_IP\_ADDRESS\_TEXT**
</dt> <dd>

The IP address is in dotted decimal text format or in DNS format.

</dd> <dt>

<span id="ISCSI_IP_ADDRESS_IPV4"></span><span id="iscsi_ip_address_ipv4"></span>**ISCSI\_IP\_ADDRESS\_IPV4**
</dt> <dd>

The IP address is a binary address that complies with version 4 of the IP protocol.

</dd> <dt>

<span id="ISCSI_IP_ADDRESS_IPV6"></span><span id="iscsi_ip_address_ipv6"></span>**ISCSI\_IP\_ADDRESS\_IPV6**
</dt> <dd>

The IP address is a binary address that complies with version 6 of the IP protocol.

</dd> <dt>

<span id="ISCSI_IP_ADDRESS_EMPTY"></span><span id="iscsi_ip_address_empty"></span>**ISCSI\_IP\_ADDRESS\_EMPTY**
</dt> <dd>

No address is specified.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsidef.h (include Iscsidef.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_IP\_Address**](iscsi-ip-address.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSIIPADDRESSTYPE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






