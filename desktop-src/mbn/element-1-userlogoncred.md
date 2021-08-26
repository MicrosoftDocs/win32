---
description: ModemDMConfigProfile\/...\/UserLogonCred (v4)
MS-HAID: WWAN\_profile\_v4.element\_1\_UserLogonCred
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: UserLogonCred (v4)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 6d563cf8-ea40-46b3-a74e-ec7640ca9824
api_name: 
 - UserLogonCred
api_type: 
 - Schema
api_location: 
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="WWAN_profile_v4.element_1_UserLogonCred"></span>ModemDMConfigProfile\/...\/UserLogonCred (v4)

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


| Child Element | Description | 
|---------------|-------------|
| <a href="element-1-ignorepassword.md">IgnorePassword</a> | <p>Specifies how passwords are handled when upgrading profiles.</p><p>If set to <strong>TRUE</strong> and a profile with the same name exists at the time of the update operation, then the password from that profile will be taken and stored in the new profile.</p><p>For more details, see the documentation for the v1 <a href="../mbn/schema-ignorepassword-userlogoncred-element.md"><strong>IgnorePassword</strong></a> element.</p> | 
| <a href="element-1-password.md">Password</a> | <p>Specifies the password used to authenticate a user.</p><p>For more information, see the documentation for the v1 <a href="../mbn/schema-password-userlogoncred-element.md"><strong>Password</strong></a> element.</p> | 
| <a href="element-1-username.md">UserName</a> | <p>The user name to use for logon.</p><p>For more details, see the documentation for the v1 <a href="../mbn/schema-username-userlogoncred-element.md"><strong>UserName</strong></a> element.</p> | 


 

### <span id="parent_elements"></span><span id="PARENT_ELEMENTS"></span>Parent Elements


| Parent Element | Description | 
|----------------|-------------|
| <a href="element-1-context.md">Context</a> | <p>Specifies the parameters required to establish a data connection.</p> | 


 

## Requirements


| Requirement | Value |
|------------|----------|
| <p>Namespace</p> | <p>https://www.microsoft.com/networking/WWAN/profile/v4</p> | 


 

 



