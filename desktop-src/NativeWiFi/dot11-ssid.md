---
description: Contains the SSID of an interface.
ms.assetid: f2b15ef9-99ee-4505-8575-224112024d7a
title: DOT11_SSID structure (Wlantypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DOT11_SSID
api_type: 
- HeaderDef
api_location: 
- wlantypes.h
---

# DOT11\_SSID structure

A **DOT11\_SSID** structure contains the SSID of an interface.

## Syntax


```C++
typedef struct _DOT11_SSID {
  ULONG uSSIDLength;
  UCHAR ucSSID[DOT11_SSID_MAX_LENGTH];
} DOT11_SSID, *PDOT11_SSID;
```



## Members

<dl> <dt>

**uSSIDLength**
</dt> <dd>

The length, in bytes, of the **ucSSID** array.

</dd> <dt>

**ucSSID**
</dt> <dd>

The SSID. DOT11\_SSID\_MAX\_LENGTH is set to 32.

</dd> </dl>

## Remarks

The SSID that is specified by the **ucSSID** member is not a null-terminated ASCII string. The length of the SSID is determined by the **uSSIDLength** member.

A wildcard SSID is an SSID whose **uSSIDLength** member is set to zero. When the desired SSID is set to the wildcard SSID, the 802.11 station can connect to any basic service set (BSS) network.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista, Windows XP with SP3 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                        |
| Redistributable<br/>          | Wireless LAN API for Windows XP with SP2<br/>                                                         |
| Header<br/>                   | <dl> <dt>Wlantypes.h (include Windot11.h)</dt> </dl> |



## See also

<dl> <dt>

[**WLAN\_CONNECTION\_PARAMETERS**](/windows/desktop/api/wlanapi/ns-wlanapi-wlan_connection_parameters)
</dt> <dt>

[**WlanGetNetworkBssList**](/windows/desktop/api/Wlanapi/nf-wlanapi-wlangetnetworkbsslist)
</dt> <dt>

[**WlanScan**](/windows/desktop/api/wlanapi/nf-wlanapi-wlanscan)
</dt> </dl>

 

 




