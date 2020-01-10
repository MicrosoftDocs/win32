---
title: Registering Components
description: Registering Components
ms.assetid: d7fd231b-17ec-42ad-9144-df7ed5ffb17b
ms.topic: article
ms.date: 05/31/2018
---

# Registering Components

When the following types of applications are installed, installation information must be added to the registry, usually through a setup program:

-   Server applications
-   Container/server applications
-   Container applications that allow linking to embedded objects

For all three instances, register COM library (DLL) information and application-specific information.

The DLL registers the information for all its components by exporting [**DllRegisterServer**](https://msdn.microsoft.com/library/ms682162(v=VS.85).aspx) and [**DllUnregisterServer**](https://msdn.microsoft.com/library/ms691457(v=VS.85).aspx). Use the following functions to register and unregister a component:

-   [**RegOpenKeyEx**](https://docs.microsoft.com/windows/desktop/api/winreg/nf-winreg-regopenkeyexa)
-   [**RegCreateKeyEx**](https://docs.microsoft.com/windows/desktop/api/winreg/nf-winreg-regcreatekeyexa)
-   [**RegSetValueEx**](https://docs.microsoft.com/windows/desktop/api/winreg/nf-winreg-regsetvalueexa)
-   [**RegEnumKeyEx**](https://docs.microsoft.com/windows/desktop/api/winreg/nf-winreg-regenumkeyexa)
-   [**RegDeleteKey**](https://docs.microsoft.com/windows/desktop/api/winreg/nf-winreg-regdeletekeya)
-   [**RegCloseKey**](https://docs.microsoft.com/windows/desktop/api/winreg/nf-winreg-regclosekey)

## Related topics

<dl> <dt>

[Registering COM Applications](registering-com-applications.md)
</dt> </dl>

 

 




