---
description: Records can have application-specific attributes that are a sequence of name or value pairs represented as an XML string in the pszAttributes member of the PEER\_RECORD structure.
ms.assetid: 2991af9b-da32-4915-b4d6-575e3faac04e
title: Record Attribute Schema
ms.topic: article
ms.date: 05/31/2018
---

# Record Attribute Schema

Records can have application-specific attributes that are a sequence of name or value pairs represented as an XML string in the **pszAttributes** member of the [**PEER\_RECORD**](/windows/desktop/api/P2P/ns-p2p-peer_record) structure. The attributes are used to filter a record search initiated by calls to [**PeerGroupSearchRecords**](/windows/desktop/api/P2P/nf-p2p-peergroupsearchrecords), which takes an XML search filter specified in [Record Search Query Format](record-search-query-format.md) as a parameter.

A record attribute can be one of the following three types:

-   **int** is an integer value.
-   **date** is a datetime value represented as one of the standard formats described at [https://www.w3.org/TR/NOTE-datetime](https://www.w3.org/TR/NOTE-datetime).
-   **string** is a Unicode string value.

The following list identifies the specific attribute names that are reserved by the Peer Infrastructure:

-   **peerlastmodifiedby**
-   **peercreatorid**
-   **peerlastmodificationtime**
-   **peerrecordid**
-   **peerrecordtype**
-   **peercreationtime**
-   **peerlastmodificationtime**

## Example of Defining Record Attributes

The following schema example shows you how to define record attributes:

``` syntax
<?xml version="1.0" encoding="utf-8" ?>
<xs:schema xmlns:xs="https://www.w3.org/2001/XMLSchema">
   <xs:simpleType name="alphanum">
       <xs:restriction base="xs:string">
          <xs:pattern value="\c+" />
       </xs:restriction>
   </xs:simpleType>
   <xs:complexType name="attributeType">
       <xs:simpleContent>
          <xs:extension base="xs:string">
                <xs:attribute name="name" type="alphanum" />
                <xs:attribute name="type">
                    <xs:simpleType>
                        <xs:restriction base="alphanum">
                           <xs:enumeration value="string"/>
                           <xs:enumeration value="date"/>
                           <xs:enumeration value="int"/>
                        </xs:restriction>
                    </xs:simpleType>
                </xs:attribute>
           </xs:extension>
       </xs:simpleContent>
    </xs:complexType>
    <xs:element name="attributes">
       <xs:complexType>
           <xs:sequence>
                <xs:element name="attribute" type="attributeType" minOccurs="0" maxOccurs="unbounded" />
           </xs:sequence>
       </xs:complexType>
    </xs:element>
</xs:schema>  
```

> [!Note]  
> Attribute names must be sequences of alphanumeric characters. Special characters like hyphens ("-") and underscores ("\_") are not allowed in an attribute name.

 

The following example of an XML attribute sequence contains the custom **AuthenticationType** and **AuthExpires** attributes that appear in the **pszAttributes** member of [**PEER\_RECORD**](/windows/desktop/api/P2P/ns-p2p-peer_record).

``` syntax
<attributes>
  <attribute name="AuthenticationType" type="string">Kerberos</attribute><attribute name="AuthExpires" type="date">2002-01-31</attribute>
<attributes>
```

 

 



