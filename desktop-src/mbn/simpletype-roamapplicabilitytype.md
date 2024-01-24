---
description: The roamApplicabilityType describes the roaming conditions for which a roaming profile applies.
MS-HAID: WWAN\_profile\_v4.simpleType\_roamApplicabilityType
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: roamApplicabilityType Simple Type
ms.topic: reference
ms.date: 05/31/2018
---

# <span id="WWAN_profile_v4.simpleType_roamApplicabilityType"></span>roamApplicabilityType Simple Type

The roamApplicabilityType describes the roaming conditions for which a roaming profile applies.

This is a more expressive attribute than [**roamControlType**](simpletype-roamcontroltype.md), and a profile should use either **roamControlType** or **roamApplicabilityType**, but not both. (If a profile uses both, then both are applied. The result is the intersection of the two.)

Use this attribute to differentiate between multiple profiles with disjoint roaming conditions, to specify different profile attributes for, for example, home versus roaming.

There are three possible home/roam registration states:

-   Home: registered on the home network
-   Partner: registered on a network closely affiliated with the home network
-   Non-partner: registered on a network that is not closely affiliated with the home network

The precise meaning of "partner" varies based upon the network, but it represents a closer relationship with more favorable rates than a non-partner. This could be the case if a regionally-based operator has a business arrangement to use another operator’s radio access network outside of its home area. It could also represent the difference between roaming within a region (e.g., EU) and outside of it.

``` syntax
<xs:simpleType name="roamApplicabilityType">
    <xs:restriction
        base="token"
    >
        <xs:enumeration
            value="NonPartnerOnly"
         />
        <xs:enumeration
            value="PartnerOnly"
         />
        <xs:enumeration
            value="HomeOnly"
         />
        <xs:enumeration
            value="HomeAndPartner"
         />
        <xs:enumeration
            value="PartnerAndNonpartner"
         />
        <xs:enumeration
            value="AllRoaming"
         />
    </xs:restriction>
</xs:simpleType>
```

## Enumeration values

The **roamApplicabilityType** simple type defines the following values.


| Value | Description | 
|-------|-------------|
| NonPartnerOnly | <p>This profile is used only when roaming on a non-partner network</p> | 
| PartnerOnly | <p>This profile is used only when roaming on a partner network</p> | 
| HomeOnly | <p>This profile is used only when on the home network</p> | 
| HomeAndPartner | <p>This profile is used only when at home or on a partner network</p> | 
| PartnerAndNonpartner | <p>This profile is used when not at home (roaming on any network)</p> | 
| AllRoaming | <p>This profile is used on all networks</p> | 


 

 



