---
description: ModemDMConfigProfile
MS-HAID: WWAN\_profile\_v4.element\_ModemDMConfigProfile
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: ModemDMConfigProfile
ms.topic: reference
ms.date: 05/31/2018
---

# <span id="WWAN_profile_v4.element_ModemDMConfigProfile"></span>ModemDMConfigProfile

Modem DM configuration profile.

## Element hierarchy

**<ModemDMConfigProfile>**

## Syntax

``` syntax
<ModemDMConfigProfile>

  <!-- Child elements -->
  Name,
  SimIccID,
  ApnID,
  OemConnectionId,
  RoamApplicability?,
  Context,
  AdminEnable,
  AdminRoamControl,
  ProfileCreationType?,
  any element in a non-schema namespace*

</ModemDMConfigProfile>
```

### Key

`?`   optional (zero or one)

`*`   optional (zero or more)

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
<td><a href="element-1-adminenable.md">AdminEnable</a></td>
<td><p>Specifies whether the profile is enabled administratively.This is a new element for v4.</p></td>
</tr>
<tr class="even">
<td><a href="element-1-adminroamcontrol.md">AdminRoamControl</a></td>
<td><p>Specifies whether the profile is administratively roam controlled. This element is new for v4. The value of this element is a <a href="simpletype-roamcontroltype.md"><strong>roamControlType</strong></a> value. This is an optional element; if no value is specified, then <strong>AllRoamAllowed</strong> is the default.</p></td>
</tr>
<tr class="odd">
<td><a href="element-1-apnid.md">ApnID</a></td>
<td><p>An APN ID associated with this profile.This element is new in v4, and it is optional.</p></td>
</tr>
<tr class="even">
<td><a href="element-1-context.md">Context</a></td>
<td><p>Specifies the parameters required to establish a data connection.</p></td>
</tr>
<tr class="odd">
<td><a href="element-1-name.md">Name</a></td>
<td><p>The name of the profile. For more information, see the documentation for the v1 <a href="../mbn/schema-name-mbnprofile-element.md"><strong>Name</strong></a> element.</p></td>
</tr>
<tr class="even">
<td><a href="element-oemconnectionid.md">OemConnectionId</a></td>
<td><p>The OEM connection ID for the modem DM configuration.</p></td>
</tr>
<tr class="odd">
<td><a href="element-1-profilecreationtype.md">ProfileCreationType (in ModemDMConfigProfile)</a></td>
<td><p>Specifies how this modem DM profile was created.</p>
<p>This value is used to decide whether a user can delete the profile. Users can only delete <strong>UserProvisioned</strong> profiles.</p></td>
</tr>
<tr class="even">
<td><a href="element-1-roamapplicability.md">RoamApplicability</a></td>
<td><p>Specifies that this profile is active only when the current roaming condition is the one specified. Otherwise, the profile is not applicable, and cannot be used to activate a Packet Data Protocol (PDP) context. The value of this element must be a valid <a href="simpletype-roamapplicabilitytype.md"><strong>roamApplicabilityType</strong></a> value.</p></td>
</tr>
<tr class="odd">
<td><a href="element-1-simiccid.md">SimIccID</a></td>
<td><p>The SIM Identifcation number for GSM devices. For more details , see the documentation for the v1 <a href="../mbn/schema-simiccid-mbnprofile-element.md"><strong>SimIccID</strong></a> element.</p></td>
</tr>
</tbody>
</table>

 

### <span id="parent_elements"></span><span id="PARENT_ELEMENTS"></span>Parent Elements

This outermost (document) element may not be contained by any other elements.

## Requirements

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Namespace</p></td>
<td><p>https://www.microsoft.com/networking/WWAN/profile/v4</p></td>
</tr>
</tbody>
</table>

 

 



