---
description: Defines a wireless LAN authentication algorithm.
ms.assetid: ac4097df-46dc-4c64-b72a-7cb9dce8b418
title: DOT11_AUTH_ALGORITHM enumeration (Wlantypes.h)
ms.topic: reference
ms.date: 04/25/2023
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

# DOT11_AUTH_ALGORITHM enumeration

The **DOT11_AUTH_ALGORITHM** enumerated type defines a wireless LAN authentication algorithm.

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
  DOT11_AUTH_ALGO_WPA3              = 8,
  DOT11_AUTH_ALGO_WPA3_ENT_192      = DOT11_AUTH_ALGO_WPA3,
  DOT11_AUTH_ALGO_WPA3_SAE          = 9,
  DOT11_AUTH_ALGO_OWE               = 10,
  DOT11_AUTH_ALGO_WPA3_ENT          = 11,
  DOT11_AUTH_ALGO_IHV_START         = 0x80000000,
  DOT11_AUTH_ALGO_IHV_END           = 0xffffffff
} DOT11_AUTH_ALGORITHM, *PDOT11_AUTH_ALGORITHM;
```

## Constants

### DOT11_AUTH_ALGO_80211_OPEN

Specifies an IEEE 802.11 Open System authentication algorithm.

### DOT11_AUTH_ALGO_80211_SHARED_KEY

Specifies an 802.11 Shared Key authentication algorithm that requires the use of a pre-shared Wired Equivalent Privacy (WEP) key for the 802.11 authentication.

### DOT11_AUTH_ALGO_WPA

Specifies a Wi-Fi Protected Access (WPA) algorithm. IEEE 802.1X port authentication is performed by the supplicant, authenticator, and authentication server. Cipher keys are dynamically derived through the authentication process.

This algorithm is valid only for BSS types of **dot11_BSS_type_infrastructure**.

When the WPA algorithm is enabled, the 802.11 station will associate only with an access point whose beacon or probe responses contain the authentication suite of type 1 (802.1X) within the WPA information element (IE).

### DOT11_AUTH_ALGO_WPA_PSK

Specifies a WPA algorithm that uses preshared keys (PSK). IEEE 802.1X port authentication is performed by the supplicant and authenticator. Cipher keys are dynamically derived through a preshared key that is used on both the supplicant and authenticator.

This algorithm is valid only for BSS types of **dot11_BSS_type_infrastructure**.

When the WPA PSK algorithm is enabled, the 802.11 station will associate only with an access point whose beacon or probe responses contain the authentication suite of type 2 (preshared key) within the WPA IE.

### DOT11_AUTH_ALGO_WPA_NONE

This value is not supported.

### DOT11_AUTH_ALGO_RSNA

Specifies an 802.11i Robust Security Network Association (RSNA) algorithm. WPA2 is one such algorithm. IEEE 802.1X port authentication is performed by the supplicant, authenticator, and authentication server. Cipher keys are dynamically derived through the authentication process.

This algorithm is valid only for BSS types of **dot11_BSS_type_infrastructure**.

When the RSNA algorithm is enabled, the 802.11 station will associate only with an access point whose beacon or probe responses contain the authentication suite of type 1 (802.1X) within the RSN IE.

### DOT11_AUTH_ALGO_RSNA_PSK

Specifies an 802.11i RSNA algorithm that uses PSK. IEEE 802.1X port authentication is performed by the supplicant and authenticator. Cipher keys are dynamically derived through a preshared key that is used on both the supplicant and authenticator.

This algorithm is valid only for BSS types of **dot11_BSS_type_infrastructure**.

When the RSNA PSK algorithm is enabled, the 802.11 station will associate only with an access point whose beacon or probe responses contain the authentication suite of type 2(preshared key) within the RSN IE.

### DOT11_AUTH_ALGO_WPA3

Deprecated (and synonymous with WPA3ENT192). Use WPA3ENT192 instead.

### DOT11_AUTH_ALGO_WPA3_ENT_192

Specifies a WPA3-Enterprise 192-bit mode algorithm.

### DOT11_AUTH_ALGO_WPA3_SAE

Specifies a WPA3-Simultaneous Authentication of Equals (WPA3-SAE) algorithm.

### DOT11_AUTH_ALGO_OWE

Specifies an opportunistic wireless encryption (OWE) algorithm.

### DOT11_AUTH_ALGO_WPA3_ENT

Specifies a WPA3-Enterprise algorithm.

### DOT11_AUTH_ALGO_IHV_START

Indicates the start of the range that specifies proprietary authentication algorithms that are developed by an IHV.

The **DOT11_AUTH_ALGO_IHV_START** enumerator is valid only when the miniport driver is operating in Extensible Station (ExtSTA) mode.

### DOT11_AUTH_ALGO_IHV_END

Indicates the end of the range that specifies proprietary authentication algorithms that are developed by an IHV.

The **DOT11_AUTH_ALGO_IHV_END** enumerator is valid only when the miniport driver is operating in ExtSTA mode.

## Requirements

| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista, Windows XP with SP3 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                        |
| Redistributable<br/>          | Wireless LAN API for Windows XP with SP2<br/>                                                         |
| Header<br/>                   | <dl> <dt>Wlantypes.h (include Windot11.h)</dt> </dl> |

## See also

<dl> <dt>

[**DOT11_AUTH_CIPHER_PAIR**](dot11-auth-cipher-pair.md)
</dt> <dt>

[**WLAN_AVAILABLE_NETWORK**](/windows/desktop/api/wlanapi/ns-wlanapi-wlan_available_network)
</dt> <dt>

[**WLAN_SECURITY_ATTRIBUTES**](/windows/desktop/api/wlanapi/ns-wlanapi-wlan_security_attributes)
</dt> </dl>
