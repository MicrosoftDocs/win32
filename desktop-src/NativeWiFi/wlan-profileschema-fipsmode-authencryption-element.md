---
description: Indicates whether Federal Information Processing Standards (FIPS) mode is enabled.
ms.assetid: 4c62c96c-82e7-4174-b833-95ee10b29344
title: FIPSMode (authEncryption) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FIPSMode
api_type: 
- Schema
api_location: 
---

# FIPSMode (authEncryption) Element

The **FIPSMode** (authEncryption) element indicates whether Federal Information Processing Standards (FIPS) mode is enabled. When a wireless connection is operating in FIPS mode, the security level of the connection complies with the FIPS 140-2 standard. For more information about FIPS, see the [FIPS Home Page](https://www.itl.nist.gov/fipspubs/).

This element is optional. If this element is not specified in a profile, then FIPS mode is not enabled.

**FIPSMode** can be set to TRUE only when the following conditions are met:

-   The [**connectionType**](wlan-profileschema-connectiontype-wlanprofile-element.md) element has a value of `ESS` (that is, the connection is an infrastructure connection).
-   The [**authentication**](wlan-profileschema-authentication-authencryption-element.md) element has a value of `WPA2` or `WPA2PSK`.
-   The [**encryption**](wlan-profileschema-encryption-authencryption-element.md) element has a value of `AES`.

Unlike most elements in the WLAN\_profile schema, this element is in the `https://www.microsoft.com/networking/WLAN/profile/v2` namespace.

The value of the **FIPSMode** element is ignored if the miniport driver for the wireless interface does not support FIPS mode.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element is not supported. If **FIPSMode** is present in a profile, the element is ignored.

``` syntax
<xs:element name="FIPSMode"
    type="boolean"
 />
```

The element is defined by the [**authEncryption**](wlan-profileschema-authencryption-security-element.md) element.

## Remarks

This parameter can be set at the command line using the **netsh wlan set profileparameter** command. For more information, see [Netsh Commands for Wireless Local Area Network (wlan)](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc755301(v=ws.10)).

## Examples

To view a sample profile that uses the **FIPSMode** element, see [FIPS Profile Sample](fips-profile-sample.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**authEncryption**](wlan-profileschema-authencryption-security-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**authEncryption (security)**](wlan-profileschema-authencryption-security-element.md)
</dt> </dl>

 

 
