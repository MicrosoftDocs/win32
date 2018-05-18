---
title: Configuration File Schema
description: The dsmlv2.config configuration file uses the following schema for validation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '77da5110-1a24-41bf-9ee1-ce6b5ca30143'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["Configuration File Schema DSML"]
---

# Configuration File Schema

The dsmlv2.config configuration file uses the following schema for validation.

## Dsmlv2.config Schema

``` syntax
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema"
            xmlns="urn:schema-microsoft-com:activedirectory:dsmlv2:configuration" 
            elementFormDefault="qualified">
            targetNamespace="urn:schema-microsoft-com:activedirectory:dsmlv2:configuration">
<xsd:element name="extensionConfiguration" type="ExtensionConfiguration"/>
<!-- *********************** -->
<!-- *** MAX Port Number *** -->
<!-- *********************** -->
<xsd:simpleType name="MAXPORT">
    <xsd:restriction base="xsd:unsignedInt">
       <xsd:minInclusive value="1"/>        
       <xsd:maxInclusive value="65535"/>
   </xsd:restriction>
</xsd:simpleType>
<!-- ******************* -->
<!-- *** MAX Integer *** -->
<!-- ******************* -->
<xsd:simpleType name="MAXINT">
    <xsd:restriction base="xsd:unsignedInt">
       <xsd:minInclusive value="1"/>    
       <xsd:maxInclusive value="2147483647"/>
   </xsd:restriction>
</xsd:simpleType>
<!-- *********************** -->
<!-- *** MAX Connections *** -->
<!-- *********************** -->
<xsd:simpleType name="MAXCONNS">
    <xsd:restriction base="xsd:unsignedInt">
       <xsd:minInclusive value="1"/>    
       <xsd:maxInclusive value="512"/>
   </xsd:restriction>
</xsd:simpleType>       
<!-- ******************** -->
<!-- *** MAX Sessions *** -->
<!-- ******************** -->
<xsd:simpleType name="MAXSESS">
    <xsd:restriction base="xsd:unsignedInt">
       <xsd:maxInclusive value="512"/>
   </xsd:restriction>
</xsd:simpleType>           
<!-- ************************ -->
<!-- *** Referral Chasing *** -->
<!-- ************************ -->
<xsd:simpleType name="REFERRALCHASE">
    <xsd:restriction base="xsd:string">
        <xsd:enumeration value="never"/>
        <xsd:enumeration value="always"/>
        <xsd:enumeration value="subordinate"/>
        <xsd:enumeration value="external"/>
    </xsd:restriction>
</xsd:simpleType>
<!-- ******************************* -->
<!-- *** Extension Configuration *** -->
<!-- ******************************* -->
<xsd:complexType name="ExtensionConfiguration">
  <xsd:sequence>
    <xsd:element name="virtualDirectory" minOccurs="1" maxOccurs="unbounded" type="VirtualDirectory"/>
  </xsd:sequence>
</xsd:complexType>
<!-- ************************* -->
<!-- *** Virtual Directory *** -->
<!-- ************************* -->
<xsd:complexType name="VirtualDirectory">
  <xsd:sequence>
    <xsd:element name="server"     minOccurs="0" maxOccurs="1" default=""      type="xsd:string"/>
    <xsd:element name="port"       minOccurs="0" maxOccurs="1" default="389"   type="MAXPORT"/>
    <xsd:element name="useSSL"     minOccurs="0" maxOccurs="1" default="false" type="xsd:boolean"/>
    <xsd:element name="useSigning" minOccurs="0" maxOccurs="1" default="false" type="xsd:boolean"/>
    <xsd:element name="useSealing" minOccurs="0" maxOccurs="1" default="false" type="xsd:boolean"/>
    <xsd:element name="readOnly"   minOccurs="0" maxOccurs="1" default="false" type="xsd:boolean"/>
    <xsd:element name="connectTimeout"      minOccurs="0" maxOccurs="1" type="MAXINT"/>    
    <xsd:element name="operationTimeout"    minOccurs="0" maxOccurs="1" type="MAXINT"/>    
    <xsd:element name="maxConnections"      minOccurs="0" maxOccurs="1" default="5"     type="MAXCONNS"/>
    <xsd:element name="maxRequestsPerBatch" minOccurs="0" maxOccurs="1" default="1000"  type="MAXINT"/>
    <xsd:element name="chaseReferrals"      minOccurs="0" maxOccurs="1" default="never" type="REFERRALCHASE"/>
    <xsd:element name="sessionsMax"         minOccurs="0" maxOccurs="1" default="100"   type="MAXSESS"/>
    <xsd:element name="sessionsMaxPerIP"    minOccurs="0" maxOccurs="1" default="5"     type="MAXSESS"/>
    <xsd:element name="sessionsIPMatch"     minOccurs="0" maxOccurs="1" default="true"  type="xsd:boolean"/>
    <xsd:element name="sessionsAuthMatch"   minOccurs="0" maxOccurs="1" default="true"  type="xsd:boolean"/>
    <xsd:element name="sessionsTTL"         minOccurs="0" maxOccurs="1" default="600"   type="MAXINT"/>
  </xsd:sequence>
  <xsd:attribute name="url" use="required" type="xsd:string"/>
</xsd:complexType>
<!-- *** END OF SCHEMA *** -->
</xsd:schema>
```

 

 




