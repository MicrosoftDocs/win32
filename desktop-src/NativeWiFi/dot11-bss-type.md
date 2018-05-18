---
Description: 'Defines a basic service set (BSS) network type.'
ms.assetid: '13d57339-655e-4978-974e-e7b12a83d18a'
title: 'DOT11\_BSS\_TYPE enumeration'
---

# DOT11\_BSS\_TYPE enumeration

The **DOT11\_BSS\_TYPE** enumerated type defines a basic service set (BSS) network type.

## Syntax


```C++
typedef enum _DOT11_BSS_TYPE { 
  dot11_BSS_type_infrastructure  = 1,
  dot11_BSS_type_independent     = 2,
  dot11_BSS_type_any             = 3
} DOT11_BSS_TYPE, *PDOT11_BSS_TYPE;
```



## Constants

<dl> <dt>

<span id="dot11_BSS_type_infrastructure"></span><span id="dot11_bss_type_infrastructure"></span><span id="DOT11_BSS_TYPE_INFRASTRUCTURE"></span>**dot11\_BSS\_type\_infrastructure**
</dt> <dd>

Specifies an infrastructure BSS network.

</dd> <dt>

<span id="dot11_BSS_type_independent"></span><span id="dot11_bss_type_independent"></span><span id="DOT11_BSS_TYPE_INDEPENDENT"></span>**dot11\_BSS\_type\_independent**
</dt> <dd>

Specifies an independent BSS (IBSS) network.

</dd> <dt>

<span id="dot11_BSS_type_any"></span><span id="dot11_bss_type_any"></span><span id="DOT11_BSS_TYPE_ANY"></span>**dot11\_BSS\_type\_any**
</dt> <dd>

Specifies either infrastructure or IBSS network.

</dd> </dl>

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista, Windows XP with SP3 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                        |
| Redistributable<br/>          | Wireless LAN API for Windows XP with SP2<br/>                                                         |
| Header<br/>                   | <dl> <dt>Wlantypes.h (include Windot11.h)</dt> </dl> |



## See also

<dl> <dt>

[**WLAN\_BSS\_ENTRY**](wlan-bss-entry.md)
</dt> <dt>

[**WLAN\_CONNECTION\_PARAMETERS**](wlan-connection-parameters.md)
</dt> <dt>

[**WlanGetNetworkBssList**](wlangetnetworkbsslist.md)
</dt> </dl>

 

 




