---
Description: The WSSQL code sample demonstrates how to communicate between Microsoft OLE DB and Windows Search through Structured Query Language (SQL).
ms.assetid: 28663608-66b3-4404-9426-5a4b5f52a408
title: WSSQL
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WSSQL

The WSSQL code sample demonstrates how to communicate between Microsoft OLE DB and Windows Search through Structured Query Language (SQL).

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
| Code Gallery  | [WSSQL sample](http://go.microsoft.com/fwlink/p/?linkid=155654)           |
| Windows 7 SDK | [Download Windows 7 SDK](http://go.microsoft.com/fwlink/p/?linkid=129787) |



 

 

> [!Note]  
> After you have downloaded and installed Windows Software Development Kit (SDK), you will find the samples in the installed directory. For example, use of the default installation path for the Windows 7 software development kit (SDK) results in the samples being placed under `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples`.

 

## Building the Sample

To build the sample from the Command Prompt window:

1.  Open the Command Prompt window and navigate to the **WSSQL** project directory. For example, the full default installation path is `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\WinUI\WindowsSearch\WSSQL`.
2.  Enter `msbuild WSSQL.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **WSSQL** project directory.
2.  Double-click the icon for the WSSQL.sln file to open the project in Visual Studio.
    > [!Note]  
    > The .sln file name extension is not shown under default folder settings. In that situation, it can be identified by its unique icon or by its type description, "Microsoft Visual Studio Solution".

     

3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the new executable, using the Command Prompt window or Windows Explorer.
2.  At the command prompt, enter `WSSQL.exe`, or from Windows Explorer, double-click the icon for WSSQL.exe.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Using Windows Search SQL Syntax](-search-sql-windowssearch-entry.md)
</dt> <dt>

[General Query Language Information](-search-sql-generalqueryinfo.md)
</dt> <dt>

[Search Code Samples](-search-samples-ovw.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[OLE DB Programming Overview](https://www.bing.com/search?q=OLE+DB+Programming+Overview)
</dt> </dl>

 

 



