---
description: Side-by-side assemblies are used with the following types of manifest and configuration files. Manifests and configurations are XML files.
ms.assetid: 8b969a8f-586c-4556-87be-92db6c61e8ce
title: Manifest Files Reference
ms.topic: article
ms.date: 05/31/2018
---

# Manifest Files Reference

Side-by-side assemblies are used with the following types of manifest and configuration files. Manifests and configurations are XML files.



| Manifest                                                               | Description                                                                                                                                                                                                   |
|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Assembly manifests](assembly-manifests.md)                           | Describes the names, versions, resources, and assembly dependencies of side-by-side assemblies.                                                                                                               |
| [Application manifests](application-manifests.md)                     | Describes the names and versions of shared side-by-side assemblies that the application should bind to at run time and may also contain metadata for private side-by-side assemblies used by the application. |
| [Application Configuration Files](application-configuration-files.md) | Redirects the assembly versions of assembly dependencies using [per-application configuration](per-application-configuration.md).                                                                            |
| [Publisher Configuration Files](publisher-configuration-files.md)     | Redirects the assembly versions of assembly dependencies on a per-assembly basis using a [publisher configuration](publisher-configuration.md).                                                              |



 

For a listing of the manifest file schema, see [Manifest File Schema](manifest-file-schema.md).

For a listing of the application configuration file schema, see [Application Configuration File Schema](application-configuration-file-schema.md).

For a listing of the publisher configuration file schema, see [Publisher Configuration File Schema](publisher-configuration-file-schema.md).

Other technologies extend the format used by Windows versioning and configuration manifests. Developers should refer to the documentation that is specific to the technology being used for information about the manifest format. For example:

-   [ClickOnce](/visualstudio/deployment/clickonce-reference)
-   [Common Language Runtime](/dotnet/standard/clr)
-   [User Account Control (UAC)](/previous-versions/bb756929(v=msdn.10))

 

 
