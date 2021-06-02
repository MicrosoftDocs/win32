---
description: Enumeration that describes the kind of network connection where a profile is applicable.
MS-HAID: WWAN\_profile\_v4.simpleType\_iwlanApplicabilityType
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: iwlanApplicabilityType Simple Type
ms.topic: reference
ms.date: 05/31/2018
---

# <span id="WWAN_profile_v4.simpleType_iwlanApplicabilityType"></span>iwlanApplicabilityType Simple Type

Enumeration that describes the kind of network connection where a profile is applicable.

``` syntax
<xs:simpleType name="iwlanApplicabilityType">
    <xs:restriction
        base="token"
    >
        <xs:enumeration
            value="CellularOnly"
         />
        <xs:enumeration
            value="CellularAndIwlan"
         />
        <xs:enumeration
            value="IwlanOnly"
         />
    </xs:restriction>
</xs:simpleType>
```

## Enumeration values

The **iwlanApplicabilityType** simple type defines the following values.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CellularOnly</td>
<td><p>Profile is valid for cellular network connections only.</p></td>
</tr>
<tr class="even">
<td>CellularAndIwlan</td>
<td><p>Profile is valid for cellular or Wi-Fi offloaded connections.</p></td>
</tr>
<tr class="odd">
<td>IwlanOnly</td>
<td><p>Profile is valid for Wi-Fi offloaded connections only.</p></td>
</tr>
</tbody>
</table>

 

 



