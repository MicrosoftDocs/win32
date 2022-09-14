---
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 0D537FD1-AD5C-43CB-989F-4B5B7C0A1208
title: A (Isolated Applications and Side-by-side Assemblies)
ms.topic: article
ms.date: 05/31/2018
---

# A (Isolated Applications and Side-by-side Assemblies)

A B C [D](d-sbscs-gly.md) E F [G](g-sbscs-gly.md) H [I](i-sbscs-gly.md) J K L [M](m-sbscs-gly.md) N O [P](p-sbscs-gly.md) Q [R](r-sbscs-gly.md) [S](s-sbscs-gly.md) T U V W X Y Z

<dl> <dt>

<span id="_win32_activation_context_gly"></span><span id="_WIN32_ACTIVATION_CONTEXT_GLY"></span>**activation context**
</dt> <dd>

A data structure in memory. Each section of this structure contains metadata for side-by-side-aware API functions. For example, one section may have DLL redirection data, which is used by the DLL loader, and another may have COM server data. This data may be used to redirect the loading of a DLL to a specific version, the creation of a COM object, or the creation of a window to a version that is most compatible for the application.

</dd> <dt>

<span id="_win32_application_configuration_gly"></span><span id="_WIN32_APPLICATION_CONFIGURATION_GLY"></span>**application configuration**
</dt> <dd>

Names and versions of side-by-side assemblies required to run an application. When an application is deployed with a manifest, dependencies on specific versions of shared side-by-side assemblies are explicitly defined. By default, the version of the assembly specified in the manifest is the version that is used upon activation. Global application configuration specifies the configuration of all applications on the system. Per-application configuration can override the global application configuration on a per-application basis.

</dd> <dt>

<span id="_win32_application_configuration_manifest_gly"></span><span id="_WIN32_APPLICATION_CONFIGURATION_MANIFEST_GLY"></span>**application configuration manifest**
</dt> <dd>

File that specifies side-by-side assemblies to be used by a fully or partially isolated application. Application configuration manifest files are installed in the same folder as the application's executable file.

</dd> <dt>

<span id="_win32_application_manifest_gly"></span><span id="_WIN32_APPLICATION_MANIFEST_GLY"></span>**application manifest**
</dt> <dd>

File that describes an isolated application. It specifies the information required to run the application, including dependencies on private assemblies, specific versions of shared assemblies and metadata for private assemblies. The name of an application manifest file is the name of the application executable followed by the extension .manifest. For example, for MySampleApp.exe, the manifest file would be MySampleApp.exe.manifest.

</dd> <dt>

<span id="_win32_assembly_gly"></span><span id="_WIN32_ASSEMBLY_GLY"></span>**assembly**
</dt> <dd>

Fundamental unit for naming, binding, versioning, deploying, or configuring a block of programming code. These code assemblies may be placed in DLLs or COM assemblies. Applications with common functionality may run shared blocks of programming code which are referred to as modules or code assemblies. The infrastructure for the safe sharing of assemblies is referred to as side-by-side assembly sharing.

</dd> <dt>

<span id="_win32_assembly_manifest_gly"></span><span id="_WIN32_ASSEMBLY_MANIFEST_GLY"></span>**assembly manifest**
</dt> <dd>

Description of a side-by-side assembly. It specifies the name, version, files, resources of the assembly, binding data for items of the assembly, and dependencies on other side-by-side assemblies. An assembly manifest file can have any valid file name, as long as it is followed by the extension .manifest.

</dd> </dl>

 

 



