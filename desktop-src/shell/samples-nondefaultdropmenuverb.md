---
description: Demonstrates how to extend the drag-and-drop shortcut menu (sometimes referred to as a context menu).
title: NonDefaultDropMenuVerb Sample
ms.topic: article
ms.date: 05/31/2018
ms.assetid: F19B7561-D280-41df-A829-15960FEB12F8
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# NonDefaultDropMenuVerb Sample

Demonstrates how to extend the drag-and-drop shortcut menu (sometimes referred to as a context menu).

This topic contains the following sections.

-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)

## Requirements



| Product                                | Minimum Product Version |
|----------------------------------------|-------------------------|
| Windows                                | Windows Vista           |
| Windows Software Development Kit (SDK) | 7.0                     |



 

## Downloading the Sample

| Location      | Path URL                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------|
| GitHub  | [NonDefaultDropMenuVerb sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/shell/appshellintegration/NonDefaultDropMenuVerb) |

## Building the Sample

To build the sample from the command prompt:

1.  Open the command prompt window and navigate to the **NonDefaultDropMenuVerb** project directory.
2.  Enter `msbuild NonDefaultDropMenuVerb.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **NonDefaultDropMenuVerb** project directory.
2.  Double-click the icon for the NonDefaultDropMenuVerb.sln file to open the project in Visual Studio.
3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the new DLL file, using the command prompt or Windows Explorer.
2.  Copy NonDefaultDropMenuVerb.dll to the System directory (for example, C:\\Windows\\System32).
3.  At a command prompt, enter `regedit NonDefaultDropMenuVerb.reg`.
4.  Use the right mouse button to drag a file from one folder to another. You will see additional menu items for the drop operation.

 

 



