---
Description: MmscUrl
MS-HAID: WWAN\_profile\_v4.element\_MmscUrl
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: MmscUrl
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="WWAN_profile_v4.element_MmscUrl"></span>MmscUrl

Specifies the URL of the MMSC server for the device. Optional.

## Element hierarchy

[<MBNProfileExt>](element-mbnprofileext.md)  
[<MmsConfiguration>](element-mmsconfiguration.md)  
**<MmscUrl>**

## Syntax

``` syntax
<MmscUrl>

  anyURI

</MmscUrl>
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
<td><a href="element-mmsconfiguration">MmsConfiguration</a></td>
<td><p>Configuration information for Multimedia Messaging Service (MMS).</p>
<p>In addition to setting the configuration elements within this element, an MMS profile must have the following settings.</p>
<ul>
<li>Its <a href="element-name"><strong>Name</strong></a> element must contain a system-wide unique name.</li>
<li>Its <a href="../mbn/schema_profilecreationtype_mbnprofile_element"><strong>ProfileCreationType</strong></a> must be set to <strong>UserProvisioned</strong>.</li>
<li>Its <a href="https://msdn.microsoft.com/en-us/library/Dd323201(v=VS.85).aspx"><strong>SimIccID</strong></a> must contain the ICCID of the SIM that this profile is intended for.</li>
<li>Its <a href="../mbn/schema_connectionmode_mbnprofile_element"><strong>ConnectionMode</strong></a> must be set to <strong>Manual</strong>.</li>
<li>Its <a href="element-purposegroupguid"><strong>PurposeGroupGuid</strong></a> must contain the GUID for MMS purpose group.</li>
<li>Its <a href="../WWAN_profile_v3/element_IsAdditionalPdpContextProfile"><strong>IsAdditionalPdpContextProfile</strong></a> must be set to <strong>true</strong>.</li>
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

 

 



