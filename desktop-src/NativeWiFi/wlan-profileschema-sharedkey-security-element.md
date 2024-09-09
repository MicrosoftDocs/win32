---
title: sharedKey (security) element
description: Contains shared key information.
ms.topic: reference
ms.date: 06/25/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- sharedKey
api_type: 
- Schema
api_location: 
ms.assetid: 9f401441-256c-4702-9503-f87b2b9cf0ee
---

# sharedKey (security) element

The sharedKey (security) element contains shared key information. This element is only required if WEP or PSK keys are required for the authentication and encryption pair.

```XSD
<xs:element name="sharedKey"
    minOccurs="0"
 >
    <xs:complexType>
        <xs:sequence>
            <xs:element name="keyType">
                <xs:simpleType>
                    <xs:restriction base="xs:string">
                        <xs:enumeration value="networkKey">
                        <xs:enumeration value="passPhrase">
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="protected"
                type="boolean"
             />
            <xs:element name="keyMaterial"
                type="string"
             />
            <xs:any
                processContents="lax"
                minOccurs="0"
                maxOccurs="unbounded"
                namespace="##other"
             />
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

## Parent elements

* [**security (MSM)**](./wlan-profileschema-security-msm-element.md)

## Child elements

| Element | Type | Description |
| - | - | - |
| [**keyType**](#keytype) | | Type of key. |
| [**protected**](#protected) | [boolean](/dotnet/api/system.boolean) | Specifies whether a shared key is encrypted. |
| [**keyMaterial**](#keymaterial) | [string](/dotnet/api/system.string) | Contains the network key or passphrase. |

### keyType

Indicates whether the shared key will be a network key or a pass phrase.

When the [**encryption**](wlan-profileschema-authencryption-security-element.md#encryption) element has a value of WEP, **keyType** must be set to **networkKey**.

### protected

Specifies whether a shared key is encrypted.

**Windows Vista and Windows Server 2008:** **protected** always has a value of "TRUE" if the profile was retrieved from the profile store (for example, by calling [**WlanGetProfile**](/windows/desktop/api/wlanapi/nf-wlanapi-wlangetprofile)).

**Windows XP with Service Pack 3 (SP3) or Wireless LAN API for Windows XP with Service Pack 2 (SP2):** This element must have a value of "FALSE".

### keyMaterial

Contains a network key or passphrase. If the [**protected**](wlan-profileschema-sharedkey-security-element.md#protected) element has a value of TRUE, then this key material is encrypted; otherwise, the key material is unencrypted. Encrypted key material is expressed in hexadecimal form.

The range of valid values for the keyMaterial element varies by the type of authentication and encryption used, as specified by the [**authentication**](wlan-profileschema-authencryption-security-element.md#authentication) and [**encryption**](wlan-profileschema-authencryption-security-element.md#encryption) elements. It also varies by [**keyType**](wlan-profileschema-sharedkey-security-element.md#keytype).

The following table shows valid **keyMaterial** values for some authentication and encryption pairs.

| [**authentication**](wlan-profileschema-authencryption-security-element.md#authentication) value | [**encryption**](wlan-profileschema-authencryption-security-element.md#encryption) value | [**keyType**](wlan-profileschema-sharedkey-security-element.md#keytype) value | Valid **keyMaterial** values |
|-|-|-|-|
| open or shared | WEP | networkKey | This element contains a WEP key of 5 or 13 ANSI characters, or of 10 or 26 hexadecimal characters. |
| WPAPSK or WPA2PSK | TKIP or AES | passPhrase | This element contains a passphrase of 8 to 63 ASCII characters, that is, 8 to 63 ANSI characters in the range of 32 to 126. Key values must comply with the requirements specified by 802.11i. |
| WPAPSK or WPA2PSK | TKIP or AES | networkKey | This element contains a key of 64 hexadecimal characters. |

Unicode characters may be entered where ANSI or ASCII characters are specified above. However, if the supplied Unicode characters cannot be mapped to ANSI or ASCII characters, then the supplied key material is rejected.

Key material returned by [**WlanGetProfile**](/windows/desktop/api/wlanapi/nf-wlanapi-wlangetprofile) is always encrypted. Also, if unencrypted key material is passed to [**WlanSetProfile**](/windows/desktop/api/wlanapi/nf-wlanapi-wlansetprofile), the key material is automatically encrypted before it is stored in the profile store.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** The key material is never encrypted.

If your process runs in the context of the LocalSystem account, then you can unencrypt key material by calling [**CryptUnprotectData**](/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata).

## Remarks

For Windows Vista and Windows Server 2008, the data associated with the **sharedKey** element is encrypted before it is saved in the profile store.

For Windows XP with SP3 and Wireless LAN API for Windows XP with SP2, the data isn't encrypted.

## Examples

To view sample profiles that use the **sharedKey** element and its child elements, see [Non-Broadcast profile sample](non-broadcast-profile-sample.md), [WPA-Personal profile sample](wpa-personal-profile-sample.md), and [WPA2-Personal profile sample](wpa2-personal-profile-sample.md). To view sample profiles that use the **protected** element, see [Wireless profile samples](wireless-profile-samples.md).

## Requirements

| Requirement | Value |
| - | - |
| Minimum supported client | Windows Vista, Windows XP with SP3 \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
| Redistributable | Wireless LAN API for Windows XP with SP2 |
