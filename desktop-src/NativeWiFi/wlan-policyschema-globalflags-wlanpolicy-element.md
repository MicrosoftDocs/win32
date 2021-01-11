---
description: Contains the global settings for the Auto Configuration Module (ACM).
ms.assetid: fb2b96d0-38cc-44fe-a82a-97e73b6a8f2a
title: globalFlags (WLANPolicy) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- globalFlags
api_type: 
- Schema
api_location: 
---

# globalFlags (WLANPolicy) Element

The globalFlags (WLANPolicy) element contains the global settings for the Auto Configuration Module (ACM). This element is mandatory.

``` syntax
<xs:element name="globalFlags">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="enableAutoConfig"
                type="boolean"
             />
            <xs:element name="showDeniedNetwork"
                type="boolean"
             />
            <xs:element name="allowEveryoneToCreateAllUserProfiles"
                type="boolean"
             />
            <xs:any
                processContents="lax"
                minOccurs="0"
                maxOccurs="unbounded"
                namespace="##other"
             />
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

The **globalFlags** element is defined by the [**WLANPolicy**](wlan-policyschema-wlanpolicy-element.md) element.

## Child elements



| Element                                                                                                                    | Type    | Description                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------------------|---------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**allowEveryoneToCreateAllUserProfiles**](wlan-policyschema-alloweveryonetocreatealluserprofiles-globalflags-element.md) | boolean | Specifies whether any user can create an all-user profile. <br/>                                                               |
| [**enableAutoConfig**](wlan-policyschema-enableautoconfig-globalflags-element.md)                                         | boolean | Specifies whether machines use the built-in automatic configuration (AutoConfig) service to manage wireless connections. <br/> |
| [**showDeniedNetwork**](wlan-policyschema-showdeniednetwork-globalflags-element.md)                                       | boolean | Specifies whether denied networks appear in the **Connect to a Network** wizard. <br/>                                         |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**WLANPolicy**](wlan-policyschema-wlanpolicy-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**WLANPolicy**](wlan-policyschema-wlanpolicy-element.md)
</dt> </dl>

 

 




