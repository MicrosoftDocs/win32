---
Description: AuthProtocol
MS-HAID: WWAN\_profile\_v4.element\_1\_AuthProtocol
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: AuthProtocol
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="WWAN_profile_v4.element_1_AuthProtocol"></span>AuthProtocol

&gt;Specifies the authentication protocol to be used for activating a Packet Data Protocol (PDP) context.

Note that in v4, a new enumeration value is available for this element. **AutoSelection** means that an auth protocol is to be picked by lower layer(s).

For further information, see the documentation for the v1 [**AuthProtocol**](../mbn/schema_authprotocol_contexttype_element.md) element.

## Element hierarchy

[&lt;MBNProfileExt&gt;](element-mbnprofileext.md)  
[&lt;Context&gt;](element-context.md)  
**&lt;AuthProtocol&gt;**

<!-- -->

[&lt;ModemDMConfigProfile&gt;](element-modemdmconfigprofile.md)  
[&lt;Context&gt;](element-1-context.md)  
**&lt;AuthProtocol&gt;**

## Syntax

``` syntax
<AuthProtocol>

  "NONE" | "PAP" | "CHAP" | "MsCHAPv2" | "AutoSelection"

</AuthProtocol>
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
<td>[Context](element-1-context.md)</td>
<td><p>Specifies the parameters required to establish a data connection.</p></td>
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

 

 



