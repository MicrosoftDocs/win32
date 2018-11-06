---
title: Compiling the Sample Application Using Visual Studio
description: Compiling the Sample Application Using Visual Studio
ms.assetid: 78345cdb-5f0d-4ea8-9492-30386f5fa6ee
keywords:
- Windows Media Device Manager,samples
- Device Manager,samples
- desktop applications,samples
- Windows Media Device Manager,desktop application sample
- Device Manager,desktop application sample
- samples,desktop applications
- samples,compiling using Visual Studio
ms.topic: article
ms.date: 05/31/2018
---

# Compiling the Sample Application Using Visual Studio

The Windows Media Device Manager SDK includes a Visual Studio solution that is compatible with Microsoft Visual Studio 2005.

Before you compile the sample application, you must rename the header file shtypes.h to prevent conflicts with a file of the same name that is found in the Microsoft Platform SDK. For example, you could rename <*SDK Installation Path*>\\WMFSDK11\\include\\shtypes.h to <*SDK Installation Path*>\\WMFSDK11\\include\\shtypes.h.backup.

To build the application, start an instance of Visual Studio 2005, open the solution file, wmdmapp.sln, which is found in the folder <*SDK installation path*>\\WMFSDK11\\apps\\wmdmapp and choose the **Build/Build Solution** option. This will create two project files: the helper project, proghelp.vcproj, as well as the main application wmdmapp.vcproj. In addition, it will create the progress helper DLL and the main application (WMDMApp.exe).

## Related topics

<dl> <dt>

[**Sample Desktop Application**](sample-desktop-application.md)
</dt> </dl>

 

 




