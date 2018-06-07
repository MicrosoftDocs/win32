---
Description: The IFilterSample code sample demonstrates how to create an IFilter base class for implementing the IFilter interface.
ms.assetid: 4c0df747-627d-4937-a117-d43137d5d081
title: IFilterSample
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IFilterSample

The IFilterSample code sample demonstrates how to create an IFilter base class for implementing the [**IFilter**](https://www.bing.com/search?q=**IFilter**) interface.

This topic contains the following sections.

-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)
-   [Related topics](#related-topics)

## Requirements



| Product     | Minimum Product Version                                                                |
|-------------|----------------------------------------------------------------------------------------|
| Windows     | Windows Vista, or Windows XP and Microsoft Windows Desktop Search (WDS) 3.x or greater |
| Windows SDK | 7.0                                                                                    |



 

## Downloading the Sample

This sample is available in the following locations.



| Location      | Path URL                                                                  |
|---------------|---------------------------------------------------------------------------|
| Code Gallery  | [IFilterSample](http://go.microsoft.com/fwlink/p/?linkid=155654)          |
| Windows 7 SDK | [Download Windows 7 SDK](http://go.microsoft.com/fwlink/p/?linkid=129787) |



 

 

> [!Note]  
> After you have downloaded and installed the Windows Software Development Kit (SDK), you will find the samples in the installed directory. For example, use of the default installation path for the Windows 7 software development kit (SDK) results in the samples being placed under `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples`.

 

## Building the Sample

To build the sample from the Command Prompt window:

1.  Open the Command Prompt window and navigate to the **FilterBase** project directory. For example, the full default installation path is `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\WinUI\WindowsSearch\IFilterSample`.
2.  Enter `msbuild FilterBase.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **FilterBase** project directory.
2.  Double-click the icon for the FilterBase.sln file to open the project in Visual Studio.
    > [!Note]  
    > The .sln file name extension is not shown under default folder settings. In that situation, it can be identified by its unique icon or by its type description, "Microsoft Visual Studio Solution".

     

3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the new executable, using the Command Prompt window or Windows Explorer.
2.  At the command prompt, enter `FilterBase.exe`, or from Windows Explorer, double-click the icon for FilterBase.exe.

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[**IFilter**](https://www.bing.com/search?q=**IFilter**)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Developing Filter Handlers](-search-ifilter-conceptual.md)
</dt> <dt>

[Search Code Samples](-search-samples-ovw.md)
</dt> </dl>

 

 



