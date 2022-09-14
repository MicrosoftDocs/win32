---
description: Learn about the PageSourceColorProfile element. This element defines the characteristics of the source color profile.
ms.assetid: aa4f5425-6ca1-4820-b15d-bbead1f6d735
title: PageSourceColorProfile
ms.topic: article
ms.date: 05/31/2018
---

# PageSourceColorProfile

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

Defines the characteristics of the source color profile.

-   [Element Information](#element-information)
-   [Structural Content](#structural-content)
-   [Extensible Markup Language (XML) Content](#extensible-markup-language-xml-content)

## Element Information



| Name                       | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Element Type <br/>   | Feature<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Scoping Prefix <br/> | Page<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Notes <br/>          | XPS-compliant consumers MUST enforce that a URI reference to a resource such as an image or color profile in either a Print Capabilities document or PrintTicket MUST refer to a part name (a relative URI to the package root) within the same XPS Document package that contains the resultant PrintTicket. A compliant XPS consumer MUST NOT use a URI that is not compliant with the part name syntax. These settings are XPS specific. <br/> URIs which are referenced in either a Print Capabilities document or PrintTicket MUST NOT be resolved as URLs. This is unsafe as they may not resolve as intended and may create harmful security risks for the driver and operating system.<br/> |



 

## Structural Content

The XML structure of this element is:

``` syntax
<psf:Feature name="psk:PageSourceColorProfile">
  <psf:Property name="psf:SelectionType">
    <psf:Value xsi:type="xs:string">psk:PickOne</psf:Value>
  </psf:Property>
  <psf:Option name="psk:_OptionName_">
    <psf:Property name="psf:IdentityOption">
      <psf:Value xsi:type="xs:string">_IdentityOptionValue_</psf:Value>
    </psf:Property>
  </psf:Option>
</psf:Feature>
```

## Structure Variables

The following table outlines the characteristics of the variables defined in the XML structure.



| Name                               | Data type         | Unit                  | Supported values                                                                                                                                                                      | Summary                                                                      |
|------------------------------------|-------------------|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| \_OptionName\_<br/>          | string<br/> | characters<br/> | Valid fully qualified name as defined by [Namespaces in XML](https://www.w3.org/TR/1999/REC-xml-names-19990114/). If no namespace is specified, default namespace is assumed.<br/> | The name of the option.<br/>                                           |
| \_IdentityOptionValue\_<br/> | string<br/> | n/a<br/>        | True, False.<br/>                                                                                                                                                               | Defines an Option which when selected would disable this feature.<br/> |



 

## Extensible Markup Language (XML) Content

The public Print Schema keywords are defined in the https://schemas.microsoft.com/windows/2003/08/printing/printschemakeywords namespace. The public Extensible Markup Language (XML) content for this keyword is defined below:

``` syntax
<psf:Feature name="psk:PageSourceColorProfile">
  <psf:Option name="psk:RGB">
    <!-- Source profile used to perform color management for untagged RGB data. -->
    <psf:ScoredProperty name="psk:SourceColorProfileURI">
      <psf:ParameterRef name="psk:PageSourceColorProfileURI" />
    </psf:ScoredProperty>
    <psf:ScoredProperty name="psk:SourceColorProfileEmbedded">
      <psf:ParameterRef name="psk:PageSourceColorProfileEmbedded" />
    </psf:ScoredProperty>
  </psf:Option>
  <psf:Option name="psk:CMYK">
    <!-- Source profile used to perform color management for untagged CMYK data. -->
    <psf:ScoredProperty name="psk:SourceColorProfileURI">
      <psf:ParameterRef name="psk:PageSourceColorProfileURI" />
    </psf:ScoredProperty>
    <psf:ScoredProperty name="psk:SourceColorProfileEmbedded">
      <psf:ParameterRef name="psk:PageSourceColorProfileEmbedded" />
    </psf:ScoredProperty>
  </psf:Option>
  <psf:Option name="psk:None" />
</psf:Feature>
```

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 




