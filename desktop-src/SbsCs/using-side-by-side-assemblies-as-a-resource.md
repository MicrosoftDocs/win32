---
description: Using Side-by-Side Assemblies as a Resource
ms.assetid: f7963d37-93c4-49d6-af7d-fc692f632894
title: Using Side-by-Side Assemblies as a Resource
ms.topic: article
ms.date: 05/31/2018
---

# Using Side-by-Side Assemblies as a Resource

You can add a manifest to a application as a resource in the application's binary executable header file. The value of the MANIFEST\_RESOURCE\_ID determines how the side-by-side assembly dependencies described in the manifest are used by the loader.

If you set the MANIFEST\_RESOURCE\_ID to 1, the loader uses the side-by-side assembly dependencies specified in the manifest as the process default. All plug-ins also use this process default.

The following table summarizes how the loader uses the manifest for different values of MANIFEST\_RESOURCE\_ID when the application is compiled with the -DISOLATION\_AWARE\_ENABLED flag. Note that the values 1-16 are reserved for use by Windows XP. A developer may use other values if they wish to manage the activation contexts using the functions describe in the [Activation Context Reference](activation-context-reference.md).



| Value of MANIFEST\_RESOURCE\_ID | Manifest specifies the Process Default? | Use for Static Imports? | Use for an EXE? | Use for a DLL? | Uses Side-by-Side version of assemblies if compiled with -DISOLATION\_AWARE\_ENABLED? |
|---------------------------------|-----------------------------------------|-------------------------|-----------------|----------------|---------------------------------------------------------------------------------------|
| 1                               | Yes                                     | Yes                     | Yes             | No             | Yes                                                                                   |
| 2                               | No                                      | Yes                     | Yes             | Yes            | Yes                                                                                   |
| 3                               | No                                      | No                      | Yes             | Yes            | Yes                                                                                   |



 

MANIFEST\_RESOURCE\_ID 1 should be used for applications that do not host plug-ins. Use MANIFEST\_RESOURCE\_ID 1 when all parts of the application should use the version of the side-by-side assembly specified in the manifest. For more information, see [Enabling an Assembly in an Application Without Extensions](enabling-an-assembly-in-an-application-without-extensions.md).

MANIFEST\_RESOURCE\_ID 2 should be used for applications that host third-party controls or plug-ins. In this case, the manifest affects all side-by-side assemblies being loaded by static loading, calls to DllMain, and calls redirected by -DISOLATION\_AWARE\_ENABLED. For more information, see [Enabling an Assembly in an Application Hosting a DLL, Extension, or Control Panel](enabling-an-assembly-in-an-application-hosting-a-dll-extension-or-control-panel.md).

MANIFEST\_RESOURCE\_ID 3 should be used for redirecting calls by -DISOLATION\_AWARE\_ENABLED only. Loading by other methods are unaffected.

 

 



