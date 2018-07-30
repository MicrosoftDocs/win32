---
Description: Context
MS-HAID: WWAN\_profile\_v4.element\_1\_Context
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: Context
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# <span id="WWAN_profile_v4.element_1_Context"></span>Context

Specifies the parameters required to establish a data connection.

## Element hierarchy

[&lt;MBNProfileExt&gt;](element-mbnprofileext.md)  
**&lt;Context&gt;**

<!-- -->

[&lt;ModemDMConfigProfile&gt;](element-modemdmconfigprofile.md)  
**&lt;Context&gt;**

## Syntax

``` syntax
<Context>

  <!-- Child elements -->
  AccessString?,
  UserLogonCred?,
  Compression?,
  AuthProtocol?,
  IPType?

</Context>
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
<td>[AccessString](element-1-accessstring.md)</td>
<td><p>Identifies the APN or dial string to be used to establish a data connection.</p>
<p>For more information, see the documentation for the v1 [<strong>AccessString</strong>](../mbn/schema_accessstring_contexttype_element.md) element.</p></td>
</tr>
<tr class="even">
<td>[AuthProtocol](element-1-authprotocol.md)</td>
<td><p>&gt;Specifies the authentication protocol to be used for activating a Packet Data Protocol (PDP) context.</p>
<p>Note that in v4, a new enumeration value is available for this element. <strong>AutoSelection</strong> means that an auth protocol is to be picked by lower layer(s).</p>
<p>For further information, see the documentation for the v1 [<strong>AuthProtocol</strong>](../mbn/schema_authprotocol_contexttype_element.md) element.</p></td>
</tr>
<tr class="odd">
<td>[Compression](element-1-compression.md)</td>
<td><p>Specifies whether compression will be used at the data link for header and data transfer.</p>
<p>For more information, see the documentation for the v1 [<strong>Compression</strong>](../mbn/schema_compression_contexttype_element.md) element.</p></td>
</tr>
<tr class="even">
<td>[IPType](element-1-iptype.md)</td>
<td><p>Specifies the IP type to be used on this data connection.</p>
<p>This element is new in v4 of the schema. The element can have one of the following values.</p>
<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Default</td>
<td>IP type is to be picked by lower layer(s)</td>
</tr>
<tr class="even">
<td>IPv4</td>
<td>Use IPv4</td>
</tr>
<tr class="odd">
<td>IPv6</td>
<td>Use IPv6</td>
</tr>
<tr class="even">
<td>IPv4v6</td>
<td>Use IPv4 and/or IPv6, as available.</td>
</tr>
<tr class="odd">
<td>XLAT</td>
<td>Use 464XLAT to tunnel IPv4 over IPv6 networks</td>
</tr>
</tbody>
</table>
<p> </p></td>
</tr>
<tr class="odd">
<td>[UserLogonCred](element-1-userlogoncred.md)</td>
<td><p>Logon credentials for a connection.</p></td>
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

 

 



