---
description: Specifies whether machines use the built-in automatic configuration (AutoConfig) service to manage wireless connections.
ms.assetid: c255e0a0-65ae-44a8-95cb-1a000394109d
title: enableAutoConfig (globalFlags) Element (LAN_policy) for WLAN
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- enableAutoConfig
api_type: 
- Schema
api_location: 
---

# enableAutoConfig (globalFlags) Element (LAN_policy) for WLAN 

The **enableAutoConfig** (globalFlags) element specifies whether machines use the built-in automatic configuration (AutoConfig) service to manage wireless connections. When **enableAutoConfig** has a value of FALSE, machines must not use AutoConfig to manage wireless connections, and the AutoConfig service only responds to requests to enable the service. When **enableAutoConfig** has a value of TRUE, machines may use the AutoConfig service.

This element is mandatory. When a profile is created by the AutoConfig service, this element will have the default value of TRUE.

``` syntax
<xs:element name="enableAutoConfig"
    type="boolean"
 />
```

The **enableAutoConfig** element is defined by the [**globalFlags**](wlan-policyschema-globalflags-wlanpolicy-element.md) element.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**globalFlags**](wlan-policyschema-globalflags-wlanpolicy-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**globalFlags (WLANPolicy)**](wlan-policyschema-globalflags-wlanpolicy-element.md)
</dt> </dl>

 

 




