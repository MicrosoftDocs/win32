---
Description: MmscPort
MS-HAID: WWAN\_profile\_v4.element\_MmscPort
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: MmscPort
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="WWAN_profile_v4.element_MmscPort"></span>MmscPort

Specifies the port number of the MMSC server for the device. Specify 0 to indicate that no specific port is specified. Optional.

## Element hierarchy

[&lt;MBNProfileExt&gt;](element-mbnprofileext.md)  
[&lt;MmsConfiguration&gt;](element-mmsconfiguration.md)  
**&lt;MmscPort&gt;**

## Syntax

``` syntax
<MmscPort>

  [TBD (missing description)]

</MmscPort>
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
<td>[MmsConfiguration](element-mmsconfiguration.md)</td>
<td><p>Configuration information for Multimedia Messaging Service (MMS).</p>
<p>In addition to setting the configuration elements within this element, an MMS profile must have the following settings.</p>
<ul>
<li>Its [<strong>Name</strong>](element-name.md) element must contain a system-wide unique name.</li>
<li>Its [<strong>ProfileCreationType</strong>](../mbn/schema_profilecreationtype_mbnprofile_element.md) must be set to <strong>UserProvisioned</strong>.</li>
<li>Its [<strong>SimIccID</strong>](https://msdn.microsoft.com/en-us/library/Dd323201(v=VS.85).aspx) must contain the ICCID of the SIM that this profile is intended for.</li>
<li>Its [<strong>ConnectionMode</strong>](../mbn/schema_connectionmode_mbnprofile_element.md) must be set to <strong>Manual</strong>.</li>
<li>Its [<strong>PurposeGroupGuid</strong>](element-purposegroupguid.md) must contain the GUID for MMS purpose group.</li>
<li>Its [<strong>IsAdditionalPdpContextProfile</strong>](../WWAN_profile_v3/element_IsAdditionalPdpContextProfile.md) must be set to <strong>true</strong>.</li>
</ul></td>
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

 

 



