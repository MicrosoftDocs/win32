---
title: Windows Color System Common Profile Types schema, Versioning and Localization Strategies
description: Windows Color System Common Profile Types schema, Versioning and Localization Strategies
ms.assetid: 295522c6-7c53-47f6-9b98-aeee2b0e34fc
keywords:
- Windows Color System (WCS),common profile types
- WCS (Windows Color System),common profile types
- image color management,common profile types
- color management,common profile types
- colors,common profile types
- Windows Color System (WCS),profiles
- WCS (Windows Color System),profiles
- image color management,profiles
- color management,profiles
- colors,profiles
- Windows Color System (WCS),versioning
- WCS (Windows Color System),versioning
- image color management,versioning
- color management,versioning
- colors,versioning
- Windows Color System (WCS),localization
- WCS (Windows Color System),localization
- image color management,localization
- color management,localization
- colors,localization
- WCS common profile types
- profile consumers
- common profile types
- schemas,common profile types


ms.topic: article
ms.date: 05/31/2018
---

# Windows Color System Common Profile Types schema, Versioning and Localization Strategies

-   [WCS Common Profile Types Schema V1](#wcs-common-profile-types-schema-v1)
-   [WCS Common Profile Types Schema V2 Additions](#wcs-common-profile-types-schema-v2-additions)
-   [WCS Profile Schema Versioning](#wcs-profile-schema-versioning)
-   [WCS Profile Localization](#wcs-profile-localization)
    -   [Expressing localizable elements](#expressing-localizable-elements)
    -   [Schema Support](#schema-support)
    -   [Selecting the Language](#selecting-the-language)
    -   [Built-in profiles](#built-in-profiles)
-   [Related topics](#related-topics)

## WCS Common Profile Types Schema V1

The following provides the v1.0 schema definition for the WCS Common Profile Types.


```XML
<?xml version="1.0" encoding="UTF-8"?>
<xs:schema
  xmlns:xs="http://www.w3.org/2001/XMLSchema"
  xmlns:wcs="http://schemas.microsoft.com/windows/2005/02/color/WcsCommonProfileTypes"
  targetNamespace="http://schemas.microsoft.com/windows/2005/02/color/WcsCommonProfileTypes"
  elementFormDefault="qualified"
  attributeFormDefault="unqualified"
  blockDefault="#all"
  version="1.0">

  <xs:import namespace="http://www.w3.org/XML/1998/namespace" />

  <xs:annotation>
    <xs:documentation xml:lang="en">
      Common types used in WCS profile schemas.
      Copyright (C) Microsoft. All rights reserved.
    </xs:documentation>
  </xs:annotation>

  <xs:simpleType name="NonNegativeFloatType">
    <xs:restriction base="xs:float">
      <xs:minInclusive value="0"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:complexType name="NonNegativeCIEXYZType">
    <xs:attribute name="X" type="wcs:NonNegativeFloatType" use="required"/>
    <xs:attribute name="Y" type="wcs:NonNegativeFloatType" use="required"/>
    <xs:attribute name="Z" type="wcs:NonNegativeFloatType" use="required"/>
  </xs:complexType>

  <xs:simpleType name="GUIDType">
    <xs:restriction base="xs:string">
      <xs:pattern value="\{[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\}"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:complexType name="LocalizedTextType">
    <xs:simpleContent>
      <xs:extension base="xs:string">
        <xs:attribute ref="xml:lang" use="required"/>
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>

  <xs:complexType name="MultiLocalizedTextType">
    <xs:sequence>
      <xs:element name="Text" type="wcs:LocalizedTextType" minOccurs="1" />
    </xs:sequence>
  </xs:complexType>

</xs:schema>

```



Only UTF-8 or UTF-16 encodings are supported. All other XML encodings are strongly discouraged in order to preserve optimum interoperability.

## WCS Common Profile Types Schema V2 Additions

In Windows 7, the WCS Common Profile Types schema has been updated to include types to support the [WCS Calibration schema](wcs-calibration-schema.md).


```XML
  <xs:complexType name="ParameterizedCurvesType">
    <xs:sequence>
      <xs:element name="RedTRC" type="wcs:ParameterizedCurveType"/>
      <xs:element name="GreenTRC" type="wcs:ParameterizedCurveType"/>
      <xs:element name="BlueTRC" type="wcs:ParameterizedCurveType"/>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="ParameterizedCurveType">
    <xs:attribute name="Gamma" type="wcs:NonNegativeFloatType" use="required"/>
    <xs:attribute name="Offset1" type="xs:float" use="optional"/>
    <xs:attribute name="Gain" type="wcs:NonNegativeFloatType" use="optional"/>
    <xs:attribute name="Offset2" type="xs:float " use="optional"/>
    <xs:attribute name="TransitionPoint" type="wcs:NonNegativeFloatType" use="optional"/>
    <xs:attribute name="Offset3" type="xs:float" use="optional"/>
  </xs:complexType>

  <xs:simpleType name="FloatList">
    <xs:list itemType="xs:float"/>
  </xs:simpleType>

  <xs:complexType name="OneDimensionLutType">
    <xs:sequence>
      <xs:element name="Input" type="wcs:FloatList"/>
      <xs:element name="Output" type="wcs:FloatList"/>
    </xs:sequence>
  </xs:complexType>

  <xs:complexType name="HDRToneResponseCurvesType">
    <xs:sequence>
      <xs:element name="RedTRC" type="wcs:OneDimensionLutType"/>
      <xs:element name="GreenTRC" type="wcs:OneDimensionLutType"/>
      <xs:element name="BlueTRC" type="wcs:OneDimensionLutType"/>
    </xs:sequence>
    <xs:attribute name="TRCLength" use="required">
      <xs:simpleType>
        <xs:restriction base="xs:int">
          <xs:minInclusive value="2" />
        </xs:restriction>
      </xs:simpleType>
    </xs:attribute>
  </xs:complexType>
```



## WCS Profile Schema Versioning

In this Appendix, the term "profile consumer" refers to the WCS software, or to a third-party software component that consumes WCS profiles.

Newer versions of profile consumers will be able to consume WCS profiles written according to older versions of the schemas. To take full advantage of features defined in the newest version of the schemas, the newest version of a profile consumer will generally be required. However, older profile consumers can consume profiles written according to newer versions of the schemas. The profile consumer can ignore XML elements and attributes that it does not understand. The results will be correct, but performance or fidelity may degraded as compared to the results achieved with the newest version of the profile consumer.

The following are versioning guidelines for profile consumers:

-   A given version of a profile consumer must recognize either all of the elements and attributes from a version namespace, or none of them.
-   If a profile consumer encounters an element or attribute from a namespace that it does not understand, it must treat this as an error condition, unless the profile contains explicit guidance on fallback processing.
-   The [Open Packaging Specification](https://www.microsoft.com/whdc/xps/xpspkg.mspx) defines an additional namespace URI, the markup compatibility namespace, which defines elements and attributes that provide this fallback processing guidance.
-   All versions of all profile consumers must recognize and respect all the elements and attributes in the markup compatibility namespace.
-   Profile consumers based on a new version of the profile schemas must support all previously defined version namespaces.

In the v1.0 release, WCS recognizes elements and attributes from the following namespaces:

-   `https://schemas.microsoft.com/windows/2005/02/color/ColorDeviceModel`
-   `https://schemas.microsoft.com/windows/2005/02/color/GamutMapModel`
-   `https://schemas.microsoft.com/windows/2005/02/color/ColorAppearanceModel`
-   `https://schemas.microsoft.com/winfx/2005/06/markup-compatibility`

The following demonstrates an example of markup compatibility.


```XML
<?xml version="1.0" encoding="utf-8" ?>
<ColorAppearanceModel
  xmlns=http://schemas.microsoft.com/windows/2005/02/color/ColorAppearanceModel
  xmlns:cam2=http://schemas.microsoft.com/windows/2007/08/color/ColorAppearanceModel
  xmlns:mc=http://schemas.microsoft.com/winfx/2005/02/markup-compatibility
  xs:schemaLocation="http://schemas.microsoft.com/windows/2005/02/color/ColorAppearanceModel ColorAppearanceModel.xsd"
  xmlns:xs='http://www.w3.org/2001/XMLSchema-instance'
  mc:Ignorable="cam2">

  <ProfileName>Default profile for ICC viewing conditions</ProfileName>
  <mc:AlternateContent>
    <mc:Choice Requires="cam2">
      <cam2:AudioDescription source="ProfileExplanation.wav"/>
    </mc:Choice>
    <mc:Fallback>
      <Description>Appropriate for a print in a D50 viewing booth</Description>
        </mc:Fallback>
  </mc:AlternateContent>
  <Author>Microsoft</Author>

  <ViewingConditions>
    <WhitePointName>D50</WhitePointName>
    <Background X="19.3" Y="20.0" Z="16.5" />
    <Surround>Average</Surround>
    <LuminanceOfAdaptingField>31.8</LuminanceOfAdaptingField>
    <DegreeOfAdaptation>-1</DegreeOfAdaptation>
    <cam2:Humidity>30%</cam2:Humidity>
  </ViewingConditions>

</ColorAppearanceModel>
```



## WCS Profile Localization

**Requirements**

WCS profiles contain certain elements such as ProfileName and Description which contain human-readable text. This text is localizable.

The following are versioning guidelines for profile creators:

-   For profiles created by 3rd parties such as printer manufacturers, the profile author should incorporate descriptive text in multiple languages.
-   The following elements should be localizable: 

    | Element     | CDMP | GMMP | CAMP |
    |-------------|------|------|------|
    | ProfileName | x    | x    | x    |
    | Description | x    | x    | x    |
    | Author      | x    | x    | x    |

    

     

### Expressing localizable elements

Instead of directly containing text, each localizable element contains one or more wcs:Text sub-elements, each of which must specify the xml:lang attribute. As described in the [XML specification](http://www.w3.org/TR/REC-xml/) Section 2.12 ("Language Identification"), the value of the xml:lang attribute must be an IETF RFC 3066 language identifier such as "en-US", "en", or "fr-FR". In WCS schemas, the value of the xml:lang attribute must not be the empty string "", even though XML allows this in the general case. For example:


```XML
<cdm:ColorDeviceModel ... />
    <cdm:Description>
        <wcs:Text xml:lang="en-US">Hello</wcs:Text>
        <wcs:Text xml:lang="fr-FR">Bonjour</wcs:Text>
    </cdm:Description>
    ...
</cdm:ColorDeviceeModel>
```



No two wcs:Text elements can have the same xml:lang attribute. Each WCS profile schema must enforce this constraint separately for each localizable element. Only UTF-8 and UTF-16 encodings are supported.

### Schema Support

The design makes use of the XSD types wcs:LocalizedText and wcs:MultiLocalizedType defined in the WCS Common Profile Type schema:


```XML
    <xs:complexType name="LocalizedText">
        <xs:simpleContent>
            <xs:extension base="xs:string">
                <xs:attribute name="xml:lang" type="xs:string" use="required"/>
            <xs:extension/>
        <xs:simpleContent/>
    </xs:complexType/>

    <xs:complexType name="MultiLocalizedType">
        <xs:element name="Text" type="cam:LocalizedText" minOccurs="1"/>
    </xs:complexType>
```



Each WCS profile schema declares each localizable element to be of type MultiLocalizedType, for example:


```XML
<xs:schema 
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:cdm="http://schemas.microsoft.com/windows/2005/02/color/ColorDeviceModel"
    xmlns:wcs="http://schemas.microsoft.com/windows/2005/02/color/WcsCommonProfileTypes"
    targetNamespace=
        "http://schemas.microsoft.com/windows/2005/02/color/ColorDeviceModel"
    version="1.0">
    <xs:import namespace=
        "http://schemas.microsoft.com/windows/2005/02/color/WcsCommonProfileTypes"/>

    <xs:element name="cdm:Description" type="wcs:MultiLocalizableType" minOccurs="0"/>

    <xs:unique name="uniqueDescriptionLanguage">
      <xs:selector xpath="cdm:ColorDeviceModel/cdm:Description/wcs:Text"/>
      <xs:field xpath="@xml:lang"/>
    </unique>

    ...
</xs:schema>
```



The CDMP schema enforces the constraint that each wcs:Text child of the cdm:Description element must have a unique xml:lang attribute. It enforces the same constraint for the other localizable elements. The CAMP and GMMP schemas do the same.

### Selecting the Language

When deciding which language version of a localizable element to display, application code should select the "closest version" to the "current language". What "closest version" and "current language" actually mean is platform-dependent; see below. If the profile does not contain a language version that matches the current language, the application should select the first version in the profile (the first wcs:Text child element of the localizable element).

On Windows Vista, the language selection is done as follows: Each thread has an associated list of "preferred UI languages", which can be obtained by calling [**GetThreadPreferredUILanguages**](/windows/win32/api/winnls/nf-winnls-getthreadpreferreduilanguages). The list is returned in order of user preference. For instance, on a system set up for US English, the list returned by **GetThreadPreferredUILanguages** is { "en-US", "en" }. This means: 1) US English if present. 2) Otherwise, use any regional variant of English, such as "en-GB" or just plain "en".

For each language in that list, in list order, the UI code looks for a wcs:Text element whose xml:lang attribute is an exact match. The first matching version is used. If no version matches, the first wcs:Text element is used.

### Built-in profiles

The standard WCS profiles shipped with Windows Vista, such as sRGB.cdmp, have the same localizable properties as other profiles.

The standard Windows solution would be to put the localized strings in a MUI DLL, and refer to them like this:


```XML
<cdm:Description resourceId="mscms.dll,-101">
    <wcs:Text xml:lang="en-US">Hello, world!</wcs:Text>
<cdm:Description>
```



On a Windows system, the description text would be extracted from resource ID 101 in the appropriate localized version of the MUI resources for mscms.dll. Non-Windows systems would use the wcs:Text sub-elements as described above.

We introduce an optional, globally unique ID attribute on the root element of each WCS profile schema. The standard profile wcsRGB.cdmp might look like this:


```XML
<cdm:ColorDeviceModel
    ID=http://schemas.microsoft.com/2005/02/color/profiles/wcsRGB.cdmp
    ... >
    <cdm:Description>
        <wcs:Text xml:lang="en-US">Hello.</wcs:Text>
        <wcs:Text xml:lang="fr-FR">Bonjour.</wcs:Text>
    </cdm:Description>
    ...
</cdm:ColorDeviceModel>
```



For the WCS color profiles shipped with windows, the Color CPL displays descriptive information from the resources, rather than from the wcs:Text elements in the profiles. This allows Windows to display localized information for these profiles in all supported languages, without requiring the profiles themlselves to contain descriptive information in all languages.

## Related topics

<dl> <dt>

[Basic color management concepts](basic-color-management-concepts.md)
</dt> <dt>

[Windows Color System Schemas and Algorithms](windows-color-system-schemas-and-algorithms.md)
</dt> </dl>

 

 
