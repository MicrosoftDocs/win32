---
Description: Are used to define an IEEE media access control (MAC) address.
ms.assetid: c1335127-a2d2-4f44-a895-1abbc5eaf98d
title: DOT11\_MAC\_ADDRESS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista, Windows XP with SP3 \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                       |
| Redistributable<br/>          | Wireless LAN API for Windows XP with SP2<br/>                                                        |
| Header<br/>                   | <dl> <dt>Windot11.h (include Windot11.h)</dt> </dl> |



## See also

<dl> <dt>

[**DOT11\_BSSID\_LIST**](dot11-bssid-list.md)
</dt> <dt>

[**WLAN\_ASSOCIATION\_ATTRIBUTES**](/windows/win32/wlanapi/ns-wlanapi-_wlan_association_attributes?branch=master)
</dt> <dt>

[**WLAN\_BSS\_ENTRY**](/windows/win32/wlanapi/ns-wlanapi-_wlan_bss_entry?branch=master)
</dt> </dl>

 

 




