---
Description: 'Demonstrates the implementation of a property handler for custom format recipe (.recipe) files.'
ms.assetid: 'C8DF5077-0C55-4c7b-8F38-090548EB3743'
title: Recipe Property Handler Sample
---

# Recipe Property Handler Sample

Demonstrates the implementation of a property handler for custom format recipe (.recipe) files.

This topic contains the following sections.

-   [Description](#description)
-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)
-   [Removing the Sample](#removing-the-sample)
-   [Related topics](#related-topics)

## Description

This format supports several properties natively and also supports reading and writing arbitrary properties and custom schema. The sample also includes a custom property schema which defines properties that are germane to the .recipe file format (those not represented by any properties in the system's property schema).

## Requirements



| Product                                | Minimum Product Version |
|----------------------------------------|-------------------------|
| Windows                                | Windows Vista           |
| Windows Software Development Kit (SDK) | 7.0                     |



 

## Downloading the Sample

This sample is available in the following locations.



| Location      | Path URL                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------|
| Code Gallery  | [Windows Shell Integration Samples on Code Gallery](http://go.microsoft.com/fwlink/p/?linkid=155659) |
| Windows 7 SDK | [Download Windows 7 SDK](http://go.microsoft.com/fwlink/p/?linkid=129787)                            |



 

In the case of the Windows SDK, once you have downloaded and installed it, you will find the samples in the installed directory. For example, use of the default installation path for the Windows 7 SDK results in the samples being placed under `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\`.

## Building the Sample

To build the sample from the command prompt:

1.  Open the command prompt window and navigate to the **RecipePropertyHandler** project directory.
2.  Enter `msbuild RecipePropertyHandler.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **RecipePropertyHandler** project directory.
2.  Double-click the icon for the RecipePropertyHandler.sln file to open the project in Visual Studio.
3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the DLL file, using the command prompt or Windows Explorer.
2.  Type `regsvr32.exe RecipePropertyHandler.dll`
3.  (Optional) Type `prop.exe schema register RecipeProperties.propdesc` to register the custom .recipe properties in the property schema.
    > [!Note]  
    > The Prop.exe file can be obtained from <http://www.codeplex.com/prop>. The [Property Schema Sample](shell.samples_PropertySchema) can also be used to register the schema.

     

## Removing the Sample

1.  Using the command prompt, navigate to the directory that contains the DLL file.
2.  Type `regsvr32.exe /u PropertyHandler.dll`.
3.  Type `prop.exe schema unregister RecipeProperties.propdesc`.
4.  Delete the folder that contains the sample source files.

## Related topics

<dl> <dt>

[Property System Code Samples](property-system-code-samples.md)
</dt> <dt>

[Ideal Property Handler Sample](shell.samples_IdealPropertyHandler)
</dt> <dt>

[Playlist Property Handler Sample](shell.samples_PlaylistPropertyHandler)
</dt> <dt>

[Property Edit Sample](shell.samples_PropertyEdit)
</dt> <dt>

[Property Schema Sample](shell.samples_PropertySchema)
</dt> </dl>

 

 



