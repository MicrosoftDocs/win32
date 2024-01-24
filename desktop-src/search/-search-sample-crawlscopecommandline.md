---
description: The CrawlScopeCommandLine code sample demonstrates how to define command line options for Crawl Scope Manager (CSM) indexing operations.
ms.assetid: 8c82fe18-8676-43d2-a3da-027a733ee0a4
title: CrawlScopeCommandLine
ms.topic: article
ms.date: 05/31/2018
---

# CrawlScopeCommandLine

The CrawlScopeCommandLine code sample demonstrates how to define command line options for Crawl Scope Manager (CSM) indexing operations.

This topic contains the following sections.

- [Requirements](#requirements)
- [Downloading the Sample](#downloading-the-sample)
- [Building the Sample](#building-the-sample)
- [Running the Sample](#running-the-sample)
- [Related topics](#related-topics)

## Requirements

| Product     | Product Version          |
|-------------|--------------------------|
| Windows     | Windows 7, 8.1, or 10    |
| Windows SDK | 7.0 or greater           |

## Downloading the Sample

This sample is available in the following location.

| Location | Path or URL                                                                |
|----------|----------------------------------------------------------------------------|
| GitHub   |    [CrawlScopeCommandLine sample](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/WindowsSearch/CrawlScopeCommandLine)|

> [!NOTE]  
> For all versions of Windows, including Windows 7, it is recommended to download the samples directly from GitHub for the most up to date version.

## Building the Sample

1. Open Windows Explorer and navigate to the **CrawlScopeCommandLine** project directory.
2. Double-click the icon for the csmcmd.sln file to open the project in Visual Studio.
  
    > [!NOTE]  
    > The sln file was created under an older version of Visual Studio, thus upgrading it will be required if you are running Visual Studio 2012 or newer. This will not impact the sample's behavior.

3. From the **Build** menu, select **Build Solution**.

## Running the Sample

1. Navigate to the directory that contains the new executable, using the Command Prompt window or Windows Explorer.
2. At the command prompt, enter `csmcmd.exe`, or from Windows Explorer, double-click the icon for csmcmd.exe.

## Related topics

### Reference

[**IEnumSearchRoots**](/windows/desktop/api/Searchapi/nn-searchapi-ienumsearchroots)

[**IEnumSearchScopeRules**](/windows/desktop/api/Searchapi/nn-searchapi-ienumsearchscoperules)

[**ISearchCrawlScopeManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcrawlscopemanager)

[**ISearchCrawlScopeManager2**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcrawlscopemanager2)

[**ISearchRoot**](/windows/desktop/api/Searchapi/nn-searchapi-isearchroot)

[**ISearchScopeRule**](/windows/desktop/api/Searchapi/nn-searchapi-isearchscoperule)

[**ISearchCatalogManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcatalogmanager)

[**ISearchCatalogManager2**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcatalogmanager2)

[**ISearchManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchmanager)

### Other Samples

[Search Code Samples](-search-samples-ovw.md)
