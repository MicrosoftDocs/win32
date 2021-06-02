---
description: This sample demonstrates the use of Windows Imaging Component (WIC) to decode an image file, and Direct2D to render the image to the screen.
ms.assetid: 4f989ff6-b513-4354-a1bb-8d9521f693a2
title: WIC image viewer using Direct2D sample
ms.topic: article
ms.date: 03/19/2021
ms.custom: project-verbatim
---

# WIC image viewer using Direct2D sample

This sample demonstrates the use of Windows Imaging Component (WIC) to decode an image file and Direct2D to render the image to the screen.

## Requirements

This sample has the following requirements.

| Requirement | Value |
|-|-|
| Minimum supported client | Windows Vista |
| Minimum Windows SDK | [Windows Software Development Kit (SDK)](https://msdn.microsoft.com/windowsvista/bb980924.aspx) for Windows 7 |

## Downloading the sample

This sample is available at [WIC Viewer D2D](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/multimedia/wic/wicviewerd2d).

## Building the sample

### Using Visual Studio (preferred method)

1. Open Windows Explorer and navigate to the directory.
2. Double-click the icon for the .sln (solution) file to open the file in Visual Studio.
3. In the **Build** menu, select **Build Solution**. The application will be built in the default \\Debug or \\Release directory.

### Using the command prompt

To build the sample by using a command prompt:

1. Open a command prompt window and navigate to the sample directory.
2. Type `msbuild WICViewerD2D.sln`

## Running the sample

After you start the application, load an image file by using the **Open** command of the **File** menu.

## See also

[Microsoft Windows Imaging Codec](-wic-lh.md)

[Programming guide](-wic-programming-guide.md)

[Reference](-wic-codec-reference.md)

[Direct2D](../direct2d/direct2d-portal.md)

[Samples and code examples](-wic-samples.md)
