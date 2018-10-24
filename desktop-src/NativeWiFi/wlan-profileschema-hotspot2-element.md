---
Description: Extends the WLAN Profile Schema v1 to support Hotspot 2.0 networks.
ms.assetid: DE30DBCB-80B9-43D0-8DE1-56BBA99DBF31
title: Hotspot2 (WLANProfile) Element
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Hotspot2
api_type: 
- Schema
api_location: 
---

# Hotspot2 (WLANProfile) Element

Extends the WLAN Profile Schema v1 to support Hotspot 2.0 networks. Hotspot 2.0 enables automatic connection to public Wi-Fi services using existing credentials and membership in service provider networks. Service providers specify how connections are made using the new schema elements to describe which networks to use, and how to authenticate to them.

``` syntax
<xs:element name="Hotspot2">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="DomainName"
                minOccurs="0"
             />
            <xs:element name="NAIRealm"
                minOccurs="0"
             />
            <xs:element name="Network3GPP"
                minOccurs="0"
             />
            <xs:element name="RoamingConsortium"
                minOccurs="0"
             />
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

The element is defined by the [**WLANProfile**](wlan-profileschema-wlanprofile-element.md) element.

## Child elements



| Element                                                                            | Type | Description                                                                                                                       |
|------------------------------------------------------------------------------------|------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**DomainName**](wlan-profileschema-hotspot2-domainname-element.md)               |      | The domain name for the device's Home Network Provider, identifying the operator of the network.<br/>                       |
| [**NAIRealm**](wlan-profileschema-hotspot2-nairealm-element.md)                   |      | A list of Network Access Identifier (NAI) Realm identifiers. Entries in this list are usually of the form user@domain.<br/> |
| [**Network3GPP**](wlan-profileschema-hotspot2-network3gpp-element.md)             |      | A list of Public Land Mobile Network (PLMN) IDs.<br/>                                                                       |
| [**RoamingConsortium**](wlan-profileschema-hotspot2-roamingconsortium-element.md) |      | A list of Organizationally Unique Identifiers (OUI) assigned by IEEE. <br/>                                                 |



## Examples


```XML
<Hotspot2>
   <DomainName>contoso.com</DomainName>
   <Network3GPP>
      <PLMNID>12345</PLMNID>
      <PLMNID>123456</PLMNID>
   </Network3GPP>
   <NAIRealm>
      <name>test1@contoso.com</name>
      <name>test2@contoso.com</name>
   </NAIRealm>
   <RoamingConsortium>
      <OUI>00AABB</OUI>
      <OUI>001122</OUI>
   </RoamingConsortium>
</Hotspot2>
```



 

 




