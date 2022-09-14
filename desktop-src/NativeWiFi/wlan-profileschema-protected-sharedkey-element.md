---
description: Indicates whether a shared key is encrypted.
ms.assetid: 9206ef74-cd3e-4374-bea9-0c10505d10bf
title: protected (sharedKey) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- protected
api_type: 
- Schema
api_location: 
---

# protected (sharedKey) Element

The protected (sharedKey) element indicates whether a shared key is encrypted.

``` syntax
<xs:element name="protected"
    type="boolean"
 />
```

The element is defined by the [**sharedKey**](wlan-profileschema-sharedkey-security-element.md) element.

## Remarks

For Windows Vista and Windows Server 2008, **protected** always has a value of TRUE if the profile was retrieved from the profile store (for example, by calling [**WlanGetProfile**](/windows/desktop/api/wlanapi/nf-wlanapi-wlangetprofile)).

For profiles intended for use on Windows XP with Service Pack 3 (SP3) or Wireless LAN API for Windows XP with Service Pack 2 (SP2), **protected** must have a value of FALSE.

## Examples

To view sample profiles that use the **protected** element, see [Wireless Profile Samples](wireless-profile-samples.md).

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

 

 




