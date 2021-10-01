---
description: Specifies how to configure the Windows search engine with respect to a given property definition.
ms.assetid: 1cb0b630-323c-41cf-8aaf-db3028b2e369
title: searchInfo
ms.topic: article
ms.date: 05/31/2018
---

# searchInfo

Specifies how to configure the Windows search engine with respect to a given property definition. If no [searchInfo]() element is provided, then the property is not included in the Windows search engine. This element has changed for Windows 7.

## Syntax for Windows 7


```
<!-- searchInfo for Windows 7-->
<xs:element name="searchInfo">
    <xs:complexType>
        <xs:attribute name="inInvertedIndex"    type="xs:boolean" default="false"/>
        <xs:attribute name="isColumn"           type="xs:boolean" default="false"/>
        <xs:attribute name="isColumnSparse"     type="xs:boolean" default="true">
            <xs:annotation>
                <xs:documentation>
                    isColumnSparse: Default is true. If the property is multi-valued, this is always true.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
        
        <xs:attribute name="columnIndexType" default="OnDemand">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="NotIndexed"/>
                    <xs:enumeration value="OnDisk"/>
                    <xs:enumeration value="OnDiskAll"/>
                    <xs:enumeration value="OnDiskVector"/>
                    <xs:enumeration value="OnDemand"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="maxSize" type="xs:nonNegativeInteger" default="512"/>
        <xs:attribute name="mnemonics" type="xs:string"/>                            
    </xs:complexType>
</xs:element>
```



## Syntax for Windows Vista


```
<!-- searchInfo for Windows Vista-->
<xs:element name="searchInfo">
    <xs:complexType>
        <xs:attribute name="inInvertedIndex"    type="xs:boolean" default="false"/>
        <xs:attribute name="isColumn"           type="xs:boolean" default="false"/>
        <xs:attribute name="isColumnSparse"     type="xs:boolean" default="true">
            <xs:annotation>
                <xs:documentation>
                    isColumnSparse: Default is true. If the property is multi-valued, this is always true.
                </xs:documentation>
            </xs:annotation>
        </xs:attribute>
        
        <xs:attribute name="columnIndexType" default="OnDemand">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="NotIndexed"/>
                    <xs:enumeration value="OnDisk"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="maxSize" type="xs:nonNegativeInteger" default="128"/>
    </xs:complexType>
</xs:element>
```



## Element Information



| Parent Element                                                   | Child Elements |
|------------------------------------------------------------------|----------------|
| [propertyDescription](./propdesc-schema-propertydescription.md) | None           |



 

## Attributes




| Attribute | Description | 
|-----------|-------------|
| inInvertedIndex | Public. Optional. Indicates whether the property value should be stored in the inverted index. This lets end users perform full-text queries over the values of this property. The default is "false". | 
| isColumn | Public. Optional. Indicates whether the property should also be stored in the Windows search database as a column, so that independent software vendors (ISVs) can create predicate-based queries (for example, "Select * Where "System.Title"='qqq'"). If the schema creator wants to enable end users (or developers) to create predicate based queries on the properties, then this needs to be set to "true". The default is "false". | 
| isColumnSparse | Public. Optional. The default is "true". If the property is multi-valued, this attribute is always "true". | 
| columnIndexType | Public. Optional. To optimize sorting and grouping, the Windows search engine can create secondary indexes for properties that have isColumn="true". This attribute is only useful when inInvertedIndex is "true" in Windows Vista or when isColumn is "true" in Windows 7. If the property tends to be sorted frequently by users, this attribute should be specified. The default value in Windows Vista is "NotIndexed". The default value in Windows 7 is "OnDemand". The following values are valid.<ul><li><strong>NotIndexed</strong>: Never build a value index.</li><li><strong>OnDisk</strong>: Build a value index by default for this property.</li><li><strong>OnDiskAll</strong> (Windows 7 and later only): Build a value index by default for this property, and if it is a vector property, also a value index for all concatenated vector values.</li><li><strong>OnDiskVector</strong> (Windows 7 and later only): Build a value index by default for the concatenated vector values.</li><li><strong>OnDemand</strong> (Windows 7 and later only): Only build value indices by demand, that is, only first time they are used for a query.</li></ul> | 
| maxSize | Public. Optional. The maximum size, in bytes, allowed for a certain property that is stored in the Windows search database. The default is:<ul><li><strong>Windows Vista</strong>: 128 bytes</li><li><strong>Windows 7 and later</strong>: 512 bytes</li></ul>Note that this maximum size is measured in bytes, not characters. The maximum number of characters depends on their encoding.<br /> | 
| mnemonics | <strong>Windows 7 and later.</strong> Public. Optional. A list of mnemonic values that can be used to refer to the property in search queries. The list is delimited with the '|' character. | 




 

 

 
