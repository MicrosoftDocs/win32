---
description: This sample demonstrates the use of Windows Imaging Component (WIC) to decode an image that is encoded with progressive levels.
ms.assetid: 14018dce-26f0-4e1e-9d19-c5b42dd2cdab
title: WIC progressive decoding sample
ms.topic: article
ms.date: 03/19/2021
ms.custom: project-verbatim
---

# WIC progressive decoding sample

This sample demonstrates the use of Windows Imaging Component (WIC) to decode an image that is encoded with progressive levels. This sample uses Direct2D to render the different progressive levels to the screen.

## Requirements

This sample has the following requirements.

| Requirement | Value |
|-|
| Minimum supported client | Windows 7 |
| Minimum Windows SDK | [Windows Software Development Kit (SDK)](https://msdn.microsoft.com/windowsvista/bb980924.aspx) for Windows 7 |

## Downloading the sample

This sample is available at [WIC progressive encoding](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/multimedia/wic/progressivedecoding).

## Building the sample

### Using Visual Studio (preferred method)

1. Open Windows Explorer and navigate to the directory.
2. Double-click the icon for the .sln (solution) file to open the file in Visual Studio.
3. In the Build menu, select Build Solution. The application will be built in the default \\Debug or \\Release directory.

### Using the command prompt

To build the sample using the command prompt.

1. Open the command prompt and navigate to the sample directory.
2. Type `msbuild WICProgressiveDecoding.sln`

## Running the sample

After the application is launched, load an image file through file open menu. On loading, the default progressive level is set to 0. You can navigate to different progressive levels either through menu or Up/Down key. The current progressive level text is displayed on the main window status bar. Window resizing is supported.

> [!NOTE]
> Progressive decoding is available only for images that have been progressively encoded. The image provided with this sample has been progressively encoded.

## See also

[Microsoft Windows Imaging Codec](-wic-lh.md)

[Programming guide](-wic-programming-guide.md)

[Reference](-wic-codec-reference.md)

[Direct2D](../direct2d/direct2d-portal.md)

[Samples and code examples](-wic-samples.md)

[Progressive decoding overview](-wic-progressive-decoding.md)
