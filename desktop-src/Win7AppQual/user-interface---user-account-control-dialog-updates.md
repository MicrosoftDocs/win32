---
Description: .
ms.assetid: f2d4b82d-a84a-4fc1-b7ad-cdc92a24f889
title: User Interface - User Account Control Dialog Updates
ms.topic: article
ms.date: 05/31/2018
---

# User Interface - User Account Control Dialog Updates

## Affected Platforms

<dl> **Clients** - Windows 7  
**Servers** - Windows Server 2008 R2  
</dl>

## Feature Impact

<dl> **Severity** - Low  
**Frequency** - Medium  
</dl>

## Description

In Windows 7, we have standardized the UAC dialog box choices. Previously, users had to select from multiple options, for example, "Continue," "Cancel," and so on. Now all dialog boxes give users a simple "Yes" or "No." The dialog layout now also clearly shows the program name, publisher, and origin.

## Leveraging Feature Capabilities

The application development requirements in Windows 7 for UAC compatibility are the same as in Windows Vista. Windows Vista-compatible applications will interact with UAC in Windows 7 without any modifications. See the User Account Control topics in the *Windows Vista Application Compatibility Cookbook* for information about how to make Windows XP applications work correctly on Windows 7. While the UAC improvements for Windows 7 will impact the user's experience, they will not impact the application interface. However, if there is any help content linked to the UAC dialogs, you may need to update the screenshots.

## Links to Other Resources

-   [Windows Vista Application Compatibility Cookbook](https://msdn.microsoft.com/library/Bb757005(v=MSDN.10).aspx)
-   [Application Compatibility Toolkit Download](http://go.microsoft.com/fwlink/p/?LinkId=526740)
-   [Standard User Analyzer](https://technet.microsoft.com/library/cc766021(WS.10).aspx)

> [!Note]  
> These resources may not be available in some languages and countries/regions.

 

 

 



