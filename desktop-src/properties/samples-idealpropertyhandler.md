---
Description: Demonstrates the implementation of an ideal property handler for an OleDoc file format (.docfile-ms) or a fictional OpenMetadata format (.openmetadata-ms) which supports reading and writing properties and custom schema.
ms.assetid: F277D4DF-1EA8-4603-B2C9-B607D2A9FC36
title: Ideal Property Handler Sample
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Ideal Property Handler Sample

Demonstrates the implementation of an ideal property handler for an OleDoc file format (.docfile-ms) or a fictional OpenMetadata format (.openmetadata-ms) which supports reading and writing properties and custom schema.

This topic contains the following sections.

-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)
-   [Removing the Sample](#removing-the-sample)
-   [Related topics](#related-topics)

## Requirements



| Product                                | Minimum Product Version |
|----------------------------------------|-------------------------|
| Windows                                | Windows Vista           |
| Windows Software Development Kit (SDK) | 7.0                     |



 

## Downloading the Sample

This sample is available in the following locations.



| Location      | Path URL                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------|
| Code Gallery  | [Windows Shell Integration Samples on Code Gallery](http://go.microsoft.com/fwlink/p/?linkid=155659) |
| Windows 7 SDK | [Download Windows 7 SDK](http://go.microsoft.com/fwlink/p/?linkid=129787)                            |



 

In the case of the Windows SDK, once you have downloaded and installed it, you will find the samples in the installed directory. For example, use of the default installation path for the Windows 7 SDK results in the samples being placed under `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\`.

## Building the Sample

To build the sample from the command prompt:

1.  Open the command prompt window and navigate to the **IdealPropertyHandler** project directory.
2.  Enter `msbuild PropertyHandler.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **IdealPropertyHandler** project directory.
2.  Double-click the icon for the PropertyHandler.sln file to open the project in Visual Studio.
3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the new DLL file, using the command prompt or Windows Explorer.
2.  At the command line, enter `regsvr32.exe PropertyHandler.exe`.
3.  New sample files can be created by selecting either **DocFile File** or **Open Metadata File** from the **New** submenu of a view's shortcut menu.

## Removing the Sample

1.  From the command prompt, navigate to the directory that contains the DLL file.
2.  Type `regsvr32.exe /u PropertyHandler.dll`
3.  Delete the folder that contains the sample's source files.

## Related topics

<dl> <dt>

[Property System Code Samples](property-system-code-samples.md)
</dt> <dt>

[Playlist Property Handler Sample](https://www.bing.com/search?q=Playlist+Property+Handler+Sample)
</dt> <dt>

[Property Edit Sample](https://www.bing.com/search?q=Property+Edit+Sample)
</dt> <dt>

[Property Schema Sample](https://www.bing.com/search?q=Property+Schema+Sample)
</dt> <dt>

[Recipe Property Handler Sample](https://www.bing.com/search?q=Recipe+Property+Handler+Sample)
</dt> </dl>

 

 



