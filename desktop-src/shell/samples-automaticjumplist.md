---
description: Demonstrates how to add items to the automatic Jump List for an application, including switching between the display of the Frequent and Recent categories.
title: Automatic Jump List Sample
ms.topic: article
ms.date: 05/31/2018
ms.assetid: C33152FE-1322-42f8-A656-3D5FAF4B612D
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Automatic Jump List Sample

Demonstrates how to add items to the automatic Jump List for an application, including switching between the display of the Frequent and Recent categories.

This topic contains the following sections.

- [Requirements](#requirements)
- [Downloading the Sample](#downloading-the-sample)
- [Building the Sample](#building-the-sample)
- [Running the Sample](#running-the-sample)
- [Related topics](#related-topics)

## Requirements



| Product                                | Minimum Product Version |
|----------------------------------------|-------------------------|
| Windows                                | Windows 7               |
| Windows Software Development Kit (SDK) | 7.0                     |



 

## Downloading the Sample

| Location      | Path URL                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------|
| GitHub  | [AutomaticJumpList sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/shell/appshellintegration/AutomaticJumpList) |

## Building the Sample

To build the sample from the command prompt:

1.  Open the command prompt window and navigate to the **AutomaticJumpList** project directory.
2.  Enter `msbuild AutomaticJumpListSample.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **AutomaticJumpList** project directory.
2.  Double-click the icon for the AutomaticJumpListSample.sln file to open the project in Visual Studio.
3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the new executable, using the command prompt or Windows Explorer.
2.  At the command line, enter `AutomaticJumpListSample.exe`. Alternatively, from Windows Explorer double-click the icon for AutomaticJumpListSample.exe.
3.  This sample must be run as an administrator the first time it is run so that it can install the necessary file type registrations. After the file types have been registered, the sample can run as a standard user.
4.  Select options from the menu in the sample application, including the selection of .txt or .doc documents through the **Open** dialog to see how they affect the application's Jump List in the taskbar.

## Related topics

<dl> <dt>

[Application User Model IDs (AppUserModelIDs)](appids.md)
</dt> </dl>

 

 



