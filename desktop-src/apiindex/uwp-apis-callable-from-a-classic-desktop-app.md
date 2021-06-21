---
description: The general rule is that a desktop app can call a Windows Runtime (WinRT) API. However, some APIs, including the XAML UI APIs, require the calling app to have a package identity.
ms.assetid: F3808C28-72DE-49B5-A389-EB085EFC02CC
title: WinRT APIs callable from a desktop app
ms.topic: article
ms.date: 05/31/2018
---

# WinRT APIs callable from a desktop app

Most [Windows Runtime (WinRT) APIs](/uwp/api/) can be used by desktop (.NET and native C++) apps. However, some WinRT classes are designed for and are only supported for use in UWP apps. This includes [CoreDispatcher](/uwp/api/Windows.UI.Core.CoreDispatcher), [CoreWindow](/uwp/api/Windows.UI.Core.CoreWindow), [ApplicationView](/uwp/api/windows.ui.viewmanagement.applicationview), and some related classes. Other WinRT classes work in desktop apps except for specific members.

For more information, see [Windows Runtime APIs not supported in desktop apps](/windows/apps/desktop/modernize/desktop-to-uwp-supported-api). Where available, this article suggests alternative APIs to achieve the same functionality as the unsupported APIs.
