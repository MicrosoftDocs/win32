---
title: Developer Overview
description: Developer Overview
ms.assetid: 72a330b4-5957-4159-b5e8-0c9a4491b589
keywords:
- Windows Media Player plug-ins,visualizations
- plug-ins,visualizations
- visualizations,developer overview
- custom visualizations,developer overview
- visualizations,COM controls
- custom visualizations,COM controls
- visualizations,audio input
- custom visualizations,audio input
- visualizations,graphical output
- custom visualizations,graphical output
- visualizations,drawing tools
- custom visualizations,drawing tools
- visualizations,programming language
- custom visualizations,programming language
- visualizations,Visual C++
- custom visualizations,Visual C++
- visualizations,plug-in wizard
- custom visualizations,plug-in wizard
- plug-in wizard
ms.topic: article
ms.date: 05/31/2018
---

# Developer Overview

From the developer's point of view, visualizations are software programs that take audio data provided by Windows Media Player and convert that data to graphics that will please the eye of the user. The main subjects a developer needs to understand to create a new visualization are the following:

## Visualization Packaging

Visualizations are COM controls that Windows Media Player uses to turn audio waveforms into animated graphics in Microsoft Windows. The COM controls are packaged as Microsoft Windows dynamic-link libraries (DLLs) and must be registered in the Windows registry. When Windows Media Player runs, registered custom visualizations are loaded and viewed in accordance with the instructions of the skin that Windows Media Player is using.

## Audio Input

Windows Media Player provides your code with snapshots of audio frequency and waveform data at timed intervals measured in fractions of a second. The snapshot interval is internally determined by the Windows Media Player.

## Graphical Output

The graphical output from your visualization is a Microsoft Windows device context. This is a standard Windows drawing surface that you can draw upon every time an audio snapshot is provided. All of the background Windows technology is taken care of for you. You just have to draw on the device context with the audio data provided.

## Drawing Tools

You can draw on the device context with standard Microsoft Windows Graphics Device Interface (GDI) functions, using pens and brushes to create designs that are modified by the audio data supplied to you by Windows Media Player. GDI provides a rich set of drawing tools that can create many kinds of visual effects.

## Programming Language

Microsoft Visual C++ 6.0 and higher is the only supported language for creating custom visualizations.

## Plug-in Wizard

Windows Media Player provides a COM wizard that you can add to Visual C++ that will generate the underlying code needed for your visualization. Not only are all source files provided, but a sample skin is generated to make it easy to test your visualization. The generated code creates a visualization similar to Bars, with two presets. You can then modify the code to create your own visualization. A registry file is also generated to register your visualization so that Windows Media Player can load it.

The following topic describes how visualization code processes audio data:

-   [Flow of Control](flow-of-control.md)

## Related topics

<dl> <dt>

[**About Custom Visualizations**](about-custom-visualizations.md)
</dt> </dl>

 

 




