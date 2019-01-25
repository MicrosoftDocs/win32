---
Description: Compression
MS-HAID: WWAN\_profile\_v4.element\_1\_Compression
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: Compression
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 8dc3acd6-5997-47a5-bd30-899569b9aad9
api_name: 
 - Compression
api_type: 
 - Schema
api_location: 
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="WWAN_profile_v4.element_1_Compression"></span>Compression

Specifies whether compression will be used at the data link for header and data transfer.

For more information, see the documentation for the v1 [**Compression**](https://msdn.microsoft.com/library/Dd323277(v=VS.85).aspx) element.

## Element hierarchy

[<MBNProfileExt>](element-mbnprofileext.md)  
[<Context>](element-context.md)  
**<Compression>**

<!-- -->

[<ModemDMConfigProfile>](element-modemdmconfigprofile.md)  
[<Context>](element-1-context.md)  
**<Compression>**

## Syntax

``` syntax
<Compression>

  "DISABLE" | "ENABLE"

</Compression>
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
<td><a href="element-1-context">Context</a></td>
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
<td><p>https://www.microsoft.com/networking/WWAN/profile/v4</p></td>
</tr>
</tbody>
</table>

 

 



