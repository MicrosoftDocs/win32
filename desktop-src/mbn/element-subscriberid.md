---
description: SubscriberID
MS-HAID: WWAN\_profile\_v4.element\_SubscriberID
MSHAttr:
- PreferredSiteName:MSDN
- PreferredLib:/library/windows/desktop
title: SubscriberID
ms.topic: reference
ms.date: 05/31/2018
---

# <span id="WWAN_profile_v4.element_SubscriberID"></span>SubscriberID

Identifies the unique identifier of the profile.

For a GSM network this should contain the IMSI (International Mobile Subscriber Identity) of the SIM and for CDMA devices it should contain the MIN (Mobile Identification Number) of the device.

For more information, see the documentation for the v1 [**SubscriberID**](./schema-subscriberid-mbnprofile-element.md) element.

## Element hierarchy

[&lt;MBNProfileExt&gt;](element-mbnprofileext.md)  
**&lt;SubscriberID&gt;**

## Syntax

``` syntax
<SubscriberID>

  subscriberIdType

</SubscriberID>
```

## <span id="Attributes_and_Elements"></span><span id="attributes_and_elements"></span><span id="ATTRIBUTES_AND_ELEMENTS"></span>Attributes and Elements

### <span id="attributes"></span><span id="ATTRIBUTES"></span>Attributes

None.

### <span id="Child_Elements"></span><span id="child_elements"></span><span id="CHILD_ELEMENTS"></span>Child Elements

None.

### <span id="parent_elements"></span><span id="PARENT_ELEMENTS"></span>Parent Elements


| Parent Element | Description | 
|----------------|-------------|
| <a href="element-mbnprofileext.md">MBNProfileExt</a> | <p>The <strong>MBNProfileExt</strong> element is an extension of the earlier MBNProfile element. It identifies a Mobile Broadband profile with a richer set of options than the MBNProfile element.</p><p>There can be more than one MbnProfileExt element in a profile, describing profile settings for a particular set of operating conditions. Use the <a href="element-profileconditionedon.md"><strong>ProfileConditionedOn</strong></a> child element of <strong>MBNProfileExt</strong> to specify which operating conditions make a particular profile the active profile.</p> | 


 

## Requirements


| Requirement | Value |
|------------|----------|
| <p>Namespace</p> | <p>https://www.microsoft.com/networking/WWAN/profile/v4</p> | 


 

 
