---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 05924c7d-e074-4835-b42c-53c77dc1bbb5
title: PageBlendColorSpaceICCProfileURI
ms.topic: article
ms.date: 05/31/2018
---

# PageBlendColorSpaceICCProfileURI

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

Specifies a relative URI reference to an ICC profile defining the color space that SHOULD be used for blending. The <Uri> is an absolute part\_name relative to the package root.

-   [Element Information](#element-information)
-   [Structure Content](#structure-content)

## Element Information



| Name | Value |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Element Type <br/>   | ParameterDef<br/>                                                                                                                |
| Scoping Prefix <br/> | Page<br/>                                                                                                                        |
| Notes <br/>          | This applies to XPS Documents only and should not be used in arbitrary PrintTickets. Linked to PageBlendColorSpace element.<br/> |



 

## Structure Content

The XML structure of this element is:

``` syntax
<psf:ParameterDef name="psk:PageBlendColorSpaceICCProfileURI">
  <psf:Property name="psf:DataType">
    <psf:Value xsi:type="xs:string">xs:string</psf:Value>
  </psf:Property>
  <psf:Property name="psf:DefaultValue">
    <psf:Value xsi:type="xs:string">_Undefined_</psf:Value>
  </psf:Property>
  <psf:Property name="psf:MaxLength">
    <psf:Value xsi:type="xs:integer">_Undefined_</psf:Value>
  </psf:Property>
  <psf:Property name="psf:MinLength">
    <psf:Value xsi:type="xs:integer">1</psf:Value>
  </psf:Property>
  <psf:Property name="psf:Mandatory">
    <psf:Value xsi:type="xs:string">psk:Conditional</psf:Value>
  </psf:Property>
  <psf:Property name="psf:UnitType">
    <psf:Value xsi:type="xs:string">characters</psf:Value>
  </psf:Property>
</psf:ParameterDef>
```

## Structure Properties

The following table outlines the characteristics of the variables defined in the XML structure.



| Property                | xsi:type           | Value                      |
|-------------------------|--------------------|----------------------------|
| DataType<br/>     | string<br/>  | xs:string<br/>       |
| DefaultValue<br/> | string<br/>  | undefined<br/>       |
| MaxLength<br/>    | integer<br/> | undefined<br/>       |
| MinLength<br/>    | integer<br/> | 1<br/>               |
| Mandatory<br/>    | string<br/>  | psk:Conditional<br/> |
| UnitType<br/>     | string<br/>  | characters<br/>      |



 

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 




