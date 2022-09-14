---
description: The StructuredQuerySample code sample demonstrates how to read lines from the console, parse them using the system schema, and display the resulting condition trees.
ms.assetid: 9bb56d80-670e-4b2b-bf3f-40d0a75a89b6
title: StructuredQuerySample
ms.topic: article
ms.date: 05/31/2018
---

# StructuredQuerySample

The StructuredQuerySample code sample demonstrates how to read lines from the console, parse them using the system schema, and display the resulting condition trees.

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
| GitHub        | [StructuredQuerySample](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/WindowsSearch/StructuredQuerySample)  |

> [!NOTE]  
> For all versions of Windows, including Windows 7, it is recommended to download the samples directly from GitHub for the most up to date version.

## Building the Sample

1. Open Windows Explorer and navigate to the **StructuredQuerySample** project directory.
2. Double-click the icon for the StructuredQuerySample.sln file to open the project in Visual Studio.

    > [!NOTE]  
    > The sln file was created under an older version of Visual Studio, thus upgrading it will be required if you are running Visual Studio 2012 or newer. This will not impact the sample's behavior.

3. From the **Build** menu, select **Build Solution**.

## Running the Sample

1. Navigate to the directory that contains the new executable, using the Command Prompt window or Windows Explorer.
2. At the command prompt, enter `StructuredQuerySample.exe`, or from Windows Explorer, double-click the icon for StructuredQuerySample.exe.

## Related topics

### Reference

[**ICondition**](/windows/desktop/api/Structuredquerycondition/nn-structuredquerycondition-icondition)

[**ICondition2**](/windows/desktop/api/Structuredquerycondition/nn-structuredquerycondition-icondition2)

[**IConditionFactory**](/windows/desktop/api/Structuredquery/nn-structuredquery-iconditionfactory)

[**IConditionFactory2**](/windows/desktop/api/Structuredquery/nn-structuredquery-iconditionfactory2)

[**IConditionGenerator**](/windows/desktop/api/Structuredquery/nn-structuredquery-iconditiongenerator)

[**IQueryParser**](/windows/desktop/api/Structuredquery/nn-structuredquery-iqueryparser)

[**IQueryParserManager**](/windows/desktop/api/Structuredquery/nn-structuredquery-iqueryparsermanager)

[**IQuerySolution**](/windows/desktop/api/Structuredquery/nn-structuredquery-iquerysolution)

### Other Samples

[Search Code Samples](-search-samples-ovw.md)
