---
Description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 1e7b0681-a29b-4fd6-8518-dc9d0b716b12
title: JobName
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# JobName

This topic is not current. For the most current information, see the [Print Schema Specification](http://go.microsoft.com/?linkid=7141496).

Specifies a descriptive name for the job.

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

The XML structure of this element is as follows:

``` syntax
<psf:Property name="psk:JobName">
    <psf:Value xsi:type="xs:string">_JobNameValue_</psf:Value>
</psf:Property>
```

## Structure Variables

The following table outlines the characteristics of the variables defined in the XML structure.



| Name                        | Data type         | Unit | Supported values | Summary |
|-----------------------------|-------------------|------|------------------|---------|
| \_JobNameValue\_<br/> | string<br/> |      |                  |         |



 

## Extensible Markup Language (XML) Content

``` syntax
<psf:Property name="psk:JobName">
    <psf:Value xsi:type="xs:string"></psf:Value> <!-- undefined -->
</psf:Property>
```

## Related topics

<dl> <dt>

[Print Schema Specification](http://go.microsoft.com/?linkid=7141496)
</dt> </dl>

 

 




