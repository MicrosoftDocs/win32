---
description: Mobile Broadband Profile Schema v1.
ms.assetid: e55775d2-1166-4f14-9553-207c69202b69
title: Mobile Broadband Profile Schema v1
ms.topic: reference
ms.date: 05/31/2018
---

# Mobile Broadband Profile Schema v1

The Windows 7Mobile Broadband Profile Schema v1 is available in the namespace `https://www.microsoft.com/networking/WWAN/profile/v1`.

-   [Mobile Broadband Profile Schema v1 Elements](schema-elements.md)
-   [Mobile Broadband Profile Schema v1 Simple Types](schema-simple-types.md)
-   [Mobile Broadband Profile Schema v1 Complex Types](schema-complex-types.md)

``` syntax
<?xml version="1.0" encoding="UTF-8" ?>
<xs:schema targetNamespace="https://www.microsoft.com/networking/WWAN/profile/v1"
    xmlns="https://www.microsoft.com/networking/WWAN/profile/v1" 
    xmlns:xs="https://www.w3.org/2001/XMLSchema"
    elementFormDefault="qualified">

  <!-- type definition section -->

  <xs:simpleType name="nameType">
    <xs:restriction base="xs:normalizedString">
      <xs:minLength value="1"/>
      <xs:maxLength value="255"/>
      <xs:whiteSpace value="collapse"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="subscriberIdType">
    <xs:restriction base="xs:token">
      <xs:minLength value="1"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="simIccIDType">
    <xs:restriction base="xs:token">
      <xs:pattern value="\d{1,20}"/>
      <xs:pattern value="[a-zA-Z\d]{1,20}"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:complexType name="contextType">
    <xs:sequence>
      <xs:element name="AccessString" minOccurs="0">
        <xs:simpleType>
          <xs:restriction base="xs:token">
            <xs:minLength value="1"/>
            <xs:maxLength value="100"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:element>
      <xs:element name="UserLogonCred" minOccurs="0">
        <xs:complexType>
          <xs:sequence>
            <xs:element name="UserName" type="nameType"/>
            <xs:element name="IgnorePassword" type="xs:boolean" minOccurs="0" />
            <xs:element name="Password" type="xs:string" minOccurs="0"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="Compression" minOccurs="0">
        <xs:simpleType>
          <xs:restriction base="xs:token">
            <xs:enumeration value="DISABLE"/>
            <xs:enumeration value="ENABLE"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:element>
      <xs:element name="AuthProtocol" minOccurs="0">
        <xs:simpleType>
          <xs:restriction base="xs:token">
            <xs:enumeration value="NONE"/>
            <xs:enumeration value="PAP"/>
            <xs:enumeration value="CHAP"/>
            <xs:enumeration value="MsCHAPv2"/>
          </xs:restriction>
        </xs:simpleType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="providerNameType">
    <xs:restriction base="xs:normalizedString">
      <xs:minLength value="1"/>
      <xs:maxLength value="20"/>
      <xs:whiteSpace value="collapse"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="providerIdType">
    <xs:restriction base="xs:token">
      <xs:pattern value="\d{1,6}"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:complexType name="providerType">
    <xs:sequence>
      <xs:element name="ProviderID" type="providerIdType"/>
      <xs:element name="ProviderName" type="providerNameType"/>
    </xs:sequence>
  </xs:complexType>

  <xs:simpleType name="iconFileType">
    <xs:restriction base="xs:token">
      <xs:minLength value="1"/>
      <xs:maxLength value="1024"/>
    </xs:restriction>
  </xs:simpleType>

  <!-- element definition section -->

  <xs:element name="MBNProfile">
    <xs:complexType>
      <xs:sequence>
        <!-- Profile name -->
        <xs:element name="Name" type="nameType"/>

        <!-- Brief description of the profile -->
        <xs:element name="Description" type="nameType" minOccurs="0"/>

        <!-- Path of the icon file for the provider -->
        <xs:element name="ICONFilePath" type="iconFileType" minOccurs="0"/>

        <!-- Flag to indicate whether this is the default profile -->
        <!-- Atmost one profile per SIM shall have this flag set to true -->
        <xs:element name="IsDefault" type="xs:boolean"/>
    
        <!-- Profile creation type -->
        <!-- This is used to decide if the user can delete the profile or not  -->
        <xs:element name="ProfileCreationType" minOccurs="0">
          <xs:simpleType>
            <xs:restriction base="xs:token">
              <xs:enumeration value="UserProvisioned"/>
              <xs:enumeration value="AdminProvisioned"/>
              <xs:enumeration value="OperatorProvisioned"/>
              <xs:enumeration value="DeviceProvisioned"/>
            </xs:restriction>
          </xs:simpleType>
        </xs:element>

        <!-- Subscriber Identification : IMSI, MIN, etc -->
        <xs:element name="SubscriberID" type="subscriberIdType"/>

        <!-- SimIccID number of the SIM -->
        <xs:element name="SimIccID" type="simIccIDType" minOccurs="0"/>

        <!-- Home Provider Name -->
        <xs:element name="HomeProviderName" type="providerNameType" minOccurs="0"/>

        <!-- Flag to indicate wether the Auto Connect should be blocked when we have Internet Connectivity -->
        <xs:element name="AutoConnectOnInternet" type="xs:boolean" minOccurs="0"/>

        <!-- Connection Mode, default is "manual" -->
        <xs:element name="ConnectionMode" minOccurs="0">
          <xs:simpleType>
            <xs:restriction base="xs:string">
              <!-- manual connect always -->
              <xs:enumeration value="manual" />
              <!-- auto connect always -->
              <xs:enumeration value="auto" />
              <!-- auto connect when not roaming -->
              <xs:enumeration value="auto-home"/>
            </xs:restriction>
          </xs:simpleType>
        </xs:element>

        <!-- Connection Settings -->
        <xs:element name="Context" type="contextType" minOccurs="0"/>

        <!-- Roaming Partner List -->
        <xs:element name="DataRoamingPartners" minOccurs="0">
          <xs:complexType>
            <xs:sequence>
              <xs:element name="Provider" type="providerType" maxOccurs="unbounded"/>
            </xs:sequence>
          </xs:complexType>
        </xs:element>

        <!-- extension point for other namespaces -->
        <xs:any namespace="##other" processContents="lax" minOccurs="0" maxOccurs="unbounded" />
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

 

 



