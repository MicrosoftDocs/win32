---
Description: MmsConfiguration
MS-HAID: WWAN\_profile\_v4.element\_MmsConfiguration
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: MmsConfiguration
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="WWAN_profile_v4.element_MmsConfiguration"></span>MmsConfiguration

Configuration information for Multimedia Messaging Service (MMS).

In addition to setting the configuration elements within this element, an MMS profile must have the following settings.

-   Its [**Name**](element-name.md) element must contain a system-wide unique name.
-   Its [**ProfileCreationType**](https://msdn.microsoft.com/library/Dd323293(v=VS.85).aspx) must be set to **UserProvisioned**.
-   Its [**SimIccID**](https://msdn.microsoft.com/en-us/library/Dd323201(v=VS.85).aspx) must contain the ICCID of the SIM that this profile is intended for.
-   Its [**ConnectionMode**](https://msdn.microsoft.com/library/Dd323278(v=VS.85).aspx) must be set to **Manual**.
-   Its [**PurposeGroupGuid**](element-purposegroupguid.md) must contain the GUID for MMS purpose group.
-   Its [**IsAdditionalPdpContextProfile**](https://msdn.microsoft.com/library/Mt156987(v=VS.85).aspx) must be set to **true**.

## Element hierarchy

[<MBNProfileExt&gt;](element-mbnprofileext.md)  
**<MmsConfiguration&gt;**

## Syntax

``` syntax
<MmsConfiguration>

  <!-- Child elements -->
  MmscUrl?,
  MmscPort?,
  MmsMaximumMessageSize?

</MmsConfiguration>
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
<td>[MmsMaximumMessageSize](element-mmsmaximummessagesize.md)</td>
<td><p>Specifies the maximum size of MMS messages, in kilobytes. Optional.</p></td>
</tr>
<tr class="even">
<td>[MmscPort](element-mmscport.md)</td>
<td><p>Specifies the port number of the MMSC server for the device. Specify 0 to indicate that no specific port is specified. Optional.</p></td>
</tr>
<tr class="odd">
<td>[MmscUrl](element-mmscurl.md)</td>
<td><p>Specifies the URL of the MMSC server for the device. Optional.</p></td>
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

 

 



