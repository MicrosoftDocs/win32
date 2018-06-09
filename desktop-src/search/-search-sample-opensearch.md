---
Description: The OpenSearch code sample demonstrates how to create a federated search service using the OpenSearch protocol, and an OpenSearch Descriptor (.osdx) file (a search connector).
ms.assetid: 792884e4-826b-4474-82e1-1680d4d8b602
title: OpenSearch
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OpenSearch

The OpenSearch code sample demonstrates how to create a federated search service using the [OpenSearch](http://go.microsoft.com/fwlink/p/?linkid=147911) protocol, and an OpenSearch Descriptor (.osdx) file (a search connector).

This topic contains the following sections.

-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)
-   [Related topics](#related-topics)

## Requirements



| Product     | Minimum Product Version |
|-------------|-------------------------|
| Windows     | Windows 7               |
| Windows SDK | 7.0                     |



 

## Downloading the Sample

This sample is available in the following locations.



| Location      | Path URL                                                                  |
|---------------|---------------------------------------------------------------------------|
| Code Gallery  | [OpenSearch sample](http://go.microsoft.com/fwlink/p/?linkid=155654)      |
| Windows 7 SDK | [Download Windows 7 SDK](http://go.microsoft.com/fwlink/p/?linkid=129787) |



 

 

> [!Note]  
> After you have downloaded and installed the Windows Software Development Kit (SDK), you will find the samples in the installed directory. For example, use of the default installation path for the Windows 7 software development kit (SDK) results in the samples being placed under `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples`.

 

## Building the Sample

To build the sample from the Command Prompt:

1.  Open the Command Prompt window and navigate to the **AdventureSearch** project directory. For example, the full default installation path is `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\WinUI\Shell\ShellExtensibility\OpenSearch`.
2.  Enter `msbuild AdventureSearch.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **AdventureSearch** project directory.
2.  Double-click the icon for the AdventureSearch.sln file to open the project in Visual Studio.
    > [!Note]  
    > The .sln file name extension is not shown under default folder settings. In that situation, it can be identified by its unique icon or by its type description, "Microsoft Visual Studio Solution".

     

3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the new executable, using the Command Prompt window or Windows Explorer.
2.  At the command prompt, enter `AdventureSearch.exe`, or from Windows Explorer, double-click the icon for AdventureSearch.exe.
3.  At the command prompt, enter `GetOSDX.exe`, or from Windows Explorer, double-click the icon for GetOSDX.exe.

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[Overview of the Search Connector Description Schema](search-sconn-desc-schema-entry.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Federated Search in Windows](-search-federated-search-overview.md)
</dt> <dt>

[Search Code Samples](-search-samples-ovw.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[Library Description Schema](12F6E6AE-2776-408c-B9AC-E885BE93C27F)
</dt> </dl>

 

 



