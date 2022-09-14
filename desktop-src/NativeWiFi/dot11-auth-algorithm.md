---
description: Defines a wireless LAN authentication algorithm.
ms.assetid: ac4097df-46dc-4c64-b72a-7cb9dce8b418
title: DOT11_AUTH_ALGORITHM enumeration (Wlantypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DOT11_AUTH_ALGORITHM
api_type: 
- HeaderDef
api_location: 
- wlantypes.h
---

# DOT11\_AUTH\_ALGORITHM enumeration

The **DOT11\_AUTH\_ALGORITHM** enumerated type defines a wireless LAN authentication algorithm.

## Syntax


```C++
typedef enum _DOT11_AUTH_ALGORITHM { 
  DOT11_AUTH_ALGO_80211_OPEN        = 1,
  DOT11_AUTH_ALGO_80211_SHARED_KEY  = 2,
  DOT11_AUTH_ALGO_WPA               = 3,
  DOT11_AUTH_ALGO_WPA_PSK           = 4,
  DOT11_AUTH_ALGO_WPA_NONE          = 5,
  DOT11_AUTH_ALGO_RSNA              = 6,
  DOT11_AUTH_ALGO_RSNA_PSK          = 7,
  DOT11_AUTH_ALGO_IHV_START         = 0x80000000,
  DOT11_AUTH_ALGO_IHV_END           = 0xffffffff
} DOT11_AUTH_ALGORITHM, *PDOT11_AUTH_ALGORITHM;
```



## Constants

<dl> <dt>

<span id="DOT11_AUTH_ALGO_80211_OPEN"></span><span id="dot11_auth_algo_80211_open"></span>**DOT11\_AUTH\_ALGO\_80211\_OPEN**
</dt> <dd>

Specifies an IEEE 802.11 Open System authentication algorithm.

</dd> <dt>

<span id="DOT11_AUTH_ALGO_80211_SHARED_KEY"></span><span id="dot11_auth_algo_80211_shared_key"></span>**DOT11\_AUTH\_ALGO\_80211\_SHARED\_KEY**
</dt> <dd>

Specifies an 802.11 Shared Key authentication algorithm that requires the use of a pre-shared Wired Equivalent Privacy (WEP) key for the 802.11 authentication.

</dd> <dt>

<span id="DOT11_AUTH_ALGO_WPA"></span><span id="dot11_auth_algo_wpa"></span>**DOT11\_AUTH\_ALGO\_WPA**
</dt> <dd>

Specifies a Wi-Fi Protected Access (WPA) algorithm. IEEE 802.1X port authentication is performed by the supplicant, authenticator, and authentication server. Cipher keys are dynamically derived through the authentication process.

This algorithm is valid only for BSS types of dot11\_BSS\_type\_infrastructure.

When the WPA algorithm is enabled, the 802.11 station will associate only with an access point whose beacon or probe responses contain the authentication suite of type 1 (802.1X) within the WPA information element (IE).

</dd> <dt>

<span id="DOT11_AUTH_ALGO_WPA_PSK"></span><span id="dot11_auth_algo_wpa_psk"></span>**DOT11\_AUTH\_ALGO\_WPA\_PSK**
</dt> <dd>

Specifies a WPA algorithm that uses preshared keys (PSK). IEEE 802.1X port authentication is performed by the supplicant and authenticator. Cipher keys are dynamically derived through a preshared key that is used on both the supplicant and authenticator.

This algorithm is valid only for BSS types of **dot11\_BSS\_type\_infrastructure**.

When the WPA PSK algorithm is enabled, the 802.11 station will associate only with an access point whose beacon or probe responses contain the authentication suite of type 2 (preshared key) within the WPA IE.

</dd> <dt>

<span id="DOT11_AUTH_ALGO_WPA_NONE"></span><span id="dot11_auth_algo_wpa_none"></span>**DOT11\_AUTH\_ALGO\_WPA\_NONE**
</dt> <dd>

This value is not supported.

</dd> <dt>

<span id="DOT11_AUTH_ALGO_RSNA"></span><span id="dot11_auth_algo_rsna"></span>**DOT11\_AUTH\_ALGO\_RSNA**
</dt> <dd>

Specifies an 802.11i Robust Security Network Association (RSNA) algorithm. WPA2 is one such algorithm. IEEE 802.1X port authentication is performed by the supplicant, authenticator, and authentication server. Cipher keys are dynamically derived through the authentication process.

This algorithm is valid only for BSS types of **dot11\_BSS\_type\_infrastructure**.

When the RSNA algorithm is enabled, the 802.11 station will associate only with an access point whose beacon or probe responses contain the authentication suite of type 1 (802.1X) within the RSN IE.

</dd> <dt>

<span id="DOT11_AUTH_ALGO_RSNA_PSK"></span><span id="dot11_auth_algo_rsna_psk"></span>**DOT11\_AUTH\_ALGO\_RSNA\_PSK**
</dt> <dd>

Specifies an 802.11i RSNA algorithm that uses PSK. IEEE 802.1X port authentication is performed by the supplicant and authenticator. Cipher keys are dynamically derived through a preshared key that is used on both the supplicant and authenticator.

This algorithm is valid only for BSS types of **dot11\_BSS\_type\_infrastructure**.

When the RSNA PSK algorithm is enabled, the 802.11 station will associate only with an access point whose beacon or probe responses contain the authentication suite of type 2(preshared key) within the RSN IE.

</dd> <dt>

<span id="DOT11_AUTH_ALGO_IHV_START"></span><span id="dot11_auth_algo_ihv_start"></span>**DOT11\_AUTH\_ALGO\_IHV\_START**
</dt> <dd>

Indicates the start of the range that specifies proprietary authentication algorithms that are developed by an IHV.

The **DOT11\_AUTH\_ALGO\_IHV\_START** enumerator is valid only when the miniport driver is operating in Extensible Station (ExtSTA) mode.

</dd> <dt>

<span id="DOT11_AUTH_ALGO_IHV_END"></span><span id="dot11_auth_algo_ihv_end"></span>**DOT11\_AUTH\_ALGO\_IHV\_END**
</dt> <dd>

Indicates the end of the range that specifies proprietary authentication algorithms that are developed by an IHV.

The **DOT11\_AUTH\_ALGO\_IHV\_END** enumerator is valid only when the miniport driver is operating in ExtSTA mode.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista, Windows XP with SP3 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                        |
| Redistributable<br/>          | Wireless LAN API for Windows XP with SP2<br/>                                                         |
| Header<br/>                   | <dl> <dt>Wlantypes.h (include Windot11.h)</dt> </dl> |



## See also

<dl> <dt>

[**DOT11\_AUTH\_CIPHER\_PAIR**](dot11-auth-cipher-pair.md)
</dt> <dt>

[**WLAN\_AVAILABLE\_NETWORK**](/windows/desktop/api/wlanapi/ns-wlanapi-wlan_available_network)
</dt> <dt>

[**WLAN\_SECURITY\_ATTRIBUTES**](/windows/desktop/api/wlanapi/ns-wlanapi-wlan_security_attributes)
</dt> </dl>

 

 




