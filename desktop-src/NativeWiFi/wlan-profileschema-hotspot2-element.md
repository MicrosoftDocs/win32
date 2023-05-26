---
title: Hotspot2 (WLANProfile) element
description: Extends the WLAN Profile Schema v1 to support Hotspot 2.0 networks.
ms.topic: reference
ms.date: 05/25/2023
ms.assetid: DE30DBCB-80B9-43D0-8DE1-56BBA99DBF31
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Hotspot2
api_type: 
- Schema
api_location: 
---

# Hotspot2 (WLANProfile) element

Extends the WLAN Profile Schema v1 to support Hotspot 2.0 networks. Hotspot 2.0 enables automatic connection to public Wi-Fi services using existing credentials and membership in service provider networks. Service providers specify how connections are made using the new schema elements to describe which networks to use, and how to authenticate to them.

``` syntax
<xs:element name="Hotspot2">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="DomainName"
                minOccurs="0"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="string"
                    >
                        <xs:minLength
                            value="1"
                        />
                        <xs:maxLength
                            value="255"
                        />
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="NAIRealm"
                minOccurs="0"
            >
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="name"
                            maxOccurs="256"
                            minOccurs="0"
                        >
                            <xs:simpleType>
                                <xs:restriction
                                    base="string"
                                >
                                    <xs:minLength
                                        value="1"
                                    />
                                    <xs:maxLength
                                        value="255"
                                    />
                                </xs:restriction>
                            </xs:simpleType>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="Network3GPP"
                minOccurs="0"
            >
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="PLMNID"
                            minOccurs="0"
                            maxOccurs="256"
                        >
                            <xs:simpleType>
                                <xs:restriction
                                    base="string"
                                >
                                    <xs:minLength
                                        value="5"
                                    />
                                    <xs:maxLength
                                        value="6"
                                    />
                                </xs:restriction>
                            </xs:simpleType>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="RoamingConsortium"
                minOccurs="0"
            >
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="OUI"
                            minOccurs="0"
                            maxOccurs="256"
                        >
                            <xs:simpleType>
                                <xs:restriction
                                    base="hexBinary"
                                >
                                    <xs:minLength
                                        value="3"
                                    />
                                    <xs:maxLength
                                        value="5"
                                    />
                                </xs:restriction>
                            </xs:simpleType>
                        </xs:element>
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

## Parent elements

* [**WLANProfile**](wlan-profileschema-wlanprofile-element.md)

## Child elements

| Element | Type | Description |
|-|-|-|
| [**DomainName**](#domainname) | | The domain name for the device's Home Network Provider, identifying the operator of the network. |
| [**NAIRealm**](#nairealm) | | A list of Network Access Identifier (NAI) Realm identifiers. Entries in this list are usually of the form `user@domain`. |
| [**Network3GPP**](#network3gpp) | | A list of Public Land Mobile Network (PLMN) IDs. |
| [**RoamingConsortium**](#roamingconsortium) | | A list of Organizationally Unique Identifiers (OUI) assigned by IEEE. |

### DomainName

The domain name for the device's Home Network Provider, identifying the operator of the network.

### NAIRealm

A list of Network Access Identifier (NAI) Realm identifiers. Entries in this list are usually of the form `user@domain`.

### Network3GPP

A list of Public Land Mobile Network (PLMN) IDs.

### RoamingConsortium

A list of Organizationally Unique Identifiers (OUI) assigned by IEEE.

## Examples

```xml
<Hotspot2>
  <DomainName>contoso.com</DomainName>
  <NAIRealm>
    <name>test1@contoso.com</name>
    <name>test2@contoso.com</name>
  </NAIRealm>
  <Network3GPP>
    <PLMNID>12345</PLMNID>
    <PLMNID>123456</PLMNID>
  </Network3GPP>
  <RoamingConsortium>
    <OUI>00AABB</OUI>
    <OUI>001122</OUI>
  </RoamingConsortium>
</Hotspot2>
```
