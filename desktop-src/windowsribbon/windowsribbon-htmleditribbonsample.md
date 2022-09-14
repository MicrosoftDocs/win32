---
title: HTMLEditRibbon Sample
description: This code sample shows markup and code required to migrate an existing Microsoft Foundation Classes (MFC) application to use the Windows Ribbon.
ms.assetid: 1505aaea-76d2-47bc-bdc9-12e761da93f9
ms.topic: article
ms.date: 07/13/2021
---

# HTMLEditRibbon Sample

This code sample shows markup and code required to migrate an existing Microsoft Foundation Classes (MFC) application to use the Windows Ribbon. It was created by taking the existing MFC HTMLEdit sample application and modifying its code and resources to use the Windows Ribbon.

- [Remarks](#remarks)
- [Usage](#usage)
  - [Building the Sample](#building-the-sample)
  - [Running the Sample](#running-the-sample)
- [Support](#support)
- [Minimum Requirements](#minimum-requirements)

## Remarks

For the MFC sample, see [HTMLEdit Sample: Wraps the Internet Explorer MSHTML Editing Control](https://msdn.microsoft.com/library/ea8hhwb6(VS.80).aspx).

## Usage

The Windows Ribbon framework samples can be downloaded as standalone Microsoft Visual Studio projects from the [Microsoft Download Center](https://www.microsoft.com/download/details.aspx?id=9620) or installed as part of the [Windows Software Development Kit (SDK)](https://developer.microsoft.com/windows/downloads/sdk-archive/).

- Windows Software Development Kit (SDK) (standard installation path): %ProgramFiles%\\Microsoft SDKs\\Windows\\\[version number\]\\Samples\\winui\\WindowsRibbon\\HTMLEditRibbon

### Building the Sample

Download the sample.

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

 

 

 





