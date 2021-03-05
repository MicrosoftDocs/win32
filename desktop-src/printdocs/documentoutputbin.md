---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 73840548-f68b-4af8-acb4-6f7faa2e8879
title: DocumentOutputBin
ms.topic: article
ms.date: 05/31/2018
---

# DocumentOutputBin

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

Describes the full list of supported bins for the device. Allows specification of output bin on a per document basis. The JobOutputBin, DocumentOutputBin and PageOutputBin keywords are mutually exclusive only one should be specified in a PrintTicket or Print Capabilities document.

-   [Element Information](#element-information)

-   [Structural Content](#structural-content)

-   [XML Content](#extensible-markup-language-xml-content)

## Element Information



| Name                       |                     |
|----------------------------|---------------------|
| Element Type <br/>   | Feature<br/>  |
| Scoping Prefix <br/> | Document<br/> |
| Notes <br/>          | None<br/>     |



 

## Structural Content

The XML structure of this element is:

``` syntax
<psf:Feature name="psk:DocumentOutputBin">
  <psf:Property name="psf:SelectionType">
    <psf:Value xsi:type="xs:string">psk:PickOne</psf:Value>
  </psf:Property>
  <psf:Option name="psk:_OptionName_">
    <psf:Property name="psf:IdentityOption">
      <psf:Value xsi:type="xs:string">_IdentityOptionValue_</psf:Value>
    </psf:Property>
    <psf:ScoredProperty name="psk:BinType">
      <psf:Value xsi:type="xs:string">_BinTypeValue_</psf:Value>
    </psf:ScoredProperty>
    <psf:ScoredProperty name="psk:MediaSheetCapacity">
      <psf:Value xsi:type="xs:integer">_MediaSheetCapacityValue_</psf:Value>
    </psf:ScoredProperty>
  </psf:Option>
</psf:Feature>
      
```

## Structure Variables

The following table outlines the characteristics of the variables defined in the XML structure.



| Name                                   | Data type          | Unit                  | Supported values                                                                                                                                                             | Summary                                                                             |
|----------------------------------------|--------------------|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| \_OptionName\_<br/>              | string<br/>  | characters<br/> | Valid fully qualified name as defined by https://www.w3.org/TR/1999/REC-xml-names-19990114/\#dt-qname. If no namespace is specified, default namespace is assumed.<br/> | The name of the option.<br/>                                                  |
| \_IdentityOptionValue\_<br/>     | string<br/>  | n/a<br/>        | True, False.<br/>                                                                                                                                                      | Defines an Option which when selected would disable this feature.<br/>        |
| \_BinTypeValue\_<br/>            | string<br/>  | n/a<br/>        | MailBox, Sorter, Stacker, Finisher, None.<br/>                                                                                                                         | Specifies the general type of the bin.<br/>                                   |
| \_MediaSheetCapacityValue\_<br/> | integer<br/> | sheets<br/>     | Greater than 0.<br/>                                                                                                                                                   | Specifies the Media capacity in number of pages (full level) of the bin.<br/> |



 

## Extensible Markup Language (XML) Content

The public Print Schema keywords are defined in the http://schemas.microsoft.com/windows/2003/08/printing/printschemakeywords namespace. The public Extensible Markup Language (XML) content for this keyword is defined below:

``` syntax
<psf:Feature name="psk:DocumentOutputBin">
  <psf:Property name="psf:SelectionType">
    <psf:Value xsi:type="xs:string">psk:PickOne</psf:Value>
  </psf:Property>
  <psf:Option>
    <!--Specifies type of output bin-->
    <psf:ScoredProperty name="psk:BinType">
      <psf:Value xsi:type="xs:string">_Undefined_</psf:Value>
    </psf:ScoredProperty>
    <!--Specifies media capacity for output bin-->
    <psf:ScoredProperty name="psk:MediaSheetCapacity">
      <psf:Value xsi:type="xs:integer">_Undefined_</psf:Value>
    </psf:ScoredProperty>
  </psf:Option>
</psf:Feature>    
```

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 




