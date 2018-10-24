---
Description: The StructuredQuerySample code sample demonstrates how to read lines from the console, parse them using the system schema, and display the resulting condition trees.
ms.assetid: 9bb56d80-670e-4b2b-bf3f-40d0a75a89b6
title: StructuredQuerySample
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StructuredQuerySample

The StructuredQuerySample code sample demonstrates how to read lines from the console, parse them using the system schema, and display the resulting condition trees.

This topic contains the following sections.

-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)
-   [Related topics](#related-topics)

## Requirements



| Product     | Minimum Product Version |
|-------------|-------------------------|
| Windows     | Windows Vista           |
| Windows SDK | 7.0                     |



 

## Downloading the Sample

This sample is available in the following locations.



| Location      | Path URL                                                                  |
|---------------|---------------------------------------------------------------------------|
| Code Gallery  | [StructuredQuerySample](http://go.microsoft.com/fwlink/p/?linkid=155654)  |
| Windows 7 SDK | [Download Windows 7 SDK](http://go.microsoft.com/fwlink/p/?linkid=129787) |



 

 

> [!Note]  
> After you have downloaded and installed the Windows Software Development Kit (SDK), you will find the samples in the installed directory. For example, use of the default installation path for the Windows 7 software development kit (SDK) results in the samples being placed under `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples`.

 

## Building the Sample

To build the sample from the Command Prompt window:

1.  Open the Command Prompt window and navigate to the **StructuredQuerySample** project directory. For example, the full default installation path is `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\WinUI\WindowsSearch\StructuredQuerySample`.
2.  Enter `msbuild StructuredQuerySample.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **StructuredQuerySample** project directory.
2.  Double-click the icon for the StructuredQuerySample.sln file to open the project in Visual Studio.
    > [!Note]  
    > The .sln file name extension is not shown under default folder settings. In that situation, it can be identified by its unique icon or by its type description, "Microsoft Visual Studio Solution".

     

3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the new executable, using the Command Prompt window or Windows Explorer.
2.  At the command prompt, enter `StructuredQuerySample.exe`, or from Windows Explorer, double-click the icon for StructuredQuerySample.exe.

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[**ICondition**](/windows/desktop/api/Structuredquerycondition/nn-structuredquerycondition-icondition)
</dt> <dt>

[**ICondition2**](/windows/desktop/api/Structuredquerycondition/nn-structuredquerycondition-icondition2)
</dt> <dt>

[**IConditionFactory**](/windows/desktop/api/Structuredquery/nn-structuredquery-iconditionfactory)
</dt> <dt>

[**IConditionFactory2**](/windows/desktop/api/Structuredquery/nn-structuredquery-iconditionfactory2)
</dt> <dt>

[**IConditionGenerator**](/windows/desktop/api/Structuredquery/nn-structuredquery-iconditiongenerator)
</dt> <dt>

[**IQueryParser**](/windows/desktop/api/Structuredquery/nn-structuredquery-iqueryparser)
</dt> <dt>

[**IQueryParserManager**](/windows/desktop/api/Structuredquery/nn-structuredquery-iqueryparsermanager)
</dt> <dt>

[**IQuerySolution**](/windows/desktop/api/Structuredquery/nn-structuredquery-iquerysolution)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Search Code Samples](-search-samples-ovw.md)
</dt> </dl>

 

 



