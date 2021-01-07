---
description: Demonstrates how to use the Shell\_NotifyIcon and Shell\_NotifyIconGetRect APIs to display a notification icon.
title: NotificationIcon Sample
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 9F31DB2D-4B12-4f65-AC91-25B4B5B1CB46
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# NotificationIcon Sample

Demonstrates how to use the [**Shell\_NotifyIcon**](/windows/desktop/api/Shellapi/nf-shellapi-shell_notifyicona) and [**Shell\_NotifyIconGetRect**](/windows/desktop/api/Shellapi/nf-shellapi-shell_notifyicongetrect) APIs to display a notification icon.

This topic contains the following sections.

-   [Description](#description)
-   [Requirements](#requirements)
-   [Downloading the Sample](#downloading-the-sample)
-   [Building the Sample](#building-the-sample)
-   [Running the Sample](#running-the-sample)

## Description

In addition to the use of [**Shell\_NotifyIcon**](/windows/desktop/api/Shellapi/nf-shellapi-shell_notifyicona) and [**Shell\_NotifyIconGetRect**](/windows/desktop/api/Shellapi/nf-shellapi-shell_notifyicongetrect) to display a notification icon, this sample also demonstrates how to display a rich flyout window, context menu, and balloon notification.

> [!Note]  
> [**Shell\_NotifyIconGetRect**](/windows/desktop/api/Shellapi/nf-shellapi-shell_notifyicongetrect) is only available on Windows 7 and later versions.

 

## Requirements



| Product                                | Minimum Product Version |
|----------------------------------------|-------------------------|
| Windows                                | Windows 7               |
| Windows Software Development Kit (SDK) | 7.0                     |



 

## Downloading the Sample

| Location      | Path URL                                                                                             |
|---------------|------------------------------------------------------------------------------------------------------|
| GitHub  | [NotificationIcon sample](https://github.com/microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/winui/shell/appshellintegration/NotificationIcon) |

## Building the Sample

To build the sample from the command prompt:

1.  Open the command prompt window and navigate to the **NotificationIcon** project directory.
2.  Enter `msbuild NotificationIcon.sln`.

To build the sample using Microsoft Visual Studio (preferred):

1.  Open Windows Explorer and navigate to the **NotificationIcon** project directory.
2.  Double-click the icon for the NotificationIcon.sln file to open the project in Visual Studio.
3.  From the **Build** menu, select **Build Solution**.

## Running the Sample

1.  Navigate to the directory that contains the new executable, using the command prompt or Windows Explorer.
2.  At the command line, enter `NotificationIcon.exe`. Alternatively, from Windows Explorer double-click the icon for NotificationIcon.exe.

> [!Note]  
> Notification icons specified with a GUID are protected against spoofing by validating that only a single application registers them. This registration is performed the first time you call Shell\_NotifyIcon(NIM\_ADD, ...) and the full path name of the calling application is stored. If you later move your binary file to a different location, the system will not allow the icon to be added again. Please see [**Shell\_NotifyIcon**](/windows/desktop/api/Shellapi/nf-shellapi-shell_notifyicona) for more information.

 

 

 



