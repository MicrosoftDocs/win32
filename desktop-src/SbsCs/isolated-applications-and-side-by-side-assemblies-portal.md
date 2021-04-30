---
description: Manage assembly sharing and DLL versioning in the systems side by side assembly store from programs. Write assembly manifests and self describing applications for assembly sharing and redirecting DLLs.
ms.assetid: 2f841eb6-9a6c-4c9b-b057-a3da6cd6b0b0
title: Isolated Applications and Side-by-side Assemblies
ms.topic: article
ms.date: 05/31/2018
---

# Isolated Applications and Side-by-side Assemblies

## Purpose

Isolated Applications and Side-by-side Assemblies is a Microsoft Windows solution that reduces versioning conflicts in Windows-client applications. With Windows, application developers can build isolated applications that are fully self-describing and unaffected by changes to the registry, other applications, or other versions of assemblies running on the system. Application authors and administrators can use manifests to manage the sharing of side-by-side assemblies after deployment on either a global or per-application basis. Customers benefit from isolated applications that are more stable and more reliably updated.

## Where applicable

Isolated applications and side-by-side assembly sharing can be used to develop applications that safely share operating system assemblies. Developers can use this technology to correct DLL versioning conflicts caused by an incompatible version of a shared assembly.

If your application must consistently get the version of a component you have tested, it is possible to isolate your application so that it will always be run with the tested version of the component on the user's computer.

Isolated Applications and Side-by-side Assemblies is intended for the development of desktop style applications.

## Developer audience

This documentation is primarily intended for software developers, application developers, and network administrators:

-   Software developers who want to create isolated applications that will use the side-by-side assemblies made available by Microsoft and other side-by-side assembly publishers.
-   Application developers who are interested in creating their own side-by-side assemblies to isolate their applications.
-   Network administrators who want more information about isolated applications.

As the primary reference for side-by-side assembly sharing and isolated applications, this documentation provides general background information about authoring manifests and side-by-side assemblies, installing isolated applications and side-by-side assemblies, and using the Activation Context API.

## Run-time requirements

Windows Server 2003 and later or Windows XP and later is required to use side-by-side assemblies and manifests to isolate applications and to use the Activation Context API.

## In this section



| Topic                                                         | Description                                                                    |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| [Reference](side-by-side-assemblies-reference.md)<br/> | Documentation of Isolated Applications and Side-by-side Assemblies.<br/> |



 

 

 




