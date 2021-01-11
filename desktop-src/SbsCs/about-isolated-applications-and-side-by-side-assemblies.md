---
description: Isolated applications and side-by-side assemblies provide a solution that reduces DLL versioning conflicts. They enable applications to safely share assemblies. For more information, see Shared Assemblies.
ms.assetid: 0fb0d9c2-9f6d-4fcd-a6c6-9ba8fe9f5fb5
title: About Isolated Applications and Side-by-side Assemblies
ms.topic: article
ms.date: 05/31/2018
---

# About Isolated Applications and Side-by-side Assemblies

[Isolated applications](isolated-applications.md) and [side-by-side assemblies](about-side-by-side-assemblies-.md) provide a solution that reduces [*DLL versioning conflicts*](d-sbscs-gly.md). They enable applications to safely share assemblies. For more information, see [Shared Assemblies](/windows/desktop/Msi/shared-assemblies).

An assembly is a fundamental unit for naming, binding, versioning, deploying, or configuring a block of programming code. Applications with common functionality may run shared blocks of programming code which are referred to as modules or code assemblies. These code assemblies may be placed in DLLs or COM assemblies. The infrastructure for the safe sharing of assemblies is referred to as side-by-side assembly sharing.

[Side-by-side assemblies](about-side-by-side-assemblies-.md) are code assemblies described by [manifests](manifests.md) and authored so that multiple versions may run at the same time without conflicting with each other. When developers author manifests and write applications to use [side-by-side assembly sharing](side-by-side-assembly-sharing.md), multiple assembly versions can run on the system and each application can specify which assembly version it should use.

A typical [*side-by-side assembly*](s-sbscs-gly.md) is a single DLL with a single manifest. Side-by-side assemblies store the information about binding and COM activation, traditionally saved in the registry, in manifests. In some cases, the versions of the assembly specified in manifests can be changed, on a global or per-application basis, by assembly publishers, application developers, or administrators. For more information, see [default configuration](default-configuration.md), [publisher configuration](publisher-configuration.md), and [per-application configuration](per-application-configuration.md).

Developers can use the side-by-side assemblies provided by Microsoft, or other side-by-side assembly publishers, in their applications. For example, developers can get the functionality of the updated common controls, such as theming, by designing their applications to use the side-by-side assembly that contains Comctl32.dll 6.0. For the list of side-by-side assemblies and manifests that ship with Windows XP, see [Supported Microsoft Side-by-side Assemblies](supported-microsoft-side-by-side-assemblies.md). Developers can also create their own side-by-side assemblies. For more information, see [Guidelines for Creating Side-by-side Assemblies](guidelines-for-creating-side-by-side-assemblies.md).

 

 
