---
Description: IPType
MS-HAID: WWAN\_profile\_v4.element\_1\_IPType
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPType
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="WWAN_profile_v4.element_1_IPType"></span>IPType

Specifies the IP type to be used on this data connection.

This element is new in v4 of the schema. The element can have one of the following values.

| Value   | Meaning                                       |
|---------|-----------------------------------------------|
| Default | IP type is to be picked by lower layer(s)     |
| IPv4    | Use IPv4                                      |
| IPv6    | Use IPv6                                      |
| IPv4v6  | Use IPv4 and/or IPv6, as available.           |
| XLAT    | Use 464XLAT to tunnel IPv4 over IPv6 networks |

 

## Element hierarchy

[&lt;MBNProfileExt&gt;](element-mbnprofileext.md)  
[&lt;Context&gt;](element-context.md)  
**&lt;IPType&gt;**

<!-- -->

[&lt;ModemDMConfigProfile&gt;](element-modemdmconfigprofile.md)  
[&lt;Context&gt;](element-1-context.md)  
**&lt;IPType&gt;**

## Syntax

``` syntax
<IPType>

  "Default" | "IPv4" | "IPv6" | "IPv4v6" | "XLAT"

</IPType>
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

 

 



