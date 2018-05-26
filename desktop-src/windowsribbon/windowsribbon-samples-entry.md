---
title: Windows Ribbon Framework Samples
description: The topics contained in this section provide details about the code samples that support the Windows Ribbon framework documentation.
ms.assetid: 79d092c9-347b-4b8f-8ba4-a8f696ce6a85
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Windows Ribbon Framework Samples

The topics contained in this section provide details about the code samples that support the Windows Ribbon framework documentation.

## Download Information

The Windows Ribbon framework samples can be downloaded as standalone Microsoft Visual Studio projects from the [Microsoft Download Center](http://go.microsoft.com/fwlink/p/?linkid=147893) or installed as part of the [Windows Software Development Kit (SDK)](http://go.microsoft.com/fwlink/p/?linkid=147890).

## Samples



| Sample                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Ribbon Development Introductory Tutorial](windowsribbon-hol.md)<br/>         | This tutorial and accompanying code samples are intended for C++ developers who develop desktop applications and want to take advantage of the Windows Ribbon framework. The tutorial steps you through adding an empty Ribbon to a small application, adding controls with icons, labels, and other resources to the Ribbon, and then connecting the controls to the existing command infrastructure of the application. You learn how the API maintains separation between control organization and event handling. Finally, the tutorial demonstrates how to specify layouts and resizing behavior to show how the Ribbon adapts and performs at different sizes. When you finish, you will have performed all the steps to add and customize a basic Ribbon application.<br/> |
| [SimpleRibbon Sample](windowsribbon-sample1.md)<br/>                          | This code sample demonstrates how to implement a simple Windows Ribbon application.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [ContextPopup Sample](windowsribbon-contextpopupsample.md)<br/>               | This code sample demonstrates the markup and code required to implement a Windows Ribbon application with ContextPopups. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [DropDownColorPicker Sample](windowsribbon-dropdowncolorpickersample.md)<br/> | This code sample demonstrates the markup and code required to use a Windows Ribbon DropDownColorPicker control. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Gallery Sample](windowsribbon-gallerysample.md)<br/>                         | This code sample demonstrates the markup and code required to use the different types of Gallery controls included in the Ribbon framework. The sample includes code that can be used to dynamically populate items into the Galleries, and handle special Gallery previewing events that support results-oriented UI. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [HTMLEditRibbon Sample](windowsribbon-htmleditribbonsample.md)<br/>           | This code sample shows markup and code required to migrate an existing Microsoft Foundation Classes (MFC) application to use the Windows Ribbon. It was created by taking the existing MFC HTMLEdit sample application and modifying its code and resources to use the Windows Ribbon. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [FontControl Sample](windowsribbon-fontcontrolsample.md)<br/>                 | This code sample demonstrates the markup and code required to implement a FontControl within a Windows Ribbon application. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [Preview Ribbon Sample](windowsribbon-previewribbon.md)<br/>                  | Preview Ribbon is an open-source prototyping application for the Windows Ribbon framework that generates a functional preview of the ribbon command bar from a Ribbon framework markup file without the need to implement any underlying command code. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |



 

## Support

The [Windows Ribbon Development Forum](http://go.microsoft.com/fwlink/p/?linkid=156613) is available to discuss topics and ask questions related to developing Windows Ribbon applications.

## Minimum Requirements



|                                        |                                                                                                                                                                          |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client               | Windows 7<br/> Windows Vista with Service Pack 2 (SP2) and [Platform Update for Windows Vista](http://go.microsoft.com/fwlink/p/?linkid=166272)<br/>         |
| Minimum supported server               | Windows Server 2008 R2<br/> Windows Server 2008 with SP2 and [Platform Update for Windows Server 2008](http://go.microsoft.com/fwlink/p/?linkid=166272)<br/> |
| Windows Software Development Kit (SDK) | 7.0                                                                                                                                                                      |
| Header and IDL files                   | uiribbon.h, uiribbon.idl                                                                                                                                                 |



 

> [!Note]  
> The [Platform Update for Windows Vista](http://go.microsoft.com/fwlink/p/?linkid=166272) and [Platform Update for Windows Server 2008](http://go.microsoft.com/fwlink/p/?linkid=166272) are sets of run-time libraries that enable developers to target Windows Ribbon applications to both Windows Vista and Windows Server 2008. The platform updates will be available to all Windows Vista and Windows Server 2008 customers through Windows Update. Third-party applications that require [Platform Update for Windows Vista](http://go.microsoft.com/fwlink/p/?linkid=166272) or [Platform Update for Windows Server 2008](http://go.microsoft.com/fwlink/p/?linkid=166272) can have Windows Update detect whether the required updated is installed; if it is not, Windows Update will download and install it in the background.

 

 

 





