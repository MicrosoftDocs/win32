---
title: About the Windows Movie Maker and Windows DVD Maker SDK
description: About the Windows Movie Maker and Windows DVD Maker SDK
ms.assetid: '32b5c064-3199-45ec-a8ac-fd6064378cd7'
keywords: ["Windows Movie Maker,about", "Movie Maker,about", "Windows DVD Maker,about", "DVD Maker,about", "Windows Movie Maker,software development kit (SDK)", "Movie Maker,software development kit (SDK)", "Windows DVD Maker,software development kit (SDK)", "DVD Maker,software development kit (SDK)", "Windows Movie Maker SDK", "Movie Maker SDK", "Windows DVD Maker SDK", "DVD Maker SDK", "transitions,about", "effects,about", "transforms,about"]
---

# About the Windows Movie Maker and Windows DVD Maker SDK

Microsoft Windows Movie Maker 2 enabled developers to load their own custom effects and transitions—generically called *transforms* —into the Windows Movie Maker interface. Both Windows Movie Maker 6.0 in Windows Vista and Windows DVD Maker 1.0 in Windows Vista implement their transforms using Microsoft Direct3D and hardware acceleration, enabling broader and more sophisticated customization.

The documentation for this SDK demonstrates both how to create custom effects and transitions for Windows Movie Maker, and how to create custom transitions, buttons, and menu styles for Windows DVD Maker. Specifically, the documentation does the following:

-   Explains how to create a custom transform in XML by modifying the parameters of existing Windows Movie Maker and Windows DVD Maker effects and transitions.
-   Demonstrates how to create your own custom buttons and menu styles in Windows DVD Maker by using XML.
-   Describes how to create your own original transforms by using the Component Object Model (COM) and Direct3D.

This SDK documentation covers both the XML file that Windows Movie Maker and Windows DVD Maker use to load your transform and how to code the actual COM transform. (To use the APIs documented in [Windows Movie Maker APIs](windows-movie-maker-apis.md), you must include certain files as described in [Samples](samples.md).) Some changes to the XML schema have been made since Windows Movie Maker 2, and these are documented in [Changes to the XML Schema](changes-to-the-xml-schema.md).

To create a transform, you must understand COM and Direct3D and how to create installation packages for components. Some experience with XML is also helpful.

This documentation assumes knowledge of Active Template Library (ATL), which, though not necessary to build a transform, simplifies its coding.

**What's New in Windows Movie Maker 6.0**

-   Transforms are built on Direct3D.
-   Transforms use hardware acceleration to increase performance. (Computers must support hardware acceleration to use Windows Movie Maker 6.0 and Windows DVD Maker 1.0.)
-   You can now specify parameter changes at specific playback times in the XML initialization file by using the new **Point** element. For information about the **Point** element, see [Changes to the XML Schema](changes-to-the-xml-schema.md).

**Important** Transforms that you create for Windows Movie Maker 6.0 will not work with earlier versions of Windows Movie Maker, and transforms created for earlier versions of Windows Movie Maker will not work in Windows Movie Maker 6.0 or Windows DVD Maker 1.0.

Only video transforms are currently supported.

## Related topics

<dl> <dt>

[**Windows Movie Maker 6.0 and Windows DVD Maker 1.0 SDK**](windows-movie-maker-6-0-and-windows-dvd-maker-1-0-sdk.md)
</dt> </dl>

 

 




