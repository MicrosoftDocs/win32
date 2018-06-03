---
title: Registering an Application with Still Image
description: Once an STI-compatible application is installed, it must be registered as an application that can use the push model with the STI API.
ms.assetid: ab4cdbd0-002a-4659-abe5-5d89f69d0cb2
keywords:
- Still Image (STI),registering applications
- STI (Still Image),registering applications
- Still Image API,registering applications
- still images,registering applications with STI
- registering applications with STI
- RegisterLaunchApplication method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Registering an Application with Still Image

Once an STI-compatible application is installed, it must be registered as an application that can use the push model with the STI API. This is done in one of two ways:

1.  The install program can call [**RegisterLaunchApplication**](istillimage-registerlaunchapplication.md).
2.  The application itself can call [**RegisterLaunchApplication**](istillimage-registerlaunchapplication.md) the first time it runs.

The application must be registered by invoking the [**RegisterLaunchApplication**](istillimage-registerlaunchapplication.md) method at least once. It is actually preferable to have your application call **RegisterLaunchApplication** every time it runs. That way, the Still Image system is able to find the application even if it has been moved.

Once the application is registered, the user must manually connect the application to device events by using the Still Image Control Panel.

When a registered, push-model application is uninstalled, it must remove its information from the Still Image system. The STI method [**UnRegisterLaunchApplication**](istillimage-unregisterlaunchapplication.md) removes this information.

 

 




