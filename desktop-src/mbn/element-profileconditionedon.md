---
Description: ProfileConditionedOn
MS-HAID: WWAN\_profile\_v4.element\_ProfileConditionedOn
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: ProfileConditionedOn
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="WWAN_profile_v4.element_ProfileConditionedOn"></span>ProfileConditionedOn

Specifies the conditions which must be satisfied for a profile to be applicable.

This element is new for v4. It enables you to specify multiple profiles that apply in different conditions, and for the proper profile to be used automatically when it is applicable. This element is optional. If you do not specify it, then the profile is always applicable with respect to the conditions listed.

## Element hierarchy

[&lt;MBNProfileExt&gt;](element-mbnprofileext.md)  
**&lt;ProfileConditionedOn&gt;**

## Syntax

``` syntax
<ProfileConditionedOn>

  <!-- Child elements -->
  CellularClass?,
  RATApplicability?,
  RoamApplicability?,
  IMSI?,
  IwlanApplicability?

</ProfileConditionedOn>
```

### Key

`?`   optional (zero or one)

## <span id="Attributes_and_Elements"></span><span id="attributes_and_elements"></span><span id="ATTRIBUTES_AND_ELEMENTS"></span>Attributes and Elements

### <span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes

None.

### <span id="Child_Elements"></span><span id="child_elements"></span><span id="CHILD_ELEMENTS"></span>Child Elements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Child Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[CellularClass](element-cellularclass.md)</td>
<td><p>Specifies that this profile is active only when the current cellular class is the one specified. Otherwise, the profile is not applicable, and cannot be used to activate a Packet Data Protocol (PDP) context.</p></td>
</tr>
<tr class="even">
<td>[IMSI](element-imsi.md)</td>
<td><p>Specifies that this profile is active only when the current IMSI being used in the ICCID is the one specified. Otherwise, the profile is not applicable, and cannot be used to activate a Packet Data Protocol (PDP) context.</p></td>
</tr>
<tr class="odd">
<td>[IwlanApplicability](element-iwlanapplicability.md)</td>
<td><p>Specifies that this profile is active only when connected to an IWLAN network. Otherwise, the profile is not applicable, and cannot be used to activate a Packet Data Protocol (PDP) context. The value of this element must be a valid [<strong>iwlanApplicabilityType</strong>](simpletype-iwlanapplicabilitytype.md) value.</p></td>
</tr>
<tr class="even">
<td>[RATApplicability](element-ratapplicability.md)</td>
<td><p>Specifies that this profile is active only when the RAT type is the one specified. Otherwise, the profile is not applicable, and cannot be used to activate a Packet Data Protocol (PDP) context.</p></td>
</tr>
<tr class="odd">
<td>[RoamApplicability](element-roamapplicability.md)</td>
<td><p>Specifies that this profile is active only when the current roaming condition is the one specified. Otherwise, the profile is not applicable, and cannot be used to activate a Packet Data Protocol (PDP) context. The value of this element must be a valid [<strong>roamApplicabilityType</strong>](simpletype-roamapplicabilitytype.md) value.</p></td>
</tr>
</tbody>
</table>

 

### <span id="parent_elements"></span><span id="PARENT_ELEMENTS"></span>Parent Elements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Parent Element</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[MBNProfileExt](element-mbnprofileext.md)</td>
<td><p>The <strong>MBNProfileExt</strong> element is an extension of the earlier MBNProfile element. It identifies a Mobile Broadband profile with a richer set of options than the MBNProfile element.</p>
<p>There can be more than one MbnProfileExt element in a profile, describing profile settings for a particular set of operating conditions. Use the [<strong>ProfileConditionedOn</strong>](element-profileconditionedon.md) child element of <strong>MBNProfileExt</strong> to specify which operating conditions make a particular profile the active profile.</p></td>
</tr>
</tbody>
</table>

 

## Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>http://www.microsoft.com/networking/WWAN/profile/v4</p></td>
</tr>
</tbody>
</table>

 

 



