---
description: A string representation of a GUID, in the usual format.
MS-HAID: WWAN\_profile\_v4.simpleType\_guidType
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: guidType simple type (Mobile Broadband)
ms.topic: reference
ms.date: 05/31/2018
---

# <span id="WWAN_profile_v4.simpleType_guidType"></span>guidType simple type (Mobile Broadband)

A string representation of a GUID, in the usual format.

``` syntax
<xs:simpleType name="guidType">
    <xs:restriction
        base="token"
    >
        <xs:pattern
            value="{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}}"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **guidType** simple type is a token that is restricted by the following pattern:

-   `{[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}}`

 

 



