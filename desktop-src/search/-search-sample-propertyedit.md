---
description: The PropertyEdit code sample demonstrates how to convert the canonical property name to a PROPERTYKEY, set the value of the property store to that of the item, and write the data back to the file stream.
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
| GitHub  | [PropertyEdit sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/shell/appplatform/PropertyEdit)    |



 

 

> [!Note]  
> For all versions of Windows, including Windows 7, it is recommended to download the samples directly from GitHub for the most up to date version.

 

## Building the Sample

To build the sample from the Command Prompt:

1.  Open the Command Prompt window and navigate to the **PropertyEdit** project directory. 
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

[**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore)
</dt> <dt>

[About Properties and Property Handlers](../properties/building-property-handlers-properties.md)
</dt> <dt>

[Property Description Schema](/previous-versions//cc144127(v=vs.85))
</dt> </dl>

 

 
