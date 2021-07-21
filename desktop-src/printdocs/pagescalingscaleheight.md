---
description: Get information about the PageScalingScaleHeight parameter. This topic isn't current. For the most current information, see the Print Schema Specification.
ms.assetid: ccc2ad1c-b0c2-4c45-bc95-7c15426c2534
title: PageScalingScaleHeight
ms.topic: article
ms.date: 05/31/2018
---

# PageScalingScaleHeight

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

Specifies the scaling factor in the ImageableSizeHeight direction for custom scaling.

-   [Element Information](#element-information)
-   [Structure Content](#structure-content)

## Element Information



| Name | Value |
|----------------------------|---------------------------------------------------------|
| Element Type <br/>   | ParameterDef<br/>                                 |
| Scoping Prefix <br/> | Page<br/>                                         |
| Notes <br/>          | Linked to PageScaling element, Custom option<br/> |



 

## Structure Content

The XML structure of this element is:

``` syntax
<psf:ParameterDef name="psk:PageScalingScaleHeight">
  <psf:Property name="psf:DataType">
    <psf:Value xsi:type="xs:string">xs:integer</psf:Value>
  </psf:Property>
  <psf:Property name="psf:DefaultValue">
    <psf:Value xsi:type="xs:integer">_Undefined_</psf:Value>
  </psf:Property>
  <psf:Property name="psf:MaxValue">
    <psf:Value xsi:type="xs:integer">_Undefined_</psf:Value>
  </psf:Property>
  <psf:Property name="psf:MinValue">
    <psf:Value xsi:type="xs:integer">1</psf:Value>
  </psf:Property>
  <psf:Property name="psf:Multiple">
    <psf:Value xsi:type="xs:integer">1</psf:Value>
  </psf:Property>
  <psf:Property name="psf:Mandatory">
    <psf:Value xsi:type="xs:string">psk:Conditional</psf:Value>
  </psf:Property>
  <psf:Property name="psf:UnitType">
    <psf:Value xsi:type="xs:string">percent</psf:Value>
  </psf:Property>
</psf:ParameterDef>
      
```

## Structure Properties

The following table outlines the characteristics of the variables defined in the XML structure.



| Property                | xsi:type           | Value                      |
|-------------------------|--------------------|----------------------------|
| DataType<br/>     | String<br/>  | xs:integer<br/>      |
| DefaultValue<br/> | Integer<br/> | undefined<br/>       |
| MaxValue<br/>     | Integer<br/> | undefined<br/>       |
| MinValue<br/>     | Integer<br/> | 1<br/>               |
| Mandatory<br/>    | String<br/>  | psk:Conditional<br/> |
| Multiple<br/>     | Integer<br/> | 1<br/>               |
| UnitType<br/>     | String<br/>  | percent<br/>         |



 

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 




