---
title: PORT\_PROTOCOL enumeration
description: The PORT\_PROTOCOL enumeration defines the set of IPv6 Firewall Configuration protocols.
ms.assetid: 775c3d29-89c7-4768-9476-2e56555fd82b
keywords:
- PORT_PROTOCOL enumeration ICS/ICF
- PORT_PROTOCOL enumeration ICS/ICF
topic_type:
- apiref
api_name:
- PORT_PROTOCOL
api_location:
- Netfwv6.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PORT\_PROTOCOL enumeration

\[The IPv6 Internet Connection Firewall is available for use in the operating systems specified in the Requirements section. It is unavailable in subsequent versions. Instead, use the [Windows Firewall API](windows-firewall-start-page.md).\]

The **PORT\_PROTOCOL** enumeration defines the set of IPv6 Firewall Configuration protocols.

## Syntax


```C++
typedef enum PORT_PROTOCOL_ { 
  PORT_PROTOCOL_TCP  = 6,
  PORT_PROTOCOL_UDP  = 17
} PORT_PROTOCOL;
```



## Constants

<dl> <dt>

<span id="PORT_PROTOCOL_TCP"></span><span id="port_protocol_tcp"></span>**PORT\_PROTOCOL\_TCP**
</dt> <dd>

Designates TCP protocol.

</dd> <dt>

<span id="PORT_PROTOCOL_UDP"></span><span id="port_protocol_udp"></span>**PORT\_PROTOCOL\_UDP**
</dt> <dd>

Designates UDP protocol.

</dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP1 \[desktop apps only\]<br/>                                 |
| Minimum supported server<br/> | None supported<br/>                                                            |
| Redistributable<br/>          | Advanced Networking Pack for Windows XP<br/>                                   |
| Header<br/>                   | <dl> <dt>Netfwv6.h</dt> </dl> |



## See also

<dl> <dt>

[IPv6 Firewall Configuration Enumerated Types](ipv6-firewall-enumeration-types.md)
</dt> </dl>

 

 





