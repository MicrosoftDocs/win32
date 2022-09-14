---
title: Desktop apps may not be visible after launching the default web browser or Windows Store apps
description: Desktop apps may not be visible after launching the default web browser or Windows Store apps
ms.assetid: 5D2CE14B-111D-4987-A9AA-B04AC030F9F0
ms.topic: article
ms.date: 05/31/2018
---

# Desktop apps may not be visible after launching the default web browser or Windows Store apps

## Platforms

**Clients** – Windows 8  
**Servers** – Windows Server 2012  


## Description

The Windows Store app user experience is focused on a single app at a time, with multitasking, app switching, and notifications provided by the Windows UI. Windows Store apps are sized to fill available space on screen, with the most common view being full screen. Therefore, when another app on the system is launched, you can no longer assume that the new app will open in a desktop window alongside your desktop app. This is always true of Windows Store apps and browsers that choose to participate in the new Windows UI experience. You may continue to see other apps at the same time, for example, if you are on the Desktop and launch another desktop application or you have applications in a snapped state.

## Manifestation

When a desktop app uses common app activation techniques such as using the ShellExecute API on a file or protocol, Windows launches the app associated with that registration, which may be a Windows Store app and / or the user’s default web browser (the default web browser might choose to participate in either the desktop or the new Windows UI). Windows Store apps are launched using the full screen, hiding the desktop and the desktop app from which it was launched.

> [!Note]  
> In Windows 8, Internet Explorer 10 is configured as the user’s default browser, but the user may choose to install and set another browser as the default (no change from Windows 7). In Internet Explorer 10, when a link is opened from a desktop application, Internet Explorer will open on the desktop. But this setting can be changed by users so that Internet Explorer is opened as a Windows Store app. Browser vendors have been encouraged to adopt a similar ”contextual launching” experience; however, developers should plan for the fact that not all browsers will behave similarly.

 

## Mitigation

While there is no change that developers can make to their apps to mitigate this behavior, there are things the end user can do that you should communicate to them. Consider using the info gathered by the extended ShellExecuteEx() API to populate a contextually appropriate dialog. In that dialog, indicate to the user what app will be launched and whether that app is a Windows Store app or a desktop app. The CLSID can be used to distinguish Windows Store apps from desktop apps. User options:

-   Users who have a wide-screen monitor can snap the Windows Store app to the edge of the screen to expose the desktop and thereby view both the Windows Store app and the desktop app at the same time.
-   If Internet Explorer is configured as the user’s default browser, users can change its behavior by changing the Internet Options in the Control Panel. On the Programs tab, users can change how Internet Explorer handles links. Other browsers may offer a similar setting.

 

 




