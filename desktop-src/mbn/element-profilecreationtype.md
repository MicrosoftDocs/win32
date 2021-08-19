---
description: ProfileCreationType (in MBNProfileExt)
MS-HAID: WWAN\_profile\_v4.element\_ProfileCreationType
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: ProfileCreationType (in MBNProfileExt)
ms.topic: reference
ms.date: 05/31/2018
---

# <span id="WWAN_profile_v4.element_ProfileCreationType"></span>ProfileCreationType (in MBNProfileExt)

Specifies the creator of the profile.

For more information about this element, see the documentation for the v1 [**ProfileCreationType**](./schema-profilecreationtype-mbnprofile-element.md) element.

## Element hierarchy

[<MBNProfileExt>](element-mbnprofileext.md)  
**<ProfileCreationType>**

## Syntax

``` syntax
<ProfileCreationType>

  "UserProvisioned" | "AdminProvisioned" | "OperatorProvisioned" | "DeviceProvisioned"

</ProfileCreationType>
```

## <span id="Attributes_and_Elements"></span><span id="attributes_and_elements"></span><span id="ATTRIBUTES_AND_ELEMENTS"></span>Attributes and Elements

### <span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes

None.

### <span id="Child_Elements"></span><span id="child_elements"></span><span id="CHILD_ELEMENTS"></span>Child Elements

None.

### <span id="parent_elements"></span><span id="PARENT_ELEMENTS"></span>Parent Elements


| Parent Element | Description | 
|----------------|-------------|
| <a href="element-mbnprofileext.md">MBNProfileExt</a> | <p>The <strong>MBNProfileExt</strong> element is an extension of the earlier MBNProfile element. It identifies a Mobile Broadband profile with a richer set of options than the MBNProfile element.</p><p>There can be more than one MbnProfileExt element in a profile, describing profile settings for a particular set of operating conditions. Use the <a href="element-profileconditionedon.md"><strong>ProfileConditionedOn</strong></a> child element of <strong>MBNProfileExt</strong> to specify which operating conditions make a particular profile the active profile.</p> | 


 

## Related elements

The following elements have the same name as this one, but different content or attributes:

-   **[ProfileCreationType (in ModemDMConfigProfile)](element-1-profilecreationtype.md)**

## Requirements


| 
|
| <p>Namespace</p> | <p>https://www.microsoft.com/networking/WWAN/profile/v4</p> | 


 

 
