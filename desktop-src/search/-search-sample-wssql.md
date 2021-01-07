---
description: The WSSQL code sample demonstrates how to communicate between Microsoft OLE DB and Windows Search through Structured Query Language (SQL).
ms.assetid: 28663608-66b3-4404-9426-5a4b5f52a408
title: WSSQL
ms.topic: article
ms.date: 05/31/2018
---

# WSSQL

The WSSQL code sample demonstrates how to communicate between Microsoft OLE DB and Windows Search through Structured Query Language (SQL).

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
| GitHub        | [WSSQL sample](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/WindowsSearch/WSSQL)           |

> [!NOTE]  
> For all versions of Windows, including Windows 7, it is recommended to download the samples directly from GitHub for the most up to date version.

## Building the Sample

1. Open Windows Explorer and navigate to the **WSSQL** project directory.
2. Double-click the icon for the WSSQL.sln file to open the project in Visual Studio.
    > [!NOTE]  
    > The sln file was created under an older version of Visual Studio, thus upgrading it will be required if you are running Visual Studio 2012 or newer. This will not impact the sample's behavior.

3. From the **Build** menu, select **Build Solution**.

## Running the Sample

1. Navigate to the directory that contains the new executable, using the Command Prompt window or Windows Explorer.
2. At the command prompt, enter `WSSQL.exe`, or from Windows Explorer, double-click the icon for WSSQL.exe.

## Related topics

### Conceptual

[Using Windows Search SQL Syntax](-search-sql-windowssearch-entry.md)

[General Query Language Information](-search-sql-generalqueryinfo.md)

[OLE DB Programming Overview](/cpp/data/oledb/ole-db-programming-overview)

### Other Samples

[Search Code Samples](-search-samples-ovw.md)
