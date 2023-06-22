---
title: security (MSM) element (for LAN_profile)
description: Contains security settings for wired networks.
ms.topic: reference
ms.date: 06/22/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- security
api_type: 
- Schema
api_location: 
ms.assetid: 08470cf4-3722-4cb9-9877-13eca2f7d04e
---

# security (MSM) element (for LAN_profile)

The security (MSM) element contains security settings for wired networks. This element is optional.

```syntax
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

## Parent elements

* [MSM (LANProfile)](./lan-profileschema-msm-lanprofile-element.md)

## Child elements

| Element | Type | Description |
| - | - | - |
| [**OneXEnforced**](#onexenforced) | boolean | Specifies whether the automatic configuration service for wired networks requires the use of 802.1X for port authentication. |
| [**OneXEnabled**](#onexenabled) | boolean | Specifies whether the automatic configuration service for wired networks will attempt port authentication using 802.1X. |
| [**OneX**](/windows/win32/nativewifi/onexschema-onex-element) | | Optional IEEE802.1X configuration. |

### OneXEnforced

The **OneXEnforced** (security) element specifies whether the automatic configuration service for wired networks requires the use of 802.1X for port authentication. When **OneXEnforced** is `TRUE`, the automatic configuration service must use 802.1X for port authentication. When **OneXEnforced** is `FALSE`, the automatic configuration service will attempt to use 802.1X for port authentication, but the service will fall back to no authentication if 802.1X authentication fails for any reason.

This element is optional. The default value is `FALSE`.

This element has a meaningful value only if [**OneXEnabled**](#onexenabled) is `TRUE`. If **OneXEnabled** is `FALSE`, then the value of this element is ignored.

### OneXEnabled

Specifies whether the automatic configuration service for wired networks will attempt port authentication using 802.1X. When **OneXEnabled** is `FALSE`, the automatic configuration service never uses 802.1X for port authentication. When **OneXEnabled** is `TRUE`, the automatic configuration service attempts port authentication using 802.1X.

This element is optional. The default value is `TRUE`. When **OneXEnabled** is not specified in a profile, 802.1X may be used for port authentication.

## Requirements

| Requirement | Value |
| - | - |
| Minimum supported client | Windows Vista \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
