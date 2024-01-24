---
description: If your application hosts a third-party DLL, extension, plug-in, or control panel, you may want to enable an assembly in your application&\#8212;without also enabling this assembly for the hosted components.
ms.assetid: 832957ca-82fc-4600-b469-512621dde921
title: Enabling an Assembly in an Application Hosting a DLL, Extension, or Control Panel
ms.topic: article
ms.date: 05/31/2018
---

# Enabling an Assembly in an Application Hosting a DLL, Extension, or Control Panel

If your application hosts a third-party DLL, extension, plug-in, or control panel, you may want to enable an assembly in your application—without also enabling this assembly for the hosted components. This can be the case when a hosted component requires code changes to use the assembly. As the application developer, you may be unable to make changes to these third-party components. In this case, you should follow the procedure described in this section so that your application can use the assembly without affecting the hosted components.

-   To enable an assembly in an application without affecting any hosted DLLs, extensions, plug-ins, or control panels, a manifest that describes the application's dependence on the assembly should be included in the application as a resource. The hosted components that are not being enabled with the assembly should not include manifests describing this dependency.
-   To enable an assembly in an application and its hosted DLLs, extensions, plug-ins, or control panels, include manifests as resources in both the application and its hosted components. The manifests included in the application and in the hosted components should each describe a dependence on the assembly. Typically, the application developer adds a manifest to the application and the hosted component developer adds a manifest to the DLL, extension, plug-in, or control panel.

The following method can be used to add a manifest to an application or a hosted component that is a DLL, extension, plug-in, or control panel.

**To enable an assembly in an application or hosted component.**

1.  Author a manifest that describes the dependence of the application or extension on the assembly.

    For example, the manifest for "YourApplication" can be created by copying the following sample manifest and substituting correct values for **assemblyIdentity**, **processorArchitecture**, and **description**. Set the value of **processorArchitecture** to x86 if building on a 32-bit platform and to ia64 if building on a 64-bit platform. The **description** element contains an option description of the application. For more information about the manifest format, see [application manifests](application-manifests.md).

    ``` syntax
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
    <assemblyIdentity
        version="1.0.0.0"
        processorArchitecture="x86"
        name="YourCompanyName.YourDivision.YourApp"
        type="win32"
    />
    <description>Your app description here</description>
    <dependency>
        <dependentAssembly>
            <assemblyIdentity
                type="win32"
                name="Proseware.Research.SampleAssembly"
                version="6.0.0.0"
                processorArchitecture="X86"
                publicKeyToken="0000000000000000"
                language="*"
            />
        </dependentAssembly>
    </dependency>
    </assembly>
    ```

2.  Create a resource in the application or extension of type RT\_MANIFEST id 2.

    For example, if the application's name is YourApp, the application should contain the following:

    ``` syntax
    #define MANIFEST_RESOURCE_ID 2
    MANIFEST_RESOURCE_ID RT_MANIFEST "YourApp.manifest"
    ```

3.  Compile the application with the -DISOLATION\_AWARE\_ENABLED flag, or insert this statement before the \#include "Windows.h" statement. In the case of an application with multiple modules, the -DISOLATION\_AWARE\_ENABLED flag is required on all modules.

    ``` syntax
    #define ISOLATION_AWARE_ENABLED 1
    ```

4.  Test to ensure that assemblies that are used by the application work correctly in the application and hosted component.

For more information about adding an assembly to applications without extensions, see [Enabling an Assembly in an Application Without Extensions](enabling-an-assembly-in-an-application-without-extensions.md).

 

 



