---
title: VML Object Model Reference
description: This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.
ms.assetid: 68a84c68-3aac-4971-9611-45f52e057708
ms.topic: article
ms.date: 05/31/2018
---

# VML Object Model Reference

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

In this topic:

-   [Introduction](#introduction)
-   [Example](#example)
-   [Setting up VML](#setting-up-vml)
-   [VML OM Reference](#vml-om-reference)
    -   [Shape element](#shape-element)
-   [Subelements of the Shape Element](#subelements-of-the-shape-element)
    -   [Background element](#background-element)
    -   [Extrusion element](#extrusion-element)
    -   [Fill element](#fill-element)
    -   [Group element](#group-element)
    -   [Imagedata element](#imagedata-element)
    -   [Path element](#path-element)
    -   [Shadow element](#shadow-element)
    -   [Skew element](#skew-element)
    -   [Stroke element](#stroke-element)
    -   [TextPath element](#textpath-element)
-   [Data Types Used in the VML Object Model](#data-types-used-in-the-vml-object-model)

## Introduction

[Vector Markup Language (VML)](https://www.w3.org/TR/NOTE-datetime.html) is a text-based language that uses [XML](https://www.w3.org/TR/REC-xml.mdl) to extend HTML for the purpose of displaying vector graphic information. The VML Document Object Model (DOM) defines a programmatic interface for the manipulation of the document elements. This enables the user to dynamically create and modify vector graphics through a platform- and language-neutral interface. The VML DOM conforms to the [Document Object Model](https://www.w3.org/TR/REC-DOM-Level-1/) specification.

VML uses the [Shape](#shape-element) element as the basic building block for vector graphic images. Once a shape is created, you can modify the shape through attributes or by attached subelements. For example, to change the color of a shape, assign a color value to the **FillColor** attribute.


```HTML
myshape.fillcolor = "red"
```



Several of the attributes of a shape are also [subelements](/windows) and have their own attributes, including the following:

-   [Background](#background-element)
-   [Extrusion](#extrusion-element)
-   [Fill](#fill-element)
-   [Group](#group-element)
-   [Imagedata](#imagedata-element)
-   [Path](#path-element)
-   [Shadow](#shadow-element)
-   [Skew](#skew-element)
-   [Stroke](#stroke-element)
-   [TextPath](#textpath-element)

The VML OM uses several [data types](/windows) to define parameters. Datatypes prefixed with "Vg" are enumerations and those prefixed with "IVg" are objects. Click here for a list. Minor datatypes are listed with specific parameters.

## Example

The following VBScript code shows how to create a simple shape:


```HTML
        Set MyRect = Document.CreateElement("v:Rect")
        Set R = MyDiv.AppendChild(MyRect)
        R.Style.Position = "absolute"
        R.Style.Width = 20
        R.Style.Height = 20
        R.Style.Top = 50
        R.Style.Left = 50
        R.FillColor = "red"
```



In the above example, a shape is created by using the Document Object Model method **CreateElement**. The shape is a VML predefined Rect shape. Even though the object exists, it cannot be part of the document until it is attached to the document. Using the **AppendChild** method, the Rect is made a child of a **DIV** element called MyDiv. A few minimum style attributes (**Position**, **Width**, **Height**, **Top**, **Left**) are set to give the shape a specific size. Finally, a color is assigned with the **FillColor** attribute. Note that any scripting language or any language that can work with Document Object Model interfaces can be used.

## Setting up VML

One implementation of VML is through Microsoft Internet Explorer 5.0 or greater. To set up the rendering object correctly in a Web page, the following additions must be made:

1.  The schema must be set up in the initial &lt;HTML&gt; tag as follows:
    ```HTML
    <HTML xmlns:v="urn:schemas-microsoft-com:vml">
    ```

    

2.  The rendering behavior must be part of the document's style:
    ```HTML
    <STYLE>
    v\:* { behavior: url(#default#VML); display:inline-block}
    </STYLE>
    ```

    

The following shows a sample HTML Web page set up correctly for VML showing the dynamic creation of a shape.


```HTML
<HTML xmlns:v="urn:schemas-microsoft-com:vml">
<HEAD>
<STYLE>
v\:* { behavior: url(#default#VML); display:inline-block}
</STYLE>
<TITLE>VML Sample</TITLE>
</HEAD>
<BODY>
<DIV id="MyDiv"></DIV>
<SCRIPT ID="MYSCRIPT" LANGUAGE="VBScript">
<!--
Set MyRect = Document.CreateElement("v:Rect")
Set R = MyDiv.AppendChild(MyRect)
R.Style.Position = "absolute"
R.Style.Width = 20
R.Style.Height = 20
R.Style.Top = 50
R.Style.Left = 50
R.FillColor = "red"
-->
</SCRIPT>
</BODY>
</HTML>
```



Note that in beta versions, an ActiveX object tag and a different behavior style was required.

## VML OM Reference

This reference defines the [Shape](#shape-element) element, [subelements](/windows), and [data types](/windows) that are used by the object model of VML.

### Shape element

Shapes are the building blocks of graphical images defined by Vector Markup Language (VML). The shape is the top-level element and several subelements help define the nature of each shape.

VML provides predefined shapes:

**Shape Attributes**

-   **Arc**
-   **Curve**
-   **Line**
-   **PolyLine**
-   **Rect**
-   **RoundRect**



|   Subelement           |    Description                                                                                                                                                                                                                                                                                                                                                                              |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Adj          | [IVgAdjustments](msdn-online-vml-ivgadjustments-data-type.md). A comma-delimited list of numbers that are the parameters for the guide formulas that define the path of the shape. Values may be omitted to allow for using defaults. There can be up to 8 adjustment values.                                                                                                   |
| Alt          | String. Alternative text associated with shape. Used for non-graphical browsing.                                                                                                                                                                                                                                                                                                 |
| Button       | [VgTriState](msdn-online-vml-vgtristate.md). Displays button behavior on click.                                                                                                                                                                                                                                                                                                 |
| BWMode       | [VgBlackWhiteMode](msdn-online-vml-vgblackwhitemode.md). Determines how shape will render in black-and-white view in apps or when printed to black-and-white printers. Values include: **Color**, **Auto**, **GrayScale**, **LightGrayScale**, **InverseGray**, **GrayOutline**, **BlackTextAndLines**, **HighContrast**, **Black**, **White**, **Undrawn**. Default: **Auto**. |
| BWNormal     | VgBlackWhiteMode. When BWMode is Auto, this property is consulted for how to render the shape in normal black and white. Values include: **Color**, **Auto**, **GrayScale**, **LightGrayScale**, **InverseGray**, **GrayOutline**, **BlackTextAndLines**, **HighContrast**, **Black**, **White**, **Undrawn**. Default: **Auto**.                                                |
| BWPure       | VgBlackWhiteMode. When BWMode is Auto, this property is consulted for how to render the shape in pure B/W. Values include: **Color**, **Auto**, **GrayScale**, **LightGrayScale**, **InverseGray**, **GrayOutline**, **BlackTextAndLines**, **HighContrast**, **Black**, **White**, **Undrawn**. Default: **Auto**.                                                              |
| ChildShapes  | IVgGroupShapes. A collection of other shapes in this group. This collection supports the standard Length and Item methods.                                                                                                                                                                                                                                                       |
| Chromakey    | [IVgColor](msdn-online-vml-ivgcolor.md). A color value that will be transparent and show anything behind the shape.                                                                                                                                                                                                                                                             |
| Control1     | [Vector2D](msdn-online-vml-ivgvector2d-data-type.md). Control point for curve.                                                                                                                                                                                                                                                                                                  |
| Control2     | [Vector2D](msdn-online-vml-ivgvector2d-data-type.md). Control point for curve.                                                                                                                                                                                                                                                                                                  |
| CoordOrigin  | [Vector2D](msdn-online-vml-ivgvector2d-data-type.md) The coordinates at the top left corner of the container rectangle. Range from 0 to infinity.                                                                                                                                                                                                                               |
| CoordSize    | [Vector2D](msdn-online-vml-ivgvector2d-data-type.md). The width and height of the coordinate space inside the reference rectangle of this shape. If it is not specified, it is the same as the width and height of the rectangle. Range from 0 to infinity. Default: "1000,1000".                                                                                               |
| EndAngle     | [VgAngleInDegrees](msdn-online-vml-vgangleindegrees-data-type.md). End angle of shape.                                                                                                                                                                                                                                                                                          |
| Extrusion    | IVgExtrusion. Specifies the Extrusion object value for this shape. See the [Extrusion](msdn-online-vml-extrusion-element.md) element for details.                                                                                                                                                                                                                               |
| Fill         | VgFillFormat. Specifies the fill value for this shape. See the [Fill](msdn-online-vml-fill-element.md) element for more details.                                                                                                                                                                                                                                                |
| FillColor    | [IVgColor](msdn-online-vml-ivgcolor.md). The primary color of the brush to use to fill the path of this shape.                                                                                                                                                                                                                                                                  |
| Filled       | [VgTriState](msdn-online-vml-vgtristate.md). If True, the path defining the shape will be filled. By default, it will be filled using a solid color unless there is a Fill subelement that specifies more complex fill properties. If False, the fill is transparent.                                                                                                           |
| Flip         | VgFlipOrientation. Values are: X Y XY YX                                                                                                                                                                                                                                                                                                                                         |
| ForceDash    | [VgTriState](msdn-online-vml-vgtristate.md). Indication that a dashed outline should be rendered when there is no line and no fill for a shape. This behavior is generally useful for making invisible shapes visible in editing applications so they can be selected and operated on, such as in an image map.                                                                 |
| Formulas     | IVgFormulas. An array of formulas that defines a shape.                                                                                                                                                                                                                                                                                                                          |
| From         | [Vector2D](msdn-online-vml-ivgvector2d-data-type.md). Starting point of line.                                                                                                                                                                                                                                                                                                   |
| HRef         | [String](#data-types-used-in-the-vml-object-model). The URL to jump to if this shape is clicked.                                                                                                                                                                                                                                                                                 |
| ImageData    | IVgImageData. Image information if the shape is a picture. See the ImageData element for more information.                                                                                                                                                                                                                                                                       |
| OnEd         | [VgTriState](msdn-online-vml-vgtristate.md). Hides all handles except the top left and bottom right, as in the handles for a straight line segment.                                                                                                                                                                                                                             |
| Opacity      | [VgFraction](msdn-online-vml-vgfraction-data-type.md). The opacity of the entire shape. A number between 0.0 and 1.0.                                                                                                                                                                                                                                                           |
| Path         | IVgPath. A string containing the commands that define the path.                                                                                                                                                                                                                                                                                                                  |
| Points       | [IVgPoints](msdn-online-vml-ivgpoints-data-type.md). A collection of points defining a shape.                                                                                                                                                                                                                                                                                   |
| Print        | [VgTriState](msdn-online-vml-vgtristate.md). If True, this shape is meant to be printed.                                                                                                                                                                                                                                                                                        |
| Rotation     | [VgAngleInDegrees](msdn-online-vml-vgangleindegrees-data-type.md). Sets rotation of shape. Value is propagated to the shape style.                                                                                                                                                                                                                                              |
| Scale        | [Vector2D](msdn-online-vml-ivgvector2d-data-type.md). Scale of shape.                                                                                                                                                                                                                                                                                                           |
| Shadow       | IVgShadow. Specifies the shadow for this shape. See the [Shadow](msdn-online-vml-shadow-element.md) element for details.                                                                                                                                                                                                                                                        |
| Spt          | Reserved.                                                                                                                                                                                                                                                                                                                                                                        |
| StartAngle   | [VgAngleInDegrees](msdn-online-vml-vgangleindegrees-data-type.md). Start angle of shape.                                                                                                                                                                                                                                                                                        |
| Stroke       | VgStrokeFormat. See Stroke element for details.                                                                                                                                                                                                                                                                                                                                  |
| StrokeColor  | [IVgColor](msdn-online-vml-ivgcolor.md). The primary color of the brush to use to stroke the path of this shape.                                                                                                                                                                                                                                                                |
| Stroked      | [VgTriState](msdn-online-vml-vgtristate.md). If True, the path defining the shape will be stroked.                                                                                                                                                                                                                                                                              |
| StrokeWeight | [VGLength](msdn-online-vml-vglength.md). The width of the brush to use to stroke the path. Ranges between 0 and 1584.                                                                                                                                                                                                                                                           |
| TextPath     | IVgTextPath. Specifies the TextPath object of the shape. See the [TextPath](msdn-online-vml-textpath-element.md) element for more information.                                                                                                                                                                                                                                  |
| To           | [Vector2D](msdn-online-vml-ivgvector2d-data-type.md). End point of line.                                                                                                                                                                                                                                                                                                        |
| Type         | String. Type of shape.                                                                                                                                                                                                                                                                                                                                                           |



 

## Subelements of the Shape Element

The following subelements are part of the VML object model.

-   [Background](#background-element)
-   [Extrusion](#extrusion-element)
-   [Fill](#fill-element)
-   [Group](#group-element)
-   [Imagedata](#imagedata-element)
-   [Path](#path-element)
-   [Shadow](#shadow-element)
-   [Skew](#skew-element)
-   [Stroke](#stroke-element)
-   [TextPath](#textpath-element)

### Background element

Describes the fill of the background of a page using VML fills.


|   Attribute        |   Description                                                                                                                                                                                      |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BWMode    | [VgBlackWhiteMode](msdn-online-vml-vgblackwhitemode.md). Determines how shape will render in black-and-white view in applications or when printed.                                     |
| BWNormal  | [VgBlackWhiteMode](msdn-online-vml-vgblackwhitemode.md). When BWMode is Auto, this property is consulted for how to render the shape in normal black and white.                        |
| BWPure    | [VgBlackWhiteMode](msdn-online-vml-vgblackwhitemode.md). When BWMode is Auto, this property is consulted for how to render the shape in pure black and white.                          |
| Fill      | VgFillFormat. Specifies the fill for this shape. See [Fill](msdn-online-vml-fill-element.md) element for more information.                                                             |
| FillColor | [IVgColor](msdn-online-vml-ivgcolor.md). The primary color of the brush to use to fill the path of this shape. Duplicate of the Color value in the Fill element. The default is white. |



 

### Extrusion element

Describes a 3-D extrusion of the shape.

**Attributes**



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td>AutoRotationCenter</td>
<td><a href="msdn-online-vml-vgtristate.md">VgTriState</a>. If True, the center of rotation of the group of 3-D objects (in fact there is only ever one object in the group) is determined automatically to be the center of the group; otherwise it is determined by the RotationCenter parameters, which are a fraction of the shape with 0,0,0 being the center.</td>
</tr>
<tr class="even">
<td>BackDepth</td>
<td><a href="msdn-online-vml-vglength.md"><strong>VgLength</strong></a>. Amount of backward extrusion. Ranges from 0 to 32767.</td>
</tr>
<tr class="odd">
<td>Brightness</td>
<td><a href="#data-types-used-in-the-vml-object-model">VgPositiveNumber</a>. Overall brightness of the scene. Default is &quot;20,000&quot;.</td>
</tr>
<tr class="even">
<td>Color</td>
<td><a href="msdn-online-vml-ivgcolor.md">IVgColor</a>. The color of the extrusion. Only used if ColorMode is Custom. Otherwise, Auto sets the extrusion effect color to the same as FillColor.</td>
</tr>
<tr class="odd">
<td>ColorMode</td>
<td>Vg3DColorMode. Values are:
<ul>
<li>Auto (default)</li>
<li>Custom</li>
</ul></td>
</tr>
<tr class="even">
<td>Diffusity</td>
<td><a href="#data-types-used-in-the-vml-object-model">VgPositiveNumber</a>. The ratio of incident to diffusely reflected light. Values less than 1.0 are normal but values higher than one can generate interesting effects.</td>
</tr>
<tr class="odd">
<td>Edge</td>
<td><a href="msdn-online-vml-vglength.md">VgLength</a>. Sets the size of a simulated rounded beveled edge. Ranges from 0 to 32767 in floating point pts. Default is &quot;1pt&quot;.</td>
</tr>
<tr class="even">
<td>Facet</td>
<td><a href="#data-types-used-in-the-vml-object-model">VgPositiveNumber</a>. Sets the facet of the scene. Default is &quot;30,000&quot;.</td>
</tr>
<tr class="odd">
<td>ForeDepth</td>
<td><a href="msdn-online-vml-vglength.md">VgLength</a>. Amount of forward extrusion. Ranges from 0 to 32767.</td>
</tr>
<tr class="even">
<td>LightFace</td>
<td><a href="msdn-online-vml-vgtristate.md">VgTriState</a>. Determimes whether the front face of the object will respond to changes in the 3-D lighting, e.g., when an object rotates.</td>
</tr>
<tr class="odd">
<td>LightHarsh</td>
<td><a href="msdn-online-vml-vgtristate.md">VgTriState</a>. Harsh lighting for the primary light source. Default is False.</td>
</tr>
<tr class="even">
<td>LightHarsh2</td>
<td><a href="msdn-online-vml-vgtristate.md">VgTriState</a>. Harsh lighting for the secondary light source. Default is False.</td>
</tr>
<tr class="odd">
<td>LightLevel</td>
<td><a href="#data-types-used-in-the-vml-object-model">VgNumber</a>. Intensity of the primary light source. Default is &quot;38000&quot;.</td>
</tr>
<tr class="even">
<td>LightLevel2</td>
<td><a href="#data-types-used-in-the-vml-object-model">VgNumber</a>. Intensity of the secondary light source. Default is &quot;38000&quot;.</td>
</tr>
<tr class="odd">
<td>LightPosition</td>
<td>Vector3D. Position of the primary light source. Default is &quot;50000,0,10000&quot;.</td>
</tr>
<tr class="even">
<td>LightPosition2</td>
<td>Vector3D. Position of the secondary light source. Default is &quot;-50000,0,10000&quot;.</td>
</tr>
<tr class="odd">
<td>LockRotationCenter</td>
<td><a href="msdn-online-vml-vgtristate.md">VgTriState</a>. &quot;Lockrotationcenter&quot; means that the rotation of the group is defined to be by rotation-angle[1] degrees about the y-axis on the page followed by rotation-angle[0] degrees about the x-axis. When LockRotationCenter is False, the rotation is defined to be by orientation-angle degrees about the vector defined by orientation. So, for example, lockrotationcenter=false orientationangle=45 orientation=(0,1,0) is equivalent to lockrotationcenter=true rotationangle=(0,45).</td>
</tr>
<tr class="even">
<td>Metal</td>
<td><a href="msdn-online-vml-vgtristate.md">VgTriState</a>. Causes specularly reflected light to be the material color instead of the light source color, making the object seem more metallic.</td>
</tr>
<tr class="odd">
<td>On</td>
<td><a href="msdn-online-vml-vgtristate.md">VgTriState</a>. Turns the display of the extrusion effect on and off.</td>
</tr>
<tr class="even">
<td>Orientation</td>
<td>Vector3D. Orientation of the camera.</td>
</tr>
<tr class="odd">
<td>OrientationAngle</td>
<td><a href="msdn-online-vml-vgangleindegrees-data-type.md">VgAngleInDegrees</a>. Angle between the orientation of the camera and the xy plane.</td>
</tr>
<tr class="even">
<td>Plane</td>
<td>Vg3DExtrudePlane. Allows extrusion from planes orthogonal to the screen plane. Requires ForeDepth and BackDepth to be specified in drawing units instead of emus. Values are:
<ul>
<li>XY</li>
<li>ZX</li>
<li>YZ</li>
</ul></td>
</tr>
<tr class="odd">
<td>Render</td>
<td>Vg3DRenderMode. Values are:
<ul>
<li>Solid (default)</li>
<li>WireFrame</li>
<li>BoundingCube</li>
</ul></td>
</tr>
<tr class="even">
<td>RotationAngle</td>
<td><a href="msdn-online-vml-ivgvector2d-data-type.md">Vector2D</a>. AngleX, AngleY, or AngleZ is controlled by the ShapeRotation attribute.</td>
</tr>
<tr class="odd">
<td>RotationCenter</td>
<td>Vector3D. Center of rotation.</td>
</tr>
<tr class="even">
<td>Shininess</td>
<td><a href="#data-types-used-in-the-vml-object-model">VgPositiveNumber</a>. Determines how concentrated or spread out specular reflection is. A high value would be 8 to 10 and would approximate a mirror, and a low value would be 2 to 3 and would approximate sequined clothing. Values of 3 to 7 are recommended. High values will reflect pinpoint light sources.</td>
</tr>
<tr class="odd">
<td>SkewAmt</td>
<td><a href="#data-types-used-in-the-vml-object-model">VgPercentage</a>. If Type is Parallel, attribute determines the amount of skew. Ranges from 0 to 100.</td>
</tr>
<tr class="even">
<td>SkewAngle</td>
<td><a href="msdn-online-vml-vgangleindegrees-data-type.md">VgAngleInDegrees</a>. If Type is Parallel, attribute determines the degree of skew. Default is &quot;-45&quot;.</td>
</tr>
<tr class="odd">
<td>Specularity</td>
<td><a href="#data-types-used-in-the-vml-object-model">VgPositiveNumber</a>. The ratio of incident to specularly reflected light. Values less than 1.0 are normal but values higher than one can generate interesting effects.</td>
</tr>
<tr class="even">
<td>Type</td>
<td>VgExtrusionType. Values are:
<ul>
<li>Parallel (default)</li>
<li>Perspective</li>
</ul></td>
</tr>
<tr class="odd">
<td>Viewpoint</td>
<td>Vector3D. The point where the scene is being viewed from.</td>
</tr>
<tr class="even">
<td>ViewpointOrigin</td>
<td><a href="msdn-online-vml-ivgvector2d-data-type.md">Vector2D</a>. Can have values from 0.5 to -0.5 to position the origin of the viewpoint within the shape bounding box.</td>
</tr>
</tbody>
</table>



 

### Fill element

Describes how a path should be filled for fills more complex than a solid color.

**Attributes**



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td>AlignShape</td>
<td><a href="msdn-online-vml-vgtristate.md">VgTriState</a>. Align the image with the shape. If False, align image with window.</td>
</tr>
<tr class="even">
<td>Angle</td>
<td><a href="msdn-online-vml-vgangleindegrees-data-type.md">VgAngleInDegrees</a>. The angle along which the gradient goes. 0 degrees is along the horizontal axis from left to right.</td>
</tr>
<tr class="odd">
<td>Aspect</td>
<td><strong>VgAspectType</strong>. ImageSize attribute will be adjusted to preserve the aspect of the image. Values include:
<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Ignore</td>
<td>Ignore aspect issues.</td>
</tr>
<tr class="even">
<td>AtLeast</td>
<td>Image is at least as big as the image size.</td>
</tr>
<tr class="odd">
<td>AtMost</td>
<td>Image is no bigger than image size.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td>Color</td>
<td><a href="msdn-online-vml-ivgcolor.md">IVgColor</a> The main fill color. Same as FillColor attribute in shape.</td>
</tr>
<tr class="odd">
<td>Color2</td>
<td><a href="msdn-online-vml-ivgcolor.md">IVgColor</a>. The secondary color for a fill when image type is Pattern or a gradient fill.</td>
</tr>
<tr class="even">
<td>Colors</td>
<td><a href="#data-types-used-in-the-vml-object-model">IVgGradientColorArray</a>. Intermediate colors in the gradient and their relative positions along the gradient, e.g., &quot;30% red, 70% blue, 90% green&quot;. Primary color (Color attribute in shape) is 0% and secondary color (Color2 attribute) is 100%.</td>
</tr>
<tr class="odd">
<td>Focus</td>
<td><a href="#data-types-used-in-the-vml-object-model">VgSignedPercentage</a>. Focal point for linear gradient fill. Values go from -100 to +100.</td>
</tr>
<tr class="even">
<td>FocusPosition</td>
<td><a href="msdn-online-vml-ivgvector2d-data-type.md">Vector2D</a>. Position of the innermost rectangle for radial gradients. The vector is a fraction (0.0 - 1.0) of the shape's width and height.</td>
</tr>
<tr class="odd">
<td>FocusSize</td>
<td><a href="msdn-online-vml-ivgvector2d-data-type.md">Vector2D</a> Size of the innermost rectangle for radial gradients. The vector is a fraction (0.0 to 1.0) of the shape's width and height.</td>
</tr>
<tr class="even">
<td>Method</td>
<td>VgSigmaType. Values include:
<ul>
<li>None</li>
<li>Linear</li>
<li>Sigma</li>
<li>Any</li>
</ul>
<p>Default is Sigma.</p></td>
</tr>
<tr class="odd">
<td>On</td>
<td><a href="msdn-online-vml-vgtristate.md">VgTriState</a>. Turns fill display on. Same as Fill attribute in shape.</td>
</tr>
<tr class="even">
<td>Opacity</td>
<td><a href="msdn-online-vml-vgfraction-data-type.md">VgFraction</a>. Opacity of the fill.</td>
</tr>
<tr class="odd">
<td>Opacity2</td>
<td><a href="msdn-online-vml-vgfraction-data-type.md">VgFraction</a>. The secondary opacity for gradients.</td>
</tr>
<tr class="even">
<td>Origin</td>
<td><a href="msdn-online-vml-ivgvector2d-data-type.md">Vector2D</a>. Point relative to upper left corner of the image that is treated as the origin of the image. Default is the center of the image. The vector is a fraction (from 0.0 to 1.0) of the image's width and height.</td>
</tr>
<tr class="odd">
<td>Position</td>
<td><a href="msdn-online-vml-ivgvector2d-data-type.md">Vector2D</a>. Point in the reference rectangle of the shape to position the origin of the image. Default is the center of the container rectangle. The vector is a fraction (0.0 - 1.0) of the image's width and height.</td>
</tr>
<tr class="even">
<td>Size</td>
<td><a href="msdn-online-vml-ivgvector2d-data-type.md">Vector2D</a>. The size of the image. Default is pixel size of the image. May be specified in absolute coordinates or percentage.</td>
</tr>
<tr class="odd">
<td>Src</td>
<td><a href="#data-types-used-in-the-vml-object-model">String</a>. URL to an image to load for image and pattern fills. This attribute must always be present and point to valid image data for a picture to appear.</td>
</tr>
<tr class="even">
<td>Type</td>
<td>VgFillType. May be one of the following types:
<ul>
<li>Background</li>
<li>Frame</li>
<li>Gradient</li>
<li>GradientCenter</li>
<li>GradientRadial</li>
<li>GradientTitle</li>
<li>GradientUnscaled</li>
<li>Pattern</li>
<li>Solid</li>
<li>Tile</li>
</ul>
Tile, Pattern, and Frame require the image attributes to be supplied. Gradient and GradientRadial require the gradient attributes to be supplied.</td>
</tr>
</tbody>
</table>



 

### Group element

A group is a collection of individual shapes that can be positioned and transformed as a unit.



|   Attribute        |   Description                                                                                                                                                                                      |
|--------|----------------------------------------------------------------------------------------------|
| Item   | [IVgShape](#data-types-used-in-the-vml-object-model). Specified item in the array of shapes. |
| Length | [Integer](#data-types-used-in-the-vml-object-model). Number of shapes in this group.         |



 

### Imagedata element

Describes a picture to be rendered on top of a shape.



|   Attribute        |   Description                                                                                                                                                                                      |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BiLevel     | [VgTriState](msdn-online-vml-vgtristate.md). Display picture in only two colors (usually black and white).                                                                                                                                                                                                                                                     |
| BlackLevel  | [VgFraction](msdn-online-vml-vgfraction-data-type.md). Allows adjustment to set the level so that blacks appear as true blacks, and all other colors are visible as shades above black.                                                                                                                                                                        |
| Chromakey   | [IVgColor](msdn-online-vml-ivgcolor.md). Transparent color of picture.                                                                                                                                                                                                                                                                                         |
| CropBottom  | [VgNumber](#data-types-used-in-the-vml-object-model). Crop distance from bottom of picture expressed as a percentage of picture size.                                                                                                                                                                                                                           |
| CropLeft    | [VgNumber](#data-types-used-in-the-vml-object-model). Crop distance from left edge of picture expressed as a fraction of picture size (from 0.0 to 1.0). However, "out-cropping" is supported and thus values of less than 0 and greater than 1 are supported; e.g., -5, 20 would out-crop the bounds 25X the picture size with 4/5 on one side of the picture. |
| CropRight   | [VgNumber](#data-types-used-in-the-vml-object-model). Crop distance from right of picture expressed as a percentage of picture size.                                                                                                                                                                                                                            |
| CropTop     | [VgNumber](#data-types-used-in-the-vml-object-model). Crop distance from top of picture expressed as a percentage of picture size.                                                                                                                                                                                                                              |
| EmbossColor | [IVgColor](msdn-online-vml-ivgcolor.md). This is set to a percentage of the shadow color to create an embossed picture effect.                                                                                                                                                                                                                                 |
| Gain        | [VgPositiveNumber](#data-types-used-in-the-vml-object-model). Adjusts the intensity of all colors. Essentially sets how bright white will be. Ranges from 0 to 32767.                                                                                                                                                                                           |
| Gamma       | [VgFraction](msdn-online-vml-vgfraction-data-type.md). Gamma correction. Increasing it gives an image more contrast.                                                                                                                                                                                                                                           |
| GrayScale   | [VgTriState](msdn-online-vml-vgtristate.md). Display picture in grayscale colors.                                                                                                                                                                                                                                                                              |
| Src         | [String](#data-types-used-in-the-vml-object-model). URL to an image to load for image and pattern fills. This attribute must always be present and point to valid image data for a picture to appear.                                                                                                                                                           |



 

### Path element

Defines the path that makes up the shape, using a string that contains a rich set of "pen movement" commands.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td>Limo</td>
<td><a href="msdn-online-vml-ivgvector2d-data-type.md">IVgVector2D</a>. Defines the point where the shape is stretched; e.g., for a giraffe shape, the limo point would be on the neck so when the shape is resized, the neck will stretch and the rest of the shape will maintain its dimensions.</td>
</tr>
<tr class="even">
<td>TextBoxRect</td>
<td><a href="#data-types-used-in-the-vml-object-model">IVgFixedRectangleArray</a>. Array containing the rectangles that define where text should go.</td>
</tr>
<tr class="odd">
<td>V</td>
<td><a href="#data-types-used-in-the-vml-object-model">String</a>. Matches the v attribute on the Path tag. Note that path may correspond to Path attribute or element.</td>
</tr>
<tr class="even">
<td>Value</td>
<td><a href="#data-types-used-in-the-vml-object-model">String</a>. A text representation of the commands that define the path. X or y-coordinate values can be a reference to a formula in the form &quot;@#&quot; where # is the formula's ordinal number, e.g., &quot;@2&quot;. This attribute string is made up of a rich set of commands including the following: <br/> 
<table>
<thead>
<tr class="header">
<th>Command</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ae (angleellipseto)</td>
<td><strong>center</strong>(x,y) <strong>size</strong>(w,h) <strong>start-angle</strong>, <strong>end-angle</strong><br/> Draw a segment of an ellipse. A straight line is drawn from the current point to the start point of the segment.<br/></td>
</tr>
<tr class="even">
<td>al (angleelipse)</td>
<td>Same as ae except that there is an implied m to the starting point of the segment.</td>
</tr>
<tr class="odd">
<td>ar (arc)</td>
<td>Same as at. However, a new subpath is started by an implied m to the start point of the arc.</td>
</tr>
<tr class="even">
<td>at (arcto)</td>
<td><strong>left</strong>, <strong>top</strong>, <strong>right</strong>, <strong>bottom</strong>, <strong>start</strong>(x,y) <strong>end</strong>(x,y) <br/> The first four values define the bounding box of an ellipse. The last four define two radial vectors. A segment of the ellipse is drawn that starts at the angle defined by the start radius vector and ends at the angle defined by the end vector. A straight line is drawn from the current point to the start of the arc. The arc is always drawn in a counterclockwise direction. <br/></td>
</tr>
<tr class="odd">
<td>c (curveto)</td>
<td><strong>control1</strong>(x,y) <strong>control2</strong>(x,y) <strong>to</strong>(x,y) <br/> Draw a cubic bezier curve from the current point to the coordinate given by the final two parameters, the control points given by the first four parameters. The current point becomes the endpoint of the bezier.<br/></td>
</tr>
<tr class="even">
<td>e (end)</td>
<td>End the current set of subpaths. A given set of subpaths (as delimited by end) are filled using eofill. Subsequent sets of subpaths are filled independently and superimposed on existing ones.</td>
</tr>
<tr class="odd">
<td>l (lineto)</td>
<td>x,y<br/> Draw a line from the current point to the given x,y-coordinate, which becomes the new current point. Additional coordinate pairs may be specified to form a polyline, e.g., &quot;l 10,13,45,27,89,-12&quot;.<br/></td>
</tr>
<tr class="even">
<td>m (moveto)</td>
<td>x,y<br/> Start a new subpath at the given x,y-coordinate.<br/></td>
</tr>
<tr class="odd">
<td>nf (nofill)</td>
<td>The current set of subpaths (delimited by end) will not be filled.</td>
</tr>
<tr class="even">
<td>ns (nostroke)</td>
<td>The current set of subpaths (delimited by end) will not be stroked.</td>
</tr>
<tr class="odd">
<td>qb (quadraticbezier)</td>
<td>(<strong>controlpoint</strong>(x, y))*,<strong>end</strong>(x,y) <br/> Defines one or more quadratic bezier curves by means of control points and an endpoint. Intermediate (on-curve) points are obtained by interpolation between successive control points similar to TrueType fonts. The subpath need not be a start, in which case the subpath is closed and the last point defines the start point.<br/></td>
</tr>
<tr class="even">
<td>qx (ellipticalquadrantx)</td>
<td><strong>end</strong>(x,y) <br/> A quarter ellipse is drawn from the current point to the given endpoint. The elliptical segment is initially tangential to a line parallel to the x-axis; i.e., the segment starts out horizontal.<br/></td>
</tr>
<tr class="odd">
<td>qy (ellipticalquadranty)</td>
<td><strong>end</strong>(x,y) <br/> Same as qx except that the elliptical segment is initially tangential to a line parallel to the y-axis; i.e., the segment starts out vertical.<br/></td>
</tr>
<tr class="even">
<td>r (rlineto)</td>
<td>x,y <br/> Draw a line from the current point to the relative coordinate (cpx + x, cpy + y). If additional coordinate pairs are given, each new point is computed relative to the last one.<br/></td>
</tr>
<tr class="odd">
<td>t (rmoveto)</td>
<td>x,y<br/> Start a new subpath at the relative coordinates ( cpx + x, cpy + y) where cpx, cpy is the current position. <br/></td>
</tr>
<tr class="even">
<td>v (curveto)</td>
<td><strong>control1</strong>(x,y) <strong>control2</strong>(x,y) <strong>to</strong> (x,y) <br/> Cubic bezier curve using the given coordinates relative to the current point. All the points are computed relative to the same starting point.<br/></td>
</tr>
<tr class="odd">
<td>wa (clockwisearcto)</td>
<td>Same as at but the arc is drawn in a clockwise direction.</td>
</tr>
<tr class="even">
<td>wr (clockwisearc)</td>
<td>Same as ar but is drawn in a clockwise direction.</td>
</tr>
<tr class="odd">
<td>x (close)</td>
<td>Close the current subpath by drawing a straight line from the current point to the original moveto point.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>



 

### Shadow element

Describes a shadow effect on a shape.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td>Color</td>
<td><a href="msdn-online-vml-ivgcolor.md">IVgColor</a>. Color of the primary shadow. Default is RGB(128,128,128)</td>
</tr>
<tr class="even">
<td>Color2</td>
<td><a href="msdn-online-vml-ivgcolor.md">IVgColor</a>. Color of the second shadow, or highlight in an embossed or engraved shadow. Default is RGB(203,203,203).</td>
</tr>
<tr class="odd">
<td>Matrix</td>
<td><a href="#data-types-used-in-the-vml-object-model">IvgSkewMatrix</a>. A perspective transform matrix in the form, &quot;sxx,sxy,syx,syy,px,py&quot; [s=scale, p=perspective]. The s items specify how the shadow should scale with respect to the shape, and the p items specify how the shadow should skew with respect to the shape. For example, the following matrix resizes the shape by a factor of 2 and skews it by a factor of 4 in all directions: <br/> &quot;2,2,2,2,4,4&quot;<br/> This matrix is only used if the type of the shadow is set to perspective.<br/></td>
</tr>
<tr class="even">
<td>Obscured</td>
<td><a href="msdn-online-vml-vgtristate.md">VgTriState</a>. The shadow can be seen through if there is no fill on the shape. Default is False.</td>
</tr>
<tr class="odd">
<td>Offset</td>
<td><a href="#data-types-used-in-the-vml-object-model">IVgSkewOffset</a>. Amount of x,y offset from the shape's location. Default is &quot;2pt,2pt&quot;.</td>
</tr>
<tr class="even">
<td>Offset2</td>
<td><a href="msdn-online-vml-ivgvector2d-data-type.md">Vector2D</a>. Amount of x,y second offset from the shape?s location. Values are either an absolute measurement, or a fractional value of shape (-0.5 to +0.5).</td>
</tr>
<tr class="odd">
<td>On</td>
<td><a href="msdn-online-vml-vgtristate.md">VgTriState</a>. Turns the display of the shadow on and off.</td>
</tr>
<tr class="even">
<td>Opacity</td>
<td><a href="msdn-online-vml-vgfraction-data-type.md">VgFraction</a>. Opacity of the shadow effect.</td>
</tr>
<tr class="odd">
<td>Origin</td>
<td><a href="msdn-online-vml-ivgvector2d-data-type.md">Vector2D</a> A pair of fractional values of shape from -0.5 to +0.5.</td>
</tr>
<tr class="even">
<td>Type</td>
<td><a href="#data-types-used-in-the-vml-object-model">VgShadowType</a>. Values are:
<ul>
<li>Single (default)</li>
<li>Double</li>
<li>Perspective</li>
<li>ShapeRelative</li>
<li>DrawingRelative</li>
<li>Emboss</li>
</ul></td>
</tr>
</tbody>
</table>



 

### Skew element

Describes a perspective skew effect on a shape. The skew is applied to vector graphic data, not image data.



|   Attribute        |   Description                                                                                                                                                                                      |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Matrix | [IVgSkewMatrix](#data-types-used-in-the-vml-object-model). A perspective transform matrix in the form, "sxx,sxy,syx,syy,px,py" \[ s=scale, p=perspective\]. If offset is in absolute units then px,py are in emu ^ -1 units; otherwise they are an inverse fraction of shape size. |
| Offset | [IvgSkewOffset](#data-types-used-in-the-vml-object-model). Amount of x,y offset from the shape's location. Default is "2pt,2pt".                                                                                                                                                   |
| On     | [VgTriState](msdn-online-vml-vgtristate.md). Turns the display of the skew on or off.                                                                                                                                                                                             |
| Origin | [Vector2D](msdn-online-vml-ivgvector2d-data-type.md). A pair of fractional values of shape from -0.5 to +0.5.                                                                                                                                                                     |



 

### Stroke element

Describes how to draw the path if something beyond a solid line with a solid color is desired.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td>Color</td>
<td><a href="msdn-online-vml-vgtristate.md">VgTriState</a>. The color of the line. Same as StrokeColor attribute in Shape but overrides it.</td>
</tr>
<tr class="even">
<td>Color2</td>
<td><a href="msdn-online-vml-ivgcolor.md">IVgColor</a>. Secondary color. Used when FillType is Pattern.</td>
</tr>
<tr class="odd">
<td>DashStyle</td>
<td><strong>VgLineDashStyle</strong>. Dash style format. May be a specific value or a sequence of numbers with a user-defined dash pattern. Values are:
<ul>
<li>Solid (default)</li>
<li>ShortDash</li>
<li>ShortDot</li>
<li>ShortDashDot</li>
<li>ShortDashDotDot</li>
<li>Dot</li>
<li>Dash</li>
<li>DashDot</li>
<li>LongDash</li>
<li>LongDashDot</li>
<li>LongDashDotDot</li>
</ul></td>
</tr>
<tr class="even">
<td>EndArrow</td>
<td><strong>VgArrowheadStyle</strong>. Arrowhead for the end of the line. Values are:
<ul>
<li>None (default)</li>
<li>Block</li>
<li>Classic</li>
<li>Diamond</li>
<li>Oval</li>
<li>Open</li>
<li>Chevron</li>
<li>DoubleChevron</li>
</ul></td>
</tr>
<tr class="odd">
<td>EndArrowLength</td>
<td><strong>VgArrowHeadLength</strong>. Arrowhead length for the end of the line. Values are:
<ul>
<li>Short</li>
<li>Medium (default)</li>
<li>Long</li>
</ul></td>
</tr>
<tr class="even">
<td>EndArrowWidth</td>
<td><strong>VgArrowheadWidth</strong>. Arrowhead width for the end of the line. Values are:
<ul>
<li>Narrow</li>
<li>Medium (default)</li>
<li>Wide</li>
</ul></td>
</tr>
<tr class="odd">
<td>EndCap</td>
<td><strong>VgLineEndCapStyle</strong>. Values are:
<ul>
<li>Flat</li>
<li>Square</li>
<li>Round</li>
</ul></td>
</tr>
<tr class="even">
<td>FillType</td>
<td><strong>VgLineFillType</strong>. Values are:
<ul>
<li>Solid (default)</li>
<li>Tile</li>
<li>Pattern</li>
<li>Frame</li>
</ul></td>
</tr>
<tr class="odd">
<td>ImageAlignShape</td>
<td><a href="msdn-online-vml-vgtristate.md">VgTriState</a>. Align the image with the shape. If False, align image with window.</td>
</tr>
<tr class="even">
<td>ImageAspect</td>
<td><strong>VgAspectType</strong>. ImageSize attribute will be adjusted to preserve the aspect of the image. Values include: 
<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Ignore</td>
<td>Ignore aspect issues.</td>
</tr>
<tr class="even">
<td>AtLeast</td>
<td>Image is at least as big as the image size.</td>
</tr>
<tr class="odd">
<td>AtMost</td>
<td>Image is no bigger than image size.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td>ImageSize</td>
<td><a href="msdn-online-vml-ivgvector2d-data-type.md">Vector2D</a>. Size of the image to form the brush with. Default is the size of the image.</td>
</tr>
<tr class="even">
<td>JoinStyle</td>
<td><strong>VgLineJoinStyle</strong>. Values are:
<ul>
<li>Round (rounded joint)</li>
<li>Bevel (beveled joint)</li>
<li>Miter (miter joint)</li>
</ul></td>
</tr>
<tr class="odd">
<td>LineStyle</td>
<td><strong>VgLineStyle</strong>. Values are:
<ul>
<li>Single</li>
<li>ThinThin (1:1:1)</li>
<li>ThinThick (1:1:2)</li>
<li>ThickThin (2:1:1)</li>
<li>ThickBetweenThin (1:1:2:1:1)</li>
</ul></td>
</tr>
<tr class="even">
<td>MiterLimit</td>
<td><a href="msdn-online-vml-vglength.md">Length</a>. The maximum distance between the inner point and outer point of a joint. This number is a multiple of the thickness of the line. Ranges from 0 to 32,767.</td>
</tr>
<tr class="odd">
<td>On</td>
<td><a href="msdn-online-vml-vgtristate.md">VgTriState</a>. Turns the display of the line on and off. Same as Stroke attribute in Shape but overrides it.</td>
</tr>
<tr class="even">
<td>Opacity</td>
<td><a href="msdn-online-vml-vgfraction-data-type.md">VgFraction</a>. Opacity of the stroke.</td>
</tr>
<tr class="odd">
<td>Src</td>
<td>String. URL to an image to load for image and pattern fills. This attribute must always be present and point to valid image data for a picture to appear.</td>
</tr>
<tr class="even">
<td>StartArrow</td>
<td><strong>VgArrowheadStyle</strong>. Arrowhead for the start of the line. Values are:
<ul>
<li>None (default)</li>
<li>Block</li>
<li>Classic</li>
<li>Diamond</li>
<li>Oval</li>
<li>Open</li>
<li>Chevron</li>
<li>DoubleChevron</li>
</ul></td>
</tr>
<tr class="odd">
<td>StartArrowLength</td>
<td>VgArrowHeadLength. Arrowhead length for the start of the line. Values are:
<ul>
<li>Short</li>
<li>Medium (default)</li>
<li>Long</li>
</ul></td>
</tr>
<tr class="even">
<td>StartArrowWidth</td>
<td>VgArrowheadWidth. Arrowhead width for the start of the line. Values are:
<ul>
<li>Narrow Medium (default) Wide</li>
</ul></td>
</tr>
<tr class="odd">
<td>Weight</td>
<td><a href="msdn-online-vml-vglength.md">VgLength</a>. Width of line. Ranges from 0 to 1584.
<div class="alert">
<blockquote>
[!Note]<br />
The DashStyle attribute allows the user to specify a custom-defined dash pattern. This is done using a series of numbers. Dash styles are defined in terms of the length of the dash (the drawn part of the stroke) and the length of the space between the dashes. The lengths are relative to the line width; a length of &quot;1&quot; is equal to the line width. The EndCap style is applied to each dash, arrow styles are not. The string first defines the length of the dash then the length of the space. This may be repeated to form complex dash styles. The string should always contain a pair of numbers; if it contains an odd number of numbers the last may be disregarded. The following table lists some typical values and a description of the intended effect. &quot;0&quot; implies a dot that should be fourfold symmetrical (with round endcaps it should be a circle). If the line endcap is Flat, a viewer should choose a built-in operating system dash where possible (i.e., something that is fast to draw). The following shows some examples.
</blockquote>
</div>
<div>
 
</div>

<table>
<tbody>
<tr class="odd">
<td>&quot;2 2&quot;</td>
<td>short-dashes (each dash and the space in between is twice the width of the line)</td>
</tr>
<tr class="even">
<td>&quot;1 2&quot;</td>
<td>dot (each dash is the width of the line while each space is twice the width of the line)</td>
</tr>
<tr class="odd">
<td>&quot;4 2&quot;</td>
<td>dash (each dash is four times the width of the line while each space is twice the width of the line)</td>
</tr>
<tr class="even">
<td>&quot;8 2&quot;</td>
<td>long-dash</td>
</tr>
<tr class="odd">
<td>&quot;4 2 1 2&quot;</td>
<td>dash dot</td>
</tr>
<tr class="even">
<td>&quot;8 2 1 2&quot;</td>
<td>long-dash dot</td>
</tr>
<tr class="odd">
<td>&quot;8 2 1 2 1 2&quot;</td>
<td>long-dash dot dot</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>



 

### TextPath element

Describes a vector path based on the text data, font, and styles supplied. The text path is warped to conform to a **Path** element if supplied.



|   Attribute        |   Description                                                                                                                                                                                      |
|----------|-------------------------------------------------------------------------------------------------------------------------------|
| FitPath  | [VgTriState](msdn-online-vml-vgtristate.md). Sizes the text to fill the path it lies out on.                                 |
| FitShape | [VgTriState](msdn-online-vml-vgtristate.md). Stretches the text path out to the edges of the shape box.                      |
| On       | [VgTriState](msdn-online-vml-vgtristate.md). Determines whether the character paths are displayed or not.                    |
| String   | String. The text to render as a text path.                                                                                    |
| Trim     | [VgTriState](msdn-online-vml-vgtristate.md). Removes any additional space reserved for ascenders and descenders if not used. |
| XScale   | [VgTriState](msdn-online-vml-vgtristate.md). Use straight x measurement instead of measuring along the path.                 |



 

## Data Types Used in the VML Object Model

The following data types are used by the VML Object Model.

-   [Double](/windows)
-   [Fixed](/windows)
-   [Integer](/windows)
-   [IVgAdjustments](/windows)
-   [IVgColor](/windows)
-   [IVgEquation](/windows)
-   [IVgFixedRectangle](/windows)
-   [IVgFixedRectangleArray](/windows)
-   [IVgFormula](/windows)
-   [IVgFormulas](/windows)
-   [IVgGradientColorArray](/windows)
-   [IVgPoints](/windows)
-   [IVgSkewMatrix](/windows)
-   [IVgSkewOffset](/windows)
-   [IVgVector2D](/windows)
-   [IVgVector3D](/windows)
-   [Length](/windows)
-   [Measure](/windows)
-   [String](/windows)
-   [VgBlackWhiteMode](/windows)
-   [VgFraction](/windows)
-   [VgTriState](/windows)

**Double data type**

A double precision integer with range from -infinity to infinity.

**Fixed data type**

Floating point number with range from -32,766.0 to 32,766.0.

**Integer data type**

An integer with a range from -infinity to infinity.

**IVgAdjustments data type**

Collection of adjustments to a shape that can be used to change the dimensions of a shape. Adjustments can be used as temporary placeholders or for any reason you would use variables. There are only 8 adjustments in the collection.



| Attribute | Description                                                                                                                                                                                                                                                                                                                                                                    |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Exists     | [IVgTriState](msdn-online-vml-vgtristate.md). Determines whether a specified adjustment exists. Note that an index must be used; that is, exists( item ) must be used to retrieve the existence of an item.                                                                                                                                                                   |
| Item       | [Long](#data-types-used-in-the-vml-object-model). Array of adjustments indexed from 0 to 7. Note that adjustments may be sparcely specified; that is, intermediate array values may not always be filled. For example, item 1, 3, and 5 could have values for a length of 3, with item(0), item(2), and item(4) specified. To see if an item exists, use the Exists attribute. |
| Length     | [Integer](#data-types-used-in-the-vml-object-model). Number of adjustments. Can be no greater than 8.                                                                                                                                                                                                                                                                          |
| Value      | [String](#data-types-used-in-the-vml-object-model). Text representation of numeric values, with commas between each number.                                                                                                                                                                                                                                                    |



 

**IVgColor**

Specifies a color.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Attributes</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>RGB</td>
<td><strong>VgRGBType</strong>. RGB value (Long) of the color. Only valid if Type is RGB.</td>
</tr>
<tr class="even">
<td>R</td>
<td><a href="#data-types-used-in-the-vml-object-model">Integer</a>. Red component of the color. Can range between 0 and 255.</td>
</tr>
<tr class="odd">
<td>G</td>
<td><a href="#data-types-used-in-the-vml-object-model">Integer</a>. Green component of the color. Can range between 0 and 255.</td>
</tr>
<tr class="even">
<td>B</td>
<td><a href="#data-types-used-in-the-vml-object-model">Integer</a>. Blue component of the color. Can range between 0 and 255.</td>
</tr>
<tr class="odd">
<td>String</td>
<td><a href="#data-types-used-in-the-vml-object-model">String</a>. Text representation of the color. The following named color types are supported:
<ul>
<li>Black (#000000)</li>
<li>Silver (#C0C0C0)</li>
<li>Gray (#808080)</li>
<li>White (#FFFFFF)</li>
<li>Maroon (#800000)</li>
<li>Red (#FF0000)</li>
<li>Purple (#800080)</li>
<li>Fuchsia (#FF00FF)</li>
<li>Green (#008000)</li>
<li>Lime (#00FF00)</li>
<li>Olive (#808000)</li>
<li>Yellow (#FFFF00)</li>
<li>Navy (#000080)</li>
<li>Blue (#0000FF)</li>
<li>Teal (#008080)</li>
<li>Aqua (#00FFFF)</li>
</ul></td>
</tr>
<tr class="even">
<td>Type</td>
<td><strong>VgColorType</strong>. Type of color. One of the following types:
<ul>
<li>Mixed</li>
<li>Named</li>
<li>RGB</li>
<li>Scheme</li>
</ul></td>
</tr>
</tbody>
</table>



 

**IVgEquation**

Equations used for formulas.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td>Operation</td>
<td><strong>VgEquationOperationType</strong> Name of operation to perform on the parameters. The following operations can be used in an equation: 
<table>
<thead>
<tr class="header">
<th>Operation</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Abs</td>
<td>Absolute value. <br/> <strong>abs</strong>(v) <br/></td>
</tr>
<tr class="even">
<td>Atan2</td>
<td>Polar arithmetic--results in fd units (degrees multiplied by 65536).<br/> <strong>atan2</strong>(p1,v) <br/></td>
</tr>
<tr class="odd">
<td>Cos</td>
<td>Cosine, argument in fd units (degrees multiplied by 65536).<br/> v * <strong>cos</strong>(p1) <br/></td>
</tr>
<tr class="even">
<td>Cosatan2</td>
<td>Preserves full accuracy in intermediate calculation.<br/> v * <strong>cos(atan2(</strong> p2,p1 <strong>))</strong><br/></td>
</tr>
<tr class="odd">
<td>Ellipse</td>
<td>Ellipse</td>
</tr>
<tr class="even">
<td>If</td>
<td>If Condition test. v > 0 <strong>?</strong> p1 : p2</td>
</tr>
<tr class="odd">
<td>Max</td>
<td>The greater of two values. <br/> <strong>max</strong>(v,p1) <br/></td>
</tr>
<tr class="even">
<td>Mid</td>
<td>Average ( v + p1)/2</td>
</tr>
<tr class="odd">
<td>Min</td>
<td>The lesser of two values. <strong>min</strong>(v,p1)</td>
</tr>
<tr class="even">
<td>Mod</td>
<td>Modulus.</td>
</tr>
<tr class="odd">
<td>Product</td>
<td>Used for multiplication and division. v * p1 / p2</td>
</tr>
<tr class="even">
<td>Sin</td>
<td>Sine, argument in fd units (degrees multiplied by 65536). <br/> v * <strong>sin</strong>(p1) <br/></td>
</tr>
<tr class="odd">
<td>Sinatan2</td>
<td>Preserves full accuracy in intermediate calculation. v * <strong>sin</strong>(<strong>atan2</strong>(p2,p1))</td>
</tr>
<tr class="even">
<td>Sqrt</td>
<td>Result is positive and rounds down. <br/> <strong>sqrt</strong>(v) <br/></td>
</tr>
<tr class="odd">
<td>Sum</td>
<td>Used for addition and subtraction.<br/> v + p1 p2<br/></td>
</tr>
<tr class="even">
<td>Sumangle</td>
<td>Existing angle (scaled by 65536), where p1 and p2 are in degrees.<br/> v + p1 * 65536 + p2 * 65536<br/></td>
</tr>
<tr class="odd">
<td>Tan</td>
<td>Tangent, argument is in fd units (degrees multiplied by 65536). <br/> v * tan( p1 )<br/></td>
</tr>
<tr class="even">
<td>Val</td>
<td>Defines a guide value from some other value.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td>Param1</td>
<td><strong>Integer</strong>. The first parameter.</td>
</tr>
<tr class="odd">
<td>Paramtype1</td>
<td><strong>VgFormulaParamType</strong>. The type of the first parameter. The following values are supported: 
<table>
<thead>
<tr class="header">
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Value</td>
<td>Parameter is simple value.</td>
</tr>
<tr class="even">
<td>AdjustmentReference</td>
<td>Parameter is a reference to an adjustment. For example, if the first parameter is 1, then the value of the first adjustment will be used.</td>
</tr>
<tr class="odd">
<td>FormulaReference</td>
<td>Parameter is the result of a reference to the result of a previous formula. For example, if the first parameter is 2, then the result of formula 2 will be used.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="even">
<td>Param2</td>
<td><strong>Integer</strong>. The second parameter.</td>
</tr>
<tr class="odd">
<td>Paramtype2</td>
<td><strong>VgFormulaParamType</strong> The type of parameter 2.</td>
</tr>
<tr class="even">
<td>Val</td>
<td><strong>Integer</strong>. The result.</td>
</tr>
<tr class="odd">
<td>Valtype2</td>
<td><strong>VgFormulaParamType</strong>. The type of the result.</td>
</tr>
</tbody>
</table>



 

**IVgFixedRectangle**

Specifies a fixed rectangle.



| Attribute | Description                                                                                 |
|------------|---------------------------------------------------------------------------------------------|
| Value      | [String](#data-types-used-in-the-vml-object-model). Text value specifying the path.         |
| Left       | [Double](#data-types-used-in-the-vml-object-model). Leftmost coordinate of the rectangle.   |
| Top        | [Double](#data-types-used-in-the-vml-object-model). Topmost coordinate of the rectangle.    |
| Right      | [Double](#data-types-used-in-the-vml-object-model). Rightmost coordinate of the rectangle.  |
| Bottom     | [Double](#data-types-used-in-the-vml-object-model). Bottommost coordinate of the rectangle. |



 

**IVgFixedRectangleArray**

Array of fixed rectangles.



| Attribute | Description                                                                                                 |
|------------|-------------------------------------------------------------------------------------------------------------|
| Value      | [String](#data-types-used-in-the-vml-object-model). Text representation of array.                           |
| Length     | [Integer](#data-types-used-in-the-vml-object-model). Number of rectangles in this array.                    |
| Item       | [IVgFixedRectangle](#data-types-used-in-the-vml-object-model). The rectangle object at the specified index. |



 

**IVgFormula** data type

Definitions for formulas that can vary the path of a shape or be used for other calculation purposes. Formulas can be based on the **Adj** attribute of a shape, which can change. Formulas can reference other formulas as well.



| Attribute| Description                                           |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Eqn        | [IVgEquation](#data-types-used-in-the-vml-object-model). Each formula defines a single value as the result of the evaluation of the expression. The expression is defined by this attribute and has the general form of an operation followed by up to three arguments, which may be adjustment values (e.g., \#2), the results of earlier formulas (e.g., @2), fixed numbers, or predefined values. |



 

**IVgFormulas data type**

A collection of formula objects.



| Attribute | Description                                                                                                                                  |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Length     | [Integer](#data-types-used-in-the-vml-object-model). Number of formula objects in collection.                                                |
| Item       | [IVgFormula](#data-types-used-in-the-vml-object-model). A specific formula. Note that the formula array may be inherited fom the shape type. |



 

**IVgGradientColorArray**

An array of colors that define a gradient (blended range of colors).



| Attribute | Description                                                                                                                  |
|------------|------------------------------------------------------------------------------------------------------------------------------|
| Value      | [String](#data-types-used-in-the-vml-object-model). Specifies the array of colors; for example, "red .2; green .4; black .7" |
| Length     | [Integer](#data-types-used-in-the-vml-object-model). Number of colors in the array.                                          |



 



| Method     | Description                                                                                                                                                                                                      |
|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AddColor    | [VgFraction](msdn-online-vml-vgfraction-data-type.md). Adds new color at endpoint specified by fraction. The new color is white by default and is the return value. The color can then be changed by reference. |
| RemoveColor | [VgFraction](msdn-online-vml-vgfraction-data-type.md). Removes a color at endpoint specified by fraction. Note: if 0.0 or 1.0 does not exist, it is implied and the color white is used at that point.          |



 

**IVgPoints datatype**

Array of points that define a shape.



| Attribute | Description                                                                                 |
|------------|---------------------------------------------------------------------------------------------|
| Value      | [String](#data-types-used-in-the-vml-object-model). Text representation of array.           |
| Length     | [Integer](#data-types-used-in-the-vml-object-model). Number of points in this array.        |
| Item       | [IVgVector2D](msdn-online-vml-ivgvector2d-data-type.md). The point at the specified index. |



 

**IVgSkewMatrix datatype**

A matrix used for skewing shapes, a perspective transform matrix in the form, "*sxx,sxy,syx,syy,px,py* " \[*s* =scale, *p* =perspective\]. If offset is in absolute units, then *px,py* are in emu ^-1 units; otherwise they are an inverse fraction of shape size.



| Attribute   | Description                                         |
|--------------|-----------------------------------------------------|
| XtoX         | [Double](#data-types-used-in-the-vml-object-model). |
| YtoX         | [Double](#data-types-used-in-the-vml-object-model). |
| XtoY         | [Double](#data-types-used-in-the-vml-object-model). |
| YtoY         | [Double](#data-types-used-in-the-vml-object-model). |
| PerspectiveX | [Double](#data-types-used-in-the-vml-object-model). |
| PerspectiveY | [Double](#data-types-used-in-the-vml-object-model). |



 

**IVgSkewOffset**

Specifies the offset of the skew.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Attributes</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Value</td>
<td><a href="#data-types-used-in-the-vml-object-model">String</a>. Text representation of offset.</td>
</tr>
<tr class="even">
<td>X</td>
<td><a href="#data-types-used-in-the-vml-object-model">Double</a>. X component. Percentage or measure. If no units, then ShapeRelative type is implied; otherwise Absolute type is implied.</td>
</tr>
<tr class="odd">
<td>Y</td>
<td><a href="#data-types-used-in-the-vml-object-model">Double</a>. Y component.</td>
</tr>
<tr class="even">
<td>Type</td>
<td><strong>VgSkewTransformType</strong>. Specifies the type of transformation. Valid values are integer points ranging between -infinity and infinity. 
<table>
<thead>
<tr class="header">
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ShapeRelative</td>
<td>The values of the offset are percentages (ratios) of the original shape's size; e.g., a value of 0.5 means an offset half the size of the shape.</td>
</tr>
<tr class="even">
<td>Absolute</td>
<td>The values are absolute units.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>



 

**IVgVector2D data type**

Specifies a two-dimensional vector consisting of two **Double** numbers.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Attributes</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Value</td>
<td><strong>String</strong>. Text representation of both vector numbers separated by a space.</td>
</tr>
<tr class="even">
<td>X</td>
<td><a href="#data-types-used-in-the-vml-object-model">Double</a>. X component of this vector.</td>
</tr>
<tr class="odd">
<td>Y</td>
<td><a href="#data-types-used-in-the-vml-object-model">Double</a>. Y component of this vector.</td>
</tr>
<tr class="even">
<td>Type</td>
<td><strong>VgVectorType</strong>. Expected units for this vector. Values are:
<ul>
<li>Measure</li>
<li>Length</li>
<li>AngleInDegrees</li>
<li>Fraction</li>
<li>Number Percentage Integer</li>
</ul></td>
</tr>
</tbody>
</table>



 

**IVgVector3D data type**

Specifies a three-dimensional vector consisting of three **Double** numbers.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<tbody>
<tr class="odd">
<td>Value</td>
<td><strong>String</strong>. Text representation of three vector numbers separated by a space.</td>
</tr>
<tr class="even">
<td>X</td>
<td><a href="#data-types-used-in-the-vml-object-model">Double</a>. X component of this vector.</td>
</tr>
<tr class="odd">
<td>Y</td>
<td><a href="#data-types-used-in-the-vml-object-model">Double</a>. Y component of this vector.</td>
</tr>
<tr class="even">
<td>Z</td>
<td><a href="#data-types-used-in-the-vml-object-model">Double</a>. Z component of this vector.</td>
</tr>
<tr class="odd">
<td>Type</td>
<td><strong>VgVectorType</strong>. Expected units for this vector. Values are:
<ul>
<li>Measure</li>
<li>Length</li>
<li>AngleInDegrees</li>
<li>Fraction</li>
<li>Number</li>
<li>Percentage</li>
<li>Integer</li>
</ul></td>
</tr>
</tbody>
</table>



 

**Length data type**

A floating point number with a range from 0 to infinity.

**Measure data type**

A floating point number from -infinity to infinity.

**String data type**

Character data of any length.

**VgBlackWhiteMode**

Rendering mode for black and white. Possible values are:

-   **Color**
-   **Auto**
-   **GrayScale**
-   **LightGrayScale**
-   **InverseGray**
-   **GrayOutline**
-   **BlackTextAndLines**
-   **HighContrast**
-   **Black**
-   **White**
-   **Undrawn**

**VgFraction data type**

Floating point number with range from 0.0 to 1.0. Fractions can also be specified as a percentage; e.g., "50%".

**VgTriState datatype**

Enumeration used for values that can be one of three states:

-   **TRUE**
-   **FALSE**
-   **MIXED**
