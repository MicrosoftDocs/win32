---
title: Dynamic-link library redirection
description: If your application depends on a specific version of a shared DLL, and another application is installed with a newer or older version of that DLL, then that can cause a problem; it can cause your app to start to fail.
ms.assetid: 3b426b6c-1ad5-43b9-81ea-5e6d3c6588c8
ms.topic: article
ms.date: 02/01/2023
---

# Dynamic-link library redirection

If your application depends on a specific version of a shared DLL, and another application is installed with a newer or older version of that DLL, then that can cause a problem; it can cause your app to start to fail.

There are two ways to ensure that your app continues to use the correct DLL:

* DLL redirection. Continue to read this topic for more details.
* Side-by-side components. Described in the topic [Isolated applications and side-by-side assemblies](/windows/win32/SbsCs/isolated-applications-and-side-by-side-assemblies-portal).

> [!TIP]
> If you're a developer or an administrator, then you should use DLL redirection for existing applications. That's because it doesn't require any changes to the app itself. But if you're creating a new app, or updating an existing app, and you want to isolate your app from potential problems, then create a side-by-side component.

To enable DLL redirection machine-wide, you must create a new registry key. Under the key `HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options`, create a new **DWORD** value with the name *DevOverrideEnable*. Set the value to 1, and restart your computer. Or use the command below (and restart your computer).

```console
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options" /v DevOverrideEnable /t REG_DWORD /d 1
```

To use DLL redirection, create a *redirection file* for your app. The redirection file must be named `<your_app_name>.local`. So if your app's name is `Editor.exe`, then name your redirection file `Editor.exe.local`. You must install the redirection file in the app directory. You must also install the DLLs in the app directory.

The contents of a redirection file are ignored, but just its presence causes Windows to check the app directory first whenever it loads a DLL, regardless of the path specified to [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) or [**LoadLibraryEx**](/windows/win32/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa). If the DLL isn't found in the app directory, then these functions use their usual search order. For example, if the app `c:\myapp\myapp.exe` calls **LoadLibrary** using the following path:

`c:\program files\common files\system\mydll.dll`

And, if both `c:\myapp\myapp.exe.local` and `c:\myapp\mydll.dll` exist, then [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) loads `c:\myapp\mydll.dll`. Otherwise, **LoadLibrary** loads `c:\program files\common files\system\mydll.dll`.

Alternatively, if a directory named `c:\myapp\myapp.exe.local` exists, and it contains `mydll.dll`, then [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) loads `c:\myapp\myapp.exe.local\mydll.dll`.

If the app has a manifest, then any redirection files are ignored.

If you're using DLL redirection and the app doesn't have access to all drives and directories in the search order, then [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) stops searching as soon as access is denied. If you're *not* using DLL redirection, then **LoadLibrary** skips directories that it can't access, and then it continues searching.

It's good practice to install app DLLs in the same directory that contains the app; even if you're not using DLL redirection. That ensures that installing the app doesn't overwrite other copies of the DLL (thereby causing other apps to fail). Also, if you follow this good practice, then other apps don't overwrite your copy of the DLL (and don't cause your app to fail).
