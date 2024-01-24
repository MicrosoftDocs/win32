---
description: Provider
MS-HAID: WWAN\_profile\_v4.element\_Provider
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: Provider
ms.topic: reference
ms.date: 05/31/2018
ms.assetid: a701c4dd-967f-4f03-ada4-d34059f5a1e4
api_name: 
 - Provider
api_type: 
 - Schema
api_location: 
topic_type: 
 - APIRef
 - kbSyntax

---

# <span id="WWAN_profile_v4.element_Provider"></span>Provider

Specifies one preferred network provider in a list of providers to be used when roaming.

The value of this element is an instance of the v1 [**providerType**](./schema-providertype-complextype.md) complex type.

## Element hierarchy

[&lt;MBNProfileExt&gt;](element-mbnprofileext.md)  
[&lt;DataRoamingPartners&gt;](element-dataroamingpartners.md)  
**&lt;Provider&gt;**

## Syntax

``` syntax
<Provider>

  providerType

</Provider>
```

## <span id="Attributes_and_Elements"></span><span id="attributes_and_elements"></span><span id="ATTRIBUTES_AND_ELEMENTS"></span>Attributes and Elements

### <span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes

None.

### <span id="Child_Elements"></span><span id="child_elements"></span><span id="CHILD_ELEMENTS"></span>Child Elements

None.

### <span id="parent_elements"></span><span id="PARENT_ELEMENTS"></span>Parent Elements


| Parent Element | Description | 
|----------------|-------------|
| <a href="element-dataroamingpartners.md">DataRoamingPartners</a> | <p>Specifies a list of preferred network providers when roaming.</p><p>For details, see the documentation for the v1 <a href="../mbn/schema-dataroamingpartners-mbnprofile-element.md"><strong>DataRoamingPartners</strong></a> element.</p> | 


 

## Requirements


| Requirement | Value |
|------------|----------|
| <p>Namespace</p> | <p>https://www.microsoft.com/networking/WWAN/profile/v4</p> | 


 

 
