---
title: Ribbon Development Introductory Tutorial
description: This tutorial and accompanying code samples are intended for C++ developers who develop desktop applications and want to take advantage of the Windows Ribbon framework.
ms.assetid: f814883f-df5c-4b61-842f-eaa176f9bde6
ms.topic: article
ms.date: 05/31/2018
---

# Ribbon Development Introductory Tutorial

This tutorial and accompanying code samples are intended for C++ developers who develop desktop applications and want to take advantage of the Windows Ribbon framework. The tutorial steps you through adding an empty Ribbon to a small application, adding controls with icons, labels, and other resources to the Ribbon, and then connecting the controls to the existing command infrastructure of the application. You learn how the API maintains separation between control organization and event handling. Finally, the tutorial demonstrates how to specify layouts and resizing behavior to show how the Ribbon adapts and performs at different sizes. When you finish, you will have performed all the steps to add and customize a basic Ribbon application.

-   [Usage](#usage)
    -   [Building the Sample](#building-the-sample)
    -   [Running the Sample](#running-the-sample)
-   [Support](#support)
-   [Minimum Requirements](#minimum-requirements)

## Usage

The [Ribbon Development Introductory Tutorial](https://www.microsoft.com/downloads/details.aspx?familyid=f62039ad-a224-4979-ae7f-67b4e09cd81e&displaylang=en) sample can be downloaded as a standalone Microsoft Visual Studio project from the [Microsoft Download Center](https://www.microsoft.com/DOWNLOADS/en/default.aspx).

### Building the Sample

Download the sample to your hard disk.

Install the Windows Software Development Kit (SDK) for Windows 7 and open its build environment command window. On the Start menu, point to All Programs, Microsoft Windows SDK, and then click CMD Shell.

To build the sample from the build environment command window, go to the source directory of the sample. At the command prompt, type MSBUILD.

To build the sample in Microsoft Visual Studio, load the sample solution or project file and then press CTRL+SHIFT+B.

### Running the Sample

To run the sample from the build environment command window, execute the .exe files in the Bin\\Debug or Bin\\Release folder contained in the sample source folder.

To run the compiled sample with debugging in Visual Studio, press F5.

## Support

The [Windows Ribbon Development Forum](https://social.msdn.microsoft.com/Forums/windowsdesktop/en-US/home?forum=windowsribbondevelopment) is available to discuss topics and ask questions related to developing Windows Ribbon applications.

## Minimum Requirements



|                          |                                                                                                                                                                          |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 7<br/> Windows Vista with Service Pack 2 (SP2) and [Platform Update for Windows Vista](https://msdn.microsoft.com/library/dd378748.aspx)<br/>         |
| Minimum supported server | Windows Server 2008 R2<br/> Windows Server 2008 with SP2 and [Platform Update for Windows Server 2008](https://msdn.microsoft.com/library/dd378748.aspx)<br/> |
| Windows SDK              | 7.0                                                                                                                                                                      |
| Visual Studio            | 2005                                                                                                                                                                     |
| Header and IDL files     | uiribbon.h, uiribbon.idl                                                                                                                                                 |



 

> [!Note]  
> The [Platform Update for Windows Vista](https://msdn.microsoft.com/library/dd378748.aspx) and [Platform Update for Windows Server 2008](https://msdn.microsoft.com/library/dd378748.aspx) are sets of run-time libraries that enable developers to target Windows Ribbon applications to both Windows Vista and Windows Server 2008. The platform updates will be available to all Windows Vista and Windows Server 2008 customers through Windows Update. Third-party applications that require [Platform Update for Windows Vista](https://msdn.microsoft.com/library/dd378748.aspx) or [Platform Update for Windows Server 2008](https://msdn.microsoft.com/library/dd378748.aspx) can have Windows Update detect whether the required updated is installed; if it is not, Windows Update will download and install it in the background.

 

 

 





