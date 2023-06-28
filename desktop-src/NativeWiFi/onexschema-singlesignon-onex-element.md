---
title: singleSignOn (OneX) element
description: Specifies single sign-on (SSO) network configuration information.
ms.topic: reference
ms.date: 06/23/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- singleSignOn
api_type: 
- Schema
api_location: 
ms.assetid: c0a26f15-77fd-43e9-a6af-54e9b46f03fa
---

# singleSignOn (OneX) element

The singleSignOn (OneX) element specifies single sign-on (SSO) network configuration information.

This element is optional. Do not use the singleSignOn element in a profile if the network does not require it.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element will be ignored if it is present in a profile.

```XSD
<xs:element name="singleSignOn"
    minOccurs="0"
 >
    <xs:complexType>
        <xs:sequence>
            <xs:element name="type">
                <xs:simpleType>
                    <xs:restriction base="xs:string">
                        <xs:enumeration value="preLogon">
                        <xs:enumeration value="postLogon">
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="maxDelay"
                minOccurs="0"
             >
                <xs:simpleType>
                    <xs:restriction base="xs:integer">
                        <xs:minInclusive value="0">
                        <xs:maxInclusive value="120">
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="allowAdditionalDialogs"
                minOccurs="0"
                type="boolean"
             />
            <xs:element name="maxDelayWithAdditionalDialogs"
                minOccurs="0"
             >
                <xs:simpleType>
                    <xs:restriction base="xs:integer">
                        <xs:minInclusive value="0">
                        <xs:maxInclusive value="120">
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="userBasedVirtualLan"
                minOccurs="0"
                type="boolean"
             />
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

## Parent elements

* [OneX](./onexschema-onex-element.md)

## Child elements

| Element | Type | Description |
| - | - | - |
| [**type**](#type) | | Specifies when single sign on is performed. |
| [**maxDelay**](#maxdelay) | | Specifies, in seconds, the maximum delay before the single sign on connection attempt fails. |
| [**allowAdditionalDialogs**](#allowadditionaldialogs) | boolean | Specifies whether EAP dialogs can be displayed at logon time. The default is `FALSE`. |
| [**maxDelayWithAdditionalDialogs**](#maxdelaywithadditionaldialogs) | | The maximum duration to wait for the connection in case UI is to be displayed. |
| [**userBasedVirtualLan**](#userbasedvirtuallan) | boolean | Specifies if the virtual LAN (VLAN) used by the device changes based on the user's credentials. |

### type

The type (singleSignOn) element specifies when single sign on is performed. When set to `preLogon`, single sign on is performed before the user logs on. When set to `postLogon`, single sign on is performed immediately after the user logs on.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element will be ignored if it is present in a profile.

### maxDelay

The maxDelay (singleSignOn) element specifies, in seconds, the maximum delay before the single sign on connection attempt fails.

This element is optional. When maxDelay is not specified in a profile, a value of 10 seconds is used.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element will be ignored if it is present in a profile.

This parameter can be set at the command line using the **netsh wlan set profileparameter** command. For more information, see [Netsh Commands for Wireless Local Area Network (wlan)](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc755301(v=ws.10)).

### allowAdditionalDialogs

Specifies whether EAP dialogs can be displayed at logon time. The default is `FALSE`.

### maxDelayWithAdditionalDialogs

The maximum duration to wait for the connection in case UI is to be displayed.

### userBasedVirtualLan

The userBasedVirtualLan (singleSignOn) element specifies if the virtual LAN (VLAN) used by the device changes based on the user's credentials. Some network access server (NAS) devices change the VLAN after a user authenticates. When userBasedVirtualLan is TRUE, the NAS may change a device's VLAN after a user authenticates.

This element is optional. When userBasedVirtualLan is not specified in a profile, a value of FALSE is used.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element will be ignored if it is present in a profile.

This parameter can be set at the command line using the **netsh wlan set profileparameter** command. For more information, see [Netsh Commands for Wireless Local Area Network (wlan)](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc755301(v=ws.10)).

## Remarks

This parameter can be set at the command line using the **netsh wlan set profileparameter** command. For more information, see [Netsh Commands for Wireless Local Area Network (wlan)](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc755301(v=ws.10)).

## Requirements

| Requirement | Value |
| - | - |
| Minimum supported client | Windows Vista \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
