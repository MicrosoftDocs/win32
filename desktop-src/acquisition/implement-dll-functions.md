---
Description: Implement DLL Functions
ms.assetid: cbb0168b-8003-4058-924f-4ebafc03f582
title: Implement DLL Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Implement DLL Functions

A plug-in that extends the Windows Vista photo acquisition experience must be a DLL that implements the following functions, so it can be registered, unregistered, and loaded into memory.

-   [*DllMain*](https://msdn.microsoft.com/library/windows/desktop/ms682583) The DLL entry point. Your implementation may wish to save the *hInstance* parameter in order to get a module path for use in the implementation of **DllRegisterServer**.
-   [**DllGetClassObject**](https://msdn.microsoft.com/library/windows/desktop/ms680760) Creates a class factory instance, using your implementation of **IClassFactory**.
-   [**DllCanUnloadNow**](https://msdn.microsoft.com/library/windows/desktop/ms690368) Queries whether the DLL can safely be unloaded.
-   [**DllRegisterServer**](https://msdn.microsoft.com/library/windows/desktop/ms682162) Creates registry entries for the DLL. The required registry entries are described in [Register the Plug-in](register-the-plug-in.md).
-   [**DllUnregisterServer**](https://msdn.microsoft.com/library/windows/desktop/ms691457) Removes registry entries for the DLL.

 

 



