---
description: Demonstrates how to implement a Shell namespace extension, including context menu behavior and custom tasks in the browser.
title: Explorer Data Provider Sample
ms.topic: article
ms.date: 05/31/2018
ms.assetid: B1B20AF8-3DDE-467b-A49E-A77849CF9F1B
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Explorer Data Provider Sample

Demonstrates how to implement a Shell namespace extension, including context menu behavior and custom tasks in the browser.

This topic contains the following sections.

-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)

## Requirements



| Product                                | Minimum Product Version |
|----------------------------------------|-------------------------|
| Windows                                | Windows Vista           |
| Windows Software Development Kit (SDK) | 6.1                     |



 

## Downloading the Sample

| Location      | Path URL                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------|
| GitHub  | [ExplorerDataProvider sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/shell/shellextensibility/explorerdataprovider) |

## Building the Sample

To build the sample from the command prompt:

1.  Open the command prompt window and navigate to the **ExplorerDataProvider** project directory.
2.  Enter `msbuild ExplorerDataProvider.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **ExplorerDataProvider** project directory.
2.  Double-click the icon for the ExplorerDataProvider.sln file to open the project in Visual Studio.
3.  From the **Build** menu, select **Build Solution**. The DLL will be built in the default \\Debug or \\Release directory.

> [!Note]  
> In the version of this sample included in the Windows SDK, the configuration for the 64-bit Release build does not include the ExplorerDataProvider.def file in the linker's **Module Definition File** option. You must specify that file yourself before building in a 64-bit environment. Add the line `ModuleDefinitionFile="ExplorerDataProvider.def"` to the VCLinkerTool section (begins at line 329) of the ExplorerDataProvider.vcproj file as shown here:
>
> 
>
> 
```
LinkIncremental="1"&gt; AdditionalLibraryDirectories=""c:\Program Files\Microsoft SDKs\Windows\v6.0\Lib\x64""&gt; ModuleDefinitionFile="ExplorerDataProvider.def"&gt; GenerateDebugInformation="true"
```
>
> 
>
> The version of this sample downloadable from Code Gallery has been corrected for this issue and no extra action is required on your part.
>
>  
>
> ## Running the Sample
>
> 1.  Navigate to the directory that contains the new .dll and .propdesc file, using the command prompt or Windows Explorer.
> 2.  At the command line, type `regsvr32.exe`.
>     > [!Note]  
>     > If you run this command from an elevated command prompt, the self-registration will also register the .propdesc file automatically. If it is run from a non-elevated command prompt then the namespace extension will work, but without custom property functionality.
>
>      
>
> 3.  Open the **My Computer** folder and browse the new namespace extension present there.
>
>  
>
>  
>


