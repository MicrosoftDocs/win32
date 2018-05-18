---
title: Creating Custom Transforms Using XML
description: Creating Custom Transforms Using XML
ms.assetid: 'e9fa51a1-3b0b-4d56-a4d4-d4a9cf0eff57'
keywords: ["Windows Movie Maker,creating custom transforms", "Movie Maker,creating custom transforms", "Windows DVD Maker,creating custom transforms", "DVD Maker,creating custom transforms", "programming guide,creating custom transforms", "creating custom transforms using XML,about", "XML,creating custom transforms", "transforms,creating using XML", "custom transforms,creating using XML"]
---

# Creating Custom Transforms Using XML

When Windows Movie Maker or Windows DVD Maker starts, it loads one or more XML initialization files that specify all the effects and transitions that it should expose. In addition, these files can also specify custom buttons and menu styles for Windows DVD Maker.

The XML files specify one or more DLLs to load, specify effects and transitions exposed by the DLL, and assign a display name and image to represent each transition and effect in the Windows Movie Maker or Windows DVD Maker user interface. In addition, the files can contain the XML that defines the layout and all textual and graphical elements of Windows DVD Maker buttons and menu styles.

The built-in effects, transitions, buttons, and menu styles in Windows Movie Maker and Windows DVD Maker are defined similarly, within several private XML files. Although you cannot view or change these files, this documentation describes how to create your own XML files that define custom transforms based on the built-in transforms. For your reference, the contents of the Windows Movie Maker private XML file are provided in [Transition and Effect Objects Provided by Windows Movie Maker](transition-and-effect-objects-provided-by-windows-movie-maker.md). More detailed information, including descriptions of most extensible parameters, is provided in [Windows Movie Maker XML Extensibility](windows-movie-maker-xml-extensibility.md). In addition, one sample custom Windows DVD Maker transition, button, and menu style are provided and annotated in [Windows DVD Maker XML Extensibility](windows-dvd-maker-xml-extensibility.md).

Both Windows Movie Maker and Windows DVD Maker store their built-in effects and transitions as COM objects inside one of several DLLs provided with the programs. Each COM object is identified by a globally unique identifier (GUID). One DLL can contain several COM objects. Each object has zero or more parameters—such as color or brightness—that can be set for that transform. The XML file specifies which objects to load and sets values for any number of those objects' parameters. An object can be loaded more than once, using different parameters, to create different effects or transitions based on the same object. For example, the slow-motion and fast-motion effects are the same object, differing only in the value of the speed parameter passed in. After learning how these transforms are addressed in the XML file, you will be able to make your own transforms from the COM objects provided.

**Notes** To install custom transforms, you must have administrator privileges on your computer.

XML file parsing in Windows Movie Maker is case sensitive.

This section includes the following topics.



| Topic                                                                                                                              | Description                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| [Reading the XML File](reading-the-xml-file.md)                                                                                   | Shows a segment of a Windows Movie Maker private XML file with a sample transition and effect. |
| [Making Your Own XML File](making-your-own-xml-file.md)                                                                           | Provides a tutorial on how to create your own initialization XML file.                         |
| [Transition and Effect Objects Provided by Windows Movie Maker](transition-and-effect-objects-provided-by-windows-movie-maker.md) | Lists all the base transition and effect objects that Windows Movie Maker provides.            |
| [Changes to the XML Schema](changes-to-the-xml-schema.md)                                                                         | Details the changes that have been made to the schema since Windows Movie Maker 2.1.           |



 

## Related topics

<dl> <dt>

[**Programming Guide**](programming-guide.md)
</dt> </dl>

 

 




