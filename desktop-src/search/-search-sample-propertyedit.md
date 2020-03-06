---
Description: The PropertyEdit code sample demonstrates how to convert the canonical property name to a PROPERTYKEY, set the value of the property store to that of the item, and write the data back to the file stream.
ms.assetid: 5918b4f6-6b6f-4229-8f29-1c41f80b3b02
title: PropertyEdit
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
| Code Gallery  | [PropertyEdit sample](https://code.msdn.microsoft.com/shellextensibility)    |
| Windows 7 SDK | [Download Windows 7 SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx) |



 

 

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

[**IPropertyStore**](https://msdn.microsoft.com/library/Bb761474(v=VS.85).aspx)
</dt> <dt>

[About Properties and Property Handlers](https://msdn.microsoft.com/library/Cc144129(v=VS.85).aspx)
</dt> <dt>

[Property Description Schema](https://msdn.microsoft.com/library/Cc144127(v=VS.85).aspx)
</dt> </dl>

 

 



