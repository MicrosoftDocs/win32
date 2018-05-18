---
Description: 'The SearchEvents code sample demonstrates how to prioritize indexing events.'
ms.assetid: 'a352c3e2-5860-4b9c-a3c7-a806f69b4f7d'
title: SearchEvents
---

# SearchEvents

The SearchEvents code sample demonstrates how to prioritize indexing events.

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
| Code Gallery  | [SearchEvents sample](http://go.microsoft.com/fwlink/p/?linkid=155654)    |
| Windows 7 SDK | [Download Windows 7 SDK](http://go.microsoft.com/fwlink/p/?linkid=129787) |



 

 

> [!Note]  
> After you have downloaded and installed Windows Software Development Kit (SDK), you will find the samples in the installed directory. For example, use of the default installation path for the Windows 7 software development kit (SDK) results in the samples being placed under `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples`.

 

## Building the Sample

To build the sample from the Command Prompt window:

1.  Open the Command Prompt window and navigate to the **StructuredQuerySample** project directory. For example, the full default installation path is `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\WinUI\WindowsSearch\SearchEvents`.
2.  Enter `msbuild Eventing.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **SearchEvents** project directory.
2.  Double-click the icon for the Eventing.sln file to open the project in Visual Studio.
    > [!Note]  
    > The .sln file name extension is not shown under default folder settings. In that situation, it can be identified by its unique icon or by its type description, "Microsoft Visual Studio Solution".

     

3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the new executable, using the Command Prompt window or Windows Explorer.
2.  At the command prompt, enter `Eventing.exe`, or from Windows Explorer, double-click the icon for Eventing.exe.

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[**IRowsetEvents**](-search-irowsetevents.md)
</dt> <dt>

[**IRowsetPrioritization**](-search-irowsetprioritization.md)
</dt> <dt>

[**PRIORITY\_LEVEL**](-search-priority-level.md)
</dt> <dt>

[**ROWSETEVENT\_ITEMSTATE**](-search-rowsetevent-itemstate.md)
</dt> <dt>

[**ROWSETEVENT\_TYPE**](-search-rowsetevent-type.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Search Code Samples](-search-samples-ovw.md)
</dt> </dl>

 

 



