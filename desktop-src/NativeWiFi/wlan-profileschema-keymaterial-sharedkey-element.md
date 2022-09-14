---
description: Contains a network key or passphrase.
ms.assetid: d2ed407e-5eaa-477b-8c4d-a47795048e0b
title: keyMaterial (sharedKey) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- keyMaterial
api_type: 
- Schema
api_location: 
---

# keyMaterial (sharedKey) Element

The keyMaterial (sharedKey) element contains a network key or passphrase. If the [**protected**](wlan-profileschema-protected-sharedkey-element.md) element has a value of TRUE, then this key material is encrypted; otherwise, the key material is unencrypted. Encrypted key material is expressed in hexadecimal form.

``` syntax
<xs:element name="keyMaterial"
    type="string"
 />
```

The element is defined by the [**sharedKey**](wlan-profileschema-sharedkey-security-element.md) element.

## Remarks

The range of valid values for the keyMaterial element varies by the type of authentication and encryption used, as specified by the [**authentication**](wlan-profileschema-authentication-authencryption-element.md) and [**encryption**](wlan-profileschema-encryption-authencryption-element.md) elements. It also varies by [**keyType**](wlan-profileschema-keytype-sharedkey-element.md).

The following table shows valid **keyMaterial** values for some authentication and encryption pairs.



| [**authentication**](wlan-profileschema-authentication-authencryption-element.md) value | [**encryption**](wlan-profileschema-encryption-authencryption-element.md) value | [**keyType**](wlan-profileschema-keytype-sharedkey-element.md) value | Valid **keyMaterial** values                                                                                                                                                                   |
|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| open or shared                                                                           | WEP                                                                              | networkKey                                                            | This element contains a WEP key of 5 or 13 ANSI characters, or of 10 or 26 hexadecimal characters.                                                                                             |
| WPAPSK or WPA2PSK                                                                        | TKIP or AES                                                                      | passPhrase                                                            | This element contains a passphrase of 8 to 63 ASCII characters, that is, 8 to 63 ANSI characters in the range of 32 to 126. Key values must comply with the requirements specified by 802.11i. |
| WPAPSK or WPA2PSK                                                                        | TKIP or AES                                                                      | networkKey                                                            | This element contains a key of 64 hexadecimal characters.                                                                                                                                      |



 

Unicode characters may be entered where ANSI or ASCII characters are specified above. However, if the supplied Unicode characters cannot be mapped to ANSI or ASCII characters, then the supplied key material is rejected.

Key material returned by [**WlanGetProfile**](/windows/desktop/api/wlanapi/nf-wlanapi-wlangetprofile) is always encrypted. Also, if unencrypted key material is passed to [**WlanSetProfile**](/windows/desktop/api/wlanapi/nf-wlanapi-wlansetprofile), the key material is automatically encrypted before it is stored in the profile store.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** The key material is never encrypted.

If your process runs in the context of the LocalSystem account, then you can unencrypt key material by calling [**CryptUnprotectData**](/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata).

## Examples

To view sample profiles that use the **keyMaterial** element, see [Non-Broadcast Profile Sample](non-broadcast-profile-sample.md), [WPA-Personal Profile Sample](wpa-personal-profile-sample.md), and [WPA2-Personal Profile Sample](wpa2-personal-profile-sample.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista, Windows XP with SP3 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                |
| Redistributable<br/>          | Wireless LAN API for Windows XP with SP2<br/>                 |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**sharedKey**](wlan-profileschema-sharedkey-security-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**sharedKey (security)**](wlan-profileschema-sharedkey-security-element.md)
</dt> </dl>

 

 
