---
description: Are used to define an IEEE media access control (MAC) address.
ms.assetid: c1335127-a2d2-4f44-a895-1abbc5eaf98d
title: DOT11_MAC_ADDRESS (Windot11.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# DOT11\_MAC\_ADDRESS

The **DOT11\_MAC\_ADDRESS** types are used to define an IEEE media access control (MAC) address.


```C++
typedef UCHAR DOT11_MAC_ADDRESS[6];
typedef DOT11_MAC_ADDRESS* PDOT11_MAC_ADDRESS;
```



<dl> <dt>

**DOT11\_MAC\_ADDRESS\[6\]**
</dt> <dd>

A MAC address in unicast, multicast, or broadcast format.

</dd> <dt>

**PDOT11\_MAC\_ADDRESS**
</dt> <dd>

Pointer to a MAC address in unicast, multicast, or broadcast format.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista, Windows XP with SP3 \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                       |
| Redistributable<br/>          | Wireless LAN API for Windows XP with SP2<br/>                                                        |
| Header<br/>                   | <dl> <dt>Windot11.h (include Windot11.h)</dt> </dl> |



## See also

<dl> <dt>

[**DOT11\_BSSID\_LIST**](dot11-bssid-list.md)
</dt> <dt>

[**WLAN\_ASSOCIATION\_ATTRIBUTES**](/windows/desktop/api/wlanapi/ns-wlanapi-wlan_association_attributes)
</dt> <dt>

[**WLAN\_BSS\_ENTRY**](/windows/desktop/api/wlanapi/ns-wlanapi-wlan_bss_entry)
</dt> </dl>

 

 




