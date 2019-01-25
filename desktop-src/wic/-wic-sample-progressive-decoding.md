---
Description: This sample demonstrates the use of Windows Imaging Component (WIC) to decode an image that is encoded with progressive levels.
ms.assetid: 14018dce-26f0-4e1e-9d19-c5b42dd2cdab
title: WIC Progressive Decoding Sample
ms.topic: article
ms.date: 05/31/2018
---

# WIC Progressive Decoding Sample

This sample demonstrates the use of Windows Imaging Component (WIC) to decode an image that is encoded with progressive levels. This sample uses Direct2D to render the different progressive levels to the screen.

This topic contains the following sections.

-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
    -   [Using Visual Studio 2008 (preferred method)](#using-visual-studio-2008-preferred-method)
    -   [Using the Command Prompt](#using-the-command-prompt)
-   [Running the Sample](#running-the-sample)
-   [See Also](#see-also)

## Requirements

This sample has the following requirements.



|                          |                                                                                                         |
|--------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 7                                                                                               |
| Windows SDK              | [Windows Software Development Kit (SDK)](https://go.microsoft.com/fwlink/p/?linkid=129787) for Windows 7 |



 

## Downloading the Sample

This sample is available in the following locations.



| Location     | Path/URL                                                                                                                                                                              |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Windows SDK  | \\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\multimedia\\wic\\ProgressiveDecoding\\ (Download the SDK at [Windows SDK](https://go.microsoft.com/fwlink/p/?linkid=129787).) |
| Code Gallery | [Windows Imaging Component Progressive Decode Win32 Sample](https://code.msdn.microsoft.com/Windows-Imaging-Component-3af3cd49)                                                       |



 

## Building the Sample

### Using Visual Studio 2008 (preferred method)

1.  Open Windows Explorer and navigate to the directory.
2.  Double-click the icon for the .sln (solution) file to open the file in Visual Studio.
3.  In the Build menu, select Build Solution. The application will be built in the default \\Debug or \\Release directory.

### Using the Command Prompt

To build the sample using the command prompt:

1.  Open the command prompt and navigate to the sample directory.
2.  Type `msbuild WICProgressiveDecoding.sln`

## Running the Sample

After the application is launched, load an image file through file open menu. On loading, the default progressive level is set to 0. The user can navigate to different progressive levels either through menu or Up/Down key. The current progressive level text is displayed on the main window status bar. Window resizing is supported.

> [!Note]  
> Progressive decoding is only available for images that have been progressively encoding. The image provided with this sample has been progressively encoded.

 

## See Also

[Microsoft Windows Imaging Codec](-wic-lh.md)


[Programming Guide](-wic-programming-guide.md)


[References](-wic-codec-reference.md)


[Samples and Code Examples](-wic-samples.md)


[Progressive Decoding Overview](-wic-progressive-decoding.md)


 

 



