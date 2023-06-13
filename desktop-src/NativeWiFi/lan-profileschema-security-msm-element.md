---
title: Security (MSM) element (LAN_policy)
description: Contains security settings for wired networks.
ms.assetid: 08470cf4-3722-4cb9-9877-13eca2f7d04e
ms.topic: reference
ms.date: 06/13/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- security
api_type: 
- Schema
api_location: 
---

# Security (MSM) element (LAN_policy)

The security (MSM) element contains security settings for wired networks. This element is optional.

``` syntax
<xs:element name="security">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="OneXEnforced"
                type="boolean"
             />
            <xs:element name="OneXEnabled"
                type="boolean"
             />
            <!-
                Extension point for other namespaces, including the OneX
                namespace currently used for optional IEEE802.1X configuration.
                The OneX configuration parameters must be present if the 
                <OneXEnforced> flag is set to "true" or the <OneXEnabled> flag
                is set to "true". See the Child elements section below.
             ->
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

The **security** element is defined by the [**MSM**](lan-profileschema-msm-lanprofile-element.md) element.

## Child elements

| Element | Type | Description |
|-|-|-|
| [**OneXEnabled**](lan-profileschema-onexenabled-security-element.md) | boolean | Specifies whether the automatic configuration service for wired networks will attempt port authentication using 802.1X. |
| [**OneXEnforced**](lan-profileschema-onexenforced-security-element.md) | boolean | Specifies whether the automatic configuration service for wired networks requires the use of 802.1X for port authentication. |
| [**OneX**](/windows/win32/nativewifi/onexschema-onex-element) | | Optional IEEE802.1X configuration. |

## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client | Windows Vista \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |

## See also

**Definition context of element in schema**

* [**MSM (LANProfile)**](lan-profileschema-msm-lanprofile-element.md)

**Possible immediate parent element in schema instance**

* [**MSM (LANProfile)**](lan-profileschema-msm-lanprofile-element.md)
