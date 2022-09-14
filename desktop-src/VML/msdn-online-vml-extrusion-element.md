---
title: VML Extrusion Element
description: VML Extrusion Element
ms.assetid: d26b2451-383a-4ded-a46d-5ecca05ddb7f
ms.topic: article
ms.date: 05/31/2018
---

# VML Extrusion Element

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

Defines an extrusion for a shape.

The following attributes modify an extrusion.



| Attribute                                                              | Description                                                                                             |
|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [AutoRotationCenter](msdn-online-vml-autorotationcenter-attribute.md) | Determines whether the center of rotation will be the geometric center of the extrusion.                |
| [BackDepth](msdn-online-vml-backdepth-attribute.md)                   | Defines the amount of backward extrusion.                                                               |
| [Brightness](msdn-online-vml-brightness-attribute.md)                 | Specifies the amount of brightness of a scene.                                                          |
| [Color](color-attribute--extrusion--vml.md)                           | Defines the color of the extrusion faces.                                                               |
| [ColorMode](msdn-online-vml-colormode-attribute.md)                   | Determines the mode of extrusion color.                                                                 |
| [Diffusity](msdn-online-vml-diffusity-attribute.md)                   | Defines the amount of diffusion of reflected light from an extruded shape.                              |
| [Edge](msdn-online-vml-edge-attribute.md)                             | Defines the apparent bevel of the extrusion edges.                                                      |
| [Ext](ext-attribute--extrusion--vml.md)                               | Defines the default extrusion behavior for graphical editors.                                           |
| [Facet](msdn-online-vml-facet-attribute.md)                           | Defines the number of facets used to describe curved surfaces of an extrusion.                          |
| [ForeDepth](msdn-online-vml-foredepth-attribute.md)                   | Defines the amount of forward extrusion.                                                                |
| [LightFace](msdn-online-vml-lightface-attribute.md)                   | Determines whether the front face of the extrusion will respond to changes in the lighting.             |
| [LightHarsh](msdn-online-vml-lightharsh-attribute.md)                 | Determines whether the primary light source will be harsh.                                              |
| [LightHarsh2](msdn-online-vml-lightharsh2-attribute.md)               | Determines whether the secondary light source will be harsh.                                            |
| [LightLevel](msdn-online-vml-lightlevel-attribute.md)                 | Defines the intensity of the primary light source for the scene.                                        |
| [LightLevel2](msdn-online-vml-lightlevel2-attribute.md)               | Defines the intensity of the secondary light source for the scene.                                      |
| [LightPosition](msdn-online-vml-lightposition-attribute.md)           | Specifies the position of the primary light in a scene.                                                 |
| [LightPosition2](msdn-online-vml-lightposition2-attribute.md)         | Specifies the position of the secondary light in a scene.                                               |
| [LockRotationCenter](msdn-online-vml-lockrotationcenter-attribute.md) | Determines whether the rotation of the extruded object is specified by the **RotationAngle** attribute. |
| [Metal](msdn-online-vml-metal-attribute.md)                           | Determines whether the surface of the extruded shape will resemble metal.                               |
| [On](on-attribute--extrusion--vml.md)                                 | Determines whether an extrusion will be displayed.                                                      |
| [Orientation](msdn-online-vml-orientation-attribute.md)               | Specifies the vector around which a shape will be rotated.                                              |
| [OrientationAngle](msdn-online-vml-orientationangle-attribute.md)     | Defines the angle that an extrusion rotates around the orientation.                                     |
| [Plane](msdn-online-vml-plane-attribute.md)                           | Specifies the plane that is at right angles to the extrusion.                                           |
| [Render](msdn-online-vml-render-attribute.md)                         | Defines the rendering mode of the extrusion.                                                            |
| [RotationAngle](msdn-online-vml-rotationangle-attribute.md)           | Specifies the rotation of the object about the x- and y-axes.                                           |
| [RotationCenter](msdn-online-vml-rotationcenter-attribute.md)         | Specifies the center of rotation for a shape.                                                           |
| [Shininess](msdn-online-vml-shininess-attribute.md)                   | Defines the concentration of reflected light of an extrusion surface.                                   |
| [SkewAmt](msdn-online-vml-skewamt-attribute.md)                       | Defines the amount of skew of an extrusion.                                                             |
| [SkewAngle](msdn-online-vml-skewangle-attribute.md)                   | Defines the angle of skew of an extrusion.                                                              |
| [Specularity](msdn-online-vml-specularity-attribute.md)               | Defines the specularity of an extruded shape.                                                           |
| [Type](type-attribute--extrusion--vml.md)                             | Defines the way that the shape is extruded.                                                             |
| [Viewpoint](msdn-online-vml-viewpoint-attribute.md)                   | Defines the viewpoint of the observer.                                                                  |
| [ViewpointOrigin](msdn-online-vml-viewpointorigin-attribute.md)       | Defines the origin of the viewpoint within the bounding box of the shape.                               |



 

**Remarks**

This element must be defined within a [Shape](shape-element--vml.md) element.

In addition, the [On](on-attribute--extrusion--vml.md) attribute must be set to **True**.

The following is the minimum code needed to produce an extrusion.


```HTML
   <v:rect style="width:50px;height:50px">
   <v:extrusion on="True"/>
   </v:rect>
```



**Examples**

-   [Simple Shape Extrusion](/previous-versions/bb229656(v=vs.85))
-   [Dynamic Shape Extrusion](/previous-versions/bb229657(v=vs.85))

 

 