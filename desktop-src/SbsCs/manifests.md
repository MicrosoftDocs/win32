---
description: Manifests are XML files that accompany and describe side-by-side assemblies or isolated applications.
ms.assetid: '53c4c2e6-fff9-4506-b7e0-d091d2ec9883'
title: Manifests
ms.topic: article
ms.date: 05/31/2018
---

# Manifests

Manifests are XML files that accompany and describe side-by-side assemblies or isolated applications. Manifests uniquely identify the assembly through the assembly's **assemblyIdentity** element. They contain information used for binding and activation, such as COM classes, interfaces, and type libraries, that has traditionally been stored in the registry. Manifests also specify the files that make up the assembly and may include Windows classes if the assembly author wants them to be versioned. Side-by-side assemblies are not registered on the system, but are available to applications and other assemblies on the system that specify dependencies in manifest files.

Manifest files enable administrators and applications to manage side-by-side assembly versions after deployment. Every side-by-side assembly must have a manifest associated with it. The installation of Windows XP installs the [supported Microsoft side-by-side assemblies](supported-microsoft-side-by-side-assemblies.md) with their manifests. If you develop your own side-by-side assemblies, you must also install manifest files. For more information, see [Installing Side-by-Side Assemblies](installing-side-by-side-assemblies.md) and [Manifest Files Reference](manifest-files-reference.md).

Manifests and configuration files are not localized.

The following types of manifests are used with side-by-side assemblies:

-   [Assembly manifests](assembly-manifests.md) describe side-by-side assemblies. They are used to manage the names, versions, resources, and dependent assemblies of side-by-side assemblies. The manifests of [shared assemblies](/windows/desktop/Msi/shared-assemblies) are stored in the WinSxS folder of the system. Private assembly manifests are stored either as a resource in the DLL or in the application folder
-   [Application manifests](application-manifests.md) describe [isolated applications](isolated-applications.md). They are used to manage the names and versions of shared side-by-side assemblies that the application should bind to at run time. Application manifests are copied into the same folder as the application executable file or included as a resource in the application's executable file.
-   [Application Configuration Files](application-configuration-files.md), are manifests used to override and redirect the versions of dependent assemblies used by side-by-side assemblies and applications.
-   [Publisher Configuration Files](publisher-configuration-files.md), are manifests used to redirect the version of a side-by-side assembly to another compatible version. The version that the assembly is being redirected to should have the same major.minor values as the original version.

 

 
