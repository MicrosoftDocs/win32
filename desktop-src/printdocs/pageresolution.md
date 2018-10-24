---
Description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 88f9a9a3-520e-4044-9ab2-961de03878fa
title: PageResolution
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PageResolution

This topic is not current. For the most current information, see the [Print Schema Specification](http://go.microsoft.com/?linkid=7141496).

Defines the page resolution of printed output as either a qualitative value or as dots per inch, or both.

-   [Element Information](#element-information)
-   [Structural Content](#structural-content)
-   [Extensible Markup Language (XML) Content](#extensible-markup-language-xml-content)

## Element Information



| Name                       |                    |
|----------------------------|--------------------|
| Element Type <br/>   | Feature<br/> |
| Scoping Prefix <br/> | Page<br/>    |
| Notes <br/>          | None<br/>    |



 

## Structural Content

The XML structure of this element is:

``` syntax
<psf:Feature name="psk:PageResolution">
  <psf:Property name="psf:SelectionType">
    <psf:Value xsi:type="xs:string">psk:PickOne</psf:Value>
  </psf:Property>
  <psf:Option>
    <psf:Property name="psf:IdentityOption">
      <psf:Value xsi:type="xs:string">_IdentityOptionValue_</psf:Value>
    </psf:Property>
    <psf:ScoredProperty name="psk:ResolutionX">
      <psf:Value xsi:type="xs:integer">_ResolutionXValue_</psf:Value>
    </psf:ScoredProperty>
    <psf:ScoredProperty name="psk:ResolutionY">
      <psf:Value xsi:type="xs:integer">_ResolutionYValue_</psf:Value>
    </psf:ScoredProperty>
    <psf:ScoredProperty name="psk:QualitativeResolution">
      <psf:Value xsi:type="xs:string">_QualitativeResolutionValue_</psf:Value>
    </psf:ScoredProperty> 
  </psf:Option>
</psf:Feature>      
```

## Structure Variables

The following table outlines the characteristics of the variables defined in the XML structure.



| Name                                      | Data type          | Unit                  | Supported values                                                                                                                                                                      | Summary                                                                                                                                                          |
|-------------------------------------------|--------------------|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \_OptionName\_<br/>                 | string<br/>  | characters<br/> | Valid fully qualified name as defined by [Namespaces in XML](http://go.microsoft.com/fwlink/p/?linkid=200944). If no namespace is specified, default namespace is assumed.<br/> | The name of the option.<br/>                                                                                                                               |
| \_IdentityOptionValue\_<br/>        | string<br/>  | n/a<br/>        | True, False.<br/>                                                                                                                                                               | Defines an Option which when selected would disable this feature.<br/>                                                                                     |
| \_ResolutionXValue\_<br/>           | integer<br/> | DPI<br/>        | Greater than 0.<br/>                                                                                                                                                            | Specifies the x component of the resolution relative to the PageImageableSize in DPI (relative to the PageMediaSize and feed direction of the media).<br/> |
| \_ResolutionYValue\_<br/>           | integer<br/> | DPI<br/>        | Greater than 0.<br/>                                                                                                                                                            | Specifies the y component of the resolution relative to the PageImageableSize in DPI (relative to the PageMediaSize and feed direction of the media).<br/> |
| \_QualitativeResolutionValue\_<br/> | string<br/>  | n/a<br/>        | Default, Draft, High, Normal, Other.<br/>                                                                                                                                       | Specifies a quality label for the resolution.<br/>                                                                                                         |



 

## Extensible Markup Language (XML) Content

The public Print Schema keywords are defined in the http://schemas.microsoft.com/windows/2003/08/printing/printschemakeywords namespace. The public Extensible Markup Language (XML) content for this keyword is defined below:

``` syntax
<psf:Feature name="psk:PageResolution">
  <psf:Property name="psf:SelectionType">
    <psf:Value xsi:type="xs:string">psk:PickOne</psf:Value>
  </psf:Property>
  <psf:Option>
    <!-- The horizontal resolution in dots per inch -->
    <psf:ScoredProperty name="psk:ResolutionX">
      <psf:Value xsi:type="xs:integer">_Undefined_</psf:Value>
    </psf:ScoredProperty>
    <!-- The vertical resolution in dots per inch -->
    <psf:ScoredProperty name="psk:ResolutionY">
      <psf:Value xsi:type="xs:integer">_Undefined_</psf:Value>
    </psf:ScoredProperty>
    <!-- Value representing the resolution -->
    <psf:ScoredProperty name="psk:QualitativeResolution">
      <psf:Value xsi:type="xs:string">Other</psf:Value>
    </psf:ScoredProperty>
  </psf:Option>
</psf:Feature>    
```

## Related topics

<dl> <dt>

[Print Schema Specification](http://go.microsoft.com/?linkid=7141496)
</dt> </dl>

 

 




