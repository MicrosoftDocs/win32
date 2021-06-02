---
description: This topic contains the definition of the Journal Reader schema.
ms.assetid: 2fa6a5d9-64d6-447f-bf2a-d3bf6ca7c093
title: Journal Reader Schema Definition
ms.topic: article
ms.date: 05/31/2018
---

# Journal Reader Schema Definition

This topic contains the definition of the Journal Reader schema.

## Schema


```C++
<xs:schema id="JntXml" xmlns:xs="https://www.w3.org/2001/XMLSchema" 
  targetNamespace="urn:schemas-microsoft-com:tabletpc:journalreader"
  xmlns="urn:schemas-microsoft-com:tabletpc:journalreader" elementFormDefault="qualified">
  <xs:annotation>
    <xs:documentation>
    Windows Journal Reader XML Schema
    Revision date:  2004-10-29
 
    This schema defines the XML format for data derived from Windows Journal
    files using the Windows Journal Reader component.
 
     This is part of the Microsoft Tablet PC Platform SDK 
 
    Copyright (c) 2004 Microsoft Corporation. All rights reserved.
    </xs:documentation>
  </xs:annotation>
  <xs:element name="JournalDocument" type="JournalDocumentType" />
  <!-- ///////////////////////////////////////////////////////////////////////////// -->
  <!-- /// Stationery schema definition starts here! -->
  <!-- ///////////////////////////////////////////////////////////////////////////// -->
  <xs:complexType name="JournalDocumentType">
    <xs:sequence>
      <xs:element name="Stationery" type="StationeryType" minOccurs="0" maxOccurs="unbounded" />
      <xs:element name="JournalPage" type="JournalPageType" maxOccurs="unbounded" />
    </xs:sequence>
    <xs:attribute name="Version" type="xs:string" use="required" fixed="1.0" />
    <xs:attribute name="DefaultPageWidth" type="xs:nonNegativeInteger" use="required" />
    <xs:attribute name="DefaultPageHeight" type="xs:nonNegativeInteger" use="required" />
  </xs:complexType>
  <xs:complexType name="StationeryType">
    <xs:sequence>
      <xs:element name="Background" type="BackgroundType" minOccurs="0" />
      <xs:element name="Title" type="TitleType" minOccurs="0" />
      <xs:element name="LineLayout" type="LineLayoutType" minOccurs="0" />
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="BackgroundType">
    <xs:sequence>
      <xs:element name="Image" type="BackgroundImageType" minOccurs="0" />
    </xs:sequence>
    <xs:attribute name="Style" use="required">
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:pattern value="None|Solid" />
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="Color" type="ColorType" />
  </xs:complexType>
  <xs:complexType name="BackgroundImageType">
    <xs:sequence>
      <xs:element name="Path" type="xs:string" minOccurs="0" />
      <xs:element name="Bitmap" type="xs:base64Binary" minOccurs="0" />
    </xs:sequence>
    <xs:attribute name="Style" use="required">
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:pattern value="Tile|Center|Stretch|TopLeft|TopRight" />
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="Fade" use="required">
      <xs:simpleType>
        <xs:restriction base="xs:integer">
          <xs:minInclusive value="0" />
          <xs:maxInclusive value="255" />
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
  </xs:complexType>
  <xs:complexType name="TitleType">
    <xs:sequence>
      <xs:element name="TitleArea" type="TitleAreaType" minOccurs="0" />
    </xs:sequence>
    <xs:attribute name="Style" use="required">
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:pattern value="None|SolidSquare|OutlineSquare|SolidRoundRect|OutlineRoundRect|SolidRoundRectDottedBaseline" />
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="DateStyle">
      <xs:simpleType>
        <xs:restriction base="xs:string">
          <xs:pattern value="None|Short" />
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
    <xs:attribute name="Color" type="ColorType" />
  </xs:complexType>
  <xs:complexType name="TitleAreaType">
    <xs:attribute name="Left" type="xs:integer" />
    <xs:attribute name="Top" type="xs:integer" />
    <xs:attribute name="Width" type="xs:nonNegativeInteger" />
    <xs:attribute name="Height" type="xs:nonNegativeInteger" />
  </xs:complexType>
  <xs:complexType name="LineLayoutType">
    <xs:sequence>
      <xs:element name="Horizontal" type="HorizontalType" minOccurs="0" />
      <xs:element name="Vertical" type="VerticalType" minOccurs="0" />
      <xs:element name="Margin" type="MarginType" minOccurs="0" />
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="HorizontalType">
    <xs:attribute name="Style" use="required" type="LineLayoutStyleType" />
    <xs:attribute name="Color" type="ColorType" />
    <xs:attribute name="SpacingBefore" type="xs:nonNegativeInteger" />
    <xs:attribute name="SpacingBetween" type="xs:nonNegativeInteger" />
  </xs:complexType>
  <xs:complexType name="VerticalType">
    <xs:attribute name="Style" use="required" type="LineLayoutStyleType" />
    <xs:attribute name="Color" type="ColorType" />
    <xs:attribute name="SpacingBefore" type="xs:nonNegativeInteger" />
    <xs:attribute name="SpacingBetween" type="xs:nonNegativeInteger" />
  </xs:complexType>
  <xs:complexType name="MarginType">
    <xs:attribute name="Style" use="required" type="LineLayoutStyleType" />
    <xs:attribute name="Color" type="ColorType" />
    <xs:attribute name="Type" type="MarginTypeType" />
    <xs:attribute name="Spacing" type="xs:nonNegativeInteger" />
  </xs:complexType>
  <xs:simpleType name="MarginTypeType">
    <xs:restriction base="xs:string">
      <xs:pattern value="Left|Right" />
    </xs:restriction>
  </xs:simpleType>
  <!-- ///////////////////////////////////////////////////////////////////////////// -->
  <!-- /// Stationery schema definition ends here! -->
  <!-- ///////////////////////////////////////////////////////////////////////////// -->
  <!-- ///////////////////////////////////////////////////////////////////////////// -->
  <!-- /// Journal Page schema definition starts here! -->
  <!-- ///////////////////////////////////////////////////////////////////////////// -->
  <xs:complexType name="JournalPageType">
    <xs:sequence>
      <xs:element name="Stationery" type="StationeryType" minOccurs="0" />
      <xs:element name="DocImage" type="xs:base64Binary" minOccurs="0" />
      <xs:element name="TitleInfo" type="TitleInfoType" minOccurs="0" />
      <xs:element name="Content" type="ContentType" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
    <xs:attribute name="Number" use="required" type="xs:positiveInteger" />
    <xs:attribute name="Width" use="required" type="xs:nonNegativeInteger" />
    <xs:attribute name="Height" use="required" type="xs:nonNegativeInteger" />
    <xs:attribute name="LineHeight" type="xs:nonNegativeInteger" />
    <xs:attribute name="LanguageId" type="xs:string" />
  </xs:complexType>
  <xs:complexType name="ContentType">
    <xs:group ref="ContentGroup" minOccurs="0" maxOccurs="unbounded" />
    <xs:attribute name="Type" use="required" type="ContentTypeType" />
  </xs:complexType>
  <xs:group name="ContentGroup" >
    <xs:choice>
      <xs:element name="GroupNode" type="GroupNodeType" />
      <xs:element name="Paragraph" type="ParagraphType" />
      <xs:element name="InkWord" type="InkWordType" />
      <xs:element name="Drawing" type="DrawingType" />
      <xs:element name="Text" type="TextType" />
      <xs:element name="Image" type="ImageType" />
      <xs:element name="Flag" type="FlagType" />
      <xs:element name="Reflow" type="ReflowType" />
    </xs:choice>
  </xs:group>
  <xs:simpleType name="ContentTypeType">
    <xs:restriction base="xs:string">
      <xs:pattern value="Normal|Inert" />
    </xs:restriction>
  </xs:simpleType>
  <xs:attributeGroup name="BoundsType">
    <xs:attribute name="Left" use="required" type="xs:integer" />
    <xs:attribute name="Top" use="required" type="xs:integer" />
    <xs:attribute name="Width" use="required" type="xs:nonNegativeInteger" />
    <xs:attribute name="Height" use="required" type="xs:nonNegativeInteger" />
  </xs:attributeGroup>
  <xs:complexType name="GroupNodeType">
    <xs:sequence>
      <xs:element name="ScalarTransform" minOccurs="0" type="ScalarTransformType" />
      <xs:group ref="ContentGroup" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
    <xs:attributeGroup ref="BoundsType" />
  </xs:complexType>
  <xs:complexType name="TextType">
    <xs:simpleContent>
      <xs:extension base="xs:string">
        <xs:attributeGroup ref="BoundsType" />
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>
  <xs:complexType name="ImageType">
    <xs:simpleContent>
      <xs:extension base="xs:base64Binary">
        <xs:attributeGroup ref="BoundsType" />
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>
  <xs:complexType name="FlagType">
    <xs:simpleContent>
      <xs:extension base="xs:base64Binary">
        <xs:attributeGroup ref="BoundsType" />
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>
  <xs:complexType name="ReflowType">
    <xs:group ref="ContentGroup" minOccurs="0" maxOccurs="unbounded" />
  </xs:complexType>
  <xs:complexType name="DrawingType">
    <xs:sequence>
      <xs:element name="ScalarTransform" minOccurs="0" type="ScalarTransformType" />
      <xs:element name="CanReclassify" minOccurs="0" type="xs:boolean" />
      <xs:element name="InkClass" minOccurs="0" type="xs:string" />
      <xs:element name="InkObject" type="xs:base64Binary" />
    </xs:sequence>
    <xs:attributeGroup ref="BoundsType" />
  </xs:complexType>
  <xs:complexType name="ParagraphType">
    <xs:sequence>
      <xs:element name="Line" type="LineType" maxOccurs="unbounded" />
    </xs:sequence>
    <xs:attribute name="BlockNumber" use="required" type="xs:nonNegativeInteger" />
  </xs:complexType>
  <xs:complexType name="LineType">
    <xs:sequence>
      <xs:element name="InkWord" type="InkWordType" maxOccurs="unbounded" />
      <xs:element name="ParagraphLineMetrics" type="ParagraphLineMetricsType" />
    </xs:sequence>
    <xs:attributeGroup ref="BoundsType" />
    <xs:attribute name="LineNumber" use="required" type="xs:nonNegativeInteger" />
  </xs:complexType>
  <xs:complexType name="InkWordType">
    <xs:sequence>
      <xs:element name="ScalarTransform" minOccurs="0" type="ScalarTransformType" />
      <xs:element name="AlternateList" minOccurs="0" type="AlternatesListType" />
      <xs:element name="CanReclassify" minOccurs="0" type="xs:boolean" />
      <xs:element name="Confidence" minOccurs="0" type="ConfidenceType" />
      <xs:element name="InkObject" type="xs:base64Binary" />
    </xs:sequence>
    <xs:attributeGroup ref="BoundsType" />
  </xs:complexType>
  <xs:complexType name="AlternatesListType">
    <xs:sequence>
      <xs:element name="Alternate" type="xs:string" minOccurs="0" maxOccurs="unbounded" />
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="ParagraphLineMetricsType">
    <xs:sequence>
      <xs:element name="Baseline" type="BaseLineType" />
    </xs:sequence>
  </xs:complexType>
  <xs:complexType name="BaseLineType">
    <xs:attribute name="StartX" use="required" type="xs:nonNegativeInteger" />
    <xs:attribute name="StartY" use="required" type="xs:nonNegativeInteger" />
    <xs:attribute name="EndX" use="required" type="xs:nonNegativeInteger" />
    <xs:attribute name="EndY" use="required" type="xs:nonNegativeInteger" />
  </xs:complexType>
  <xs:complexType name="ScalarTransformType">
    <xs:attribute name="Mat1" use="required" type="xs:decimal" />
    <xs:attribute name="Mat2" use="required" type="xs:decimal" />
    <xs:attribute name="Mat3" use="required" type="xs:decimal" />
    <xs:attribute name="Mat4" use="required" type="xs:decimal" />
    <xs:attribute name="Mat5" use="required" type="xs:decimal" />
    <xs:attribute name="Mat6" use="required" type="xs:decimal" />
    <xs:attribute name="Mat7" use="required" type="xs:decimal" />
    <xs:attribute name="Mat8" use="required" type="xs:decimal" />
    <xs:attribute name="Mat9" use="required" type="xs:decimal" />
  </xs:complexType>
  <xs:complexType name="TitleInfoType">
    <xs:sequence>
      <xs:element name="Text" type="xs:string" />
      <xs:element name="Date" type="xs:dateTime" />
    </xs:sequence>
  </xs:complexType>
  <!-- ///////////////////////////////////////////////////////////////////////////// -->
  <!-- /// Journal Page schema definition ends here! -->
  <!-- ///////////////////////////////////////////////////////////////////////////// -->
  <!-- ///////////////////////////////////////////////////////////////////////////// -->
  <!-- /// General schema definition starts here! -->
  <!-- ///////////////////////////////////////////////////////////////////////////// -->
  <xs:simpleType name="ColorType">
    <xs:restriction base="xs:string">
      <xs:pattern value="#[0-9a-fA-F]{6}" />
      <xs:length value="7" />
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="LineLayoutStyleType">
    <xs:restriction base="xs:string">
      <xs:pattern value="None|Solid|Dash|Dot|DashDot|DashDotDot|Double" />
    </xs:restriction>
  </xs:simpleType>
  <xs:simpleType name="ConfidenceType">
    <xs:restriction base="xs:nonNegativeInteger">
      <xs:maxInclusive value="2" />
    </xs:restriction>
  </xs:simpleType>
  <!-- ///////////////////////////////////////////////////////////////////////////// -->
  <!-- /// General schema definition ends here! -->
  <!-- ///////////////////////////////////////////////////////////////////////////// -->
</xs:schema>
```



 

 



