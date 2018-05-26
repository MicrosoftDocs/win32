---
title: Changes to the XML Schema
description: Changes to the XML Schema
ms.assetid: f02856d3-8696-4247-ae95-e913f366fe01
keywords:
- Windows Movie Maker,XML schema changes
- Movie Maker,XML schema changes
- programming guide,XML schema changes
- XML,schema changes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Changes to the XML Schema

The following changes to the XML schema have been made for Windows Movie Maker 6.0. For more information, see [Windows Movie Maker XML Extensibility](windows-movie-maker-xml-extensibility.md).

-   The **version** attribute of the root **TransitionsAndEffects** element must be set to "2.8".
-   When you modify a built-in Windows Movie Maker transform, the **guid** attribute of the **TransitionDLL** or **EffectDLL** element must be set to "TFX". This applies to all built-in transforms.
-   The **Param** element now supports a new child element: **Point**. Each **Param** element supports zero or more **Point** elements. The **Point** element is used to specify the values of the parameter at specific times; therefore, when a **Param** element has **Point** child elements, it should not also have a **value** attribute. The **Point** element has the following attributes:

    -   **time** A numeric value from 0.0 (start) to 1.0 (end), specifying the point during the effect at which the value should be applied. If the parameter specifies a number larger than 1.0, the time will be scaled from 0.0 to the largest number specified.
    -   **value** The value to apply.

    The following code example demonstrates increasing the particle speed from 1 to 40 over the course of a shatter transition.

    ```C++
    <Param name="ParticleSpeed" />
        <Point time="0.0" value="1.0" />
        <Point time="1.0" value="40.0" />
    </Param>
    ```

    

-   Parameter (and point) values can now be arrays with up to 4 elements. To specify an array, include comma-delimited elements in the value string. For example, a three-element array with values of 1, 2, and 3 would be written this way:
    ```C++
    value="1,2,3" 
    ```

    

-   The **Param** element supports a new attribute, **curve**. This attribute specifies how the values in the element should change over time. The supported values are defined by the [**EVALUATION\_CURVE\_TYPE**](evaluation-curve-type.md) enumeration. For a description of the different curve types, see the enumeration documentation.
-   The **Transition** and **Effect** elements now accept two new attributes: **vertexShaderVersion** and **pixelShaderVersion**. These attributes specify the shader model hardware that is required to enable that specific effect or transition. If the computer does not have suitable hardware, the effect or transition will be marked as unavailable in the user interface. The following are the valid values for each attribute:

    -   **vertexShaderVersion**: "none", "1\_1", "2\_0", "2\_x", "3\_0"
    -   **pixelShaderVersion**: "none", "1\_1", "1\_2", "1\_3", "1\_4", "2\_0", "2\_x", "3\_0"

    For these values, "none" means that vertex or pixel shading is not required, and "2\_x" means that any version 2 shader will work. Windows Movie Maker 3 requires only version 2.0 for the effects that use vertex or pixel shading; if you choose a higher level of shader, some users may not be able to use your transform.

-   An alternate way of specifying parameter XML elements is now supported. Instead of using a **Param** element to specify a parameter in any **Effect** or **Transition** element, you can now add an element with the name of the parameter. For example, the following two code snippets are equivalent declarations of a *Color* parameter:

    ```C++
    <Effect>
        <Param name="Color" value="red"/>
    </Effect>

    <Effect>
        <Color value="red"/>
    </Effect>
    ```

    

    These custom child elements can have any non-reserved names, but cannot use any of the following three characters: ()/. Custom elements can contain child elements.

## Related topics

<dl> <dt>

[**Creating Custom Transforms Using XML**](creating-custom-transforms-using-xml.md)
</dt> </dl>

 

 




