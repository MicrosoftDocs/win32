---
title: WLAN_profile schema simple types
description: The WLAN\_profile schema defines the following simple type.
ms.topic: reference
ms.date: 05/25/2023
ms.assetid: 93aef1f1-d443-4c0f-9097-3fd229305130
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# WLAN_profile schema simple types

The WLAN\_profile schema defines the following simple type.

## nameType

The **nameType** simple type can contain either the name, or a description, of a wireless LAN profile. This string value must be between 1 and 255 characters long.

``` syntax
<xs:simpleType name="nameType">
    <xs:restriction
        base="string"
    >
        <xs:minLength
            value="1"
         />
        <xs:maxLength
            value="255"
         />
    </xs:restriction>
</xs:simpleType>
```

## Requirements

| Requirement | Value |
|-|--|
| Minimum supported client | Windows Vista, Windows XP with SP3 \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
| Redistributable | Wireless LAN API for Windows XP with SP2 |
