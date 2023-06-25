---
title: globalFlags (WLANPolicy) element
description: Contains the global settings for the Auto Configuration Module (ACM).
ms.topic: reference
ms.date: 06/24/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- globalFlags
api_type: 
- Schema
api_location: 
ms.assetid: fb2b96d0-38cc-44fe-a82a-97e73b6a8f2a
---

# globalFlags (WLANPolicy) element

The globalFlags (WLANPolicy) element contains the global settings for the Auto Configuration Module (ACM). This element is mandatory.

```XSD
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
            <xs:element name="onlyUseGPProfilesForAllowedNetworks"
                minOccurs="0"
                type="boolean"
             />
            <xs:element name="enbleSoftAP"
                minOccurs="0"
                type="boolean"
             />
            <xs:element name="enableExplicitCreds"
                minOccurs="0"
                type="boolean"
             />
            <xs:element name="blockPeriod"
                minOccurs="0"
             >
                <xs:simpleType>
                    <xs:restriction base="xs:integer">
                        <xs:minInclusive value="0">
                        <xs:maxInclusive value="60">
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="enableWFD"
                minOccurs="0"
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

## Parent elements

* [WLANPolicy](./wlan-policyschema-wlanpolicy-element.md)

## Child elements

| Element | Type | Description |
| - | - | - |
| [**enableAutoConfig**](#enableautoconfig) | boolean | Specifies whether machines use the built-in automatic configuration (AutoConfig) service to manage wireless connections. |
| [**showDeniedNetwork**](#showdeniednetwork) | boolean | Specifies whether denied networks appear in the Connect to a Network wizard. |
| [**allowEveryoneToCreateAllUserProfiles**](#alloweveryonetocreatealluserprofiles) | boolean | Specifies whether any user can create an all-user profile. |
| [**onlyUseGPProfilesForAllowedNetworks**](#onlyusegpprofilesforallowednetworks) | boolean | Indicates whether to restrict networks configured by GP to use GP profiles only. |
| [**enbleSoftAP**](#enblesoftap) | boolean | Indicates whether to enable software access point. |
| [**enableExplicitCreds**](#enableexplicitcreds) | boolean | Indicates whether to enable explicit credentials. |
| [**blockPeriod**](#blockperiod) | | The value of the block timeout period. |
| [**enableWFD**](#enablewfd) | boolean | Flag to indicate whether to enable WFD. |

### enableAutoConfig

The **enableAutoConfig** (globalFlags) element specifies whether machines use the built-in automatic configuration (AutoConfig) service to manage wireless connections. When **enableAutoConfig** has a value of FALSE, machines must not use AutoConfig to manage wireless connections, and the AutoConfig service only responds to requests to enable the service. When **enableAutoConfig** has a value of TRUE, machines may use the AutoConfig service.

This element is mandatory. When a profile is created by the AutoConfig service, this element will have the default value of TRUE.

### showDeniedNetwork

The **showDeniedNetwork** (globalFlags) element specifies whether denied networks appear in the **Connect to a Network** wizard. Networks may be denied by group policy or by user settings. When **showDeniedNetwork** has a value of TRUE, denied networks appear in the **Connect to a Network** wizard; otherwise, denied networks do not appear in the wizard.

This element is mandatory. When a profile is created by the AutoConfig service, this element will take the default value of FALSE.

### allowEveryoneToCreateAllUserProfiles

The **allowEveryoneToCreateAllUserProfiles** (globalFlags) element specifies whether any user can create an all-user profile. An all-user profile can be used by any user on the machine to connect to the wireless network associated with the profile.

If **allowEveryoneToCreateAllUserProfiles** is TRUE, than any user can create an all-user profile. If **allowEveryoneToCreateAllUserProfiles** is FALSE, then not all users can create an all-user profile, and there is a DACL associated with the wlan\_secure\_add\_new\_all\_user\_profiles security object that specifies the users or user groups with permission to create all-user profiles. The default DACL specifies that only users that are logged on as a member of the Administrators group can create an all-user profile. The default security settings can be changed by calling [**WlanSetSecuritySettings**](/windows/desktop/api/wlanapi/nf-wlanapi-wlansetsecuritysettings). To get the current security settings, call [**WlanGetSecuritySettings**](/windows/desktop/api/wlanapi/nf-wlanapi-wlangetsecuritysettings).

This element is mandatory. When a profile is created by the AutoConfig service, this element will have the default value of TRUE.

### onlyUseGPProfilesForAllowedNetworks

Flag to indicate whether to restrict networks configured by GP to use GP profiles only.

The target namespace for the **onlyUseGPProfilesForAllowedNetworks** element is `http://www.microsoft.com/networking/WLAN/policy/v2`.

### enbleSoftAP

Flag to indicate whether to enable software access point.

The target namespace for the **enbleSoftAP** element is `http://www.microsoft.com/networking/WLAN/policy/v3`.

### enableExplicitCreds

Flag to indicate whether to enable explicit credentials.

The target namespace for the **enableExplicitCreds** element is `http://www.microsoft.com/networking/WLAN/policy/v3`.

### blockPeriod

The value of the block timeout period. The default value is 20 minutes when the element isn't present.

The target namespace for the **blockPeriod** element is `http://www.microsoft.com/networking/WLAN/policy/v3`.

### enableWFD

Flag to indicate whether to enable WFD. The target namespace for the **enableWFD** element is `http://www.microsoft.com/networking/WLAN/policy/v4`.

## Requirements

| Requirement | Value |
| - | - |
| Minimum supported client | Windows Vista \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
