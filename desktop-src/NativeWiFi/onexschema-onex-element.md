---
description: Specifies 802.1X configuration information for a wired or wireless LAN profile.
ms.assetid: 4528fcb5-ee8e-4824-a69e-8d67622c4b4d
title: OneX Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- OneX
api_type: 
- Schema
api_location: 
---

# OneX Element

The OneX element specifies 802.1X configuration information for a wired or wireless LAN profile. This element is the unique root element for an 802.1X profile.

The target namespace for the OneX element is `https://www.microsoft.com/networking/OneX/v1`. Most child elements of the OneX element are in the `OneX` namespace. There is one exception: the [**EAPConfig**](onexschema-eapconfig-onex-element.md) element is in the `https://www.microsoft.com/provisioning/EapHostConfig` namespace.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** Only the [**EAPConfig**](onexschema-eapconfig-onex-element.md) element is supported. Other elements, if present in a profile, will be ignored.

``` syntax
<xs:element name="OneX">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="cacheUserData"
                type="boolean"
                minOccurs="0"
             />
            <xs:element name="heldPeriod"
                minOccurs="0"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="integer"
                    >
                        <xs:enumeration
                            value="1"
                         />
                        <xs:enumeration
                            value="3600"
                         />
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="authPeriod"
                minOccurs="0"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="integer"
                    >
                        <xs:enumeration
                            value="1"
                         />
                        <xs:enumeration
                            value="3600"
                         />
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="startPeriod"
                minOccurs="0"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="integer"
                    >
                        <xs:enumeration
                            value="1"
                         />
                        <xs:enumeration
                            value="3600"
                         />
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="maxStart"
                minOccurs="0"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="integer"
                    >
                        <xs:enumeration
                            value="1"
                         />
                        <xs:enumeration
                            value="100"
                         />
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="maxAuthFailures"
                minOccurs="0"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="integer"
                    >
                        <xs:enumeration
                            value="1"
                         />
                        <xs:enumeration
                            value="100"
                         />
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="supplicantMode"
                minOccurs="0"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="string"
                    >
                        <xs:enumeration
                            value="inhibitTransmission"
                         />
                        <xs:enumeration
                            value="includeLearning"
                         />
                        <xs:enumeration
                            value="compliant"
                         />
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="authMode"
                minOccurs="0"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="string"
                    >
                        <xs:enumeration
                            value="machineOrUser"
                         />
                        <xs:enumeration
                            value="machine"
                         />
                        <xs:enumeration
                            value="user"
                         />
                        <xs:enumeration
                            value="guest"
                         />
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="singleSignOn"
                minOccurs="0"
            >
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
            <xs:element name="EAPConfig">
                <xs:complexType>
                    <xs:sequence>
                        <xs:any
                            processContents="lax"
                            minOccurs="1"
                            maxOccurs="unbounded"
                            namespace="##other"
                         />
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
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

## Child elements



| Element                                                                            | Type    | Description                                                                                                                                                                                                                  |
|------------------------------------------------------------------------------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**authMode**](onexschema-authmode-onex-element.md)                               |         | Specifies the type of credentials used for authentication.<br/>                                                                                                                                                        |
| [**authPeriod**](onexschema-authperiod-onex-element.md)                           |         | Specifies the maximum length of time, in seconds, in which a client waits for a response from the authenticator.<br/>                                                                                                  |
| [**cacheUserData**](onexschema-cacheuserdata-onex-element.md)                     | boolean | Specifies whether the user credentials are cached for subsequent connections.<br/>                                                                                                                                     |
| [**EAPConfig**](onexschema-eapconfig-onex-element.md)                             |         | Specifies the EAPHost configuration.<br/>                                                                                                                                                                              |
| [**heldPeriod**](onexschema-heldperiod-onex-element.md)                           |         | Specifies the length of time, in seconds, in which a client will not re-attempt authentication after a failed authentication attempt.<br/>                                                                             |
| [**maxAuthFailures**](onexschema-maxauthfailures-onex-element.md)                 |         | Specifies the maximum number of authentication failures allowed for a set of credentials.<br/>                                                                                                                         |
| [**maxDelay**](onexschema-maxdelay-singlesignon-element.md)                       |         | Specifies, in seconds, the maximum delay before the single sign-on connection attempt fails.<br/>                                                                                                                      |
| [**maxStart**](onexschema-maxstart-onex-element.md)                               |         | Specifies the maximum number of EAPOL-Start messages sent.<br/>                                                                                                                                                        |
| [**singleSignOn**](onexschema-singlesignon-onex-element.md)                       |         | Specifies single sign-on network configuration information.<br/>                                                                                                                                                       |
| [**startPeriod**](onexschema-startperiod-onex-element.md)                         |         | Specifies the length of time, in seconds, to wait before an EAPOL-Start is sent.<br/>                                                                                                                                  |
| [**supplicantMode**](onexschema-supplicantmode-onex-element.md)                   |         | Specifies the method of transmission used for EAPOL packets.<br/>                                                                                                                                                      |
| [**type**](onexschema-type-singlesignon-element.md)                               |         | Specifies when single sign-on is performed. When set to `preLogon`, single sign-on is performed before the user logs on. When set to `postLogon`, single sign-on is performed immediately after the user logs on.<br/> |
| [**userBasedVirtualLan**](onexschema-userbasedvirtuallan-singlesignon-element.md) | boolean | Specifies if the virtual LAN (VLAN) used by the device changes based on the user's credentials.<br/>                                                                                                                   |



## Remarks

To view the list of child elements in a tree-like structure, see [OneX Schema Elements](onexschema-elements.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista, Windows XP with SP3 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                |
| Redistributable<br/>          | Wireless LAN API for Windows XP with SP2<br/>                 |



 

 




