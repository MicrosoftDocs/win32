---
Description: SimIccID
MS-HAID: WWAN\_profile\_v4.element\_SimIccID
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: SimIccID
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="WWAN_profile_v4.element_SimIccID"></span>SimIccID

The SIM Identifcation number for GSM devices. For more details , see the documentation for the v1 [**SimIccID**](https://msdn.microsoft.com/library/Dd323302(v=VS.85).aspx) element.

## Element hierarchy

[<MBNProfileExt&gt;](element-mbnprofileext.md)  
**<SimIccID&gt;**

<!-- -->

[<ModemDMConfigProfile&gt;](element-modemdmconfigprofile.md)  
**<SimIccID&gt;**

## Syntax

``` syntax
<SimIccID>

  simIccIDType

</SimIccID>
```

## <span id="Attributes_and_Elements"></span><span id="attributes_and_elements"></span><span id="ATTRIBUTES_AND_ELEMENTS"></span>Attributes and Elements

### <span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes

None.

### <span id="Child_Elements"></span><span id="child_elements"></span><span id="CHILD_ELEMENTS"></span>Child Elements

None.

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
<tr class="even">
<td>[ModemDMConfigProfile](element-modemdmconfigprofile.md)</td>
<td><p>Modem DM configuration profile.</p></td>
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

 

 



