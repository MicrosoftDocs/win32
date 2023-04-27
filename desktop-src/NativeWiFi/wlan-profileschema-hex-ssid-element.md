---
title: hex (SSID) element
description: Contains the SSID of a wireless LAN in hexadecimal format.
ms.assetid: 6c49a3e6-f167-408b-a96f-5b6032108f34
ms.topic: reference
ms.date: 04/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- hex
api_type: 
- Schema
api_location: 
---

# hex (SSID) element

The hex (SSID) element contains the SSID of a wireless LAN in hexadecimal format.

``` syntax
<xs:element name="hex"
    minOccurs="0"
>
    <xs:simpleType>
        <xs:restriction
            base="hexBinary"
        >
            <xs:minLength
                value="1"
             />
            <xs:maxLength
                value="32"
             />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The element is defined by the [**SSID**](wlan-profileschema-ssid-ssidconfig-element.md) element.

## Remarks

Although the **hex** and [**name**](wlan-profileschema-name-ssid-element.md) elements are optional, at least one **hex** or [**name**](wlan-profileschema-name-ssid-element.md) element must appear as a child of the [**SSID**](wlan-profileschema-ssid-ssidconfig-element.md) element.

When profile information is converted to an SSID, the **hex** element is converted to the SSID (if present) and the [**name**](wlan-profileschema-name-ssid-element.md) element is ignored . If the **hex** element is not present, the [**name**](wlan-profileschema-name-ssid-element.md) element is converted to an SSID using Unicode to ASCII conversion.

When an SSID is stored in a profile, the **hex** element is always generated. The [**name**](wlan-profileschema-name-ssid-element.md) element is only generated if the both the ASCII to Unicode conversion of the SSID and the XML profile generation are successful. Some information from the original SSID may be lost when it is converted to a [**name**](wlan-profileschema-name-ssid-element.md).

## Examples

To view a sample profile that uses the **hex** element, see [FIPS Profile Sample](fips-profile-sample.md).

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

[**SSID**](wlan-profileschema-ssid-ssidconfig-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**SSID (SSIDConfig)**](wlan-profileschema-ssid-ssidconfig-element.md)
</dt> </dl>
