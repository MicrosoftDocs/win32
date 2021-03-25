---
description: This sample demonstrates decoding various frames in a GIF file, reading appropriate metadata for each frame, composing frames, and rendering the animation with Direct2D.
ms.assetid: d71c66b5-d37c-4c8a-bfd7-b97c69c3b8e9
title: WIC Animated Gif Sample
ms.topic: article
ms.date: 03/19/2021
ms.custom: project-verbatim
---

# WIC animated GIF sample

This sample demonstrates decoding various frames in a GIF file, reading appropriate metadata for each frame, composing frames, and rendering the animation with Direct2D.

## Requirements

This sample has the following requirements.

| Requirement | Value |
|-|-|
| Minimum supported client | Windows 7 |
| Minimum Windows SDK | [Windows Software Development Kit (SDK)](https://msdn.microsoft.com/windowsvista/bb980924.aspx) for Windows 7 |

## Downloading the sample

This sample is available at [WIC animated GIF](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/multimedia/wic/wicanimatedgif).

## Building the sample

### Using Visual Studio (preferred method)

1. Open Windows Explorer and navigate to the directory.
2. Double-click the icon for the .sln (solution) file to open the file in Visual Studio.
3. In the **Build** menu, select **Build Solution**. The application will be built in the default \\Debug or \\Release directory.

### Using the command prompt

To build the sample by using a command prompt.

1. Open the command prompt and navigate to the sample directory.
2. Type `msbuild WICAnimatedGif.sln`

## Running the sample

After the application is launched, load an image file by using the **Open** command of the **File** menu. Window resizing is supported.

## See also

[Microsoft Windows Imaging Codec](-wic-lh.md)

[Programming guide](-wic-programming-guide.md)

[Reference](-wic-codec-reference.md)

[Direct2D](../direct2d/direct2d-portal.md)

[Samples and code examples](-wic-samples.md)
