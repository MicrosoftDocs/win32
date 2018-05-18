---
Description: 'The CrawlScopeCommandLine code sample demonstrates how to define command line options for Crawl Scope Manager (CSM) indexing operations.'
ms.assetid: '8c82fe18-8676-43d2-a3da-027a733ee0a4'
title: CrawlScopeCommandLine
---

# CrawlScopeCommandLine

The CrawlScopeCommandLine code sample demonstrates how to define command line options for Crawl Scope Manager (CSM) indexing operations.

This topic contains the following sections.

-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)
-   [Related topics](#related-topics)

## Requirements



| Product                                          | Minimum Product Version                                                                |
|--------------------------------------------------|----------------------------------------------------------------------------------------|
| Windows                                          | Windows Vista, or Windows XP and Microsoft Windows Desktop Search (WDS) 3.x or greater |
| Microsoft Windows Software Development Kit (SDK) | 7.0                                                                                    |



 

## Downloading the Sample

This sample is available in the following locations.



| Location                                                                              | Path or URL                                                                                                      |
|---------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Code Gallery                                                                          | [CrawlScopeCommandLine sample](http://go.microsoft.com/fwlink/p/?linkid=155654)                                  |
| Microsoft Windows Software Development Kit (SDK) for Windows 7 and .NET Framework 4.0 | [Download the Windows SDK for Windows 7 and .NET Framework 4.0](http://go.microsoft.com/fwlink/p/?linkid=129787) |



 

 

> [!Note]  
> After you have downloaded and installed the Windows Software Development Kit (SDK), you will find the samples in the installed directory. For example, use of the default installation path for the Windows 7 software development kit (SDK) results in the samples being placed under `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples`.

 

## Building the Sample

To build the sample from the Command Prompt window:

1.  Open the Command Prompt window and navigate to the **CrawlScopeCommandLine** project directory. For example, the full default installation path is `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\WinUI\WindowsSearch\CrawlScopeCommandLine`.
2.  Enter `msbuild csmcmd.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **CrawlScopeCommandLine** project directory.
2.  Double-click the icon for the csmcmd.sln file to open the project in Visual Studio.
    > [!Note]  
    > The .sln file name extension is not shown under default folder settings. In that situation, it can be identified by its unique icon or by its type description, "Microsoft Visual Studio Solution".

     

3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the new executable, using the Command Prompt window or Windows Explorer.
2.  At the command prompt, enter `csmcmd.exe`, or from Windows Explorer, double-click the icon for csmcmd.exe.

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[**IEnumSearchRoots**](-search-ienumsearchroots.md)
</dt> <dt>

[**IEnumSearchScopeRules**](-search-ienumsearchscoperules.md)
</dt> <dt>

[**ISearchCrawlScopeManager**](-search-isearchcrawlscopemanager.md)
</dt> <dt>

[**ISearchCrawlScopeManager2**](-search-isearchcrawlscopemanager2.md)
</dt> <dt>

[**ISearchRoot**](-search-isearchroot.md)
</dt> <dt>

[**ISearchScopeRule**](-search-isearchscoperule.md)
</dt> <dt>

[**ISearchCatalogManager**](-search-isearchcatalogmanager.md)
</dt> <dt>

[**ISearchCatalogManager2**](-search-isearchcatalogmanager2.md)
</dt> <dt>

[**ISearchManager**](-search-isearchmanager.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Search Code Samples](-search-samples-ovw.md)
</dt> </dl>

 

 



