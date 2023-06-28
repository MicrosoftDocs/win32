---
title: Hotspot2 (WLANProfile) element
description: Extends the WLAN Profile Schema v1 to support Hotspot 2.0 networks.
ms.topic: reference
ms.date: 06/25/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Hotspot2
api_type: 
- Schema
api_location: 
ms.assetid: DE30DBCB-80B9-43D0-8DE1-56BBA99DBF31
---

# Hotspot2 (WLANProfile) element

Extends the WLAN Profile Schema v1 to support Hotspot 2.0 networks. Hotspot 2.0 enables automatic connection to public Wi-Fi services using existing credentials and membership in service provider networks. Service providers specify how connections are made using the new schema elements to describe which networks to use, and how to authenticate to them.

```XSD
<xs:element name="Hotspot2"
    minOccurs="0"
 >
    <xs:complexType>
        <xs:sequence>
            <xs:element name="DomainName"
                minOccurs="0"
             >
                <xs:simpleType>
                    <xs:restriction base="xs:string">
                        <xs:minLength value="1">
                        <xs:maxLength value="255">
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="NAIRealm"
                minOccurs="0"
                ...
             />
            <xs:element name="Network3GPP"
                minOccurs="0"
                ...
             />
            <xs:element name="RoamingConsortium"
                minOccurs="0"
                ...
             />
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

## Parent elements

* [**WLANProfile**](./wlan-profileschema-wlanprofile-element.md)

## Child elements

| Element | Type | Description |
| - | - | - |
| [**DomainName**](#domainname) | | The domain name for the device's Home Network Provider, identifying the operator of the network. |
| [**NAIRealm**](./wlan-profileschema-nairealm-hotspot2-element.md) | | A list of Network Access Identifier (NAI) Realm identifiers. |
| [**Network3GPP**](./wlan-profileschema-network3gpp-hotspot2-element.md) | | A list of Public Land Mobile Network (PLMN) IDs. |
| [**RoamingConsortium**](./wlan-profileschema-roamingconsortium-hotspot2-element.md) | | A list of Organizationally Unique Identifiers (OUI) assigned by IEEE. |

### DomainName

The domain name for the device's Home Network Provider, identifying the operator of the network.

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
## Requirements

TBD
