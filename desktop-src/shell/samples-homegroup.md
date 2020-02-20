---
Description: Demonstrates how to determine HomeGroup membership status, enumerate top-level items in the HomeGroup Shell folder, and launch the HomeGroup Sharing Wizard.
title: HomeGroup Sample
ms.topic: article
ms.date: 05/31/2018
ms.assetid: FDEFF261-BF86-4fbb-8567-892F79F23D92
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# HomeGroup Sample

Demonstrates how to determine HomeGroup membership status, enumerate top-level items in the **HomeGroup** Shell folder, and launch the **HomeGroup Sharing Wizard**.

This topic contains the following sections.

-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)
-   [Related topics](#related-topics)

## Requirements



| Product                                | Minimum Product Version |
|----------------------------------------|-------------------------|
| Windows                                | Windows 7               |
| Windows Software Development Kit (SDK) | 7.0                     |



 

## Downloading the Sample

This sample is available in the following locations.



| Location      | Path URL                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------|
| Code Gallery  | [Windows Shell Integration Samples on Code Gallery](https://code.msdn.microsoft.com/shellintegration) |
| Windows 7 SDK | [Download Windows 7 SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx)                            |



 

In the case of the Windows SDK, once you have downloaded and installed it, you will find the samples in the installed directory. For example, use of the default installation path for the Windows 7 software development kit (SDK) results in the samples being placed under `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\`.

## Building the Sample

To build the sample from the command prompt:

1.  Open the command prompt window and navigate to the **HomeGroup** project directory.
2.  Enter `msbuild HomeGroup.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **HomeGroup** project directory.
2.  Double-click the icon for the HomeGroup.sln file to open the project in Visual Studio.
3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the new executable, using the command prompt or Windows Explorer.
2.  At the command line, enter `HomeGroup.exe`. Alternatively, from Windows Explorer double-click the icon for HomeGroup.exe.

## Related topics

<dl> <dt>

[**IHomeGroup**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-ihomegroup)
</dt> <dt>

[**KNOWNFOLDERID**](knownfolderid.md)
</dt> </dl>

 

 



