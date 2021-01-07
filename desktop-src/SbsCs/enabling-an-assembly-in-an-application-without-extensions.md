---
description: If your application does not host a DLL, extension, plug-in, or control panel, you can use the method described in this section to enable an assembly for your application.
ms.assetid: d043ec1b-ac31-45fb-9232-eec42aef4ac3
title: Enabling an Assembly in an Application Without Extensions
ms.topic: article
ms.date: 05/31/2018
---

# Enabling an Assembly in an Application Without Extensions

If your application does not host a DLL, extension, plug-in, or control panel, you can use the method described in this section to enable an assembly for your application. For more information about adding an assembly to applications with extensions, see [Enabling an Assembly in an Application Hosting a DLL, Extension, or Control Panel](enabling-an-assembly-in-an-application-hosting-a-dll-extension-or-control-panel.md).

**To enable an assembly in an application without any hosted components**

1.  Author a manifest that describes the dependence of the application or extension on the assembly.

    For example, the manifest for "YourApplication" can be created by copying the following sample manifest and substituting correct values for **assemblyIdentity**, **processorArchitecture**, and **description**. Set the value of **processorArchitecture** to x86 if building on a 32-bit platform, and to ia64 if building on a 64-bit platform. The **description** element contains an option description of the application. For more information about the manifest format, see [application manifests](application-manifests.md).

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

2.  Add the manifest to the application as a resource in the application's binary executable header file. It is not recommended that you add the manifest to the application as an external manifest file.

    To add the manifest as a resource, create a resource in the application of type RT\_MANIFEST id 1. For example, if the application's name is YourApp, the application's header file should contain the following:

    ``` syntax
    #define MANIFEST_RESOURCE_ID 1
    MANIFEST_RESOURCE_ID RT_MANIFEST "YourApp.manifest"
    ```

    If you instead add the manifest as an external manifest file, be sure that the installation copies the manifest file into the folder containing the application's executable file.

3.  Test to ensure that assemblies used by the application work correctly in the application.

 

 



