---
description: A call to the PeerGroupSearchRecords function requires an XML query string parameter that is used to determine the basic criteria of a search.
ms.assetid: 2c5ab425-6959-418a-8d9a-c8155257fc7e
title: Record Search Query Format
ms.topic: article
ms.date: 05/31/2018
---

# Record Search Query Format

A call to the [**PeerGroupSearchRecords**](/windows/desktop/api/P2P/nf-p2p-peergroupsearchrecords) function requires an XML query string parameter that is used to determine the basic criteria of a search. Use the following schema to formulate an XML string:

``` syntax
<?xml version="1.0" encoding="utf-8" ?>
<xs:schema xmlns:xs="https://www.w3.org/2001/XMLSchema">

  <xs:simpleType name="alphanumType">
     <xs:restriction base="xs:string">
        <xs:pattern value="\c+"/>
     </xs:restriction>
  </xs:simpleType>

  <xs:complexType name="operatorType">
      <xs:choice maxOccurs="unbounded">
         <xs:element ref="and" />
         <xs:element ref="or" />
         <xs:element ref="clause" />
      </xs:choice>
  </xs:complexType>

  <xs:element name="and" type="operatorType"/>

  <xs:element name="or" type="operatorType"/>

  <xs:element name="clause">
      <xs:complexType>
          <xs:simpleContent>
              <xs:extension base="xs:string">
        <xs:attribute name="attrib" type="alphanumType" />
        <xs:attribute name="type">
                  <xs:simpleType>
                    <xs:restriction base="xs:string">
                      <xs:enumeration value="string"/>
                      <xs:enumeration value="date"/>
                      <xs:enumeration value="int"/>
                    </xs:restriction>
                  </xs:simpleType>
                </xs:attribute>
        <xs:attribute name="compare" default="equal">
                  <xs:simpleType>
                    <xs:restriction base="xs:string">
                      <xs:enumeration value="equal"/>
                      <xs:enumeration value="greater"/>
                      <xs:enumeration value="less"/>
                      <xs:enumeration value="notequal"/>
                      <xs:enumeration value="greaterorequal"/>
                      <xs:enumeration value="lessorequal"/>
                    </xs:restriction>
                  </xs:simpleType>
                </xs:attribute>
              </xs:extension>
          </xs:simpleContent>
      </xs:complexType>
  </xs:element>

  <xs:element name="peersearch">
      <xs:complexType>
          <xs:choice>
              <xs:element ref="clause" />
              <xs:element ref="and" />
              <xs:element ref="or" />
          </xs:choice>
      </xs:complexType>
  </xs:element>
</xs:schema> 
```

### Elements to Use for a Record Search

The primary element in a record search is **peersearch**, which contains the Uniform Resource Identifier (URI) of the associated schema in the **xmlns** attribute. When **peersearch** is used as a child element, you can use **and**, **clause**, and **or** as child elements.

-   **and** - The **and** element performs a logical AND operation on one or more clauses contained between the opening and closing tags. Other **and** and **or** tags can be children, and recursive results of their child clauses are included in the operation.

    For example, if you want to obtain a record that contains a name equal to James Peters, and a last update that is greater than 2/28/2003, or a creation date that is less than 1/31/2003, use the following XML query string:

    ``` syntax
    <?xml version="1.0" encoding="utf-8" ?> 
    <peersearch xmlns:xs="https://www.w3.org/2001/XMLSchema">
       <and>
          <clause attrib="peercreatorid" type="string" compare="equal">James Peters</clause>
          <or>
             <clause attrib="peerlastmodificationtime" type="date" compare="greater">2003-01-31</clause>
             <clause attrib="peercreationtime" type="date" compare="less">2003-02-328</clause>
          </or>
       </and>
    </peersearch>
    ```

<!-- -->

