---
description: Describes how the profile controls roaming.
MS-HAID: WWAN\_profile\_v4.simpleType\_roamControlType
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: roamControlType Simple Type
ms.topic: reference
ms.date: 05/31/2018
---

# <span id="WWAN_profile_v4.simpleType_roamControlType"></span>roamControlType Simple Type

Describes how the profile controls roaming.

There are two possible roam registration states:

-   Partner: registered on a network closely affiliated with the home network
-   Non-partner: registered on a network that is not closely affiliated with the home network

The precise meaning of "partner" varies based upon the network, but it represents a closer relationship with more favorable rates than a non-partner. This could be the case if a regionally-based operator has a business arrangement to use another operator’s radio access network outside of its home area. It could also represent the difference between roaming within a region (e.g., EU) and outside of it.

Note that [**roamApplicabilityType**](simpletype-roamapplicabilitytype.md) is a more expressive attribute than **roamControlType**, and a profile should use either **roamControlType** or **roamApplicabilityType**, but not both. (If a profile uses both, then both are applied. The result is the intersection of the two.)

``` syntax
<xs:simpleType name="roamControlType">
    <xs:restriction>
        <xs:enumeration
            value="AllRoamAllowed"
         />
        <xs:enumeration
            value="PartnerRoamAllowed"
         />
        <xs:enumeration
            value="NoRoamAllowed"
         />
    </xs:restriction>
</xs:simpleType>
```

## Enumeration values

The **roamControlType** simple type defines the following values.

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
<td>AllRoamAllowed</td>
<td><p>Roaming is allowed on Partner and Non-Partner networks.</p></td>
</tr>
<tr class="even">
<td>PartnerRoamAllowed</td>
<td><p>Roaming is allowed only on Partner networks.</p></td>
</tr>
<tr class="odd">
<td>NoRoamAllowed</td>
<td><p>No roaming is allowed.</p></td>
</tr>
</tbody>
</table>

 

 



