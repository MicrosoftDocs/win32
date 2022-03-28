---
description: Demonstrates how to create a verb that operates on Shell items and containers which plays items or adds items to a queue.
title: Player Verb Sample
ms.topic: article
ms.date: 05/31/2018
ms.assetid: ABD905DD-F216-495e-A052-E43D93DD3D6B
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Player Verb Sample

Demonstrates how to create a verb that operates on Shell items and containers which plays items or adds items to a queue. This sample is particularly useful for media applications.

This topic contains the following sections.

- [Requirements](#requirements)
- [Downloading the Sample](#downloading-the-sample)
- [Building the Sample](#building-the-sample)
- [Running the Sample](#running-the-sample)

## Requirements



| Product                                | Minimum Product Version |
|----------------------------------------|-------------------------|
| Windows                                | Windows Vista           |
| Windows Software Development Kit (SDK) | 7.0                     |



 

## Downloading the Sample

| Location      | Path URL                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------|
| GitHub  | [PlayerVerb sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/shell/appshellintegration/PlayerVerbSample) |

## Building the Sample

To build the sample from the command prompt:

1.  Open the command prompt window and navigate to the **PlayerVerbSample** project directory.
2.  Enter `msbuild PlayerVerbSample.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **PlayerVerbSample** project directory.
2.  Double-click the icon for the PlayerVerbSample.sln file to open the project in Visual Studio.
3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the new executable, using the command prompt or Windows Explorer.
2.  At the command line, enter `PlayerVerbSample.exe`. Alternatively, from Windows Explorer double-click the icon for PlayerVerbSample.exe.
3.  Select `Register Verbs` in the **Player Verb Sample** dialog.
4.  Right-click picture items (file, folder, or stack) in Windows Explorer to add them to a queue or play them in the sample application. Use music items when you change the sample to work with music.

 

 



