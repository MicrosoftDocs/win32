---
title: Preview Ribbon Sample
description: Preview Ribbon is an open-source prototyping application for the Windows Ribbon framework that generates a functional preview of the ribbon command bar from a Ribbon framework markup file \ 8212;without the need to implement any underlying command code.
ms.assetid: aec52d8d-d9e1-4a12-a4a9-cf25b9ca7cce
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Preview Ribbon Sample

Preview Ribbon is an open-source prototyping application for the Windows Ribbon framework that generates a functional preview of the ribbon command bar from a Ribbon framework markup file without the need to implement any underlying command code.

-   [Description](#description)
-   [Usage](#usage)
    -   [Building the Sample](#building-the-sample)
    -   [Running the Sample](#running-the-sample)
-   [Support](#support)
-   [Minimum Requirements](#minimum-requirements)

## Description

The markup file is compiled by the Preview Ribbon application into a standard Ribbon framework binary resource. This binary resource is then processed by the application to simulate the visual style, control layout, and basic command functionality of the prototype ribbon command bar.

> [!Note]  
> As a Windows Forms application, the Preview Ribbon code includes a sample implementation of lightweight managed wrappers for the Ribbon framework native APIs.

 

In addition to generating a preview of a ribbon command bar, Preview Ribbon supports the following functionality:

-   Displays all compiler output, including error, warning, and informational messages, in a command line window.
-   Allows custom ribbon color settings to be specified in a configuration file.
-   Allows custom locations for markup compiler files (Link.exe, RC.exe, and UICC.exe) to be specified in a configuration file.
-   Identifies and exposes all application modes, contextual tabs, and context maps.
-   Provides the ability to enable and disable application modes and contextual tabs at run time.
-   Allows ribbon color settings to be specified from a set of default colors at run time.

The following screen shot shows the Preview Ribbon application and a basic one button ribbon prototype.

![screen shot showing the preview ribbon application and a basic one button ribbon prototype.](images/samples/previewribbon.png)

## Usage

The [Preview Ribbon Code Sample](http://go.microsoft.com/fwlink/p/?linkid=177607) can be downloaded as a standalone Microsoft Visual Studio project from the [MSDN Code Gallery](http://go.microsoft.com/fwlink/p/?linkid=177607).

### Building the Sample

Download the sample to your hard disk.

Install the Windows Software Development Kit (SDK) for Windows 7 and open its build environment command window. On the Start menu, point to All Programs, Microsoft Windows SDK, and then click CMD Shell.

To build the sample from the build environment command window, go to the source directory of the sample. At the command prompt, type MSBUILD.

To build the sample in Microsoft Visual Studio, load the sample solution or project file and then press CTRL+SHIFT+B.

The Preview Ribbon executable requires the Windows SDK for Windows 7. Specifically it requires access to three companion executables: UICC.exe, RC.exe, and link.exe. The application searches commonly used directories for these files and displays an error if they cannot be found.

### Running the Sample

To run the sample from the build environment command window, execute the .exe files in the Bin\\Debug or Bin\\Release folder contained in the sample source folder.

To run the compiled sample with debugging in Visual Studio, press F5.

**PreviewRibbon.exe.config**

-   Custom locations for the three companion executables can be specified in the PreviewRibbon.exe.config file by removing the comment delimiters on the UiccPath, RCExePath, and LinkExePath lines.
    > [!Note]  
    > Fully qualified paths must be used.

     

-   Custom ribbon color values can be specified in the PreviewRibbon.exe.config file (the Preview Ribbon application provides a selection of predefined color values). Remove the comment delimiters on the ColorizationValues line and replace the default values with custom values.
    > [!Note]  
    > Comment the ColorizationValues line in the PreviewRibbon.exe.config and restart the application to restore the Preview Ribbon default ribbon color values.

     

**PreviewRibbon.exe**

-   The Preview Ribbon executable takes a path to a valid ribbon markup file as an argument.
-   The Preview Ribbon command-line syntax is shown in the following example.
    ```
    RibbonPreview.exe BasicRibbon.xml
    ```

    

-   To start the Preview Ribbon application from Windows Explorer, drag and drop a valid ribbon markup file on top of the executable.
    > [!Note]  
    > Compiler messages are not displayed with this method.

     

-   The Preview Ribbon application can be used as an external tool within Visual Studio 2008. On the Tools menu, click External Tools..., and add the Preview Ribbon application.

## Support

The [Windows Ribbon Development Forum](http://go.microsoft.com/fwlink/p/?linkid=156613) is available to discuss topics and ask questions related to developing Windows Ribbon applications.

## Minimum Requirements



|                          |                                                                                                                                                                          |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 7<br/> Windows Vista with Service Pack 2 (SP2) and [Platform Update for Windows Vista](http://go.microsoft.com/fwlink/p/?linkid=166272)<br/>         |
| Minimum supported server | Windows Server 2008 R2<br/> Windows Server 2008 with SP2 and [Platform Update for Windows Server 2008](http://go.microsoft.com/fwlink/p/?linkid=166272)<br/> |
| Windows SDK              | 7.0                                                                                                                                                                      |
| Visual Studio            | 2008                                                                                                                                                                     |
| Header and IDL files     | uiribbon.h, uiribbon.idl                                                                                                                                                 |



 

> [!Note]  
> The [Platform Update for Windows Vista](http://go.microsoft.com/fwlink/p/?linkid=166272) and [Platform Update for Windows Server 2008](http://go.microsoft.com/fwlink/p/?linkid=166272) are sets of run-time libraries that enable developers to target Windows Ribbon applications to both Windows Vista and Windows Server 2008. The platform updates will be available to all Windows Vista and Windows Server 2008 customers through Windows Update. Third-party applications that require [Platform Update for Windows Vista](http://go.microsoft.com/fwlink/p/?linkid=166272) or [Platform Update for Windows Server 2008](http://go.microsoft.com/fwlink/p/?linkid=166272) can have Windows Update detect whether the required update is installed. If it is not, Windows Update will download and install it in the background.

 

 

 





