---
Description: Demonstrates how to implement a Shell verb using the ExplorerCommand and ExplorerCommandState methods.
title: Explorer Command Verb Sample
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 2310A6AA-EAF9-4d7a-A784-04931BDC2089
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Explorer Command Verb Sample

Demonstrates how to implement a Shell verb using the ExplorerCommand and ExplorerCommandState methods.

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

This sample is available in the following locations.



| Location      | Path URL                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------|
| Code Gallery  | [Windows Shell Integration Samples on Code Gallery](https://code.msdn.microsoft.com/shellintegration) |
| Windows 7 SDK | [Download Windows 7 SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx)                            |



 

In the case of the Windows SDK, once you have downloaded and installed it, you will find the samples in the installed directory. For example, use of the default installation path for the Windows 7 SDK results in the samples being placed under `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\`.

## Building the Sample

To build the sample from the command prompt:

1.  Open the command prompt window and navigate to the **ExplorerCommandVerb** project directory.
2.  Enter `msbuild ExplorerCommandVerb.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **ExplorerCommandVerb** project directory.
2.  Double-click the icon for the ExplorerCommandVerb.sln file to open the project in Visual Studio.
3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the ExplorerCommandVerb.dll, using the command prompt or Windows Explorer. Make sure you use the 64-bit DLL file on 64-bit Windows.
2.  At the command line, enter `regsvr32.exe ExplorerCommandVerb.dll`.
3.  Two new verbs will be shown on the context menu when you right-click a .txt file.

 

 



