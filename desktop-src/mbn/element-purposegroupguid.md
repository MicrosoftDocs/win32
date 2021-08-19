---
description: PurposeGroupGuid
MS-HAID: WWAN\_profile\_v4.element\_PurposeGroupGuid
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: PurposeGroupGuid
ms.topic: reference
ms.date: 05/31/2018
---

# <span id="WWAN_profile_v4.element_PurposeGroupGuid"></span>PurposeGroupGuid

Represents one profile in a PurposeGroup of profiles.

Profiles are specified by their [**guidType**](simpletype-guidtype.md) value.

Four GUID values are defined, as listed in the following table.

| Purpose group | GUID                                 |
|---------------|--------------------------------------|
| Internet      | 3E5545D2-1137-4DC8-A198-33F1C657515F |
| MMS           | 53E2C5D3-D13C-4068-AA38-9C48FF2E55A8 |
| IMS           | 474D66ED-0E4B-476B-A455-19BB1239ED13 |
| SUPL          | 6D42669F-52A9-408E-9493-1071DCC437BD |

 

## Element hierarchy

[<MBNProfileExt>](element-mbnprofileext.md)  
[<PurposeGroups>](element-purposegroups.md)  
**<PurposeGroupGuid>**

## Syntax

``` syntax
<PurposeGroupGuid>

  guidType

</PurposeGroupGuid>
```

## <span id="Attributes_and_Elements"></span><span id="attributes_and_elements"></span><span id="ATTRIBUTES_AND_ELEMENTS"></span>Attributes and Elements

### <span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes

None.

### <span id="Child_Elements"></span><span id="child_elements"></span><span id="CHILD_ELEMENTS"></span>Child Elements

None.

### <span id="parent_elements"></span><span id="PARENT_ELEMENTS"></span>Parent Elements


| Parent Element | Description | 
|----------------|-------------|
| <a href="element-purposegroups.md">PurposeGroups</a> | <p>An optional list of groups of profiles, where each group includes profiles used for a common purpose.</p><p>This element is new for v4 of the schema.</p><p>One profile can be listed in multiple groups.</p> | 


 

## Requirements


| 
|
| <p>Namespace</p> | <p>https://www.microsoft.com/networking/WWAN/profile/v4</p> | 


 

 



