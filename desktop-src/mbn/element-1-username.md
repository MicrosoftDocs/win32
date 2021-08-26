---
description: ModemDMConfigProfile\/...\/UserName (v4)
MS-HAID: WWAN\_profile\_v4.element\_1\_UserName
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: UserName (v4)
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: 1b43a275-cdbd-44e6-adc6-121aa935447e
api_name: 
 - UserName
api_type: 
 - Schema
api_location: 
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="WWAN_profile_v4.element_1_UserName"></span>ModemDMConfigProfile\/...\/UserName (v4)

The user name to use for logon.

For more details, see the documentation for the v1 [**UserName**](./schema-username-userlogoncred-element.md) element.

## Element hierarchy

[\<MBNProfileExt\>](element-mbnprofileext.md)  
&nbsp;&nbsp;[\<Context\>](element-context.md)  
&nbsp;&nbsp;&nbsp;&nbsp;[\<UserLogonCred\>](element-userlogoncred.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**\<UserName\>**

[\<ModemDMConfigProfile\>](element-modemdmconfigprofile.md)  
&nbsp;&nbsp;[\<Context\>](element-1-context.md)  
&nbsp;&nbsp;&nbsp;&nbsp;[\<UserLogonCred\>](element-1-userlogoncred.md)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**\<UserName\>**

## Syntax

``` syntax
<UserName>

  nameType

</UserName>
```

## <span id="Attributes_and_Elements"></span><span id="attributes_and_elements"></span><span id="ATTRIBUTES_AND_ELEMENTS"></span>Attributes and Elements

### <span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes

None.

### <span id="Child_Elements"></span><span id="child_elements"></span><span id="CHILD_ELEMENTS"></span>Child Elements

None.

### <span id="parent_elements"></span><span id="PARENT_ELEMENTS"></span>Parent Elements


| Parent Element | Description | 
|----------------|-------------|
| <a href="element-1-userlogoncred.md">UserLogonCred</a> | <p>Logon credentials for a connection.</p> | 


 

## Requirements


| Requirement | Value |
|------------|----------|
| <p>Namespace</p> | <p>https://www.microsoft.com/networking/WWAN/profile/v4</p> | 


 

 
