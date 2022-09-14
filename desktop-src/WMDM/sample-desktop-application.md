---
title: Sample Desktop Application
description: Sample Desktop Application
ms.assetid: 3736dd01-b02f-4056-b19b-0e7cc6c9aa67
keywords:
- Windows Media Device Manager,samples
- Device Manager,samples
- desktop applications,samples
- Windows Media Device Manager,desktop application sample
- Device Manager,desktop application sample
- wmdmapp sample application
- samples,desktop applications
ms.topic: article
ms.date: 05/31/2018
---

# Sample Desktop Application

The Windows Media Device Manager ships with a sample desktop application called wmdmapp. This application has a graphical user interface that allows you to browse connected devices, create playlists on the device, and drag media files to the device.

This sample application consists of two pieces:

-   wmdapp.exe, an executable that displays a window and performs most of the user interface and basic functionality of the program, and
-   proghelp.dll, a helper DLL that performs utility functions for the application. You must register this DLL after building the project.

To compile the sample application, you can use Visual Studio. The following section describes how this is done:

-   [Compiling the Sample Application Using Visual Studio](compiling-the-sample-application-using-visual-studio.md)

After compiling the project, register the proghelp.dll file. To register this DLL, open a command prompt and browse to the directory containing this DLL and type `regsvr32 proghelp.dll`.

 

 




