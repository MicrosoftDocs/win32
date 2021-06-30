---
description: Learn about the JobDuplexAllDocumentsContiguously element, which describes the duplex characteristics of the output.
ms.assetid: dd24166c-d5e2-420e-8a8c-e1a25728ab2f
title: JobDuplexAllDocumentsContiguously
ms.topic: article
ms.date: 05/31/2018
---

# JobDuplexAllDocumentsContiguously

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

Describes the duplex characteristics of the output. The duplex feature allows for printing on both sides of the media. All Documents in the job are duplexed together contiguously. JobDuplexAllDocumentsContiguously and DocumentDuplex are mutually exclusive. It is up to the driver to determine constraint handling between these keywords.

-   [Element Information](#element-information)
-   [Structural Content](#structural-content)
-   [Extensible Markup Language (XML) Content](#extensible-markup-language-xml-content)

## Element Information



| Name | Value |
|----------------------------|--------------------|
| Element Type <br/>   | Feature<br/> |
| Scoping Prefix <br/> | Job<br/>     |
| Notes <br/>          | None<br/>    |



 

## Structural Content

The XML structure of this element is:

``` syntax
<psf:Feature name="psk:JobDuplexAllDocumentsContiguously">
  <psf:Property name="psf:SelectionType">
    <psf:Value xsi:type="xs:string">psk:PickOne</psf:Value>
  </psf:Property>
  <psf:Option name="psk:_OptionName_">
    <psf:Property name="psf:IdentityOption">
      <psf:Value xsi:type="xs:string">_IdentityOptionValue_</psf:Value>
    </psf:Property>
    <psf:ScoredProperty name="psk:DuplexMode">
      <psf:Value xsi:type="xs:string">_DuplexModeValue_</psf:Value>
    </psf:ScoredProperty>
  </psf:Option>
</psf:Feature>      
```

## Structure Variables

The following table outlines the characteristics of the variables defined in the XML structure.



| Name                               | Data type         | Unit                  | Supported values                                                                                                                                                             | Summary                                                                                                                                |
|------------------------------------|-------------------|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| \_OptionName\_<br/>          | string<br/> | characters<br/> | Valid fully qualified name as defined by https://www.w3.org/TR/1999/REC-xml-names-19990114/\#dt-qname. If no namespace is specified, default namespace is assumed.<br/> | The name of the option.<br/>                                                                                                     |
| \_IdentityOptionValue\_<br/> | string<br/> | n/a<br/>        | True, False.<br/>                                                                                                                                                      | Defines an Option which when selected would disable this feature.<br/>                                                           |
| \_DuplexModeValue\_<br/>     | string<br/> | n/a<br/>        | Automatic, Manual.<br/>                                                                                                                                                | Defines the duplex mode. Automatic duplex is performed by hardware. Manual duplexing is performed by software and the user.<br/> |



 

## Extensible Markup Language (XML) Content

The public Print Schema keywords are defined in the https://schemas.microsoft.com/windows/2003/08/printing/printschemakeywords namespace. The public Extensible Markup Language (XML) content for this keyword is defined below:

``` syntax
<psf:Feature name="psk:JobDuplexAllDocumentsContiguously">
  <psf:Property name="psf:SelectionType">
    <psf:Value xsi:type="xs:string">psk:PickOne</psf:Value>
  </psf:Property>
  <!-- Specifies one sided printing. -->
  <psf:Option name="psk:OneSided" />
  <!-- Specifies two sided printing such that the page is flipped parallel to the MediaSizeWidth direction. -->
  <psf:Option name="psk:TwoSidedShortEdge">
    <psf:ScoredProperty name="psk:DuplexMode">
      <psf:Value xsi:type="xs:string">_Undefined_</psf:Value>
    </psf:ScoredProperty>
  </psf:Option>
  <!-- Specifies two sided printing such that the page is flipped parallel to the MediaSizeHeight direction. -->
  <psf:Option name="psk:TwoSidedLongEdge">
    <psf:ScoredProperty name="psk:DuplexMode">
      <psf:Value xsi:type="xs:string">_Undefined_</psf:Value>
    </psf:ScoredProperty>
  </psf:Option>
</psf:Feature>    
```

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 




