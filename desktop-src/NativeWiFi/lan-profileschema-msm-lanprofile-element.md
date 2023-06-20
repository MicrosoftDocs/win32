---
title: MSM (LANProfile) element
description: Contains media-specific module (MSM) settings.
ms.topic: reference
ms.date: 06/20/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSM
api_type: 
- Schema
api_location: 
ms.assetid: fe858701-e0eb-4817-b3c2-ae61e96a4cbe
---

# MSM (LANProfile) element

The MSM (LANProfile) element contains media-specific module (MSM) settings.

```syntax
<xs:element name="MSM">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="security"
                ...
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

* [LANProfile](./lan-profileschema-lanprofile-element.md)

## Child elements

| Element | Type | Description |
| - | - | - |
| [**security**](./lan-profileschema-security-msm-element.md) |  | Contains security settings. |

## Requirements

| Requirement | Value |
| - | - |
| Minimum supported client | Windows Vista \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
