---
title: Implementing and Exporting the DLL Entry Points
description: Implementing and Exporting the DLL Entry Points
ms.assetid: 95b4c251-6c45-48c6-a630-6d94532da25a
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Implementing and Exporting the DLL Entry Points

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Each filter DLL (denoted by filter.dll in this section) must implement and export the following entry points. These entry points are typically exported using a module-definition (.def) file for the filter or by using the **\_\_declspec(dllexport)** keyword. The DLL file can be registered to be in any folder, but it usually resides in the %SystemRoot%\\system32 folder.

### DllRegisterServer

The [DllRegisterServer](_com_dllregisterserver) entry point registers the DLL as a persistent handler in the registry. You register the DLL by running the regsvr32.exe program with the filter DLL file name as an argument.

**regsvr32.exe %SystemRoot%\\system32\\filter.dll**

All the sample filters use macros defined in the header file filtreg.hxx to implement the registration entry point.

### DllUnregisterServer

The [DllUnregisterServer](_com_dllunregisterserver) entry point removes the DLL as a persistent handler in the registry. You unregister the DLL by running the regsvr32.exe program with the /u flag:

**regsvr32.exe /u %SystemRoot%\\system32\\filter.dll**

All the sample filters use macros, defined in the header file filtreg.hxx, to implement the unregistration entry point.

### DllGetClassObject

The content indexing client calls the [DllGetClassObject](_com_dllgetclassobject) entry point, through COM, to create a class factory object for the filter and to get a pointer to the class factory interface of that object.

### DllCanUnloadNow

The content-indexing client calls the [DllCanUnloadNow](_com_dllcanunloadnow) entry point, through COM, to determine whether it is possible to unload the filter DLL. The filter is unloaded after it is unused for an interval of time as specified by the [FilterIdleTimeOut](filteridletimeout.md) registry value.

 

 




