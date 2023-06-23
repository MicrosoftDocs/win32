---
title: LANPolicy element
description: Contains a wired LAN policy.
ms.topic: reference
ms.date: 06/23/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LANPolicy
api_type: 
- Schema
api_location: 
ms.assetid: c06bdbc4-4199-4eec-a22f-684745912970
---

# LANPolicy element

The LANPolicy element contains a wired LAN policy. This element is the unique root element for a wired network policy profile.

The target namespace for the **LANPolicy** element is `https://www.microsoft.com/networking/LAN/policy/v1`.

```syntax
<xs:element name="LANPolicy">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="name"
                type="nameType"
             />
            <xs:element name="description"
                minOccurs="0"
                type="nameType"
             />
            <xs:element name="globalFlags"
                ...
             />
            <xs:element name="profileList"
                minOccurs="0"
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
| [**name**](#name) | nameType | Contains the name of a wired LAN policy. |
| [**description**](#description) | nameType | Contains the description of a wired LAN policy. |
| [**globalFlags**](./lan-policyschema-globalflags-lanpolicy-element.md) | | Contains the global settings for the automatic configuration of wired networks. |
| [**profileList**](#profilelist) | | profileList (LANPolicy) Element - Contains a list of profiles to be applied at the domain or machine level. |

### name

The name (LANPolicy) element contains the name of a wired LAN policy.

Names are not case-sensitive.

### description

The description (LANPolicy) element contains the description of a wired LAN policy.

### profileList

The profileList (LANPolicy) element contains a list of profiles to be applied at the domain or machine level. Profiles must be based on the [LAN\_profile schema](lan-profileschema-schema.md), with a root element of [**LANProfile**](lan-profileschema-lanprofile-element.md). Profiles based on any other schema will be ignored.

When [**enableAutoConfig**](./lan-policyschema-globalflags-lanpolicy-element.md#enableautoconfig) is set to `FALSE`, this element must not be present in a LAN policy profile. When **enableAutoConfig** is set to `TRUE`, this element is required.

This element should contain exactly one network profile. If more than one profile is specified in the policy, then only the first network will be applied.

## Remarks

To view the list of child elements in a tree-like structure, see [LAN\_policy Schema Elements](lan-policyschema-elements.md).

## Requirements

| Requirement | Value |
| - | - |
| Minimum supported client | Windows Vista \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |

