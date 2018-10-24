---
title: Registering Components
description: Registering Components
ms.assetid: d7fd231b-17ec-42ad-9144-df7ed5ffb17b
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Registering Components

When the following types of applications are installed, installation information must be added to the registry, usually through a setup program:

-   Server applications
-   Container/server applications
-   Container applications that allow linking to embedded objects

For all three instances, register COM library (DLL) information and application-specific information.

The DLL registers the information for all its components by exporting [**DllRegisterServer**](https://msdn.microsoft.com/en-us/library/ms682162(v=VS.85).aspx) and [**DllUnregisterServer**](https://msdn.microsoft.com/en-us/library/ms691457(v=VS.85).aspx). Use the following functions to register and unregister a component:

-   [**RegOpenKeyEx**](https://msdn.microsoft.com/library/windows/desktop/ms724897)
-   [**RegCreateKeyEx**](https://msdn.microsoft.com/library/windows/desktop/ms724844)
-   [**RegSetValueEx**](https://msdn.microsoft.com/library/windows/desktop/ms724923)
-   [**RegEnumKeyEx**](https://msdn.microsoft.com/library/windows/desktop/ms724862)
-   [**RegDeleteKey**](https://msdn.microsoft.com/library/windows/desktop/ms724845)
-   [**RegCloseKey**](https://msdn.microsoft.com/library/windows/desktop/ms724837)

## Related topics

<dl> <dt>

[Registering COM Applications](registering-com-applications.md)
</dt> </dl>

 

 