-   **clause** - The **clause** element specifies a basic comparative rule that compares the value of a specific record attribute with the value contained between the opening and closing tags. The **type** and **compare** attributes must be provided **compare** indicates the comparison operation to be performed. For example, a simple search that indicates all matched records must have a **peercreatorid** value equal to James Peters appears in the XML query string as the following:

    ``` syntax
    <?xml version="1.0" encoding="utf-8" ?> 
    <peersearch xmlns:xs="https://www.w3.org/2001/XMLSchema">
       <clause attrib="peercreatorid" type="string" compare="equal">James Peters</clause>
    </peersearch>
    ```

    Common **type** attributes include **int**, **string**, and **date**. The **date** attribute can be one of the standard date formats described at [https://www.w3.org/TR/NOTE-datetime](https://www.w3.org/TR/NOTE-datetime).

    Values for the **compare** attribute are **equal**, **notequal**, **less**, **greater**, **lessorequal**, and **greaterorequal**.

<!-- -->

-   **or** - The **or** element performs a logical OR operation on one or more clauses contained between the opening and closing tags. Other **or** and **and** elements can be children, and recursive results of the child clauses are included in the operation. For example, if you want to obtain a record that contains a name equal to James Peters, or a last update that is between 1/31/2003 and 2/28/2003, use the following XML query string:

``` syntax
<?xml version="1.0" encoding="utf-8" ?> 
<peersearch xmlns:xs="https://www.w3.org/2001/XMLSchema">
   <or>
      <clause attrib="peercreatorid" type="string" compare="equal">James Peters</clause>
      <and>
         <clause attrib="peerlastmodificationtime" type="date" compare="greater">2003-01-31</clause>
         <clause attrib="peerlastmodificationtime" type="date" compare="less">2003-02-28</clause>
      </and>
   </or>
</peersearch>
```

## More Information About a Record Search

The first level of nodes after **peersearch** can have only one element. However, subsequent children of that element can have many elements at the same level.

The following search query is incorrect:

``` syntax
<?xml version="1.0" encoding="utf-8" ?> 
<peersearch xmlns:xs="https://www.w3.org/2001/XMLSchema">
   <clause attrib="peercreatorid" type="string" compare="equal">James Peters</clause>
   <and>
      <clause attrib="peerlastmodificationtime" type="date" compare="greater">2003-01-31</clause>
      <clause attrib="peerlastmodificationtime" type="date" compare="less">2003-02-28</clause>
   </and>
</peersearch>
```

The query fails because two values are returned for the match without being resolved into one true/false value, which means that one clause is a query for the name of a record that equals James Peters, and the AND operation matches the two component clauses. The result is two logical true/false values that are contradictory.

To obtain all records that contain a name equal to James Peters, and a last update that is between 1/31/2003 and 2/28/2003, place the **clause** and **and** tags that are at the same level between opening and closing **and** tags. The following example shows you the successful query:

``` syntax
<?xml version="1.0" encoding="utf-8" ?> 
<peersearch xmlns:xs="https://www.w3.org/2001/XMLSchema">
    <and>
      <clause attrib="peercreatorid" type="string" compare="equal">James Peters</clause>
      <and>
         <clause attrib="peerlastmodificationtime" type="date" compare="greater">2003-01-31</clause>
         <clause attrib="peerlastmodificationtime" type="date" compare="less">2003-02-28</clause>
      </and>
   </and>
</peersearch>
```

The following list identifies other specific information that you must know to write a successful query:

-   The **and** and **or** tags cannot be located between opening and closing **clause** tags because, in that configuration, they are interpreted as part of the value to match against, which results in an error or a failed match.
-   Each pair of **and** and **or** opening and closing tags must include at least one or more child nodes.
-   A zero set of elements is not allowed in this schema.

## Record Attributes

By using the [Record Attribute Schema](record-attribute-schema.md), a user can create record attributes that the **attrib** XML attribute in a clause element specifies. Attributes for a new record are added by setting the **pszAttributes** member of [**PEER\_RECORD**](/windows/desktop/api/P2P/ns-p2p-peer_record) to an XML string using the format specified in the schema.

The Peer Infrastructure reserves the following attribute names:

-   **peerlastmodifiedby**
-   **peercreatorid**
-   **peerlastmodificationtime**
-   **peerrecordid**
-   **peerrecordtype**
-   **peercreationtime**
-   **peerlastmodificationtime**

## Special Characters

Certain characters can be used to express matching patterns, or to escape other special characters. These characters are described in the table below. 

| Character pattern | Description                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \*                | The wildcard character. When this character is encountered in a clause value, it matches 0-n characters of any value, including whitespace and nonalphanumeric characters. For example:<br/> "\<clause attrib="peercreatorid" type="string" compare="equal"\>James P\*&lt;/clause&gt;"<br/> This clause matches all **peercreatorid** values with a first name of "James" and a last name starting with "P".<br/> |
| \\\*              | An escaped asterisk. This sequence matches an asterisk character.                                                                                                                                                                                                                                                                                                                                                                       |
| ?                 | The single-character wildcard character. When this character is encountered in a clause value, it matches any single character, including whitespace and nonalphanumeric characters.For example:<br/> "\<clause attrib="filename" type="string" compare="equal"\>data-0?.xml&lt;/clause&gt;"<br/> This clause matches **filename** values like "data-01.xml" and "data-0B.xml".<br/>                              |
| \\?               | An escaped question mark. This sequence matches a question mark character.                                                                                                                                                                                                                                                                                                                                                              |
| \\\\              | An escaped backslash. This sequence matches a single backslash character.                                                                                                                                                                                                                                                                                                                                                               |



 

If the character sequence is not valid, the [**PeerGroupSearchRecords**](/windows/desktop/api/P2P/nf-p2p-peergroupsearchrecords) function returns the error **E\_INVALIDARG**. An invalid sequence is any sequence that contains a "\\" (backslash) character not immediately followed by either an "\*" (asterisk) character, a "?" (question mark) character, or another "\\" (backslash) character.

 

 




