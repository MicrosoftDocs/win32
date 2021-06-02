---
description: DLL/COM redirection is an application isolation strategy employed by corporate administrators on Windows XP.
ms.assetid: 5bbb0bee-d457-4dfa-93a0-82537fe11f2d
title: DLL/COM Redirection on Windows
ms.topic: article
ms.date: 05/31/2018
---

# DLL/COM Redirection on Windows

DLL/COM redirection is an application isolation strategy employed by corporate administrators on Windows XP.

**Windows Server 2008, Windows Vista, Windows Server 2003 and Windows XP with SP2:  ** The use of DLL/COM redirection strategies is not recommended because isolated applications that use manifests and [side-by-side assemblies](about-side-by-side-assemblies-.md) can be easier to update and service. The presence of a .local file is ignored if a manifest is present. The DLL/COM Redirection strategy using .local files works if the application does not have a manifest.

DLL/COM redirection binds an application to a local version of a component. The local component's files can be kept separate from the system's version of the component in a location that is private to the application. The system's version of the component is globally registered and available to any other applications that bind to it. The local version of the component is reserved for the exclusive use of the application. If necessary, the component files used by the application can be loaded into memory at the same time as the system's component files.

DLL/COM redirection is activated by installing a special file along with a copy of the local component file into the same directory as the application's executable file. The special file is an empty file named after the application executable's file name and appended with .local. For example, to activate DLL/COM redirection for an application named Myapp, the local version of the component and an empty file named Myapp.exe.local must be copied into the folder containing Myapp.exe. This binds the application to the local version of the component rather than the globally shared version of the component.

When an application loads a component file, such as a DLL or .ocx file, Windows first searches for it in the folder where the application's .local and executable file is installed. If found, the application uses that component file regardless of any directory search path defined in the application or the registry. If not found, the component file in the defined search path is used.

The installation utility must do the following to install the application with DLL/COM redirection:

-   An empty .local file must be copied into the same folder as the application's executable file.
-   All of the components, DLL, and .ocx files used by the application must be copied into the same folder as the application's executable file.
-   Isolated COM components must be registered with Windows so that different versions of the assembly will not conflict with each other when loaded into memory at the same time. The registration process requires that, while the implementation of the component can change between versions, certain COM metadata such as CLSID, ProgID, Type Library, and Threading Model cannot.
-   If the application is installed using the Windows Installer, then the application directory can be secured by using the LockPermissions table. Typically, the system is given read, write, and execute access; all other processes are given only execute and read access.

 

 



