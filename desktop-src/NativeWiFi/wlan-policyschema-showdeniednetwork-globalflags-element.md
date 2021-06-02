---
description: Specifies whether denied networks appear in the Connect to a Network wizard.
ms.assetid: d0a13a80-2532-4383-8946-2536cc1f5e12
title: showDeniedNetwork (globalFlags) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- showDeniedNetwork
api_type: 
- Schema
api_location: 
---

# showDeniedNetwork (globalFlags) Element

The **showDeniedNetwork** (globalFlags) element specifies whether denied networks appear in the **Connect to a Network** wizard. Networks may be denied by group policy or by user settings. When **showDeniedNetwork** has a value of TRUE, denied networks appear in the **Connect to a Network** wizard; otherwise, denied networks do not appear in the wizard.

This element is mandatory. When a profile is created by the AutoConfig service, this element will take the default value of FALSE.

``` syntax
<xs:element name="showDeniedNetwork"
    type="boolean"
 />
```

The **showDeniedNetwork** element is defined by the [**globalFlags**](wlan-policyschema-globalflags-wlanpolicy-element.md) element.

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

 

 




