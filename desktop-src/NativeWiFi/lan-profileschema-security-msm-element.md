---
description: Contains security settings for wired networks.
ms.assetid: 08470cf4-3722-4cb9-9877-13eca2f7d04e
title: Security (MSM) Element (LAN_policy)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- security
api_type: 
- Schema
api_location: 
---

# Security (MSM) Element (LAN_policy)

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



| Element                                                                 | Type    | Description                                                                                                                              |
|-------------------------------------------------------------------------|---------|------------------------------------------------------------------------------------------------------------------------------------------|
| [**OneXEnabled**](lan-profileschema-onexenabled-security-element.md)   | boolean | Specifies whether the automatic configuration service for wired networks will attempt port authentication using 802.1X. <br/>      |
| [**OneXEnforced**](lan-profileschema-onexenforced-security-element.md) | boolean | Specifies whether the automatic configuration service for wired networks requires the use of 802.1X for port authentication. <br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**MSM**](lan-profileschema-msm-lanprofile-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**MSM (LANProfile)**](lan-profileschema-msm-lanprofile-element.md)
</dt> </dl>

 

 




