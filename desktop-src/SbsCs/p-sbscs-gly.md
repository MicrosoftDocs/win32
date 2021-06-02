---
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 9BC3D6A3-D8F5-42C6-9A68-68F1741207D7
title: P (Isolated Applications and Side-by-side Assemblies)
ms.topic: article
ms.date: 05/31/2018
---

# P (Isolated Applications and Side-by-side Assemblies)

[A](a-sbscs-gly.md) B C [D](d-sbscs-gly.md) E F [G](g-sbscs-gly.md) H [I](i-sbscs-gly.md) J K L [M](m-sbscs-gly.md) N O P Q [R](r-sbscs-gly.md) [S](s-sbscs-gly.md) T U V W X Y Z

<dl> <dt>

<span id="_win32_per_application_configuration_gly"></span><span id="_WIN32_PER_APPLICATION_CONFIGURATION_GLY"></span>**per-application configuration**
</dt> <dd>

Configuration that can override a specific assembly's global application configuration. A per-application configuration is specified by an application configuration manifest file installed in the same folder as the executable file. The manifest file describes the version, or range of versions, of side-by-side assemblies to be used by the application. Per-application configuration might be used when a new version of an assembly is incompatible with an application. In this case, the application's default or global configuration can be overridden for a specific side-by-side assembly.

</dd> <dt>

<span id="_win32_private_side_by_side_assembly_gly"></span><span id="_WIN32_PRIVATE_SIDE_BY_SIDE_ASSEMBLY_GLY"></span>**private side-by-side assembly**
</dt> <dd>

A private side-by-side assembly is only visible to a specified application. It is installed locally to an isolated application and the assembly's code becomes private to the application context. The dependencies of a private side-by-side assembly are described in the application manifest file. Private side-by-side assemblies can be used to offset the negative effects of assembly sharing, such as DLL conflicts, and to facilitate application deployment.

</dd> <dt>

<span id="_win32_public_key_token_gly"></span><span id="_WIN32_PUBLIC_KEY_TOKEN_GLY"></span>**public key token**
</dt> <dd>

A 16-character hexadecimal string that represents the last 8 bytes of the SHA-1 hash of the public key under which the assembly is signed. The public key used to sign the catalog must be 2048 bits or greater. Required for all shared side-by-side assemblies.

</dd> </dl>

 

 



