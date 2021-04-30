---
description: Defines a type for the ProviderID element of the Mobile Broadband profile.
ms.assetid: 84193749-c98d-4313-bf99-3da1c74d7cc4
title: providerIdType Simple Type
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- providerIdType
api_type: 
- Schema
---

# providerIdType Simple Type

The **providerIdType** simple type defines a type for the [**ProviderID**](schema-providerid-providertype-element.md) element of the Mobile Broadband profile. This type is a collection of digits at least one digit long and at most 6 digits long.

``` syntax
<xs:simpleType name="providerIdType">
    <xs:restriction
        base="token"
    >
        <xs:pattern
            value="\d{1,6}"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **providerIdType** simple type is a token that is restricted by the following pattern:

-   `\d{1,6}`

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported server<br/> | None supported<br/>                         |



 

 




