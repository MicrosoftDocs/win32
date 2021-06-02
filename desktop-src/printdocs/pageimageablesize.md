---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 6b81814f-2d9e-4862-8633-6ba016c11dac
title: PageImageableSize
ms.topic: article
ms.date: 05/31/2018
---

# PageImageableSize

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

Describes the imaged canvas for layout and rendering. This will be reported based on PageMediaSize and PageOrientation.

The following diagrams illustrate the PageImageableSize variables usage based on PageOrientation.

![a diagram that shows page measurements](images/local-1641910626-image.png)

-   [Element Information](#element-information)
-   [Structural Content](#structural-content)
-   [Extensible Markup Language (XML) Content](#extensible-markup-language-xml-content)

## Element Information



|                            |                     |
|----------------------------|---------------------|
| Name | Value |
| Element Type<br/>    | Property<br/> |
| Scoping Prefix <br/> | Page<br/>     |
| Notes <br/>          | None<br/>     |



 

## Structural Content

The XML structure of this element is:

``` syntax
<psf:Property name="psk:PageImageableSize">
  <psf:Property name="psk:ImageableSizeWidth">
    <psf:Value xsi:type="xs:integer">_ImageableSizeWidthValue_</psf:Value>
  </psf:Property>
  <psf:Property name="psk:ImageableSizeHeight">
    <psf:Value xsi:type="xs:integer">_ImageableSizeHeightValue_</psf:Value>
  </psf:Property>
  <!--Specifies the imageable area within the logical page.  -->
  <psf:Property name="psk:ImageableArea">
    <psf:Property name="psk:OriginWidth">
      <psf:Value xsi:type="xs:integer">_OriginWidthValue_</psf:Value>
    </psf:Property>
    <psf:Property name="psk:OriginHeight">
      <psf:Value xsi:type="xs:integer">_OriginHeightValue_</psf:Value>
    </psf:Property>
    <psf:Property name="psk:ExtentWidth">
      <psf:Value xsi:type="xs:integer">_ExtentWidthValue_</psf:Value>
    </psf:Property>
    <psf:Property name="psk:ExtentHeight">
      <psf:Value xsi:type="xs:integer">_ExtentHeightValue_</psf:Value>
    </psf:Property>
  </psf:Property>
</psf:Property>
```

## Structure Variables

The following table outlines the characteristics of the variables defined in the XML structure.



| Name                                    | Data type          | Unit               | Supported values                       | Summary                                                                                                                    |
|-----------------------------------------|--------------------|--------------------|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| \_ImageableSizeWidthValue\_<br/>  | integer<br/> | microns<br/> | Greater than 0.<br/>             | Specifies the horizontal dimension of the application media size relative to the PageOrientation.<br/>               |
| \_ImageableSizeHeightValue\_<br/> | integer<br/> | microns<br/> | Greater than 0.<br/>             | Specifies the vertical dimension of the application media size relative to the PageOrientation.<br/>                 |
| \_OriginWidthValue\_<br/>         | integer<br/> | microns<br/> | Greater than or equal to 0.<br/> | Specifies the horizontal origin of the imageable area relative to the application media size.<br/>                   |
| \_OriginHeightValue\_<br/>        | integer<br/> | microns<br/> | Greater than or equal to 0.<br/> | Specifies the vertical origin of the imageable area relative to the application media size.<br/>                     |
| \_ExtentWidthValue\_<br/>         | integer<br/> | microns<br/> | Greater than 0.<br/>             | Specifies the horizontal distance between the origin and the bounding limit of the application media size.<br/>      |
| \_ExtentHeightValue\_<br/>        | integer<br/> | microns<br/> | Greater than 0.<br/>             | Specifies the vertical distance between the origin and the bounding limit of the canvas application media size.<br/> |



 

## Extensible Markup Language (XML) Content

The public Print Schema keywords are defined in the https://schemas.microsoft.com/windows/2003/08/printing/printschemakeywords namespace. The public Extensible Markup Language (XML) content for this keyword is defined below:

``` syntax
<psf:Property name="psk:PageImageableSize">
  <psf:Property name="psk:ImageableSizeWidth">
    <psf:Value xsi:type="xs:integer">_Undefined_</psf:Value>
  </psf:Property>
  <psf:Property name="psk:ImageableSizeHeight">
    <psf:Value xsi:type="xs:integer">_Undefined_</psf:Value>
  </psf:Property>
    <psf:Property name="psk:ImageableArea">
      <psf:Property name="psk:OriginWidth">
        <psf:Value xsi:type="xs:integer">_Undefined_</psf:Value>
      </psf:Property>
    <psf:Property name="psk:OriginHeight">
      <psf:Value xsi:type="xs:integer">_Undefined_</psf:Value>
    </psf:Property>
    <psf:Property name="psk:ExtentWidth">
      <psf:Value xsi:type="xs:integer">_Undefined_</psf:Value>
    </psf:Property>
    <psf:Property name="psk:ExtentHeight">
      <psf:Value xsi:type="xs:integer">_Undefined_</psf:Value>
    </psf:Property>
  </psf:Property>
</psf:Property>
  
```

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 




