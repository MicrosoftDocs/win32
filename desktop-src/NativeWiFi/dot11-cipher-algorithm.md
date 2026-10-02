---
description: Defines a cipher algorithm for data encryption and decryption.
ms.assetid: 6b634d76-a159-438e-8fc6-5f05b326ed68
title: DOT11_CIPHER_ALGORITHM enumeration (Wlantypes.h)
ms.topic: reference
ms.date: 09/23/2026
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DOT11_CIPHER_ALGORITHM
api_type: 
- HeaderDef
api_location: 
- wlantypes.h
---

# DOT11_CIPHER_ALGORITHM enumeration

The **DOT11_CIPHER_ALGORITHM** enumerated type defines a cipher algorithm for data encryption and decryption.

## Syntax

```C++
typedef enum _DOT11_CIPHER_ALGORITHM { 
  DOT11_CIPHER_ALGO_NONE           = 0x00,
  DOT11_CIPHER_ALGO_WEP40          = 0x01,
  DOT11_CIPHER_ALGO_TKIP           = 0x02,
  DOT11_CIPHER_ALGO_CCMP           = 0x04,
  DOT11_CIPHER_ALGO_WEP104         = 0x05,
  DOT11_CIPHER_ALGO_BIP            = 0x06,              // BIP-CMAC-128
  DOT11_CIPHER_ALGO_GCMP           = 0x08,              // GCMP-128
  DOT11_CIPHER_ALGO_GCMP_256       = 0x09,              // GCMP-256
  DOT11_CIPHER_ALGO_CCMP_256       = 0x0a,              // CCMP-256
  DOT11_CIPHER_ALGO_BIP_GMAC_128   = 0x0b,              // BIP-GMAC-128
  DOT11_CIPHER_ALGO_BIP_GMAC_256   = 0x0c,              // BIP-GMAC-256
  DOT11_CIPHER_ALGO_BIP_CMAC_256   = 0x0d,              // BIP-CMAC-256
  DOT11_CIPHER_ALGO_WPA_USE_GROUP  = 0x100,
  DOT11_CIPHER_ALGO_RSN_USE_GROUP  = 0x100,
  DOT11_CIPHER_ALGO_WEP            = 0x101,
  DOT11_CIPHER_ALGO_IHV_START      = 0x80000000,
  DOT11_CIPHER_ALGO_IHV_END        = 0xffffffff
} DOT11_CIPHER_ALGORITHM, *PDOT11_CIPHER_ALGORITHM;
```

## Constants

### DOT11_CIPHER_ALGO_NONE

Specifies that no cipher algorithm is enabled or supported.

### DOT11_CIPHER_ALGO_WEP40

Specifies a Wired Equivalent Privacy (WEP) algorithm, which is the RC4-based algorithm that is specified in the 802.11-1999 standard. This enumerator specifies the WEP cipher algorithm with a 40-bit cipher key (WEP-40).

### DOT11_CIPHER_ALGO_TKIP

Specifies a Temporal Key Integrity Protocol (TKIP) algorithm, which is the RC4-based cipher suite that is based on the algorithms that are defined in the WPA specification and IEEE 802.11i-2004 standard. This cipher also uses the Michael Message Integrity Code (MIC) algorithm for forgery protection.

### DOT11_CIPHER_ALGO_CCMP

Specifies an AES-CCMP algorithm with a 128-bit cipher key, as specified in the IEEE 802.11i-2004 standard and RFC 3610. Advanced Encryption Standard (AES) is the encryption algorithm defined in FIPS 197.

### DOT11_CIPHER_ALGO_WEP104

Specifies a WEP cipher algorithm with a 104-bit cipher key (WEP104).

### DOT11_CIPHER_ALGO_BIP

Specifies a Broadcast/multicast integrity protocol (BIP) cipher algorithm, using AES in Cipher-based Message Authentication Code (CMAC) mode, with 128-bit key/length (BIP-CMAC-128). 

CMAC is defined in NIST SP 800-38B. This is a group management cipher algorithm.

### DOT11_CIPHER_ALGO_GCMP

Specifies a Galois/Counter Mode Protocol (GCMP) cipher algorithm with a 128-bit cipher key (AES-GCMP-128). Galois/Counter Mode (GCM) is part of the AES algorithm, defined in FIPS 197.

### DOT11_CIPHER_ALGO_GCMP_256

Specifies a GCMP cipher algorithm with a 256-bit cipher key (AES-GCMP-256).

### DOT11_CIPHER_ALGO_CCMP_256

Specifies an AES-CCMP algorithm with a 256-bit cipher key (AES-CCMP-256).

### DOT11_CIPHER_ALGO_BIP_GMAC_128

Specifies a Broadcast Integrity Protocol Galois Message Authentication Code (BIP-GMAC) cipher algorithm with a 128-bit cipher key (BIP-GMAC-128).

GMAC is defined in NIST SP 800-38D. This is a group management cipher algorithm.

### DOT11_CIPHER_ALGO_BIP_GMAC_256

Specifies a BIP-GMAC cipher algorithm with a 256-bit cipher key (BIP-GMAC-256).

This is a group management cipher algorithm.

### DOT11_CIPHER_ALGO_BIP_CMAC_256

Specifies a BIP-CMAC cipher algorithm with a 256-bit cipher key  (BIP-CMAC-256).

This is a group management cipher algorithm.

### DOT11_CIPHER_ALGO_WPA_USE_GROUP

Specifies a Wi-Fi Protected Access (WPA) Use Group Key cipher suite. For more information about the Use Group Key cipher suite, refer to Clause 7.3.2.25.1 of the IEEE 802.11i-2004 standard.

### DOT11_CIPHER_ALGO_RSN_USE_GROUP

Specifies a Robust Security Network (RSN) Use Group Key cipher suite. For more information about the Use Group Key cipher suite, refer to Clause 7.3.2.25.1 of the IEEE 802.11i-2004 standard.

### DOT11_CIPHER_ALGO_WEP

Specifies a WEP cipher algorithm with a cipher key of any length.

### DOT11_CIPHER_ALGO_IHV_START

Specifies the start of the range that is used to define proprietary cipher algorithms that are developed by an independent hardware vendor (IHV).

### DOT11_CIPHER_ALGO_IHV_END

Specifies the end of the range that is used to define proprietary cipher algorithms that are developed by an IHV.

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
