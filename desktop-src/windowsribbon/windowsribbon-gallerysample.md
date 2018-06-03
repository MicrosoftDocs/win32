---
title: Gallery Sample
description: This code sample demonstrates the markup and code required to use the different types of Gallery controls included in the Windows Ribbon framework.
ms.assetid: 1a462f4e-e75a-40cf-9c52-0bad0a645d57
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Gallery Sample

This code sample demonstrates the markup and code required to use the different types of Gallery controls included in the Windows Ribbon framework. The sample includes code that can be used to dynamically populate items into the Galleries, and handle special Gallery previewing events that support results-oriented UI.

-   [Usage](#usage)
    -   [Building the Sample](#building-the-sample)
    -   [Running the Sample](#running-the-sample)
-   [Support](#support)
-   [Minimum Requirements](#minimum-requirements)
-   [Related topics](#related-topics)

## Usage

The Gallery Sample can be downloaded as a standalone Microsoft Visual Studio project from the [Microsoft Download Center](http://go.microsoft.com/fwlink/p/?linkid=147893) or installed as part of the [Windows Software Development Kit (SDK)](http://go.microsoft.com/fwlink/p/?linkid=147890).

-   Microsoft Download Center: [Windows Ribbon Samples](http://go.microsoft.com/fwlink/p/?linkid=137045)
-   Windows Software Development Kit (SDK) (standard installation path): %ProgramFiles%\\Microsoft SDKs\\Windows\\\[version number\]\\Samples\\winui\\WindowsRibbon\\Gallery

### Building the Sample

Download the sample to your hard disk.

Install the Windows SDK for Windows 7 and open its build environment command window. On the Start menu, point to All Programs, Microsoft Windows SDK, and then click CMD Shell.

To build the sample from the build environment command window, go to the source directory of the sample. At the command prompt, type MSBUILD.

To build the sample in Microsoft Visual Studio, load the sample solution or project file and then press CTRL+SHIFT+B.

### Running the Sample

To run the sample from the build environment command window, execute the .exe files in the Bin\\Debug or Bin\\Release folder contained in the sample source folder.

To run the compiled sample with debugging in Visual Studio, press F5.

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
> The [Platform Update for Windows Vista](http://go.microsoft.com/fwlink/p/?linkid=166272) and [Platform Update for Windows Server 2008](http://go.microsoft.com/fwlink/p/?linkid=166272) are sets of run-time libraries that enable developers to target Windows Ribbon applications to both Windows Vista and Windows Server 2008. The platform updates will be available to all Windows Vista and Windows Server 2008 customers through Windows Update. Third-party applications that require [Platform Update for Windows Vista](http://go.microsoft.com/fwlink/p/?linkid=166272) or [Platform Update for Windows Server 2008](http://go.microsoft.com/fwlink/p/?linkid=166272) can have Windows Update detect whether the required updated is installed; if it is not, Windows Update will download and install it in the background.

 

## Related topics

<dl> <dt>

[Working with Galleries](ribbon-controls-galleries.md)
</dt> <dt>

[Combo Box](windowsribbon-controls-combobox.md)
</dt> <dt>

[Drop-Down Gallery](windowsribbon-controls-dropdowngallery.md)
</dt> <dt>

[In-Ribbon Gallery](windowsribbon-controls-inribbongallery.md)
</dt> <dt>

[Split Button Gallery](windowsribbon-controls-splitbuttongallery.md)
</dt> <dt>

[Collection Properties](windowsribbon-reference-properties-collection.md)
</dt> </dl>

 

 





