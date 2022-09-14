---
title: Classes and Servers
description: Classes and Servers
ms.assetid: cc88be56-0d96-47d2-b23b-6a6ad376bdae
ms.topic: article
ms.date: 05/31/2018
---

# Classes and Servers

COM uses **HKEY\_CLASSES\_ROOT** for computer-wide settings but also allows per-user configuration of CLSIDS for greater security and flexibility. COM first consults **HKEY\_CURRENT\_USER\\Software\\Classes** before looking under **HKEY\_CLASSES\_ROOT**. COM keeps computer-wide information related to CLSIDs under **HKEY\_CLASSES\_ROOT\\CLSID** and keeps per-user class information under **HKEY\_CURRENT\_USER\\Software\\Classes\\CLSID**.

COM servers support self-registration. For an in-process server, this means that the DLL must export the following functions:

-   [**DllRegisterServer**](/windows/win32/api/olectl/nf-olectl-dllregisterserver)
-   [**DllUnregisterServer**](/windows/win32/api/olectl/nf-olectl-dllunregisterserver)

You must explicitly export these functions by using a module definition file, linker switches, or compiler directives. The class store uses these functions to configure the local registry after downloading the file to the client machine. In addition to class store, these functions are also used by other environments to install servers on host computers.

## Related topics

<dl> <dt>

[Registering COM Applications](registering-com-applications.md)
</dt> </dl>

 

 