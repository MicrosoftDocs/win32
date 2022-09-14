---
description: Applications can depend on a specific version of a shared DLL and start to fail if another application is installed with a newer or older version of the same DLL.
ms.assetid: 3b426b6c-1ad5-43b9-81ea-5e6d3c6588c8
title: Dynamic-Link Library Redirection
ms.topic: article
ms.date: 05/31/2018
---

# Dynamic-Link Library Redirection

Applications can depend on a specific version of a shared DLL and start to fail if another application is installed with a newer or older version of the same DLL. There are two ways to ensure that your application uses the correct DLL: DLL redirection and side-by-side components. Developers and administrators should use DLL redirection for existing applications, because it does not require any changes to the application. If you are creating a new application or updating an application and want to isolate your application from potential problems, create a [side-by-side component](/windows/desktop/SbsCs/isolated-applications-and-side-by-side-assemblies-portal).

To enable DLL redirection machine-wide, you must create a new registry key. Create a new DWORD key called **DevOverrideEnable** at **HKLM\Software\Microsoft\Windows NT\CurrentVersion\Image File Execution Options** and set it to 1. After this, you must restart your computer to see the effects.

To use DLL redirection, create a *redirection file* for your application. The redirection file must be named as follows: *App\_name*.local. For example, if the application name is Editor.exe, the redirection file should be named Editor.exe.local. You must install the .local file in the application directory. You must also install the DLLs in the application directory.

The contents of a redirection file are ignored, but its presence causes Windows to check the application directory first whenever it loads a DLL, regardless of the path specified to [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) or [**LoadLibraryEx**](/windows/desktop/api/LibLoaderAPI/nf-libloaderapi-loadlibraryexa). If the DLL is not found in the application directory, then these functions use their usual search order. For example, if the application c:\\myapp\\myapp.exe calls **LoadLibrary** using the following path:

c:\\program files\\common files\\system\\mydll.dll

And, if both c:\\myapp\\myapp.exe.local and c:\\myapp\\mydll.dll exist, [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) loads c:\\myapp\\mydll.dll. Otherwise, **LoadLibrary** loads c:\\program files\\common files\\system\\mydll.dll.

Alternatively, if a directory named c:\\myapp\\myapp.exe.local exists and contains mydll.dll, [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) loads c:\\myapp\\myapp.exe.local\\mydll.dll.

If the application has a manifest, then any .local files are ignored.

If you are using DLL redirection and the application does not have access to all drives and directories in the search order, [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) stops searching as soon as access is denied. (If you are not using DLL redirection, **LoadLibrary** skips directories that it cannot access and then continues searching.)

It is good practice to install application DLLs in the same directory that contains the application, even if you are not using DLL redirection. This ensures that installing the application does not overwrite other copies of the DLL and cause other applications to fail. Also, if you follow this good practice, other applications do not overwrite your copy of the DLL and cause your application to fail.

 

 
