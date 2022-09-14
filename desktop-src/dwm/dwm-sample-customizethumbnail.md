---
title: Customize an Iconic Thumbnail and a Live Preview Bitmap
description: Shows how to customize an iconic thumbnail and a live preview bitmap (also called a Peek preview).
ms.assetid: 43fe71e7-4e5c-46fb-876b-e26996071665
ms.topic: article
ms.date: 05/31/2018
ms.custom: project-verbatim
---

# Customize an Iconic Thumbnail and a Live Preview Bitmap

## Description

You can customize an iconic thumbnail and a *live preview* (or *Peek preview*) bitmap by using functions and messages that are introduced in the Windows 7 Desktop Window Manager (DWM) APIs.

Specifically, you use the [**DwmSetIconicThumbnail**](/windows/win32/api/Dwmapi/nf-dwmapi-dwmseticonicthumbnail) function and the [**WM\_SENDICONICTHUMBNAILBITMAP**](wm-dwmsendiconicthumbnail.md) message to customize an iconic thumbnail. You can also use the [**DwmSetIconicLivePreviewBitmap**](/windows/win32/api/Dwmapi/nf-dwmapi-dwmseticoniclivepreviewbitmap) function and the [**WM\_SENDICONICLIVEPREVIEWBITMAP**](wm-dwmsendiconiclivepreviewbitmap.md) message to set an iconic live preview bitmap.

For a sample application that uses the **DwmSetIconicThumbnail** function, see [TabThumbnails sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/shell/appshellintegration/TabThumbnails).

The following illustration shows a default thumbnail transformed into a customized thumbnail.

![illustration of an original thumbnail image and a modified thumbnail image with a custom bitmap](images/customthumbnail.jpg)

## Requirements

| Requirement | Value |
|--------------------------|---------------------------------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 7 or Windows Vista with Service Pack 2 (SP2) and Platform Update for Windows Vista                          |
| Minimum supported server | Windows Server 2008 R2 or Windows Server 2008 with Service Pack 2 (SP2) and Platform Update for Windows Server 2008 |
| Minimum Windows SDK      | [Windows Software Development Kit (SDK) for Windows 7](https://msdn.microsoft.com/windows/bb980924.aspx)             |

## Building the TabThumbnails sample

**To build the sample by using Microsoft Visual Studio (preferred method)**

1.  Open Windows Explorer and browse to the folder where the TabThumbnails.sln file is located.
2.  Double-click the solution file (.sln) to open the file in Microsoft Visual Studio.
3.  On the **Build** menu, click **Build Solution**. The application is built in the default \\Debug or \\Release directory.

**To build the sample by using the command prompt**

1.  Open a Command Prompt window and browse to the sample directory.
2.  Enter `msbuild TabThumbnails.sln`.

## Related topics

[Desktop Window Manager](dwm-overview.md)

[Windows Development](/windows/desktop/win32-and-com-development)
