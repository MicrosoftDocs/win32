---
description: A custom action can call a function defined in a dynamic-link library (DLL) written in C or C++.
ms.assetid: 605c7b97-70bd-467a-9438-47b05d8b6b5d
title: Dynamic-Link Libraries (Windows Installer)
ms.topic: article
ms.date: 05/31/2018
---

# Dynamic-Link Libraries (Windows Installer)

A custom action can call a function defined in a dynamic-link library (DLL) written in C or C++. The DLL can exist as a file installed during the current installation or as a temporary binary stream originating from the [Binary table](binary-table.md) of the installation database.

Note that any called functions, including custom actions in DLLs, must specify the \_\_stdcall calling convention. For example, to call CustomAction use the following.


```C++
#include <windows.h>
#include <msi.h>
#include <Msiquery.h>
#pragma comment(lib, "msi.lib")

UINT __stdcall CustomAction(MSIHANDLE hInstall)
```



For more information see, [Accessing the Current Installer Session from Inside a Custom Action](accessing-the-current-installer-session-from-inside-a-custom-action.md)

The following types of custom actions call a dynamic-link library.



| Custom action type                                 | Description                               |
|----------------------------------------------------|-------------------------------------------|
| [Custom Action Type 1](custom-action-type-1.md)   | DLL file stored in a Binary table stream. |
| [Custom Action Type 17](custom-action-type-17.md) | DLL file installed with a product.        |



 

> [!Note]  
> To use COM you need to call [**CoInitializeEx**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex) in the custom action. Do not quit if you find that the thread has already been initialized. For example, the thread is initialized in a per-machine installation but not in a per-user installation.

 

See [Summary List of All Custom Action Types](summary-list-of-all-custom-action-types.md) for a summary of all types of custom actions and how they are encoded into the [CustomAction table](customaction-table.md).

 

 
