---
Description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: f0b2192d-4bb7-4ba2-8dd0-35a20183ea31
title: DocumentSeparatorSheet
ms.topic: article
ms.date: 05/31/2018
---

# DocumentSeparatorSheet

This topic is not current. For the most current information, see the [Print Schema Specification](http://go.microsoft.com/?linkid=7141496).

Describes the separator sheet usage for a document. Separator sheets should appear in the output as indicated by the Option specified below.

-   [Element Information](#element-information)
-   [Structural Content](#structural-content)
-   [Extensible Markup Language (XML) Content](#extensible-markup-language-xml-content)

## Element Information



| Name                       |                     |
|----------------------------|---------------------|
| Element Type <br/>   | Feature<br/>  |
| Scoping Prefix <br/> | Document<br/> |
| Notes <br/>          | None<br/>     |



 

## Structural Content

The XML structure of this element is:

``` syntax
<psf:Feature name="psk:DocumentSeparatorSheet">
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
| \_OptionName\_<br/>          | string<br/> | characters<br/> | Valid fully qualified name as defined by [Namespaces in XML](http://go.microsoft.com/fwlink/p/?linkid=200944). If no namespace is specified, default namespace is assumed.<br/> | The name of the option.<br/>                                           |
| \_IdentityOptionValue\_<br/> | string<br/> | n/a<br/>        | True, False.<br/>                                                                                                                                                               | Defines an Option which when selected would disable this feature.<br/> |



 

## Extensible Markup Language (XML) Content

The public Print Schema keywords are defined in the http://schemas.microsoft.com/windows/2003/08/printing/printschemakeywords namespace. The public Extensible Markup Language (XML) content for this keyword is defined below:

``` syntax
<psf:Feature name="psk:DocumentSeparatorSheet">
  <psf:Property name="psf:SelectionType">
    <psf:Value xsi:type="xs:string">psk:PickOne</psf:Value>
  </psf:Property>
  <!-- Specifies a separator sheet at the start and end of the document. -->
  <psf:Option name="psk:BothSheets" />
  <!-- Specifies a separator sheet at the end of the document. -->
  <psf:Option name="psk:EndSheet" />
  <!-- Specifies no separator sheet(s). -->
  <psf:Option name="psk:None" />
  <!-- Specifies a separator sheet at the start of the document. -->
  <psf:Option name="psk:StartSheet" />
</psf:Feature>
    
```

## Related topics

<dl> <dt>

[Print Schema Specification](http://go.microsoft.com/?linkid=7141496)
</dt> </dl>

 

 




