---
description: Specifies whether any user can create an all-user profile.
ms.assetid: b9bdfe85-b9d5-4dcc-a7f8-05cce9702ec3
title: allowEveryoneToCreateAllUserProfiles (globalFlags) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- allowEveryoneToCreateAllUserProfiles
api_type: 
- Schema
api_location: 
---

# allowEveryoneToCreateAllUserProfiles (globalFlags) Element

The **allowEveryoneToCreateAllUserProfiles** (globalFlags) element specifies whether any user can create an all-user profile. An all-user profile can be used by any user on the machine to connect to the wireless network associated with the profile.

If **allowEveryoneToCreateAllUserProfiles** is TRUE, than any user can create an all-user profile. If **allowEveryoneToCreateAllUserProfiles** is FALSE, then not all users can create an all-user profile, and there is a DACL associated with the wlan\_secure\_add\_new\_all\_user\_profiles security object that specifies the users or user groups with permission to create all-user profiles. The default DACL specifies that only users that are logged on as a member of the Administrators group can create an all-user profile. The default security settings can be changed by calling [**WlanSetSecuritySettings**](/windows/desktop/api/wlanapi/nf-wlanapi-wlansetsecuritysettings). To get the current security settings, call [**WlanGetSecuritySettings**](/windows/desktop/api/wlanapi/nf-wlanapi-wlangetsecuritysettings).

This element is mandatory. When a profile is created by the AutoConfig service, this element will have the default value of TRUE.

``` syntax
<xs:element name="allowEveryoneToCreateAllUserProfiles"
    type="boolean"
 />
```

The **allowEveryoneToCreateAllUserProfiles** element is defined by the [**globalFlags**](wlan-policyschema-globalflags-wlanpolicy-element.md) element.

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

 

 




