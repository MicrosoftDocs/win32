---
description: ModemDMConfigProfile\/...\/IPType (v4)
MS-HAID: WWAN\_profile\_v4.element\_1\_IPType
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: IPType (v4)
ms.topic: reference
ms.date: 05/31/2018
---

# <span id="WWAN_profile_v4.element_1_IPType"></span>ModemDMConfigProfile\/...\/IPType (v4)

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

[\<MBNProfileExt\>](element-mbnprofileext.md)  
&nbsp;&nbsp;[\<Context\>](element-context.md)  
&nbsp;&nbsp;&nbsp;&nbsp;**\<IPType\>**

[\<ModemDMConfigProfile\>](element-modemdmconfigprofile.md)  
&nbsp;&nbsp;[\<Context\>](element-1-context.md)  
&nbsp;&nbsp;&nbsp;&nbsp;**\<IPType\>**

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


| Parent Element | Description | 
|----------------|-------------|
| <a href="element-1-context.md">Context</a> | <p>Specifies the parameters required to establish a data connection.</p> | 


 

## Requirements


| Requirement | Value |
|------------|----------|
| <p>Namespace</p> | <p>https://www.microsoft.com/networking/WWAN/profile/v4</p> | 


 

 



