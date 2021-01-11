---
description: Specifies single sign-on (SSO) network configuration information.
ms.assetid: c0a26f15-77fd-43e9-a6af-54e9b46f03fa
title: singleSignOn (OneX) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- singleSignOn
api_type: 
- Schema
api_location: 
---

# singleSignOn (OneX) Element

The singleSignOn (OneX) element specifies single sign-on (SSO) network configuration information.

This element is optional. Do not use the singleSignOn element in a profile if the network does not require it.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element will be ignored if it is present in a profile.

``` syntax
<xs:element name="singleSignOn">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="type"
                minOccurs="1"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="string"
                    >
                        <xs:enumeration
                            value="preLogon"
                         />
                        <xs:enumeration
                            value="postLogon"
                         />
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="maxDelay"
                minOccurs="0"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="integer"
                    >
                        <xs:enumeration
                            value="0"
                         />
                        <xs:enumeration
                            value="120"
                         />
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="userBasedVirtualLan"
                type="boolean"
                minOccurs="0"
             />
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

The **singleSignOn** element is defined by the [**OneX**](onexschema-onex-element.md) element.

## Child elements



| Element                                                                            | Type    | Description                                                                                                                                                                                                                  |
|------------------------------------------------------------------------------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**maxDelay**](onexschema-maxdelay-singlesignon-element.md)                       |         | Specifies, in seconds, the maximum delay before the single sign-on connection attempt fails.<br/>                                                                                                                      |
| [**type**](onexschema-type-singlesignon-element.md)                               |         | Specifies when single sign-on is performed. When set to `preLogon`, single sign-on is performed before the user logs on. When set to `postLogon`, single sign-on is performed immediately after the user logs on.<br/> |
| [**userBasedVirtualLan**](onexschema-userbasedvirtuallan-singlesignon-element.md) | boolean | Specifies if the virtual LAN (VLAN) used by the device changes based on the user's credentials.<br/>                                                                                                                   |



## Remarks

This parameter can be set at the command line using the **netsh wlan set profileparameter** command. For more information, see [Netsh Commands for Wireless Local Area Network (wlan)](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc755301(v=ws.10)).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**OneX**](onexschema-onex-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**OneX**](onexschema-onex-element.md)
</dt> </dl>

 

 
