---
description: The general rule is that a desktop app can call a Windows Runtime (WinRT) API. However, some APIs, including the XAML UI APIs, require the calling app to have a package identity.
ms.assetid: F3808C28-72DE-49B5-A389-EB085EFC02CC
title: WinRT APIs callable from a desktop app
ms.topic: article
ms.date: 05/31/2018
---

# Calling WinRT APIs from a desktop app

The general rule is that a desktop app can call a WinRT API. However, some APIs, including the XAML UI APIs, require the calling app to have a package identity. UWP apps have a well-defined app model, and they have a package identity. The other types of desktop apps have neither a well-defined app model, nor a package identity. Therefore, if an API requires a package identity, a WPF, Windows Forms, or Win32 app cannot call it unless the app [is packaged in an MSIX package](/windows/msix/desktop/desktop-to-uwp-root).

## The DualApiPartition attribute

This is the process to follow whenever there's a particular WinRT that you'd like to call from your desktop app. This process will answer the question of whether the API is allowed to be called from a desktop app. First, visit the [Windows API reference for Windows Runtime apps](/uwp/), find the reference topic for the class or member API you're interested in, and check whether the [**DualApiPartition**](/uwp/api/Windows.Foundation.Metadata.DualApiPartitionAttribute) attribute is listed in the Attributes section.

## If the DualApiPartition attribute is listed

If the DualApiPartition attribute is listed, the API does not need the calling app to have a package identity, and the API is allowed to be called from any desktop app. [**Windows.Devices.Geolocation.Geolocator**](/uwp/api/Windows.Devices.Geolocation.Geolocator) is an example; an app does not need to be uniquely identified in order to perform location tasks.

## If the DualApiPartition attribute is not listed

If the DualApiPartition attribute is not listed, the API does need the calling app to have a package identity. Therefore a WPF, Windows Forms, or Win32 app is not allowed to call the API unless the app has been converted to a UWP app. [**Windows.UI.Xaml.Controls.Button**](/uwp/api/Windows.UI.Xaml.Controls.Button) is an example.
