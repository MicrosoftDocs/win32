---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 70790dc2-180a-4e04-91a9-a10ee76c836b
title: JobOptimalDestinationColorProfile
ms.topic: article
ms.date: 05/31/2018
---

# JobOptimalDestinationColorProfile

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

Specifies the optimal color profile given the current device configuration.

-   [Element Information](#element-information)
-   [Structural Content](#structural-content)
-   [Extensible Markup Language (XML) Content](#extensible-markup-language-xml-content)

## Element Information



| Name                       |                     |
|----------------------------|---------------------|
| Element Type <br/>   | Property<br/> |
| Scoping Prefix <br/> | Job<br/>      |
| Notes <br/>          | None<br/>     |



 

## Structural Content

The XML structure of this element is:

``` syntax
<psf:Property name="psk:JobOptimalDestinationColorProfile">
  <psf:Property name="psk:Profile">
    <psf:Value xsi:type="xs:string">_ProfileValue_</psf:Value>
    <psf:Property name="psk:ProfileData">
      <psf:Value xsi:type="xs:string">_ProfileDataValue_</psf:Value>
    </psf:Property>
    <psf:Property name="psk:Path">
      <psf:Value xsi:type="xs:string">_PathValue_</psf:Value>
    </psf:Property>
  </psf:Property>
</psf:Property>
```

## Structure Variables

The following table outlines the characteristics of the variables defined in the XML structure.



| Name                            | Data type         | Unit           | Supported values          | Summary                                        |
|---------------------------------|-------------------|----------------|---------------------------|------------------------------------------------|
| \_ProfileValue\_<br/>     | string<br/> | n/a<br/> | RGB, ICC, CMYK<br/> | Specifies the color profile.<br/>        |
| \_PathValue\_<br/>        | string<br/> | n/a<br/> | n/a<br/>            | Specifies file path to the profile.<br/> |
| \_ProfileDataValue\_<br/> | string<br/> | n/a<br/> | n/a<br/>            | Contains profile data content.<br/>      |



 

## Extensible Markup Language (XML) Content

The public Print Schema keywords are defined in the http://schemas.microsoft.com/windows/2003/08/printing/printschemakeywords namespace. The public Extensible Markup Language (XML) content for this keyword is defined below:

``` syntax
 <psf:Property name="psk:JobOptimalDestinationColorProfile">
  <psf:Property name="psk:Profile">
    <psf:Value xsi:type="xs:string">_Undefined_</psf:Value>
    <psf:Property name="psk:ProfileData">
      <psf:Value xsi:type="xs:string">_Undefined_</psf:Value>
    </psf:Property>
    <psf:Property name="psk:Path">
      <psf:Value xsi:type="xs:string">_Undefined_</psf:Value>
    </psf:Property>
  </psf:Property>
</psf:Property>
```

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 




