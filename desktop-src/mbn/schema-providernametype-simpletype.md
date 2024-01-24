---
description: Defines a string type for the ProviderName element in the Mobile Broadband profile.
ms.assetid: 1644ded2-f931-4920-848d-e0405d8723e3
title: providerNameType Simple Type
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- providerNameType
api_type: 
- Schema
---

# providerNameType Simple Type

The **providerNameType** simple type defines a string type for the [**ProviderName**](schema-providername-providertype-element.md) element in the Mobile Broadband profile. This string is at least one character long and at most 20 characters long.

``` syntax
<xs:simpleType name="providerNameType">
    <xs:restriction
        base="normalizedString"
    >
        <xs:minLength
            value="1"
         />
        <xs:maxLength
            value="20"
         />
    </xs:restriction>
</xs:simpleType>
```

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported server<br/> | None supported<br/>                         |



 

 




