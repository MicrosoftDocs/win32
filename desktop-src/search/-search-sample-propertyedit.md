---
Description: The PropertyEdit code sample demonstrates how to convert the canonical property name to a PROPERTYKEY, set the value of the property store to that of the item, and write the data back to the file stream.
ms.assetid: 5918b4f6-6b6f-4229-8f29-1c41f80b3b02
title: PropertyEdit
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PropertyEdit

The PropertyEdit code sample demonstrates how to convert the canonical property name to a PROPERTYKEY, set the value of the property store to that of the item, and write the data back to the file stream.

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
| Code Gallery  | [PropertyEdit sample](http://go.microsoft.com/fwlink/p/?linkid=155658)    |
| Windows 7 SDK | [Download Windows 7 SDK](http://go.microsoft.com/fwlink/p/?linkid=129787) |



 

 

> [!Note]  
> After you have downloaded and installed the Windows Software Development Kit (SDK), you will find the samples in the installed directory. For example, use of the default installation path for the Windows 7 software development kit (SDK) results in the samples being placed under `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples`.

 

## Building the Sample

To build the sample from the Command Prompt:

1.  Open the Command Prompt window and navigate to the **PropertyEdit** project directory. For example, the full default installation path is `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\WinUI\Shell\AppPlatform\PropertyEdit`.
2.  Enter `msbuild PropertyEdit.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **PropertyEdit** project directory.
2.  Double-click the icon for the PropertyEdit.sln file to open the project in Visual Studio.
    > [!Note]  
    > The .sln file name extension is not shown under default folder settings. In that situation, it can be identified by its unique icon or by its type description, "Microsoft Visual Studio Solution".

     

3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the new executable, using the Command Prompt window or Windows Explorer.
2.  At the command prompt, enter `PropertyEdit.exe`, or from Windows Explorer, double-click the icon for PropertyEdit.exe.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Search Code Samples](-search-samples-ovw.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**IPropertyStore**](https://msdn.microsoft.com/windows/desktop/e995aaa1-d4c9-475f-b1fa-b9123cd5b653)
</dt> <dt>

[About Properties and Property Handlers](https://msdn.microsoft.com/windows/desktop/a773c7b3-a1a2-4cce-ae5f-b54217ea06f4)
</dt> <dt>

[Property Description Schema](https://www.bing.com/search?q=Property+Description+Schema)
</dt> </dl>

 

 



