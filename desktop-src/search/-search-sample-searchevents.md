---
description: The SearchEvents code sample demonstrates how to prioritize indexing events.
ms.assetid: a352c3e2-5860-4b9c-a3c7-a806f69b4f7d
title: SearchEvents
ms.topic: article
ms.date: 05/31/2018
---

# SearchEvents

The SearchEvents code sample demonstrates how to prioritize indexing events.

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

| Location      | Path URL                                                                  |
|---------------|---------------------------------------------------------------------------|
| GitHub        | [SearchEvents sample](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/WindowsSearch/SearchEvents)    |

> [!NOTE]  
> For all versions of Windows, including Windows 7, it is recommended to download the samples directly from GitHub for the most up to date version.

## Building the Sample

1. Open Windows Explorer and navigate to the **SearchEvents** project directory.
2. Double-click the icon for the Eventing.sln file to open the project in Visual Studio.
  
    > [!NOTE]  
    > The sln file was created under an older version of Visual Studio, thus upgrading it will be required if you are running Visual Studio 2012 or newer. This will not impact the sample's behavior.

3. From the **Build** menu, select **Build Solution**.

## Running the Sample

1. Navigate to the directory that contains the new executable, using the Command Prompt window or Windows Explorer.
2. At the command prompt, enter `Eventing.exe`, or from Windows Explorer, double-click the icon for Eventing.exe.

## Related topics

### Reference

[**IRowsetEvents**](/windows/desktop/api/Searchapi/nn-searchapi-irowsetevents)

[**IRowsetPrioritization**](/windows/desktop/api/Searchapi/nn-searchapi-irowsetprioritization)

[**PRIORITY\_LEVEL**](/windows/win32/api/searchapi/ne-searchapi-priority_level)

[**ROWSETEVENT\_ITEMSTATE**](/windows/win32/api/searchapi/ne-searchapi-rowsetevent_itemstate)

[**ROWSETEVENT\_TYPE**](/windows/win32/api/searchapi/ne-searchapi-rowsetevent_type)

### Other Samples

[Search Code Samples](-search-samples-ovw.md)
