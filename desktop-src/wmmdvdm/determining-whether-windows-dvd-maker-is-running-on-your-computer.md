---
title: Determining Whether Windows DVD Maker is Running on Your Computer
description: Determining Whether Windows DVD Maker is Running on Your Computer
ms.assetid: 0a64e774-f3dd-401d-843e-644a1713e821
keywords:
- Windows DVD Maker,verifying whether program is running
- DVD Maker,verifying whether program is running
- programming guide,verifying whether Windows DVD Maker is running
- CreateMutex function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Determining Whether Windows DVD Maker is Running on Your Computer

You can determine whether Windows DVD Maker is running on your computer by using the following system services function:


```C++
HANDLE WINAPI CreateMutex( LPSECURITY_ATTRIBUTES 
lpMutexAttributes, BOOL 
bInitialOwner, LPCTSTR 
lpName ); 
```



By calling **CreateMutex** with the string "Global\\\\BurnWizard" as the value of the *lpName* parameter, you will be attempting to create the same mutex that Windows DVD Maker creates when it runs. If your creation fails (the handle returned is **NULL**), then Windows DVD Maker is already running on your system.

For more information, see the reference for the [CreateMutex](http://go.microsoft.com/fwlink/p/?linkid=91954) function on MSDN.

## Related topics

<dl> <dt>

[**Getting Information from Windows Vista About Windows Movie Maker and Windows DVD Maker**](getting-information-from-windows-vista-about-windows-movie-maker-and-windows-dvd-maker.md)
</dt> </dl>

 

 




