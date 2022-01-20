---
title: SVG Support
description: Beginning in Windows 10 Anniversary Update, Direct2D supports rendering color fonts that contain SVG glyph outlines, as described in the OpenType specification (see the ‘SVG ’ table).
ms.assetid: 5cb4cb7c-9b96-e110-bff9-d75ad1980010
ms.topic: article
ms.date: 05/31/2018
---

# SVG Support

Beginning in Windows 10 Anniversary Update, Direct2D supports rendering [color fonts](../directwrite/color-fonts.md) that contain SVG glyph outlines, as described in the [OpenType specification](/typography/opentype/spec/) (see [The SVG table](/typography/opentype/spec/svg)). Beginning in Windows 10 Creators Update, Direct2D also supports rendering standalone SVG images. However, certain SVG features are disallowed within OpenType SVG fonts, and certain SVG features are currently unsupported by Direct2D.  

This topic identifies the set of [SVG 1.1](https://www.w3.org/TR/SVG11/) features supported by Direct2D in Windows 10 Anniversary Update and newer. This document applies to SVG in OpenType fonts as well as standalone SVG images.

## Supported SVG elements and attributes

Direct2D supports rendering the following SVG elements and the associated attributes for each element. Other elements and regular attributes are ignored.



| Element                                                                                  | Supported regular attributes                                                             |
|------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [circle](https://www.w3.org/TR/SVG11/shapes.mdl#circleelement)                           | id, style, transform, cx, cy, r                                                          |
| [clipPath](https://www.w3.org/TR/SVG11/masking.mdl#clippathelement)                      | id, style, transform, clipPathUnits                                                      |
| [defs](https://www.w3.org/TR/SVG11/struct.mdl#defselement)                               | id, style, transform                                                                     |
| [desc](https://www.w3.org/TR/SVG11/struct.mdl#descriptionandtitleelements)<sup>\*</sup>  | id                                                                                       |
| [ellipse](https://www.w3.org/TR/SVG11/shapes.mdl#ellipseelement)                         | id, style, transform, cx, cy, rx, ry                                                     |
| [g](https://www.w3.org/TR/SVG11/struct.mdl#gelement)                                     | id, style, transform                                                                     |
| [image](https://www.w3.org/TR/SVG11/struct.mdl#imageelement)                             | id, style, transform, x, y, width, height, preserveAspectRatio, xlink:href               |
| [line](https://www.w3.org/TR/SVG11/shapes.mdl#lineelement)                               | id, style, transform, x1, y1, x2, y2                                                     |
| [linearGradient](https://www.w3.org/TR/SVG11/pservers.mdl#lineargradientelement)         | id, style, x1, y1, x2, y2, gradientUnits, gradientTransform, spreadMethod, xlink:href    |
| [path](https://www.w3.org/TR/SVG11/paths.html#PathElement)                                | id, style, transform, d                                                                  |
| [polygon](https://www.w3.org/TR/SVG11/shapes.mdl#polygonelement)                         | id, style, transform, points                                                             |
| [polyline](https://www.w3.org/TR/SVG11/shapes.mdl#polylineelement)                       | id, style, transform, points                                                             |
| [radialGradient](https://www.w3.org/TR/SVG11/pservers.mdl#radialgradientelement)         | id, style, cx, cy, r, fx, fy, gradientUnits, gradientTransform, spreadMethod, xlink:href |
| [rect](https://www.w3.org/TR/SVG11/shapes.mdl#rectelement)                               | id, style, transform, x, y, width, height, rx, ry                                        |
| [stop](https://www.w3.org/TR/SVG11/pservers.mdl#stopelement)                             | id, style, offset                                                                        |
| [svg](https://www.w3.org/TR/SVG11/struct.mdl#svgelement)                                 | id, style, x, y, width, height, viewBox, preserveAspectRatio                             |
| [title](https://www.w3.org/TR/SVG11/struct.mdl#descriptionandtitleelements)<sup>\*</sup> | id                                                                                       |
| [use](https://www.w3.org/TR/SVG11/struct.mdl#useelement)                                 | id, style, transform, x, y, width, height, xlink:href                                    |



 

<sup>\*</sup> Only supported in Windows 10 Creators Update and newer

## Supported SVG presentation attributes

Direct2D also supports the following presentation attributes. These can be specified on any SVG elements, but they only affect the appearance of certain elements as described in the SVG specification (see [Presentation attributes](https://www.w3.org/TR/SVG11/attindex.mdl#presentationattributes)).

-   clip-path
-   clip-rule
-   color
-   display<sup>\*</sup>
-   fill
-   fill-opacity
-   fill-rule
-   opacity
-   overflow
-   stop-color
-   stop-opacity
-   stroke
-   stroke-dasharray
-   stroke-dashoffset
-   stroke-linecap
-   stroke-linejoin
-   stroke-miterlimit
-   stroke-opacity
-   stroke-width
-   visibility<sup>\*</sup>

<sup>\*</sup> Only supported in Windows 10 Creators Update and newer

## Unsupported SVG features

### Unsupported elements and attributes

Any element or attribute not included in the above lists is considered unsupported by Direct2D. When parsing SVG content that contains an unsupported element or attribute, the unsupported entity is ignored. The remainder of the content is rendered as faithfully as possible.

### Unsupported length units

As of Windows 10 Anniversary Update, Direct2D only supports user-space length values and percentage length values. Lengths with unit suffixes, like “mm” or “em,” are unsupported.

Starting in Windows 10 Fall Creators Update, Direct2D also supports absolute unit identifiers: px, pt, pc, cm, mm, and in. Relative unit identifiers (em, ex) are not supported.

### Unsupported image sources

The image element is only supported if its xlink:href attribute is set to a base64-encoded image. Remote references are not supported.

 

 
