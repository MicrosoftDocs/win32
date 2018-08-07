---
Description: ModemDMConfigProfile
MS-HAID: WWAN\_profile\_v4.element\_ModemDMConfigProfile
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: ModemDMConfigProfile
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="WWAN_profile_v4.element_ModemDMConfigProfile"></span>ModemDMConfigProfile

Modem DM configuration profile.

## Element hierarchy

**<ModemDMConfigProfile&gt;**

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
<td>[AdminEnable](element-1-adminenable.md)</td>
<td><p>Specifies whether the profile is enabled administratively.This is a new element for v4.</p></td>
</tr>
<tr class="even">
<td>[AdminRoamControl](element-1-adminroamcontrol.md)</td>
<td><p>Specifies whether the profile is administratively roam controlled. This element is new for v4. The value of this element is a [<strong>roamControlType</strong>](simpletype-roamcontroltype.md) value. This is an optional element; if no value is specified, then <strong>AllRoamAllowed</strong> is the default.</p></td>
</tr>
<tr class="odd">
<td>[ApnID](element-1-apnid.md)</td>
<td><p>An APN ID associated with this profile.This element is new in v4, and it is optional.</p></td>
</tr>
<tr class="even">
<td>[Context](element-1-context.md)</td>
<td><p>Specifies the parameters required to establish a data connection.</p></td>
</tr>
<tr class="odd">
<td>[Name](element-1-name.md)</td>
<td><p>The name of the profile. For more information, see the documentation for the v1 [<strong>Name</strong>](../mbn/schema_name_mbnprofile_element.md) element.</p></td>
</tr>
<tr class="even">
<td>[OemConnectionId](element-oemconnectionid.md)</td>
<td><p>The OEM connection ID for the modem DM configuration.</p></td>
</tr>
<tr class="odd">
<td>[ProfileCreationType (in ModemDMConfigProfile)](element-1-profilecreationtype.md)</td>
<td><p>Specifies how this modem DM profile was created.</p>
<p>This value is used to decide whether a user can delete the profile. Users can only delete <strong>UserProvisioned</strong> profiles.</p></td>
</tr>
<tr class="even">
<td>[RoamApplicability](element-1-roamapplicability.md)</td>
<td><p>Specifies that this profile is active only when the current roaming condition is the one specified. Otherwise, the profile is not applicable, and cannot be used to activate a Packet Data Protocol (PDP) context. The value of this element must be a valid [<strong>roamApplicabilityType</strong>](simpletype-roamapplicabilitytype.md) value.</p></td>
</tr>
<tr class="odd">
<td>[SimIccID](element-1-simiccid.md)</td>
<td><p>The SIM Identifcation number for GSM devices. For more details , see the documentation for the v1 [<strong>SimIccID</strong>](../mbn/schema_simiccid_mbnprofile_element.md) element.</p></td>
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
<td><p>http://www.microsoft.com/networking/WWAN/profile/v4</p></td>
</tr>
</tbody>
</table>

 

 



