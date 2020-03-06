---
Description: This sample demonstrates the use of Windows Imaging Component (WIC) to decode an image file and Direct2D to render the image to the screen.
ms.assetid: 4f989ff6-b513-4354-a1bb-8d9521f693a2
title: WIC Image Viewer Using Direct2D Sample
ms.topic: article
ms.date: 05/31/2018
---

# WIC Image Viewer Using Direct2D Sample

This sample demonstrates the use of Windows Imaging Component (WIC) to decode an image file and Direct2D to render the image to the screen.

This topic contains the following sections.

-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
    -   [Using Visual Studio 2008 (preferred method)](#using-visual-studio-2008-preferred-method)
    -   [Using the Command Prompt](#using-the-command-prompt)
-   [Running the Sample](#running-the-sample)
-   [See Also](#see-also)

## Requirements

This sample has the following requirements:



|                          |                                                                                                         |
|--------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client | Windows Vista                                                                                           |
| Windows SDK              | [Windows Software Development Kit (SDK)](https://msdn.microsoft.com/windowsvista/bb980924.aspx) for Windows 7 |



 

## Downloading the Sample

This sample is available in the following locations:



| Location     | Path/URL                                                                                                                               |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Windows SDK  | \\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\multimedia\\wic\\WICViewerD2D\\                                               |
| Code Gallery | [Windows Imaging Component and Direct2D Image Viewer Win32 Sample](https://code.msdn.microsoft.com/Windows-Imaging-Component-c5191dfc) |



 

## Building the Sample

### Using Visual Studio 2008 (preferred method)

1.  Open Windows Explorer and navigate to the directory.
2.  Double-click the icon for the .sln (solution) file to open the file in Visual Studio.
3.  In the **Build** menu, select **Build Solution**. The application will be built in the default \\Debug or \\Release directory.

### Using the Command Prompt

To build the sample by using a command prompt:

1.  Open a command prompt window and navigate to the sample directory.
2.  Type `msbuild WICViewerD2D.sln`

## Running the Sample

After you start the application, load an image file by using the **Open** command of the **File** menu.

## See Also

[Microsoft Windows Imaging Codec](-wic-lh.md)


[Programming Guide](-wic-programming-guide.md)


[References](-wic-codec-reference.md)


[Direct2D](https://msdn.microsoft.com/library/dd370990(VS.85).aspx)


[Samples and Code Examples](-wic-samples.md)


 

 



