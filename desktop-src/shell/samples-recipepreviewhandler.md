---
Description: Demonstrates how to write a handler used to display a file preview inside the Windows Explorer preview pane or other preview handler hosts.
title: Recipe Preview Handler Sample
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 2C926922-48C0-46f5-8928-67007C6FF957
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Recipe Preview Handler Sample

Demonstrates how to write a handler used to display a file preview inside the Windows Explorer preview pane or other preview handler hosts.

This topic contains the following sections:

-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)
-   [Unregistering the Sample Preview Handler DLL](#unregistering-the-sample-preview-handler-dll)
-   [Related topics](#related-topics)

## Requirements



| Product                                | Minimum Product Version |
|----------------------------------------|-------------------------|
| Windows                                | Windows Vista           |
| Windows Software Development Kit (SDK) | 7.0                     |



 

## Downloading the Sample

This sample is available in the following locations.



| Location      | Link                                                                                                 |
|---------------|------------------------------------------------------------------------------------------------------|
| Code Gallery  | [Windows Shell Integration Samples on Code Gallery](https://code.msdn.microsoft.com/shellintegration) |
| Windows 7 SDK | [Download Windows 7 SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx)                            |



 

In the case of the Windows SDK, once you have downloaded and installed it, you will find the samples in the installed directory. For example, use of the default installation path for the Windows 7 SDK results in the samples being placed under `C:\Program Files\Microsoft SDKs\Windows\v7.0\Samples\`.

## Building the Sample

To build the sample from the command prompt:

1.  Open the command prompt window and navigate to the **RecipePreviewHandler** project directory. For example, `C:\Program Files\MicrosoftSDKs\Windows\v7.0\Samples\WinUI\Shell\AppShellIntegration\RecipePreviewHandler`.
2.  Enter `msbuild PreviewHandlerSDKSample.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **RecipePreviewHandler** project directory.
2.  Double-click the icon for the PreviewHandlerSDKSample.sln file to open the project in Visual Studio.
    > [!Note]  
    > The .sln file name extension is not shown under default folder settings. In that situation, it can be identified by its unique icon or by its type description "Microsoft Visual Studio Solution".

     

3.  From the **Build** menu, select **Build Solution**.

> [!Note]  
> If the target system is 64-bit (x64), this sample preview handler must be built as a 64-bit application.

 

## Running the Sample

1.  Open the command prompt window and navigate to the built **RecipePreviewHandler** project directory. For example, `C:\Program Files\MicrosoftSDKs\Windows\v7.0\Samples\WinUI\Shell\AppShellIntegration\RecipePreviewHandler\RecipePreviewHandler`. Enter `regsvr32.exe PreviewHandlerSDKSample.dll` to register the handler.
2.  Open Windows Explorer and show the preview pane if it is not already displayed.
    -   **Windows 7**: Click the preview pane button.
    -   **Windows Vista**: Click the **Organize** menu, go to the **Layout** submenu and select **Preview Pane**.
3.  Use Windows Explorer to navigate to the **RecipePreviewHandler** project directory.
4.  Select the example .recipe file.

To make both the 32-bit (x86) and 64-bit (x64) output work on a 64-bit version of Windows, set the **AppId** value to the WOW64 surrogate host `{534A1E02-D58F-44f0-B58B-36CBED287C7C}`, as shown in the following code.


```
{HKEY_CURRENT_USER,   
 L"Software\\Classes\\CLSID\\" SZ_CLSID_RecipePreviewHandler,
 L"AppID",
 L"{534A1E02-D58F-44f0-B58B-36CBED287C7C}"}
```



## Unregistering the Sample Preview Handler DLL

-   Open the command prompt window and enter `regsvr32.dll /u PreviewHandlerSDKSample.dll` to unregister the handler.

## Related topics

<dl> <dt>

[**IPreviewHandler**](https://msdn.microsoft.com/library/Bb775315(v=VS.85).aspx)
</dt> <dt>

[**IPreviewHandlerFrame**](https://msdn.microsoft.com/library/Bb775309(v=VS.85).aspx)
</dt> <dt>

[Application User Model IDs (AppUserModelIDs)](appids.md)
</dt> </dl>

 

 



