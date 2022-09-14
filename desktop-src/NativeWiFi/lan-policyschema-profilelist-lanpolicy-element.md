---
description: profileList (LANPolicy) Element - Contains a list of profiles to be applied at the domain or machine level.
ms.assetid: 4f010449-0c6b-4a01-8253-4f82cd628f0a
title: profileList (LANPolicy) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- profileList
api_type: 
- Schema
api_location: 
---

# profileList (LANPolicy) Element

The profileList (LANPolicy) element contains a list of profiles to be applied at the domain or machine level. Profiles must be based on the [LAN\_profile schema](lan-profileschema-schema.md), with a root element of [**LANProfile**](lan-profileschema-lanprofile-element.md). Profiles based on any other schema will be ignored.

When [**enableAutoConfig**](lan-policyschema-enableautoconfig-globalflags-element.md) is set to FALSE, this element must not be present in a LAN policy profile. When **enableAutoConfig** is set to TRUE, then this element is required.

``` syntax
<xs:element name="profileList">
    <xs:complexType>
        <xs:sequence>
            <xs:any
                processContents="lax"
                maxOccurs="unbounded"
                namespace="##other"
             />
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

The **profileList** element is defined by the [**LANPolicy**](lan-policyschema-lanpolicy-element.md) element.

## Remarks

This element should contain exactly one network profile. If more than one profile is specified in the policy, only the first network will be applied.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**LANPolicy**](lan-policyschema-lanpolicy-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**LANPolicy**](lan-policyschema-lanpolicy-element.md)
</dt> </dl>

 

 




