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

The DLL registers the information for all its components by exporting [**DllRegisterServer**](/windows/win32/api/olectl/nf-olectl-dllregisterserver) and [**DllUnregisterServer**](/windows/win32/api/olectl/nf-olectl-dllunregisterserver). Use the following functions to register and unregister a component:

-   [**RegOpenKeyEx**](/windows/desktop/api/winreg/nf-winreg-regopenkeyexa)
-   [**RegCreateKeyEx**](/windows/desktop/api/winreg/nf-winreg-regcreatekeyexa)
-   [**RegSetValueEx**](/windows/desktop/api/winreg/nf-winreg-regsetvalueexa)
-   [**RegEnumKeyEx**](/windows/desktop/api/winreg/nf-winreg-regenumkeyexa)
-   [**RegDeleteKey**](/windows/desktop/api/winreg/nf-winreg-regdeletekeya)
-   [**RegCloseKey**](/windows/desktop/api/winreg/nf-winreg-regclosekey)

## Related topics

<dl> <dt>

[Registering COM Applications](registering-com-applications.md)
</dt> </dl>

 

 