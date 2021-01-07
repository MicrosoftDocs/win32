---
description: MBNProfileExt\/...\/UserLogonCred (v4)
MS-HAID: WWAN\_profile\_v4.element\_UserLogonCred
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: UserLogonCred
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 12a65d91-1917-49d4-9b58-68c60464c857
api_name: 
 - UserLogonCred
api_type: 
 - Schema
api_location: 
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="WWAN_profile_v4.element_UserLogonCred"></span>MBNProfileExt\/...\/UserLogonCred (v4)

Logon credentials for a connection.

## Element hierarchy

[\<MBNProfileExt\>](element-mbnprofileext.md)  
&nbsp;&nbsp;[\<Context\>](element-context.md)  
&nbsp;&nbsp;&nbsp;&nbsp;[\<UserLogonCred\>](element-userlogoncred.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**\<UserLogonCred\>**

[\<ModemDMConfigProfile\>](element-modemdmconfigprofile.md)  
&nbsp;&nbsp;[\<Context\>](element-1-context.md)  
&nbsp;&nbsp;&nbsp;&nbsp;[\<UserLogonCred\>](element-1-userlogoncred.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**\<UserLogonCred\>**

## Syntax

``` syntax
<UserLogonCred>

  <!-- Child elements -->
  UserName,
  IgnorePassword?,
  Password?

</UserLogonCred>
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
<td><a href="element-ignorepassword.md">IgnorePassword</a></td>
<td><p>Specifies how passwords are handled when upgrading profiles.</p>
<p>If set to <strong>TRUE</strong> and a profile with the same name exists at the time of the update operation, then the password from that profile will be taken and stored in the new profile.</p>
<p>For more details, see the documentation for the v1 <a href="../mbn/schema-ignorepassword-userlogoncred-element.md"><strong>IgnorePassword</strong></a> element.</p></td>
</tr>
<tr class="even">
<td><a href="element-password.md">Password</a></td>
<td><p>Specifies the password used to authenticate a user.</p>
<p>For more information, see the documentation for the v1 <a href="../mbn/schema-password-userlogoncred-element.md"><strong>Password</strong></a> element.</p></td>
</tr>
<tr class="odd">
<td><a href="element-username.md">UserName</a></td>
<td><p>The user name to use for logon.</p>
<p>For more details, see the documentation for the v1 <a href="../mbn/schema-username-userlogoncred-element.md"><strong>UserName</strong></a> element.</p></td>
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
<td><a href="element-context.md">Context</a></td>
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

 

 



