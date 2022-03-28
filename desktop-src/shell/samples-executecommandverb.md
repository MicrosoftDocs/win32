---
description: Demonstrates how to implement a Shell verb using the ExecuteCommand method.
title: Execute Command Verb Sample
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 0418318A-3E62-4690-AFB3-9B4A391C537E
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Execute Command Verb Sample

Demonstrates how to implement a Shell verb using the ExecuteCommand method.

This topic contains the following sections.

- [Description](#description)
- [Requirements](#requirements)
- [Downloading the Sample](#downloading-the-sample)
- [Building the Sample](#building-the-sample)
- [Running the Sample](#running-the-sample)

## Description

This method is preferred for verb implementations because it provides the most flexibility, is simple, and supports out-of-process activation. This sample implements a standalone, local server Component Object Model (COM) object, but it is expected that the verb implementation will be integrated into existing applications. To do so, your main application object must register a class factory for itself. That object implements [**IDropTarget**](/windows/win32/api/oleidl/nn-oleidl-idroptarget) for your application's verbs. Note that COM launches your application if it is not already running but connects to a running instance of your application if one is present.

## Requirements



| Product                                | Minimum Product Version |
|----------------------------------------|-------------------------|
| Windows                                | Windows 7               |
| Windows Software Development Kit (SDK) | 7.0                     |



 

## Downloading the Sample

| Location      | Path URL                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------|
| GitHub  | [ExecuteCommandVerb sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/shell/appshellintegration/ExecuteCommandVerb) |

## Building the Sample

To build the sample from the command prompt:

1.  Open the command prompt window and navigate to the **ExecuteCommandVerb** project directory.
2.  Enter `msbuild ExecuteCommand.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **ExecuteCommandVerb** project directory.
2.  Double-click the icon for the ExecuteCommand.sln file to open the project in Visual Studio.
3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the new executable, using the command prompt or Windows Explorer.
2.  At the command line, enter `ExecuteCommand.exe`. Alternatively, from Windows Explorer double-click the icon for ExecuteCommand.exe.
3.  Follow the instructions in the displayed dialog

 

 
