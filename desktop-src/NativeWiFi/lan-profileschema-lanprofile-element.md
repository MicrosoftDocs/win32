---
title: LANProfile element
description: Contains a wired network profile.
ms.topic: reference
ms.date: 06/20/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LANProfile
api_type: 
- Schema
api_location: 
ms.assetid: f5f9fcdc-febf-4730-8be4-5e1885d9ab08
---

# LANProfile element

The LANProfile element contains a wired network profile. This element is the unique root element for a wired network profile.

The target namespace for the LANProfile element is `https://www.microsoft.com/networking/LAN/profile/v1`.

```syntax
<xs:element name="LANProfile">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="MSM"
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

None.

## Child elements

| Element | Type | Description |
| - | - | - |
| [**MSM**](./lan-profileschema-msm-lanprofile-element.md) |  | Contains media-specific module (MSM) settings. |

## Remarks

To view the list of child elements in a tree-like structure, see [LAN\_profile Schema Elements](lan-profileschema-elements.md).

## Requirements

| Requirement | Value |
| - | - |
| Minimum supported client | Windows Vista \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
