---
title: SimpleRibbon Sample
description: This code sample demonstrates how to implement a simple Windows Ribbon application.
ms.assetid: 9196ae63-ca9e-43ae-8b4c-a30f1ef700f0
ms.topic: article
ms.date: 05/31/2018
---

# SimpleRibbon Sample

This code sample demonstrates how to implement a simple Windows Ribbon application.

-   [Usage](#usage)
    -   [Building the Sample](#building-the-sample)
    -   [Running the Sample](#running-the-sample)
-   [Support](#support)
-   [Minimum Requirements](#minimum-requirements)

## Usage

The SimpleRibbon Sample can be downloaded as a standalone Microsoft Visual Studio project from the [Microsoft Download Center](https://www.microsoft.com/DOWNLOADS/en/default.aspx) or installed as part of the [Windows Software Development Kit (SDK)](https://msdn.microsoft.com/windows/bb980924.aspx).

-   Microsoft Download Center: [Windows Ribbon Samples](https://www.microsoft.com/downloads/details.aspx?familyid=141e13e8-b10b-4356-aaa5-609b2981574a&displaylang=en)
-   Windows Software Development Kit (SDK) (standard installation path): %ProgramFiles%\\Microsoft SDKs\\Windows\\\[version number\]\\Samples\\winui\\WindowsRibbon\\SimpleRibbon

### Building the Sample

Download the sample to your hard disk.

Install the Windows SDK for Windows 7 and open its build environment command window. On the Start menu, point to All Programs, Microsoft Windows SDK, and then click CMD Shell.

To build the sample from the build environment command window, go to the source directory of the sample. At the command prompt, type MSBUILD.

To build the sample in Microsoft Visual Studio, load the sample solution or project file and then press CTRL+SHIFT+B.

### Running the Sample

To run the sample from the build environment command window, execute the .exe files in the Bin\\Debug or Bin\\Release folder contained in the sample source folder.

To run the compiled sample with debugging in Visual Studio, press F5.

## Support

The [Windows Ribbon Development Forum](https://social.msdn.microsoft.com/Forums/windowsdesktop/home?forum=windowsribbondevelopment) is available to discuss topics and ask questions related to developing Windows Ribbon applications.

## Minimum Requirements



| Requirement | Value |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 7<br/> Windows Vista with Service Pack 2 (SP2) and [Platform Update for Windows Vista](https://msdn.microsoft.com/library/dd378748.aspx)<br/>         |
| Minimum supported server | Windows Server 2008 R2<br/> Windows Server 2008 with SP2 and [Platform Update for Windows Server 2008](https://msdn.microsoft.com/library/dd378748.aspx)<br/> |
| Windows SDK              | 7.0                                                                                                                                                                      |
| Visual Studio            | 2008                                                                                                                                                                     |
| Header and IDL files     | uiribbon.h, uiribbon.idl                                                                                                                                                 |



 

> [!Note]  
> The [Platform Update for Windows Vista](https://msdn.microsoft.com/library/dd378748.aspx) and [Platform Update for Windows Server 2008](https://msdn.microsoft.com/library/dd378748.aspx) are sets of run-time libraries that enable developers to target Windows Ribbon applications to both Windows Vista and Windows Server 2008. The platform updates will be available to all Windows Vista and Windows Server 2008 customers through Windows Update. Third-party applications that require [Platform Update for Windows Vista](https://msdn.microsoft.com/library/dd378748.aspx) or [Platform Update for Windows Server 2008](https://msdn.microsoft.com/library/dd378748.aspx) can have Windows Update detect whether the required updated is installed; if it is not, Windows Update will download and install it in the background.

 

 

 





