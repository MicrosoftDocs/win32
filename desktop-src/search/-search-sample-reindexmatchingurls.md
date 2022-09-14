---
description: 'The ReindexMatchingUrls code sample demonstrates how to provide three ways to specify the files to re-index: URLs that match a file type, mime type, or a specified WHERE clause.'
ms.assetid: f7b3a8a6-b464-46d4-a99c-fc56eea9b1ec
title: ReindexMatchingUrls
ms.topic: article
ms.date: 05/31/2018
---

# ReindexMatchingUrls

The ReindexMatchingUrls code sample demonstrates how to provide three ways to specify the files to re-index: URLs that match a file type, mime type, or a specified WHERE clause.

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

| Location      | Path URL                                                                      |
|---------------|-------------------------------------------------------------------------------|
| GitHub  | [ReindexMatchingUrls sample](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/WindowsSearch/ReindexMatchingUrls) |

> [!NOTE]  
> For all versions of Windows, including Windows 7, it is recommended to download the samples directly from GitHub for the most up to date version.

## Building the Sample

1. Open Windows Explorer and navigate to the **ReindexMatchingUrls** project directory. For example, the full default installation path is `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\WinUI\WindowsSearch\ReindexMatchingUrls`.
2. Double-click the icon for the Reindex.sln file to open the project in Visual Studio.
  
    > [!NOTE]  
    > The sln file was created under an older version of Visual Studio, thus upgrading it will be required if you are running Visual Studio 2012 or newer. This will not impact the sample's behavior.

3. From the **Build** menu, select **Build Solution**.

## Running the Sample

1. Navigate to the directory that contains the new executable, using the Command Prompt window or Windows Explorer.
2. At the command prompt, enter `Reindex.exe`, or from Windows Explorer, double-click the icon for Reindex.exe.

## Related topics

### Reference

[**ISearchCatalogManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcatalogmanager)

[**ISearchCatalogManager2**](/windows/desktop/api/Searchapi/nn-searchapi-isearchcatalogmanager2)

[**ISearchManager**](/windows/desktop/api/Searchapi/nn-searchapi-isearchmanager)

[**ISearchPersistentItemsChangedSink**](/windows/desktop/api/Searchapi/nn-searchapi-isearchpersistentitemschangedsink)

[**ISearchViewChangedSink**](/windows/desktop/api/searchapi/nn-searchapi-isearchviewchangedsink)

[**PRIORITIZE\_FLAGS**](/windows/win32/api/searchapi/ne-searchapi-tagprioritize_flags)

### Other Samples

[Search Code Samples](-search-samples-ovw.md)
