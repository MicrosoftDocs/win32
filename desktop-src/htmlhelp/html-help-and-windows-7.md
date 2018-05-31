---
title: HTML Help and Windows 7
description: This topic describes an important safety feature added to HTML Help in Windows 7.
ms.assetid: D289B585-E119-4059-845F-AFA4DB8BA478
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HTML Help and Windows 7

This topic describes an important safety feature added to HTML Help in Windows 7.

To help protect against malicious websites launched through legacy Help content, Windows 7 introduces the **IHxHelpPane::Execute()** method for HTML Help. In essence, this new method ensures that any browser window opened by HTML Help will have the same protection as a new browser window launched directly by the user. It helps prevent an HTML Help instance with elevated permissions from launching a browser window with those same elevated permissions.

> \[!Important\]  
> The **IHxHelpPane::Execute()** method may not be available in future versions of Windows, and is therefore not recommended for use.

 

## Description

Developers can call **IHxHelpPane::Execute()**, passing in any valid URL. If the URL is an HTTP address, it is passed to the user's default browser. An instance of the default browser will open with the same privileges as the logged-on user, even if the application that makes the call is running with elevated permissions or is running under a different user. If the user's default browser is Internet Explorer, this method gives the added benefit of Protected Mode browsing, which is turned on by default for non-elevated instances of the browser.

For example, suppose a user is logged on as a Standard user and has Internet Explorer set as the default browser. The user runs your application as an Administrator. Your application can call the **Execute()** method for a given URL, and the instance of Internet Explorer that launches will be run as a Standard user.

## Related topics

<dl> <dt>

[IHxHelpPane::Execute Method](http://msdn.microsoft.com/library/ihxhelppane__execute_method(VS.85).aspx)
</dt> </dl>

 

 




