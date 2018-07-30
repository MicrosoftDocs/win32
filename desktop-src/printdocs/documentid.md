---
Description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 6e7899e3-9b64-48bd-8683-aba627458f2a
title: DocumentID
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DocumentID

This topic is not current. For the most current information, see the [Print Schema Specification](http://go.microsoft.com/?linkid=7141496).

Specifies a unique ID for the document.

-   [Element Information](#element-information)
-   [Structural Content](#structural-content)
-   [Extensible Markup Language (XML) Content](#extensible-markup-language-xml-content)

## Element Information



| Name                       |                     |
|----------------------------|---------------------|
| Element Type <br/>   | Property<br/> |
| Scoping Prefix <br/> | Document<br/> |
| Notes <br/>          | None<br/>     |



 

## Structural Content

The XML structure of this element is as follows:

``` syntax
<psf:Property name="psk:DocumentID">
    <psf:Value xsi:type="xs:string">_DocumentIDValue_</psf:Value>
</psf:Property>
```

## Structure Variables

The following table outlines the characteristics of the variables defined in the XML structure.



| Name                           | Data type         | Unit | Supported values | Summary |
|--------------------------------|-------------------|------|------------------|---------|
| \_DocumentIDValue\_<br/> | string<br/> |      |                  |         |



 

## Extensible Markup Language (XML) Content

``` syntax
<psf:Property name="psk:DocumentID">
    <psf:Value xsi:type="xs:string"></psf:Value> <!-- undefined -->
</psf:Property>
```

## Related topics

<dl> <dt>

[Print Schema Specification](http://go.microsoft.com/?linkid=7141496)
</dt> </dl>

 

 




