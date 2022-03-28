---
description: Demonstrates how to implement a Shell verb using the CreateProcess method.
title: CreateProcess Verb Sample
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 2939BC36-35C0-4549-9971-742CBDA02547
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# CreateProcess Verb Sample

Demonstrates how to implement a Shell verb using the CreateProcess method.

This topic contains the following sections.

- [Description](#description)
- [Requirements](#requirements)
- [Downloading the Sample](#downloading-the-sample)
- [Building the Sample](#building-the-sample)
- [Running the Sample](#running-the-sample)

## Description

CreateProcess-based verbs depend on running a executable and passing it a command-line argument. This method is not as powerful as the DropTarget and ExecuteCommand methods but it does achieve the desirable out-of-process behavior.

## Requirements



| Product                                | Minimum Product Version |
|----------------------------------------|-------------------------|
| Windows                                | Windows Vista           |
| Windows Software Development Kit (SDK) | 7.0                     |



 

## Downloading the Sample

| Location      | Path URL                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------|
| GitHub  | [CreateProcessVerb sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/shell/appshellintegration/CreateProcessVerb) |

## Building the Sample

To build the sample from the command prompt:

1.  Open the command prompt window and navigate to the **CreateProcessVerb** project directory.
2.  Enter `msbuild CreateProcessVerb.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **CreateProcessVerb** project directory.
2.  Double-click the icon for the CreateProcessVerb.sln file to open the project in Visual Studio.
3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the new executable, using the command prompt or Windows Explorer.
2.  At the command line, enter `CreateProcessVerb.exe`. Alternatively, from Windows Explorer double-click the icon for CreateProcessVerb.exe.
3.  Follow the instructions in the displayed dialog

 

 



