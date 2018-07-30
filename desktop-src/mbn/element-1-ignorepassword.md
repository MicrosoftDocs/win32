---
Description: IgnorePassword
MS-HAID: WWAN\_profile\_v4.element\_1\_IgnorePassword
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IgnorePassword
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="WWAN_profile_v4.element_1_IgnorePassword"></span>IgnorePassword

Specifies how passwords are handled when upgrading profiles.

If set to **TRUE** and a profile with the same name exists at the time of the update operation, then the password from that profile will be taken and stored in the new profile.

For more details, see the documentation for the v1 [**IgnorePassword**](../mbn/schema_ignorepassword_userlogoncred_element.md) element.

## Element hierarchy

[&lt;MBNProfileExt&gt;](element-mbnprofileext.md)  
[&lt;Context&gt;](element-context.md)  
[&lt;UserLogonCred&gt;](element-userlogoncred.md)  
**&lt;IgnorePassword&gt;**

<!-- -->

[&lt;ModemDMConfigProfile&gt;](element-modemdmconfigprofile.md)  
[&lt;Context&gt;](element-1-context.md)  
[&lt;UserLogonCred&gt;](element-1-userlogoncred.md)  
**&lt;IgnorePassword&gt;**

## Syntax

``` syntax
<IgnorePassword>

  boolean

</IgnorePassword>
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
<td>[UserLogonCred](element-1-userlogoncred.md)</td>
<td><p>Logon credentials for a connection.</p></td>
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

 

 



