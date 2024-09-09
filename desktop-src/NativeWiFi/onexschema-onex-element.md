---
title: OneX element
description: Specifies 802.1X configuration information for a wired or wireless LAN profile.
ms.topic: reference
ms.date: 06/23/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- OneX
api_type: 
- Schema
api_location: 
ms.assetid: 4528fcb5-ee8e-4824-a69e-8d67622c4b4d
---

# OneX element

The OneX element specifies 802.1X configuration information for a wired or wireless LAN profile. This element is the unique root element for an 802.1X profile.

The target namespace for the OneX element is `https://www.microsoft.com/networking/OneX/v1`. Most child elements of the OneX element are in the `OneX` namespace. There is one exception: the [**EAPConfig**](onexschema-onex-element.md#eapconfig) element is in the `https://www.microsoft.com/provisioning/EapHostConfig` namespace.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** Only the [**EAPConfig**](onexschema-onex-element.md#eapconfig) element is supported. Other elements, if present in a profile, will be ignored.

```XSD
<xs:element name="OneX">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="cacheUserData"
                minOccurs="0"
                type="boolean"
             />
            <xs:element name="heldPeriod"
                minOccurs="0"
             >
                <xs:simpleType>
                    <xs:restriction base="xs:integer">
                        <xs:minInclusive value="1">
                        <xs:maxInclusive value="3600">
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="authPeriod"
                minOccurs="0"
             >
                <xs:simpleType>
                    <xs:restriction base="xs:integer">
                        <xs:minInclusive value="1">
                        <xs:maxInclusive value="3600">
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="startPeriod"
                minOccurs="0"
             >
                <xs:simpleType>
                    <xs:restriction base="xs:integer">
                        <xs:minInclusive value="1">
                        <xs:maxInclusive value="3600">
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="maxStart"
                minOccurs="0"
             >
                <xs:simpleType>
                    <xs:restriction base="xs:integer">
                        <xs:minInclusive value="1">
                        <xs:maxInclusive value="100">
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="maxAuthFailures"
                minOccurs="0"
             >
                <xs:simpleType>
                    <xs:restriction base="xs:integer">
                        <xs:minInclusive value="1">
                        <xs:maxInclusive value="100">
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="supplicantMode"
                minOccurs="0"
             >
                <xs:simpleType>
                    <xs:restriction base="xs:string">
                        <xs:enumeration value="inhibitTransmission">
                        <xs:enumeration value="includeLearning">
                        <xs:enumeration value="compliant">
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="authMode"
                minOccurs="0"
             >
                <xs:simpleType>
                    <xs:restriction base="xs:string">
                        <xs:enumeration value="machineOrUser">
                        <xs:enumeration value="machine">
                        <xs:enumeration value="user">
                        <xs:enumeration value="guest">
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="singleSignOn"
                minOccurs="0"
                ...
             />
            <xs:element name="EAPConfig"/>
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

None.

## Child elements

| Element | Type | Description |
| - | - | - |
| [**cacheUserData**](#cacheuserdata) | boolean | Specifies whether the user credentials are cached for subsequent connections. |
| [**heldPeriod**](#heldperiod) | | Specifies the length of time, in seconds, in which a client will not re-attempt authentication after a failed authentication attempt. |
| [**authPeriod**](#authperiod) | | Specifies the maximum length of time, in seconds, in which a client waits for a response from the authenticator. |
| [**startPeriod**](#startperiod) | | Specifies the length of time, in seconds, to wait before an EAPOL-Start is sent. |
| [**maxStart**](#maxstart) | | Specifies the maximum number of EAPOL-Start messages sent. |
| [**maxAuthFailures**](#maxauthfailures) | | Specifies the maximum number of authentication failures allowed for a set of credentials. |
| [**supplicantMode**](#supplicantmode) | | Specifies the method of transmission used for EAPOL-Start messages. |
| [**authMode**](#authmode) | | Specifies the type of credentials used for authentication. |
| [**singleSignOn**](./onexschema-singlesignon-onex-element.md) | | Specifies single sign-on (SSO) network configuration information. |
| [**EAPConfig**](#eapconfig) | | specifies the EAPHost configuration. |

### cacheUserData

The cacheUserData (OneX) element specifies whether the user credentials are cached for subsequent connections. When cacheUserData is TRUE, the credentials are cached. When cacheUserData is FALSE, the credentials are not cached and the user may be prompted for credentials on subsequent connection attempts.

This element is optional. When cacheUserData is not specified in a profile, the user credentials are cached.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element will be ignored if it is present in a profile.

### heldPeriod

The heldPeriod (OneX) element specifies the length of time, in seconds, in which a client will not re-attempt authentication after a failed authentication attempt.

This element is optional. When heldPeriod is not specified in a profile, a value of 1 second is used.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element will be ignored if it is present in a profile.

### authPeriod

The authPeriod (OneX) element specifies the maximum length of time, in seconds, in which a client waits for a response from the authenticator. If a response is not received within the specified period, the client assumes that there is no authenticator present on the network.

This element is optional. When authPeriod is not specified in a profile, a value of 18 seconds is used.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element will be ignored if it is present in a profile.

### startPeriod

The startPeriod (OneX) element specifies the length of time, in seconds, to wait before an EAPOL-Start is sent. An EAPOL-Start message is sent to start the 802.1X authentication process.

This element is optional. When startPeriod is not specified in a profile, a value of 5 seconds is used.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element will be ignored if it is present in a profile.

### maxStart

The maxStart (OneX) element specifies the maximum number of EAPOL-Start messages sent. After the maximum number of EAPOL-Start messages has been sent, the client assumes that there is no authenticator present on the network.

This element is optional. When maxStart is not specified in a profile, a value of 3 messages is used.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element will be ignored if it is present in a profile.

### maxAuthFailures

The maxAuthFailures (OneX) element specifies the maximum number of authentication failures allowed for a set of credentials.

This element is optional. When maxAuthFailures is not specified in a profile, a value of one is used.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element will be ignored if it is present in a profile.

### supplicantMode

The supplicantMode (OneX) element specifies the method of transmission used for EAPOL-Start messages. The following table describes the possible values.



| Value               | Description                                                                                                                                                              |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| inhibitTransmission | EAPOL-Start messages are not transmitted. Valid for wired LAN profiles only.                                                                                             |
| includeLearning     | The client determines when to send EAPOL-Start packets based on network capability. EAPOL-Start messages are only sent when required. Valid for wired LAN profiles only. |
| compliant           | EAPOL-Start messages are transmitted as specified by 802.1X. Valid for both wired and wireless LAN profiles.                                                             |





This element is optional. When supplicantMode is not specified in a profile, a value of `compliant` is used for both wired and wireless LAN profiles.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element will be ignored if it is present in a profile.

### authMode

The authMode (OneX) element specifies the type of credentials used for authentication. The following table describes the possible values.



| Value         | Description                                                                                                                                                             |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| machineOrUser | Use machine or user credentials. When a user is logged on, the user's credentials are used for authentication. When no user is logged on, machine credentials are used. |
| machine       | Use machine credentials only.                                                                                                                                           |
| user          | Use user credentials only.                                                                                                                                              |
| guest         | Use guest (empty) credentials only.                                                                                                                                     |





This element is optional. When authMode is not specified in a profile, a value of `machineOrUser` is used.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element will be ignored if it is present in a profile.

This parameter can be set at the command line using the **netsh wlan set profileparameter** command. For more information, see [Netsh Commands for Wireless Local Area Network (wlan)](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc755301(v=ws.10)).

### EAPConfig

The **EAPConfig** (OneX) element specifies the EAPHost configuration.

Unlike most elements in the 802.1X profile schema, this element is in the `https://www.microsoft.com/provisioning/EapHostConfig` namespace. Its child elements are defined in the [eaphostconfig schema](../eaphost/eaphostconfigschema-schema.md). The [**EapHostConfig**](../eaphost/eaphostconfigschema-eaphostconfig-element.md) element is a child of the **EAPConfig** element.

## Remarks

To view the list of child elements in a tree-like structure, see [OneX Schema Elements](onexschema-elements.md).

## Requirements

| Requirement | Value |
| - | - |
| Minimum supported client | Windows Vista, Windows XP with SP3 \[desktop apps only\] |
| Minimum supported server | Windows Server 2008 \[desktop apps only\] |
| Redistributable | Wireless LAN API for Windows XP with SP2 |
